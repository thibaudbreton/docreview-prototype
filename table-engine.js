/* =====================================================
   TABLE ENGINE — shared review-table interaction behaviour
   (B5, was ticket 5). Spliced verbatim by build_merge.py into
   both revue-documentaire.html and suivi-experts-et-versions.html
   — edit this ONE file to change behaviour on both screens.

   Design: stateless/functional, not a class or owned state object.
   Each host keeps its OWN `state` shape exactly as before (selection
   Set, colFilters, filterToSelection, savedColFilters, activeCell,
   colCollapsed) — TE's functions take that state plus a small adapter
   of host-specific callbacks (how to read visible rows, find a row's
   DOM element, which columns exist, how to trigger a re-render). This
   keeps the integration a thin call-site swap in each host rather than
   a data-model rewrite, which is what makes reusing this safe on a
   second, structurally different screen.

   Covers exactly the behaviours the ticket named as shared: row
   checkboxes / multi-select (incl. drag-select), the Bulk Action Bar
   shell (show/hide on selection, "Show only selected"), Filter to
   Selection (suspend/restore column filters), keyboard row×column
   navigation, and the Column Visibility Menu checklist. Per-column
   Excel-style filter POPOVERS, sorting, and row/grouping rendering
   stay host-specific — the ticket does not ask for those to be shared,
   and they differ enough between screens (document structure vs.
   branch tracking) that forcing them into one shape would cost more
   than it's worth in a prototype.
===================================================== */
const TE = {

/* ---------- selection ---------- */
toggleSelect(selection, id){
  selection.has(id) ? selection.delete(id) : selection.add(id);
},

/* Drag-select across a range of rows, Excel-style: mousedown on a row's selection
   gutter starts the drag: the range between the anchor and the current row is live-
   applied on top of whatever was selected before, and rows outside the range fall
   back to their pre-drag state. `idsInOrder` is the host's current on-screen row-id
   order (parents only — no checkbox on branch/child rows, per the app's own rule). */
bindDragSelect({ scroller, selCellSelector, rowSelector, getIdsInOrder, selection, onChange }){
  let dragSel = null, dragTick = false;
  scroller.addEventListener("mousedown", e => {
    const cell = e.target.closest(selCellSelector); if(!cell) return;
    const row = cell.closest(rowSelector); if(!row) return;
    e.preventDefault();
    const idsInOrder = getIdsInOrder();
    const id = row.dataset.id, anchorIdx = idsInOrder.indexOf(id); if(anchorIdx<0) return;
    const before = new Set(selection);
    const willSelect = !selection.has(id);
    willSelect ? selection.add(id) : selection.delete(id);
    dragSel = { anchorIdx, willSelect, before, idsInOrder };
    document.body.classList.add("no-select");
    onChange(id);
  });
  document.addEventListener("mousemove", e => {
    if(!dragSel || dragTick) return;
    if(!(e.buttons & 1)){ dragSel=null; document.body.classList.remove("no-select"); return; }
    dragTick = true;
    requestAnimationFrame(() => {
      dragTick = false;
      if(!dragSel) return;
      const row = document.elementFromPoint(e.clientX, e.clientY)?.closest(rowSelector);
      if(!row || !row.dataset.id) return;
      const idx = dragSel.idsInOrder.indexOf(row.dataset.id); if(idx<0) return;
      const [lo,hi] = [Math.min(dragSel.anchorIdx,idx), Math.max(dragSel.anchorIdx,idx)];
      selection.clear();
      dragSel.before.forEach(x=>selection.add(x));
      for(let i=lo;i<=hi;i++){
        const rid = dragSel.idsInOrder[i];
        dragSel.willSelect ? selection.add(rid) : selection.delete(rid);
      }
      onChange(row.dataset.id);
    });
  });
  document.addEventListener("mouseup", () => {
    if(dragSel){ dragSel=null; document.body.classList.remove("no-select"); }
  });
},

/* ---------- Filter to Selection ---------- */
/* state needs: {filterToSelection:bool, colFilters:{[col]:Set}, savedColFilters, selection:Set}.
   emptyColFilters() must return a fresh all-clear colFilters object shaped like the host's. */
enterFilterToSelection(state, emptyColFilters){
  if(state.filterToSelection) return;
  state.filterToSelection = true;
  state.savedColFilters = state.colFilters;
  state.colFilters = emptyColFilters();
},
exitFilterToSelection(state){
  state.filterToSelection = false;
  if(state.savedColFilters){ state.colFilters = state.savedColFilters; state.savedColFilters = null; }
},

/* ---------- keyboard — active cell (row × column) ---------- */
/* adapter: {getVisibleRows(): [{id,bidx}] in on-screen order,
             getNavCols(): [colKey] respecting current column visibility,
             activeCellRowEl(ac): DOM element for that row or null,
             onRowChange(id): called when the row changes (e.g. sync a detail panel)} */
moveActiveCellDelta(state, dRow, dCol, adapter){
  const list = adapter.getVisibleRows(); if(!list.length) return;
  let ri = list.findIndex(r=>r.id===state.activeCell.id && r.bidx===state.activeCell.bidx);
  if(ri===-1) ri=0; else ri = Math.max(0, Math.min(list.length-1, ri+dRow));
  const cols = adapter.getNavCols();
  let ci = cols.indexOf(state.activeCell.col);
  if(ci===-1) ci = 0;
  ci = Math.max(0, Math.min(cols.length-1, ci+dCol));
  state.activeCell = { id:list[ri].id, bidx:list[ri].bidx, col:cols[ci] };
  if(dRow!==0 && list[ri].bidx==null && adapter.onRowChange) adapter.onRowChange(list[ri].id);
  this.paintActiveCell(state, adapter);
  this.scrollActiveCellIntoView(state, adapter);
},
paintActiveCell(state, adapter){
  document.querySelectorAll(".rcell.active-cell").forEach(c=>c.classList.remove("active-cell"));
  const ac = state.activeCell; if(!ac.id || !ac.col) return;
  const row = adapter.activeCellRowEl(ac); if(!row) return;
  const cell = row.querySelector(`.rcell.c-${ac.col}`);
  if(cell) cell.classList.add("active-cell");
},
/* USER-TEST-session-3.md §1.4 — must follow the active cell on both axes: vertically
   between rows, horizontally between columns. Scrolling the specific cell (not just the
   row) is what gets inline:"nearest" to actually move the horizontal scrollbar when a
   column is off-screen — scrolling the row only ever addressed the vertical axis. */
scrollActiveCellIntoView(state, adapter){
  const row = adapter.activeCellRowEl(state.activeCell); if(!row) return;
  const cell = state.activeCell.col && row.querySelector(`.rcell.c-${state.activeCell.col}`);
  (cell || row).scrollIntoView({ block:"nearest", inline:"nearest" });
},
focusActiveCellControl(state, adapter){
  const row = adapter.activeCellRowEl(state.activeCell); if(!row) return;
  const cell = row.querySelector(`.rcell.c-${state.activeCell.col}`); if(!cell) return;
  const ctrl = cell.querySelector("input,select"); if(ctrl) ctrl.focus();
},
/* wires Enter (confirm + move down, "type down a column") / Escape (cancel + blur)
   on one editable control; call once per .cell-text/.cell-select after each render */
bindCellEditKeys(el, state, adapter){
  if(el.tagName==="INPUT") el.addEventListener("focus", ()=>{ el.dataset.orig = el.value; });
  el.addEventListener("keydown", e=>{
    if(e.key==="Enter"){
      e.preventDefault(); el.blur();
      this.moveActiveCellDelta(state, 1, 0, adapter);
      this.focusActiveCellControl(state, adapter);
    } else if(e.key==="Escape"){
      e.preventDefault();
      if(el.tagName==="INPUT" && el.dataset.orig!==undefined) el.value = el.dataset.orig;
      el.blur();
    }
  });
},
/* Handles the shared arrow/space keys for a document-level keydown listener.
   Returns true if it handled the key (host should e.preventDefault and stop there),
   false otherwise (host is free to check its own extra shortcuts, e.g. j/k/v/a). */
handleNavKeydown(e, state, adapter){
  if(e.key==="ArrowDown"){ this.moveActiveCellDelta(state,1,0,adapter); return true; }
  if(e.key==="ArrowUp"){ this.moveActiveCellDelta(state,-1,0,adapter); return true; }
  if(e.key==="ArrowRight"){ this.moveActiveCellDelta(state,0,1,adapter); return true; }
  if(e.key==="ArrowLeft"){ this.moveActiveCellDelta(state,0,-1,adapter); return true; }
  if(e.key===" " && state.activeCell.col==="sel" && state.activeCell.id && state.activeCell.bidx==null){
    this.toggleSelect(state.selection, state.activeCell.id);
    if(adapter.onSelectionToggle) adapter.onSelectionToggle(state.activeCell.id);
    return true;
  }
  return false;
},

/* ---------- Column Visibility + Reorder Menu ---------- */
/* USER-TEST-session-3.md §1.4 — columns must be fully removable (not just collapsed
   to a sliver) and reorderable by the user. columnDefs: [{k,label}] — only the
   optional columns (sel/id/req stay pinned, hosts don't pass those in). colOrder:
   array of every columnDefs key, in current display order — mutated in place by
   drag-and-drop. colCollapsed: Set of keys currently hidden. */
reorderableColumnListHTML(columnDefs, colOrder, colCollapsed){
  const byKey = Object.fromEntries(columnDefs.map(c=>[c.k,c]));
  return colOrder.filter(k=>byKey[k]).map(k=>{
    const c = byKey[k];
    return `<div class="colf-row" draggable="true" data-colkey="${c.k}">
      <span class="colf-handle" title="Drag to reorder">⠿</span>
      <label class="colf-opt"><input type="checkbox" data-colvis="${c.k}" ${colCollapsed.has(c.k)?"":"checked"}>${c.label}</label>
    </div>`;
  }).join("");
},
bindReorderableColumnList(panelEl, colOrder, colCollapsed, onChange){
  panelEl.querySelectorAll("[data-colvis]").forEach(cb=>cb.addEventListener("change", ()=>{
    const k = cb.dataset.colvis;
    cb.checked ? colCollapsed.delete(k) : colCollapsed.add(k);
    onChange();
  }));
  let dragKey = null;
  panelEl.querySelectorAll("[data-colkey]").forEach(row=>{
    row.addEventListener("dragstart", e=>{
      dragKey = row.dataset.colkey;
      e.dataTransfer.effectAllowed = "move";
      row.classList.add("dragging");
    });
    row.addEventListener("dragend", ()=>{ row.classList.remove("dragging"); dragKey = null; });
    row.addEventListener("dragover", e=>{ e.preventDefault(); e.dataTransfer.dropEffect = "move"; });
    row.addEventListener("drop", e=>{
      e.preventDefault();
      const targetKey = row.dataset.colkey;
      if(!dragKey || dragKey===targetKey) return;
      const from = colOrder.indexOf(dragKey), to = colOrder.indexOf(targetKey);
      if(from<0 || to<0) return;
      colOrder.splice(from,1);
      colOrder.splice(to,0,dragKey);
      onChange();
    });
  });
},

};
