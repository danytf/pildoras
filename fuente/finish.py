import os
import re,sys
SKEL='<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n'
PARA_CSS='<style id="para-puesto">.card small.para{display:inline-flex;width:fit-content;border:1.5px solid var(--red);color:var(--red-text);border-radius:999px;padding:2px 10px;font-size:13.5px;font-weight:700;letter-spacing:0;text-transform:none;line-height:1.35;margin-top:6px}</style>\n'
ICO_CSS='<style id="serie-ico">.serie-ico{width:52px;height:52px;border-radius:var(--r,8px);background:var(--red);color:#fff;display:flex;align-items:center;justify-content:center;margin:22px 0 14px}</style>'
def finish(raw,icon_paths,puesto,puesto_title=None):
    s=raw[raw.index('<title>'):]
    s=s.replace('</head><body>','',1)
    assert s.rstrip().endswith('</body></html>')
    s=s.rstrip()[:-len('</body></html>')]
    t=' title="%s"'%puesto_title if puesto_title else ''
    s=re.sub(r'(<h3>[^<]*</h3><small>[^<]*· [^<]*min</small>)',lambda m:m.group(1)+'<small class="para"%s>Dirigida a: %s</small>'%(t,puesto),s)
    ico='<span class="serie-ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg></span>'%icon_paths
    pat=re.compile(r'(<div id="view-inicio" class="view">\s*<main class="wrap">)(\s*)(<h1 tabindex="-1">)')
    assert len(pat.findall(s))==1
    s=pat.sub(lambda m:m.group(1)+m.group(2)+ico+m.group(2)+m.group(3),s)
    snip=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'pasos.html'),encoding='utf8').read().strip()
    return SKEL+PARA_CSS_PLACE(s)+'\n'+ICO_CSS+snip+'\n</body></html>'
def PARA_CSS_PLACE(s):
    # tras el primer bloque <style>…</style> principal
    i=s.index('</style>')+len('</style>')
    return s[:i]+'\n'+PARA_CSS+s[i:]
if __name__=='__main__':
    pass
