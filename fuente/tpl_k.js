
(function(){
  var KEY=__KEY__;
  var GEN=__GEN__;
  var PLAN=__PLAN__;
  var CHULETA=__CHULETA__;
  var MISLAB=__MISLAB__;
  var PLAN_TOTAL=__PLAN_TOTAL__;
  var VIEWS=__VIEWS__;
  var S={};
  function $(id){return document.getElementById(id);}
  function fg(g){var r=[],a=[],i;for(i=0;i<g.k;i++)r.push(null);for(i=0;i<g.q;i++)a.push('');return {r:r,a:a,hecho:false};}
  var storageOk=true;
  try{
    var raw=localStorage.getItem(KEY);
    if(raw){var s0=JSON.parse(raw);
      GEN.forEach(function(g){var v=s0&&s0['g'+g.n];if(v&&v.r&&v.r.length===g.k&&v.a&&v.a.length===g.q)S['g'+g.n]=v;});}
  }catch(e){storageOk=false;}
  GEN.forEach(function(g){if(!S['g'+g.n])S['g'+g.n]=fg(g);});
  function persist(){try{localStorage.setItem(KEY,JSON.stringify(S));return true;}catch(e){storageOk=false;return false;}}
  var msgNo='Tus respuestas no se guardan en este navegador. Cópialas si las quieres conservar.';
  var msgOk='Guardado en este dispositivo. Solo lo ves tú.';
  function filled(arr){return arr.filter(function(x){return x.trim().length>0;}).length;}
  function countG(g){var st=S['g'+g.n],m=0;for(var i=0;i<g.k;i++){if(st.r[i]!==null)m++;}return m+filled(st.a)+(st.hecho?1:0);}
  function tx(v){return (v||'').trim();}
  function planDone(){var n=0;PLAN.forEach(function(g){g[1].forEach(function(r){if(tx(S['g'+r[1]].a[r[2]]))n++;});});return n;}
  function setBar(pre,n,t){
    $(pre+'-prog-txt').textContent=n+' de '+t;
    $(pre+'-bar-i').style.width=(n/t*100)+'%';
    $(pre+'-bar').setAttribute('aria-valuenow',n);
  }
  function renderIndex(){
    GEN.forEach(function(g){
      var c=countG(g);
      $('idx-'+g.n+'-n').textContent=c+' de '+g.T;
      $('idx-'+g.n+'-bar').style.width=(c/g.T*100)+'%';
      $('idx-'+g.n+'-txt').textContent=c===0?'Sin empezar':(c>=g.T?'Completada':'En curso');
    });
    var pn=planDone();
    $('plan-n').textContent=pn+' de '+PLAN_TOTAL+' apartados';
    $('plan-bar').style.width=(pn/PLAN_TOTAL*100)+'%';
  }
  var msgs={
    ok:'Coincide. ',
    ko:'Otra opción también es defendible si sabes por qué. '
  };
  var GR={};
  GEN.forEach(function(g){
    var n=g.n,pre='g'+n,as=[];
    for(var j=0;j<g.q;j++)as.push($(pre+'-a'+j));
    function render(){
      var st=S[pre];
      for(var i=0;i<g.k;i++){
        var bs=$(pre+'-r'+i).querySelectorAll('button');
        for(var k=0;k<bs.length;k++){bs[k].setAttribute('aria-pressed',st.r[i]===+bs[k].getAttribute('data-k')?'true':'false');}
        var fb=$(pre+'-fb'+i);
        if(fb){
          if(st.r[i]===null){fb.textContent='';}
          else if(g.ans[i]===null){fb.textContent=(g.opt&&g.opt[i]&&g.opt[i][st.r[i]])||'';}
          else fb.textContent=(st.r[i]===g.ans[i]?msgs.ok:(g.strict?'Revisa: ':msgs.ko))+g.fb[i];
        }
      }
      if(g.grp){
        var box=$(pre+'-res');
        if(box){
          var p=box.querySelector('p'),tot=0,ans=0,best=-1,bi=0,parts=[];
          g.grp.forEach(function(gr,gi){
            var c=0;
            gr.i.forEach(function(ix){if(st.r[ix]!==null)ans++;if(st.r[ix]===0)c++;});
            tot+=c;parts.push(gr.n+' '+c+' de '+gr.i.length);
            var ratio=c/gr.i.length;if(ratio>best){best=ratio;bi=gi;}
          });
          if(ans<g.k){p.textContent=ans===0?'Marca los síntomas para ver tu resultado.':'Llevas '+ans+' de '+g.k+'. Sigue marcando para ver tu resultado.';}
          else if(tot===0){p.textContent='No has marcado ningún síntoma. Puedes seguir las píldoras en el orden normal.';}
          else{p.innerHTML=parts.join(' · ')+'. Lo que más pesa: '+g.grp[bi].n.toLowerCase()+'. '+g.grp[bi].r;}
        }
      }
      setBar(pre,countG(g),g.T);
    }
    GR[n]=render;
    Array.prototype.forEach.call(document.querySelectorAll('#view-pildora-'+n+' .zs button'),function(b){
      b.addEventListener('click',function(){
        var i=+b.getAttribute('data-i'),k=+b.getAttribute('data-k');
        S[pre].r[i]=S[pre].r[i]===k?null:k;render();renderIndex();persist();
      });
    });
    var tm=null;
    as.forEach(function(el,j){
      el.value=S[pre].a[j]||'';
      el.addEventListener('input',function(){
        S[pre].a[j]=el.value;render();renderIndex();
        clearTimeout(tm);tm=setTimeout(function(){$(pre+'-save').textContent=persist()?msgOk:msgNo;},500);
      });
    });
    var hb=$(pre+'-hecho');
    if(hb){hb.checked=!!S[pre].hecho;hb.addEventListener('change',function(){S[pre].hecho=this.checked;render();renderIndex();persist();});}
    if(!storageOk)$(pre+'-save').textContent=msgNo;
    var box=$(pre+'-reset');
    function show(){
      box.innerHTML='<button class="btn" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8" /> <path d="M3 3v5h5" /></svg>Empezar esta píldora de nuevo</button>';
      box.querySelector('button').addEventListener('click',conf);
    }
    function conf(){
      box.innerHTML='<span>¿Borrar tus respuestas de esta píldora?</span><button class="btn danger" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 11v6" /> <path d="M14 11v6" /> <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6" /> <path d="M3 6h18" /> <path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" /></svg>Sí, borrar</button><button class="btn" type="button">Cancelar</button>';
      var bs=box.querySelectorAll('button');
      bs[0].addEventListener('click',function(){
        S[pre]=fg(g);as.forEach(function(el){el.value='';});if(hb)hb.checked=false;
        $(pre+'-save').textContent='Respuestas borradas.';persist();render();renderIndex();show();
      });
      bs[1].addEventListener('click',show);
    }
    show();render();
  });

  /* hoja final */
  function planText(){
    var out=[__PLAN_TITLE__+' · Serie «'+__SERIE_NOMBRE__+'»',''];
    CHULETA.forEach(function(g){out.push(g[0]);g[1].forEach(function(r){out.push('- '+r[0]+': '+r[1]);});out.push('');});
    if(CHULETA.length&&planDone()>0){out.push(MISLAB.toUpperCase());out.push('');}
    PLAN.forEach(function(g){
      var l=[];
      g[1].forEach(function(r){var v=tx(S['g'+r[1]].a[r[2]]);if(v)l.push('- '+r[0]+': '+v);});
      if(l.length){out.push(g[0]);out=out.concat(l);out.push('');}
    });
    return out.join('\n').trim();
  }
  function pad(n){return ('0'+n).slice(-2);}
  function renderPlan(){
    var box=$('plan-body');box.innerHTML='';
    CHULETA.forEach(function(g){
      var sec=document.createElement('section');sec.className='pg';
      var h=document.createElement('h2');h.className='lab';h.textContent=g[0];sec.appendChild(h);
      g[1].forEach(function(r){
        var d=document.createElement('div');d.className='pr';
        var sm=document.createElement('small'),sp=document.createElement('span');sp.textContent=r[0];sm.appendChild(sp);d.appendChild(sm);
        var p=document.createElement('p');p.textContent=r[1];d.appendChild(p);sec.appendChild(d);
      });
      box.appendChild(sec);
    });
    if(CHULETA.length){var hh=document.createElement('h2');hh.className='lab';hh.style.marginTop='28px';hh.textContent=MISLAB;box.appendChild(hh);}
    PLAN.forEach(function(g){
      var sec=document.createElement('section');sec.className='pg';
      var h=document.createElement('h2');h.className='lab';h.textContent=g[0];sec.appendChild(h);
      g[1].forEach(function(r){
        var v=tx(S['g'+r[1]].a[r[2]]),d=document.createElement('div');d.className='pr'+(v?'':' vacio');
        var sm=document.createElement('small'),sp=document.createElement('span');sp.textContent=r[0];
        var a=document.createElement('a');a.href='#pildora-'+r[1];a.textContent=(v?'Editar · ':'')+'Píldora '+pad(r[1]);
        sm.appendChild(sp);sm.appendChild(a);d.appendChild(sm);
        var p=document.createElement('p');
        if(v){p.textContent=v;}
        else{p.appendChild(document.createTextNode('Pendiente. '));var l=document.createElement('a');l.href='#pildora-'+r[1];l.textContent='Complétalo en la píldora '+pad(r[1]);p.appendChild(l);}
        d.appendChild(p);sec.appendChild(d);
      });
      box.appendChild(sec);
    });
    var n=planDone();
    $('plan-prog-txt').textContent=n+' de '+PLAN_TOTAL;
    $('plan-pbar-i').style.width=(n/PLAN_TOTAL*100)+'%';
    $('plan-pbar').setAttribute('aria-valuenow',n);
    updateWa();
  }
  /* ---- Generar PDF y compartir por WhatsApp ---- */
  function planHasContent(){return planDone()>0;}
  function pdfEnc(s){
    var M={'€':128,'‚':130,'„':132,'…':133,'‘':145,'’':146,'“':147,'”':148,'•':149,'–':150,'—':151,'™':153},o='',i,c,ch;
    s=String(s).normalize('NFC');
    for(i=0;i<s.length;i++){ch=s.charAt(i);c=s.charCodeAt(i);
      if(M[ch])c=M[ch];else if(c>255||(c>126&&c<160))c=(ch===' '?32:63);
      if(c===92||c===40||c===41)o+='\\';
      o+=String.fromCharCode(c);}
    return o;
  }
  function pdfBuild(){
    var W=595,H=842,MX=48,TOP=70,BOT=60,cv=document.createElement('canvas').getContext('2d');
    var RED='0.702 0.059 0.078',INK='0.082 0.075 0.075',MUT='0.357 0.333 0.318',LINE='0.867 0.843 0.812';
    var pages=[],cur=null,y=0;
    function np(){cur=[];pages.push(cur);cur.push('0.898 0.106 0.106 rg 0 '+(H-10)+' '+W+' 10 re f');y=H-TOP;}
    function wid(s,bold,size){cv.font=(bold?'bold ':'')+'100px Arial, Helvetica, sans-serif';return cv.measureText(s).width*size/100;}
    function wrap(t,bold,size,maxW){
      var out=[];String(t).split('\n').forEach(function(p){
        var words=p.split(/\s+/).filter(Boolean),ln='';
        if(!words.length){out.push('');return;}
        words.forEach(function(w){
          var tr=ln?ln+' '+w:w;
          if(wid(tr,bold,size)<=maxW||!ln){ln=tr;}else{out.push(ln);ln=w;}
        });
        out.push(ln);});
      return out;
    }
    function txt(x,yy,f,size,col,s){cur.push('BT /'+f+' '+size+' Tf '+col+' rg '+x+' '+yy.toFixed(1)+' Td ('+pdfEnc(s)+') Tj ET');}
    function need(h){if(y-h<BOT)np();}
    np();
    /* logo */
    var img=document.querySelector('.logo img'),logo=null,lh=0,lw=0;
    try{
      if(img&&img.naturalWidth){
        var c=document.createElement('canvas');c.width=img.naturalWidth;c.height=img.naturalHeight;
        var g=c.getContext('2d');g.fillStyle='#fff';g.fillRect(0,0,c.width,c.height);g.drawImage(img,0,0);
        var b64=c.toDataURL('image/jpeg',0.92).split(',')[1],bin=atob(b64);
        lh=40;lw=lh*c.width/c.height;logo={w:c.width,h:c.height,data:bin};
      }
    }catch(e){logo=null;}
    var serie=(VIEWS.inicio&&VIEWS.inicio[1])||'',head=planText().split('\n')[0].split(' · ')[0];
    if(logo){cur.push('q '+lw.toFixed(1)+' 0 0 '+lh+' '+MX+' '+(y-lh+14)+' cm /Im1 Do Q');y-=lh+8;}
    y-=14;txt(MX,y,'F2',22,RED,head);
    y-=18;txt(MX,y,'F1',10.5,MUT,'Serie «'+serie+'» · '+new Date().toLocaleDateString('es-ES'));
    y-=14;cur.push(LINE+' RG 1 w '+MX+' '+y+' m '+(W-MX)+' '+y+' l S');y-=24;
    var SECS=CHULETA.map(function(g){return [g[0],g[1].map(function(r){return [r[0],r[1],true];})];}).concat(PLAN.map(function(g){return [g[0],g[1].map(function(r){return [r[0],tx(S['g'+r[1]].a[r[2]]),false];})];}));
    SECS.forEach(function(g){
      need(70);
      txt(MX,y,'F2',13,RED,g[0].toUpperCase());y-=7;
      cur.push(LINE+' RG 0.8 w '+MX+' '+y+' m '+(W-MX)+' '+y+' l S');y-=18;
      g[1].forEach(function(r){
        var v=r[1],lab=wrap(r[0],true,10,W-2*MX),val=v?wrap(v,false,11,W-2*MX):['Pendiente'];
        need((lab.length*13)+(val.length*15)+14);
        lab.forEach(function(l){txt(MX,y,'F2',10,MUT,l);y-=13;});
        val.forEach(function(l){txt(MX,y,v?'F1':'F3',11,v?INK:MUT,l);y-=15;});
        y-=9;
      });
      y-=8;
    });
    var n=pages.length;
    pages.forEach(function(p,i){
      cur=p;
      cur.push(LINE+' RG 0.8 w '+MX+' 44 m '+(W-MX)+' 44 l S');
      txt(MX,30,'F1',8,MUT,'Formación y Desarrollo · Serie «'+serie+'»');
      var pg='Página '+(i+1)+' de '+n;txt(W-MX-wid(pg,false,8),30,'F1',8,MUT,pg);
    });
    /* objetos */
    var objs=[],k;
    objs[1]='<< /Type /Catalog /Pages 2 0 R >>';
    objs[3]='<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>';
    objs[4]='<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>';
    objs[5]='<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>';
    var next=6,imgNo=0;
    if(logo){imgNo=next++;objs[imgNo]='<< /Type /XObject /Subtype /Image /Width '+logo.w+' /Height '+logo.h+' /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length '+logo.data.length+' >>\nstream\n'+logo.data+'\nendstream';}
    var kids=[];
    pages.forEach(function(p){
      var pn=next++,cn=next++,body=p.join('\n');
      kids.push(pn+' 0 R');
      objs[pn]='<< /Type /Page /Parent 2 0 R /MediaBox [0 0 '+W+' '+H+'] /Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >>'+(imgNo?' /XObject << /Im1 '+imgNo+' 0 R >>':'')+' >> /Contents '+cn+' 0 R >>';
      objs[cn]='<< /Length '+body.length+' >>\nstream\n'+body+'\nendstream';
    });
    objs[2]='<< /Type /Pages /Kids ['+kids.join(' ')+'] /Count '+n+' >>';
    var out='%PDF-1.4\n',offs=[];
    for(k=1;k<next;k++){offs[k]=out.length;out+=k+' 0 obj\n'+objs[k]+'\nendobj\n';}
    var xr=out.length;
    out+='xref\n0 '+next+'\n0000000000 65535 f \n';
    for(k=1;k<next;k++){out+=('0000000000'+offs[k]).slice(-10)+' 00000 n \n';}
    out+='trailer\n<< /Size '+next+' /Root 1 0 R >>\nstartxref\n'+xr+'\n%%EOF';
    var u=new Uint8Array(out.length);for(k=0;k<out.length;k++)u[k]=out.charCodeAt(k)&255;
    return new Blob([u],{type:'application/pdf'});
  }
  var pdfUrl=null;
  $('plan-pdf').addEventListener('click',function(){
    var msg=$('plan-msg');
    if(!planHasContent()){msg.textContent='Todavía no hay nada que incluir: completa alguna píldora.';return;}
    try{
      var blob=pdfBuild(),name=((VIEWS.inicio&&VIEWS.inicio[1])||'plan').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')+'-mi-plan.pdf';
      if(pdfUrl)try{URL.revokeObjectURL(pdfUrl);}catch(e){}
      pdfUrl=URL.createObjectURL(blob);
      var a=document.createElement('a');a.href=pdfUrl;a.download=name;document.body.appendChild(a);a.click();document.body.removeChild(a);
      msg.innerHTML='';msg.appendChild(document.createTextNode('PDF generado ('+name+'). Si no se ha descargado, '));
      var l=document.createElement('a');l.href=pdfUrl;l.target='_blank';l.rel='noopener';l.textContent='ábrelo aquí';msg.appendChild(l);msg.appendChild(document.createTextNode('.'));
    }catch(e){msg.textContent='No se ha podido generar el PDF en este dispositivo. Usa «Compartir por WhatsApp» para enviarte el texto.';}
  });
  function waText(){
    var t=planText()+'\n\nFormación y Desarrollo · Wesser';
    if(t.length>3500)t=t.slice(0,3500).replace(/\s+\S*$/,'')+'…';
    return t;
  }
  function updateWa(){var a=$('plan-wa');if(a)a.href=planHasContent()?'https://wa.me/?text='+encodeURIComponent(waText()):'https://wa.me/';}
  $('plan-wa').addEventListener('click',function(e){
    if(!planHasContent()){e.preventDefault();$('plan-msg').textContent='Todavía no hay nada que compartir: completa alguna píldora.';return;}
    updateWa();$('plan-msg').textContent='Se abrirá WhatsApp con tu plan en texto. Elige a quién enviarlo.';
  });

  /* rutas por hash */
  function route(focus){
    var h=(location.hash||'').replace('#','');
    if(!VIEWS[h])h='inicio';
    Object.keys(VIEWS).forEach(function(k){$('view-'+k).hidden=(k!==h);});
    $('tag-b').textContent=VIEWS[h][0];$('tag-a').textContent=VIEWS[h][1];$('tag-s').textContent=VIEWS[h][2];
    if(h==='mi-kit')renderPlan();
    window.scrollTo(0,0);
    if(focus){var t=$('view-'+h).querySelector('h1');if(t)t.focus({preventScroll:true});}
  }
  window.addEventListener('hashchange',function(){route(true);});
  renderIndex();route(false);
})();
