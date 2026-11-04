import sys,subprocess,re,os
HERE=os.path.dirname(os.path.abspath(__file__)); REPO=os.path.dirname(HERE)
sys.path.insert(0,HERE)
from finish import *
slug,data,h1a,h1b,puesto,dest=sys.argv[1:7]
subprocess.run(['python3','-I',os.path.join(HERE,'build_k.py'),os.path.join(HERE,data),'/tmp/genk_raw.html'],check=True)
raw=open('/tmp/genk_raw.html',encoding='utf8').read()
h=open(os.path.join(REPO,'index.html'),encoding='utf8').read()
i=h.index('href="#%s"'%slug); seg=h[i:i+2500]
icon=re.search(r'<span class="ico"[^>]*><svg[^>]*>(.*?)</svg>',seg,re.S).group(1)
out=finish(raw,icon,puesto)
hh='<h1 tabindex="-1">%s<em>%s</em></h1>'%(h1a,h1b)
assert out.count(hh)==1
out=out.replace(hh,hh.replace('<h1 tabindex="-1">','<h1 tabindex="-1" style="font-size:clamp(34px,11vw,64px)">'))
open(dest,'w',encoding='utf8').write(out); print('ok',len(out))
