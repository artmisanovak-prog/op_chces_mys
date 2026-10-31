from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json, html, uuid

BASE=Path(__file__).parent
DATA=BASE/"data"; RECORDS=BASE/"records"; RECORDS.mkdir(exist_ok=True)
def esc(x): return html.escape(str(x))
def read(p):
    try: return json.loads(p.read_text(encoding="utf-8"))
    except Exception: return None
def tasks():
    out=[]
    for p in sorted(DATA.glob("*.json")):
        d=read(p)
        if isinstance(d,dict) and "train" in d and "test" in d: out.append((p.stem,p.name,d))
    return out
def records(t):
    x=read(RECORDS/(t+".json")); return x if isinstance(x,list) else []
def grid(g,label):
    if not g: return "<p>"+esc(label)+": žádná mřížka</p>"
    s="<div><small>"+esc(label)+"</small><table style='border-collapse:collapse;margin:5px 0 15px'>"
    for row in g:
        s+="<tr>"
        for v in row:
            colors=["#fff","#0074D9","#2ECC40","#FF4136","#FFDC00","#aaa","#F012BE","#FF851B","#7FDBFF","#870C25"]
            s+=f"<td style='border:1px solid #aaa;background:{colors[int(v)]};width:26px;height:26px;text-align:center'>{v}</td>"
        s+="</tr>"
    return s+"</table></div>"
def page(task=None):
    ts=tasks()
    links="<p>Zatím žádné úlohy.</p>" if not ts else "<ul>"+"".join(
        f"<li><a href='/?task={esc(t)}'>{esc(n)}</a> ({len(d['train'])} ukázek, {len(d['test'])} testů)</li>" for t,n,d in ts)+"</ul>"
    detail=""
    if task:
        found=next(((t,n,d) for t,n,d in ts if t==task),None)
        if found:
            t,n,d=found; chunks=[f"<h2>Úloha {esc(n)}</h2>"]
            for i,p in enumerate(d["train"],1):
                chunks.append(f"<h3>Ukázka {i}</h3><div style='display:flex;gap:25px;flex-wrap:wrap'>{grid(p.get('input'),'Vstup')}{grid(p.get('output'),'Výstup')}</div>")
            for i,p in enumerate(d["test"],1): chunks.append(f"<h3>Test {i}</h3>{grid(p.get('input'),'Vstup')}")
            chunks.append(f"""<h3>Přidat záznam myši</h3><form method='post' action='/record'>
<input type='hidden' name='task' value='{esc(t)}'>
Typ: <select name='kind'><option>property</option><option>relation</option><option>uncertainty</option><option>source</option></select>
Stav: <select name='status'><option>observed</option><option>derived</option><option>unresolved</option><option>contradicted</option></select><p>
Popis/tvrzení: <input name='claim' required style='width:70%'></p>
Evidence (např. train[0].input): <input name='evidence' style='width:60%'><p>
Metoda: <input name='method' style='width:60%'></p>
Poznámky: <br><textarea name='notes' style='width:90%;height:65px'></textarea><p><button>Uložit záznam</button></p></form><h3>Uložené záznamy</h3>""")
            rs=records(t)
            chunks += [f"<section style='border:1px solid #ddd;padding:10px;margin:8px 0'><b>{esc(r.get('kind'))} / {esc(r.get('status'))}</b><p>{esc(r.get('claim'))}</p><small>Evidence: {esc(r.get('evidence'))} · Metoda: {esc(r.get('method'))}</small><p>{esc(r.get('notes'))}</p></section>" for r in rs]
            detail="".join(chunks)
    return """<!doctype html><html lang='cs'><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>Myš + ARC-AGI-2</title><style>body{font:16px system-ui;max-width:1100px;margin:25px auto;padding:0 16px;background:#f7f7f4;color:#222}section,main{background:white;border:1px solid #ddd;border-radius:10px;padding:15px;margin:12px 0}header{background:#222722;color:white;padding:16px;border-radius:10px}input,select,textarea,button{font:inherit;padding:7px;margin:4px}button{background:#222722;color:white;border:0;border-radius:5px;cursor:pointer}a{color:#145c9e}</style>
<header><h1>Myš + ARC-AGI-2</h1>Lokální repozitář a evidence. Myš není AI.</header><main><h2>Načtené úlohy</h2>
<p>Pro přidání úloh zkopíruj JSON soubory do složky <code>data</code> a obnov stránku.</p>"""+links+detail+"""<hr><p><b>Stavy:</b> observed = přímo v datech; derived = odvozené; unresolved = nevyřešené; contradicted = rozpor.</p><p>Vše zůstává lokálně. Neznámé není totéž co nula a důvod chybějícího údaje se nesmí domýšlet.</p></main></html>"""
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        q=parse_qs(urlparse(self.path).query); body=page(q.get("task",[None])[0]).encode()
        self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_POST(self):
        n=int(self.headers.get("Content-Length","0")); f=parse_qs(self.rfile.read(n).decode())
        v=lambda k:f.get(k,[""])[0].strip()
        t="".join(c for c in v("task") if c.isalnum() or c in "-_")
        r=records(t); r.append({"id":str(uuid.uuid4()),"task_id":t,"kind":v("kind"),"status":v("status"),"claim":v("claim"),"evidence":v("evidence"),"method":v("method"),"notes":v("notes")})
        (RECORDS/(t+".json")).write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding="utf-8")
        self.send_response(303); self.send_header("Location","/?task="+t); self.end_headers()
    def log_message(self,*args): pass
if __name__=="__main__":
    print("Otevři http://127.0.0.1:8000 — ukončení Ctrl+C")
    HTTPServer(("127.0.0.1",8000),H).serve_forever()
