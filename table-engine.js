/* =====================================================
   TABLE ENGINE — shared review-table interaction behaviour
   (B5, was ticket 5). Spliced verbatim by build_merge.py into
   both revue-documentaire.html and compliance.html
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

/* ---------- Advanced Filter (SPEC-advanced-filters.md) ---------- */
/* A filter is {op:"AND"|"OR", items:[condition|group]}. A condition is
   {field,op,value}. A group is {op:"AND"|"OR", items:[condition,...]} — ONE
   level only, per §4: a group never contains another group. fieldDefs is
   {key:{label,type:"text"|"enum"|"date"|"boolean",options,get(row)}} — get()
   returns an ARRAY of values so one field (e.g. Activity) can carry several. */
OPS_BY_TYPE:{
  text:["contains","not_contains","is","is_not","starts_with","is_empty","is_not_empty"],
  enum:["is","is_not","is_any_of","is_none_of","is_empty"],
  date:["before","after","between","in_last","is_empty"],
  boolean:["is_true","is_false"],
},
OP_LABEL:{contains:"contains",not_contains:"does not contain",is:"is",is_not:"is not",starts_with:"starts with",
  is_empty:"is empty",is_not_empty:"is not empty",is_any_of:"is any of",is_none_of:"is none of",
  before:"before",after:"after",between:"between",in_last:"in the last N days",is_true:"is true",is_false:"is false"},
matchesCondition(fieldDefs, cond, row){
  const def=fieldDefs[cond.field]; if(!def) return true;
  const vals=def.get(row)||[];
  const present=vals.filter(v=>v!==""&&v!=null);
  const s=v=>String(v).toLowerCase();
  switch(cond.op){
    case "is_empty": return present.length===0;
    case "is_not_empty": return present.length>0;
    case "contains": return present.some(v=>s(v).includes(s(cond.value||"")));
    case "not_contains": return !present.some(v=>s(v).includes(s(cond.value||"")));
    case "is": return present.some(v=>s(v)===s(cond.value||""));
    case "is_not": return !present.some(v=>s(v)===s(cond.value||""));
    case "starts_with": return present.some(v=>s(v).startsWith(s(cond.value||"")));
    case "is_any_of": { const set=new Set(cond.value||[]); return present.some(v=>set.has(v)); }
    case "is_none_of": { const set=new Set(cond.value||[]); return present.length>0 && !present.some(v=>set.has(v)); }
    case "before": return present.some(v=>v<cond.value);
    case "after": return present.some(v=>v>cond.value);
    case "between": return present.some(v=>v>=(cond.value&&cond.value.from) && v<=(cond.value&&cond.value.to));
    case "in_last": { const days=+cond.value||0, cutoff=Date.now()-days*86400000; return present.some(v=>new Date(v).getTime()>=cutoff); }
    case "is_true": return present.some(v=>v===true);
    case "is_false": return present.length===0 || present.every(v=>v!==true);
    default: return true;
  }
},
matchesGroupItem(fieldDefs, item, row){
  return item.items ? this.matchesFilter(fieldDefs,item,row) : this.matchesCondition(fieldDefs,item,row);
},
matchesFilter(fieldDefs, filter, row){
  if(!filter || !filter.items || !filter.items.length) return true;
  const results=filter.items.map(it=>this.matchesGroupItem(fieldDefs,it,row));
  return filter.op==="OR" ? results.some(Boolean) : results.every(Boolean);
},
optLabel(def,v){ const o=(def.options||[]).find(o=>o.v===v); return o?o.l:v; },
describeValue(def, cond){
  if(cond.op==="is_any_of"||cond.op==="is_none_of") return (cond.value||[]).map(v=>this.optLabel(def,v)).join(", ");
  if(cond.op==="between") return `${(cond.value&&cond.value.from)||"…"} and ${(cond.value&&cond.value.to)||"…"}`;
  if(cond.op==="in_last") return `${cond.value||"N"} days`;
  if(cond.op==="is_empty"||cond.op==="is_not_empty"||cond.op==="is_true"||cond.op==="is_false") return "";
  return def.type==="enum" ? this.optLabel(def,cond.value) : (cond.value||"");
},
describeCondition(fieldDefs, cond){
  const def=fieldDefs[cond.field]; if(!def) return "";
  const val=this.describeValue(def,cond);
  return `${def.label} ${this.OP_LABEL[cond.op]||cond.op}${val?" "+val:""}`;
},
describeGroupItem(fieldDefs,item){
  return item.items ? `(${this.describeFilter(fieldDefs,item)})` : this.describeCondition(fieldDefs,item);
},
describeFilter(fieldDefs, filter){
  if(!filter || !filter.items || !filter.items.length) return "";
  return filter.items.map(it=>this.describeGroupItem(fieldDefs,it)).join(` ${filter.op} `);
},
/* Saved filters — personal, cross-project (§6): localStorage, keyed per table
   (not per project — that's the point) so review's saved filters stay separate
   from any other table's. This is the prototype's first use of localStorage;
   everything else resets with the demo on purpose, but a "saved" filter that
   didn't survive a reload wouldn't actually demonstrate what §6 is selling. */
savedFiltersKey(tableKey){ return `srm-saved-filters-${tableKey}`; },
loadSavedFilters(tableKey){
  try{ return JSON.parse(localStorage.getItem(this.savedFiltersKey(tableKey))||"[]"); }catch(e){ return []; }
},
saveSavedFilters(tableKey, list){
  try{ localStorage.setItem(this.savedFiltersKey(tableKey), JSON.stringify(list)); }catch(e){}
},

};
