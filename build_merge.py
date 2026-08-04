#!/usr/bin/env python3
"""Merge the 5 Smart Requirement Manager (SRM) source screens into the single-file docreview-app.html deliverable.

Usage: python3 build_merge.py
Reads the 5 source files below, base64-encodes each (UTF-8), and writes docreview-app.html
plus an identical index.html (GitHub Pages serves index.html as the site entry point —
writing both here keeps the hosted copy in sync with the deliverable automatically).
Always edit the 5 sources — never the merged files directly — then re-run this script.

Cross-screen navigation is expressed in the sources as parent.route(...) /
parent.routeUrl(...) / goRoute(...) JS calls (see dashboard-et-config.html's
goRoute() for the standalone-fallback pattern) — not <a href="X.html"> tags.
Keep new cross-screen links in that form; there is no href rewriting here.
"""
import base64

SOURCES = [
    ("dash", "dashboard-et-config.html"),
    ("review", "revue-documentaire.html"),
    ("followup", "suivi-experts-et-versions.html"),
    ("create", "creation-projet.html"),
    ("home", "accueil.html"),
]

OUTPUT = "docreview-app.html"
PAGES_OUTPUT = "index.html"  # GitHub Pages entry point — same bytes as OUTPUT

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Smart Requirement Manager — STB-2026 · Full app</title>
<link rel="icon" type="image/svg+xml" media="(prefers-color-scheme: light)" href="data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIyIDIwIDg0IDQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJNMy4wNzAzMSA0NC4yMTczQzMuMDcwMzEgMzEuMzI4NiAxMy41MTg2IDIwLjg4MDMgMjYuNDA3MyAyMC44ODAzSDYxLjE5MDVDNjEuMzEzMiAyMC44ODAzIDYxLjQxMjcgMjAuOTc5OCA2MS40MTI3IDIxLjEwMjVWNjcuMzMyMUM2MS40MTI3IDY3LjQ1NDggNjEuMzEzMiA2Ny41NTQyIDYxLjE5MDUgNjcuNTU0MkgyNi40MDczQzEzLjUxODYgNjcuNTU0MiAzLjA3MDMxIDU3LjEwNTkgMy4wNzAzMSA0NC4yMTczVjQ0LjIxNzNaIiBmaWxsPSJ1cmwoI2ZsYSkiIGZpbGwtb3BhY2l0eT0iLjU0Ii8+CjxwYXRoIGQ9Ik0xOC40MjM4IDQ0LjIxNzNDMTguNDIzOCAzMS4zMjg2IDI4Ljg3MjEgMjAuODgwMyA0MS43NjA4IDIwLjg4MDNINjMuMDg0NkM2My4xNzg5IDIwLjg4MDMgNjMuMjU1MyAyMC45NTY4IDYzLjI1NTMgMjEuMDUxVjY3LjM4MzVDNjMuMjU1MyA2Ny40Nzc4IDYzLjE3ODkgNjcuNTU0MiA2My4wODQ2IDY3LjU1NDJINDEuNzYwOEMyOC44NzIxIDY3LjU1NDIgMTguNDIzOCA1Ny4xMDU5IDE4LjQyMzggNDQuMjE3M1Y0NC4yMTczWiIgZmlsbD0idXJsKCNmbGIpIiBmaWxsLW9wYWNpdHk9Ii41NCIvPgo8cGF0aCBkPSJNMzUuMDA1NCA0NC4yMTczQzM1LjAwNTQgMzEuMzI4NiA0NS40NTM3IDIwLjg4MDMgNTguMzQyMyAyMC44ODAzSDYxLjQxM0M3NC4zMDE2IDIwLjg4MDMgODQuNzQ5OSAzMS4zMjg2IDg0Ljc0OTkgNDQuMjE3M1Y0NC4yMTczQzg0Ljc0OTkgNTcuMTA1OSA3NC4zMDE2IDY3LjU1NDIgNjEuNDEzIDY3LjU1NDJINTguMzQyM0M0NS40NTM3IDY3LjU1NDIgMzUuMDA1NCA1Ny4xMDU5IDM1LjAwNTQgNDQuMjE3M1Y0NC4yMTczWiIgZmlsbD0idXJsKCNmbGMpIiBmaWxsLW9wYWNpdHk9Ii41NCIvPgo8Y2lyY2xlIGN4PSI2MC4zMTA1IiBjeT0iNDQuMzQzMSIgcj0iMTguNTQ5NyIgZmlsbD0iI2ZmZiIvPgo8ZGVmcz4KPGxpbmVhckdyYWRpZW50IGlkPSJmbGEiIHgxPSIzLjA3IiB5MT0iNDQuMjIiIHgyPSI2MS40MSIgeTI9IjQ0LjIyIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iIzFFMzI0NiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzFFMzI0NiIgc3RvcC1vcGFjaXR5PSIwIi8+PC9saW5lYXJHcmFkaWVudD4KPGxpbmVhckdyYWRpZW50IGlkPSJmbGIiIHgxPSIxOC40MiIgeTE9IjQ0LjIyIiB4Mj0iNjMuMjYiIHkyPSI0NC4yMiIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiMxRTMyNDYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiMxRTMyNDYiIHN0b3Atb3BhY2l0eT0iMCIvPjwvbGluZWFyR3JhZGllbnQ+CjxsaW5lYXJHcmFkaWVudCBpZD0iZmxjIiB4MT0iMzUuMDEiIHkxPSI0NC4yMiIgeDI9Ijg0Ljc1IiB5Mj0iNDQuMjIiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjMUUzMjQ2Ii8+PHN0b3Agb2Zmc2V0PSIuMTY4IiBzdG9wLWNvbG9yPSIjMUUzMjQ2Ii8+PC9saW5lYXJHcmFkaWVudD4KPC9kZWZzPgo8L3N2Zz4=">
<link rel="icon" type="image/svg+xml" media="(prefers-color-scheme: dark)" href="data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIyIDIwIDg0IDQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cGF0aCBkPSJNMy4wNzAzMSA0NC4yMTczQzMuMDcwMzEgMzEuMzI4NiAxMy41MTg2IDIwLjg4MDMgMjYuNDA3MyAyMC44ODAzSDYxLjE5MDVDNjEuMzEzMiAyMC44ODAzIDYxLjQxMjcgMjAuOTc5OCA2MS40MTI3IDIxLjEwMjVWNjcuMzMyMUM2MS40MTI3IDY3LjQ1NDggNjEuMzEzMiA2Ny41NTQyIDYxLjE5MDUgNjcuNTU0MkgyNi40MDczQzEzLjUxODYgNjcuNTU0MiAzLjA3MDMxIDU3LjEwNTkgMy4wNzAzMSA0NC4yMTczVjQ0LjIxNzNaIiBmaWxsPSJ1cmwoI2ZkYSkiIGZpbGwtb3BhY2l0eT0iLjU0Ii8+CjxwYXRoIGQ9Ik0xOC40MjM4IDQ0LjIxNzNDMTguNDIzOCAzMS4zMjg2IDI4Ljg3MjEgMjAuODgwMyA0MS43NjA4IDIwLjg4MDNINjMuMDg0NkM2My4xNzg5IDIwLjg4MDMgNjMuMjU1MyAyMC45NTY4IDYzLjI1NTMgMjEuMDUxVjY3LjM4MzVDNjMuMjU1MyA2Ny40Nzc4IDYzLjE3ODkgNjcuNTU0MiA2My4wODQ2IDY3LjU1NDJINDEuNzYwOEMyOC44NzIxIDY3LjU1NDIgMTguNDIzOCA1Ny4xMDU5IDE4LjQyMzggNDQuMjE3M1Y0NC4yMTczWiIgZmlsbD0idXJsKCNmZGIpIiBmaWxsLW9wYWNpdHk9Ii41NCIvPgo8cGF0aCBkPSJNMzUuMDA1NCA0NC4yMTczQzM1LjAwNTQgMzEuMzI4NiA0NS40NTM3IDIwLjg4MDMgNTguMzQyMyAyMC44ODAzSDYxLjQxM0M3NC4zMDE2IDIwLjg4MDMgODQuNzQ5OSAzMS4zMjg2IDg0Ljc0OTkgNDQuMjE3M1Y0NC4yMTczQzg0Ljc0OTkgNTcuMTA1OSA3NC4zMDE2IDY3LjU1NDIgNjEuNDEzIDY3LjU1NDJINTguMzQyM0M0NS40NTM3IDY3LjU1NDIgMzUuMDA1NCA1Ny4xMDU5IDM1LjAwNTQgNDQuMjE3M1Y0NC4yMTczWiIgZmlsbD0idXJsKCNmZGMpIiBmaWxsLW9wYWNpdHk9Ii41NCIvPgo8Y2lyY2xlIGN4PSI2MC4zMTA1IiBjeT0iNDQuMzQzMSIgcj0iMTguNTQ5NyIgZmlsbD0iI2ZmZiIvPgo8ZGVmcz4KPGxpbmVhckdyYWRpZW50IGlkPSJmZGEiIHgxPSIzLjA3IiB5MT0iNDQuMjIiIHgyPSI2MS40MSIgeTI9IjQ0LjIyIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agc3RvcC1jb2xvcj0iI2ZmZiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iI2ZmZiIgc3RvcC1vcGFjaXR5PSIwIi8+PC9saW5lYXJHcmFkaWVudD4KPGxpbmVhckdyYWRpZW50IGlkPSJmZGIiIHgxPSIxOC40MiIgeTE9IjQ0LjIyIiB4Mj0iNjMuMjYiIHkyPSI0NC4yMiIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIHN0b3AtY29sb3I9IiNmZmYiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNmZmYiIHN0b3Atb3BhY2l0eT0iMCIvPjwvbGluZWFyR3JhZGllbnQ+CjxsaW5lYXJHcmFkaWVudCBpZD0iZmRjIiB4MT0iMzUuMDEiIHkxPSI0NC4yMiIgeDI9Ijg0Ljc1IiB5Mj0iNDQuMjIiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjZmZmIi8+PHN0b3Agb2Zmc2V0PSIuMTY4IiBzdG9wLWNvbG9yPSIjZmZmIi8+PC9saW5lYXJHcmFkaWVudD4KPC9kZWZzPgo8L3N2Zz4=">
<style>
html,body{margin:0;height:100%;background:#0d0f14}
#frame{border:0;width:100vw;height:100vh;display:block}
</style>
</head>
<body>
<iframe id="frame" title="Smart Requirement Manager"></iframe>
<script>
const BLOBS = {
"""

FOOTER = """
};
const ROUTES = {"home": ["home", null], "dashboard": ["dash", "dashboard"], "config": ["dash", "config"], "review": ["review", null], "followup": ["followup", "followup"], "versions": ["followup", "versions"], "new": ["create", null]};
function b64utf8(s){return decodeURIComponent(Array.prototype.map.call(atob(s),c=>'%'+('00'+c.charCodeAt(0).toString(16)).slice(-2)).join(''));}
const frame = document.getElementById('frame');

/* ============ WORKSPACE — project list + background processing ============ */
function seedProjects(){
  return [
    {id:"stb2026", ref:"STB-2026", name:"Energy Monitoring System", line:"Signalling & Urban", days:23, deadline:1,
     status:"requirement_review", done:10, total:12, updated:"today", primary:true},
    {id:"rfp114", ref:"RFP-2026-114", name:"Urban Line 4 Signalling Upgrade", line:"Signalling & Urban", days:9, deadline:1,
     status:"expert_review", done:34, total:41, updated:"2h ago"},
    {id:"ao088", ref:"AO-2026-088", name:"Depot Maintenance Systems", line:"Services", days:41, deadline:1,
     status:"processing", progress:38, procLabel:"Characterising requirements…", updated:"just now"},
    {id:"stb133", ref:"STB-2026-133", name:"Regional Fleet Telemetry", line:"Rolling stock", days:5, deadline:1,
     status:"qa_versioning", done:58, total:63, updated:"yesterday"},
    {id:"stb2025", ref:"STB-2025-071", name:"Metro Depot Power Supply", line:"Systems", days:-12, deadline:1,
     status:"submitted", reqs:88, updated:"Jun 3"},
  ];
}
let PROJECTS = seedProjects();
let currentProjectId = "stb2026";
window.getProjects = ()=>PROJECTS;
window.getCurrentProject = ()=>PROJECTS.find(p=>p.id===currentProjectId)||null;

/* background processing loop — runs in the shell, survives navigation */
let procTimer=null;
function startProcLoop(){
  if(procTimer) return;
  procTimer=setInterval(()=>{
    let anyActive=false;
    PROJECTS.forEach(p=>{
      if(p.status==="processing"){
        anyActive=true;
        p.progress=(p.progress||0)+ (2+Math.random()*4);
        if(p.progress>=100){
          p.progress=100; p.status="requirement_review";
          p.done=0; p.total=p.total|| (60+Math.floor(Math.random()*40));
          p.updated="just now";
        }else{
          if(p.progress<35) p.procLabel="Capturing requirements…";
          else if(p.progress<70) p.procLabel="Characterising requirements…";
          else p.procLabel="Allocating to experts…";
        }
      }
    });
    if(!anyActive){ clearInterval(procTimer); procTimer=null; }
  }, 700);
}
startProcLoop();

window.addProject = function(meta){
  const id="p"+Date.now().toString(36);
  const manual = meta.mode==="manual";
  const p={ id, ref:meta.ref||("AO-"+id.slice(-4).toUpperCase()), name:meta.name||"Untitled tender",
    line:meta.line||"—", days:meta.days!=null?meta.days:30, deadline:1, updated:"just now" };
  if(manual){ p.status="requirement_review"; p.done=0; p.total=0; }
  else { p.status="processing"; p.progress=3; p.procLabel="Capturing requirements…"; p.total=(60+Math.floor(Math.random()*40)); }
  PROJECTS.unshift(p);
  startProcLoop();
  return id;
};
window.openProject = function(id){
  const p=PROJECTS.find(x=>x.id===id);
  if(!p || p.status==="processing") return;
  currentProjectId=id;
  window.route("dashboard");
};
window.resetDemo = function(){
  PROJECTS = seedProjects();
  currentProjectId="stb2026";
  reviewValidated=false; projectMode='ai'; projectMeta=null;
  aiFeedback.length=0; redactMode='redact';
  if(procTimer){ clearInterval(procTimer); procTimer=null; }
  startProcLoop();
  window.route("home");
};

// ---- shared cross-screen state ----
let reviewValidated = false;
window.isReviewValidated = ()=>reviewValidated;
window.setReviewValidated = (v)=>{ reviewValidated = !!v; };
let projectMode = 'ai';
window.getProjectMode = ()=>projectMode;
window.setProjectMode = (m)=>{ projectMode = m || 'ai'; };
let projectMeta = null;
window.getProjectMeta = ()=>projectMeta;
window.setProjectMeta = (m)=>{ projectMeta = m; };
// AI feedback — accumulated across screens, future-training only
const aiFeedback = [];
window.pushAIFeedback = (f)=>{ aiFeedback.push(Object.assign({at:Date.now()},f)); };
window.getAIFeedback = ()=>aiFeedback;
let redactMode = 'redact';
window.getRedactMode = ()=>redactMode;
window.setRedactMode = (m)=>{ redactMode = m || 'redact'; };
let theme = 'dark';
window.getTheme = ()=>theme;
window.setTheme = (t)=>{ theme = (t==='light')?'light':'dark';
  try{ const fr=document.getElementById('frame'); if(fr&&fr.contentDocument) fr.contentDocument.documentElement.setAttribute('data-theme',theme); }catch(e){}
};
let _sub = null;
function load(routeKey){
  const r = ROUTES[routeKey] || ROUTES['dashboard'];
  _sub = r[1];
  frame.onload = function(){
    try{
      const cw = frame.contentWindow;
      if(_sub === 'config' && cw.showConfig) cw.showConfig(true);
      else if(_sub === 'dashboard' && cw.showConfig) cw.showConfig(false);
      else if(_sub === 'versions' && cw.setScreen) cw.setScreen(3);
      else if(_sub === 'followup' && cw.setScreen) cw.setScreen(2);
    }catch(e){}
  };
  frame.srcdoc = b64utf8(BLOBS[r[0]]);
}
// called from inside the iframe (same-origin srcdoc)
window.route = function(key){
  if(location.hash.slice(1) === key){ load(key); }   // same route: force reload
  else location.hash = key;                            // triggers hashchange -> load
};
const URLMAP = {
  'accueil.html':'home',
  'revue-documentaire.html':'review',
  'suivi-experts-et-versions.html':'followup',
  'suivi-experts-et-versions.html#versions':'versions',
  'dashboard-et-config.html':'dashboard',
  'dashboard-et-config.html#config':'config',
  'creation-projet.html':'new'
};
window.routeUrl = function(u){ window.route(URLMAP[u] || 'dashboard'); };
// moderator shortcut: Ctrl+Shift+R resets the demo
window.addEventListener('keydown', (e)=>{
  if(e.ctrlKey && e.shiftKey && (e.key==='R'||e.key==='r')){ e.preventDefault();
    if(confirm('Reset the demo to its initial state?')) window.resetDemo();
  }
});
window.addEventListener('hashchange', ()=>load(location.hash.slice(1) || 'home'));
load(location.hash.slice(1) || 'home');
</script>
</body>
</html>
"""

def main():
    blob_lines = []
    for key, filename in SOURCES:
        with open(filename, encoding="utf-8") as f:
            html = f.read()
        b64 = base64.b64encode(html.encode("utf-8")).decode("ascii")
        blob_lines.append(f'{key}:"{b64}",')

    body = HEADER + "\n".join(blob_lines) + FOOTER
    for target in (OUTPUT, PAGES_OUTPUT):
        with open(target, "w", encoding="utf-8") as f:
            f.write(body)
    print(f"Wrote {OUTPUT} and {PAGES_OUTPUT} ({len(body)} bytes) from {len(SOURCES)} sources.")

if __name__ == "__main__":
    main()
