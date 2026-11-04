(function(){var IT=__IT__,TP=__TP__,NM={D:'Conductor (D)',I:'Promotor (I)',S:'Apoyo (S)',C:'Analítico (C)'},K='wesser-serie-disc-test';
function ld(){try{return JSON.parse(localStorage.getItem(K)||'{}')||{};}catch(e){return {};}}
function sv(a){try{localStorage.setItem(K,JSON.stringify(a));}catch(e){}}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');}
function init(){var f=document.getElementById('ch-form');if(!f||f.children.length)return;var a=ld(),i;
 for(i=0;i<IT.length;i++){(function(it,n){var d=document.createElement('div');d.className='chq';
  d.innerHTML='<p><b>'+(n+1)+'.</b> '+esc(it[2])+'</p><div class="chr"><label><input type="radio" name="ch'+it[0]+'" value="+"><span>Me describe</span></label><label><input type="radio" name="ch'+it[0]+'" value="-"><span>No me describe</span></label></div>';
  f.appendChild(d);var v=a[it[0]];if(v){var r=d.querySelector('input[value="'+v+'"]');if(r)r.checked=true;}})(IT[i],i);}
 f.addEventListener('change',function(ev){var t=ev.target;if(!t||t.type!=='radio')return;var s=ld();s[t.name.slice(2)]=t.value;sv(s);cnt();});
 document.getElementById('ch-go').addEventListener('click',calc);cnt();if(Object.keys(a).length>=IT.length)calc();}
function cnt(){var a=ld(),n=0,i;for(i=0;i<IT.length;i++){if(a[IT[i][0]])n++;}var c=document.getElementById('ch-cnt');if(c)c.textContent='Respondidas: '+n+' de '+IT.length;return n;}
function calc(){var a=ld(),o=document.getElementById('ch-out'),n=cnt(),i;
 if(n<IT.length){o.innerHTML='<p class="nota" style="color:var(--ink);font-weight:800">Faltan '+(IT.length-n)+' frases por responder.</p>';return;}
 var sc={D:0,I:0,S:0,C:0};for(i=0;i<IT.length;i++){if(a[IT[i][0]]==='+')sc[IT[i][1]]++;}
 var mx=Math.max(sc.D,sc.I,sc.S,sc.C),top=Object.keys(sc).filter(function(k){return sc[k]===mx;});
 var h='<div class="decir cso" style="margin-top:14px"><small>Tu resultado</small><p>'+Object.keys(NM).map(function(k){return NM[k]+': '+sc[k]+' de 9';}).join(' · ')+'.</p><p>Estilo con más frases: <b>'+top.map(function(k){return NM[k];}).join(' y ')+'</b>'+(top.length>1?'. Hay empate: combina las ideas de los estilos empatados.':'.')+' Es una pista para conversar, no un diagnóstico: nadie es un solo estilo.</p></div>';
 top.forEach(function(k){var t=TP[k];h+='<h2 class="lab" style="margin-top:18px">'+esc(t[0])+' · '+esc(t[1])+'</h2><div class="faq">';t[2].forEach(function(x){h+='<div><b>'+esc(x[0])+'</b><p>'+esc(x[1])+'</p></div>';});h+='</div>';});
 o.innerHTML=h;}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
window.addEventListener('hashchange',function(){setTimeout(init,30);});})();
