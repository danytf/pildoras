# -*- coding: utf-8 -*-
import html
def e(s): return html.escape(s, quote=True)
def T(label, hint, tips, ks=(0, 1)):
    return (label, hint, tips if isinstance(tips, dict) else {k: tips for k in ks})
def I(label, hint, ans, fb):
    return (label, hint, ans, fb)

KEY = 'wesser-serie-sesgos'
EQ = [
 ('Laura', '2 años y 3 meses', '30 → 27 → 29', '21', 'Buena', 'Laura es un regalo. Lleva mucho tiempo y prácticamente no tienes que estar encima.'),
 ('Dani', '6 meses', '24 → 27 → 33', '22', 'Mejorable', 'Dani es de la vieja escuela. Tiene hambre, pregunta y quiere crecer.'),
 ('Sara', '1 año y 2 meses', '31 → 30 → 31', '25', 'Muy buena', 'Sara va haciendo. Para estar contenta necesita salir a las 13 h; empieza antes.'),
 ('Marcos', '3 meses', '— → 26 → 22', '19', 'Correcta', 'Con Marcos tengo dudas. Hay que repetirle cosas y no muestra ambición.'),
 ('Ana', '1 año y 8 meses', '34 → 36 → 35', '26', 'Buena', 'Ana es muy fiable. Dale una campaña cada mes y sabes que la va a sacar adelante.'),
]
def tarjetas():
    o = ['<div class="eq" role="list">']
    for n, a, u, m, c, t in EQ:
        o.append('<div class="cap" role="listitem"><h4>%s</h4><dl><div><dt>Antigüedad</dt><dd>%s</dd></div><div><dt>Calidad</dt><dd>%s</dd></div>'
                 '<div><dt>Socios, últimos 3 meses</dt><dd>%s</dd></div><div><dt>Socios este mes, hasta hoy</dt><dd>%s</dd></div></dl>'
                 '<p class="cm"><small>Comentario del anterior RE</small>«%s»</p></div>' % (e(n), e(a), e(c), e(u), e(m), e(t)))
    o.append('</div>')
    return ''.join(o)

STYLE = """.eq{display:grid;gap:10px;margin-top:12px}
.cap{background:var(--surface);border:2px solid var(--line);border-radius:var(--r);padding:12px 14px;min-width:0}
.cap h4{margin:0;font-family:var(--f-display);font-size:26px;text-transform:uppercase;letter-spacing:.8px;line-height:1.05}
.cap dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 12px;margin:8px 0 0}
.cap dl>div{min-width:0}.cap dt{font-size:12.5px;font-weight:700;color:var(--muted);line-height:1.25}
.cap dd{margin:2px 0 0;font-weight:800;font-size:15.5px;overflow-wrap:anywhere}
.cap .cm{margin:10px 0 0;padding:8px 12px;background:var(--tint);border-left:5px solid var(--red);border-radius:0 var(--r) var(--r) 0;font-size:15.5px;line-height:1.4;font-weight:600}
.cap .cm small{display:block;font-family:var(--f-display);font-weight:800;letter-spacing:.8px;text-transform:uppercase;color:var(--red-text);font-size:13.5px;margin-bottom:2px}
.cnt{margin-top:12px;background:var(--tint);border:2px solid var(--red);border-radius:var(--r);padding:10px 14px;font-weight:800;font-size:16px;line-height:1.4}
.cnt[data-over="1"]{background:var(--bg)}"""

SCRIPT = """(function(){var KEY=%s;var N=['Laura','Dani','Sara','Marcos','Ana'];
function st(){try{return JSON.parse(localStorage.getItem(KEY)||'{}')||{};}catch(e){return {};}}
function upd(){var s=st(),a=(s.g4&&s.g4.r)||[],b=(s.g5&&s.g5.r)||[],c=document.getElementById('cv-cnt'),r=document.getElementById('cv-res');
 if(c){var u=0,i;for(i=0;i<5;i++){if(a[i]===0)u++;}
  c.setAttribute('data-over',u>4?'1':'0');
  c.textContent=u>4?'Has marcado '+u+' acompañamientos y solo tienes 4 turnos. Deja a alguien fuera o en reserva.':'Turnos asignados: '+u+' de 4. '+(u<4?'Quedan '+(4-u)+' en reserva.':'No queda ninguno en reserva.');}
 if(r){var p=r.querySelector('p'),ac=[],ch=[],ans=0,i;
  for(i=0;i<5;i++){if(a[i]===0)ac.push(N[i]);if(b[i]!==null&&b[i]!==undefined)ans++;if(b[i]===1)ch.push(N[i]);}
  var first=a.filter(function(x){return x===0||x===1;}).length;
  if(first<1){p.textContent='Primero reparte los turnos en la píldora 4: marca a quién acompañas.';}
  else if(ans<5){p.textContent='Tu primer reparto: acompañabas a '+(ac.join(', ')||'nadie')+'. Marca ahora si mantienes o cambias cada decisión.';}
  else if(ch.length===0){p.textContent='Tu primer reparto: acompañabas a '+(ac.join(', ')||'nadie')+'. No has cambiado ninguna decisión. Pregúntate qué información te habría hecho cambiar y si la habrías pedido antes de decidir.';}
  else{p.textContent='Tu primer reparto: acompañabas a '+(ac.join(', ')||'nadie')+'. Has cambiado '+ch.length+' de 5 decisiones ('+ch.join(', ')+') al conocer más. Cada cambio señala algo que dabas por cierto y era una interpretación, no un dato.';}}}
document.addEventListener('click',function(ev){if(ev.target.closest&&ev.target.closest('.zs button'))setTimeout(upd,30);});
window.addEventListener('hashchange',function(){setTimeout(upd,30);});setTimeout(upd,60);})();""" % ("'%s'" % KEY)

SERIE = dict(
    key=KEY, dur='3-4 min',
    nombre1='Sesgos inconscientes', nombre2='en tu equipo',
    sub='Cómo decidir sobre las personas de tu equipo con más datos y menos automatismos',
    intro=('Esta serie va dirigida a Responsables de Equipo (RE) y forma parte del Plan de Igualdad de Wesser. Cada semana tomas decenas de pequeñas decisiones sobre tu equipo: a quién acompañas, qué cuentas de cada persona al RP, cómo explicas un buen o un mal dato y a quién animas a crecer. '
           'Empiezas por un caso: heredas un equipo y reparten cuatro turnos; después conoces seis sesgos con ejemplos y una pregunta para comprobar cada uno. '
           'Son 12 píldoras de 3 a 4 minutos y cada una se entiende sola, aunque conviene hacer antes las píldoras 4 y 5.'),
    aviso=('No es una evaluación de ti ni dice que haya discriminación: todas las personas tenemos sesgos. Los casos son ficticios y no describen procesos reales de Wesser. Reconocerlos no sustituye a hablar con quien corresponda en Wesser si necesitas plantear una situación real.'),
    glosario=[
        ('RE y RP', 'Responsable de Equipo y Responsable Provincial, a quien el RE traslada su valoración del equipo.'),
        ('Sesgo inconsciente', 'Creencia o suposición adquirida que puede actuar sin que nos demos cuenta y teñir cómo juzgamos.'),
        ('Evidencia', 'Dato o conducta concreta que otra persona también podría comprobar.'),
        ('Interpretación', 'La explicación que damos a un dato: puede ser correcta, pero hay que comprobarla.'),
        ('Criterio común', 'Lo que esperas del puesto, definido antes de valorar y aplicado igual a todas las personas.'),
        ('Segunda mirada', 'Pedir a otra persona que revise los hechos en los que apoyas tu decisión.'),
    ],
    tema=[
        ('Cómo decidimos', 'Atajos del cerebro, comprobar lo evidente y qué te hace vulnerable como RE. Píldoras 1 a 3.'),
        ('Un caso: heredas un equipo', 'Reparte cuatro turnos, recibe información nueva y mira qué cambia. Píldoras 4 y 5.'),
        ('Seis sesgos', 'Metasesgo, simpatía, rendimiento, atribución, afinidad y maternidad o paternidad. Píldoras 6 a 11.'),
        ('Para terminar', 'Cómo una expectativa se cumple sola y tu ficha «¿Qué sé y qué estoy suponiendo?». Píldora 12.'),
    ],
    ruta=[2, 4, 5, 9, 12],
    chuleta=[
        ('Antes de decidir sobre una persona', [
            ('¿Qué sé?', 'Hechos que otra persona también podría ver o comprobar.'),
            ('¿Qué estoy suponiendo?', 'Explicaciones, etiquetas o expectativas que no he comprobado.'),
            ('¿Qué dato me falta?', 'Contexto: campaña, localización, acompañamiento recibido, serie de meses.'),
            ('¿Qué criterio común aplico?', 'Lo que espero del puesto, igual para todas las personas.'),
            ('¿Quién me da una segunda mirada?', 'Alguien que revise los hechos, también cuando estoy muy seguro.'),
        ]),
        ('Seis sesgos de un vistazo', [
            ('Metasesgo', 'Creo que mis valoraciones son más objetivas que las de otros. Reducirlo: revisar qué hechos sostienen la decisión y pedir una segunda mirada.'),
            ('Simpatía', 'Valoro mejor a quien me resulta agradable. Reducirlo: valorar las mismas conductas con criterios comunes.'),
            ('Rendimiento', 'El mismo resultado se valora distinto según lo que esperaba de cada persona. Reducirlo: definir antes qué espero del puesto y mirar series y contexto.'),
            ('Atribución', 'Explico un dato por cómo es la persona y no por sus circunstancias. Reducirlo: separar el hecho de la explicación y preguntar.'),
            ('Afinidad', 'Favorezco a quien se parece a mí o trabaja como yo. Reducirlo: definir qué conductas requiere el puesto y comprobarlas en estilos distintos.'),
            ('Maternidad o paternidad', 'Supongo disponibilidad o compromiso por las responsabilidades de cuidado. Reducirlo: explicar los requisitos y preguntar igual a todas las personas.'),
        ]),
        ('Cuatro decisiones donde aparecen', [
            ('Acompañamiento', '¿A quién dedico más tiempo y por qué?'),
            ('Feedback', '¿Qué traslado al RP sobre cada persona y con qué hechos?'),
            ('Resultados', '¿Qué explicación doy a un buen o a un mal dato?'),
            ('Crecimiento', '¿A quién animo a asumir más responsabilidad y a quién no se lo he preguntado?'),
        ]),
    ],
    plan=[
        ('Mi caso: heredo un equipo', [('Mi reparto de turnos y por qué', 4, 0), ('Qué tendría que pasar para asignar la reserva', 4, 1), ('Qué decisión he cambiado y por qué dato', 5, 0), ('Qué comentario era una interpretación', 5, 1)]),
        ('Mis sesgos', [('Metasesgo: dónde puede actuar', 6, 0), ('Metasesgo: mi comprobación', 6, 1), ('Simpatía: dónde puede actuar', 7, 0), ('Simpatía: mi criterio común', 7, 1),
                        ('Rendimiento: dónde puede actuar', 8, 0), ('Rendimiento: lo que definiré antes', 8, 1), ('Atribución: dónde puede actuar', 9, 0), ('Atribución: lo que preguntaré', 9, 1),
                        ('Afinidad: dónde puede actuar', 10, 0), ('Afinidad: lo que comprobaré', 10, 1), ('Maternidad o paternidad: dónde puede actuar', 11, 0), ('Maternidad o paternidad: lo que preguntaré', 11, 1)]),
        ('Mi decisión de esta semana', [('La decisión sobre una persona', 12, 0), ('Lo que sé y lo que supongo', 12, 1), ('El dato que me falta o la segunda mirada', 12, 2)]),
    ],
    plan_tag='MI FICHA', plan_nombre='Mi ficha de decisión', plan_mis='Lo que has escrito',
    plan_card='Una ficha con las cinco preguntas antes de decidir, los seis sesgos y lo que has escrito en cada píldora.',
    plan1='Mi ficha', plan2='de decisión',
    plan_sub='Tus cinco preguntas y tus compromisos, en una sola hoja',
    plan_gancho='Arriba tienes las chuletas de consulta. Debajo se rellenan tus respuestas; lo que falta aparece como pendiente, con un enlace a la píldora donde se completa. Solo la ves tú.',
    plan_rev='Revisa esta ficha antes de tu próxima decisión importante sobre una persona de tu equipo: qué sabes, qué supones y qué te falta.',
    plan_frase='¿Qué sé… y qué estoy suponiendo?',
    plan_titulo_texto='Mi ficha de decisión · Sesgos inconscientes en tu equipo',
    style_extra=STYLE, script_extra=SCRIPT,
)

def sesgo(n, area, t1, t2, idx, idxp, gancho, noT, siT, caso, rl, items, extra, error, qs, acc, chk, rev, frase, glos=None, clab='¿Se ve el sesgo?', clead='Marca si el ejemplo muestra el sesgo.', **kw):
    d = dict(n=n, area=area, t1=t1, t2=t2, idx=idx, idx_corto=kw.pop('idx_corto', idx), idxp=idxp, gancho=gancho, noT=noT, siT=siT, caso=caso,
             clab=clab, clead=clead, rl=rl, items=items, extra=extra, error=error, plead=kw.pop('plead', 'Piensa en tu equipo de esta semana.'),
             q=qs, acc=acc, chk=chk, rev=rev, frase=frase, estricto=True)
    if glos: d['glos'] = glos
    d.update(kw)
    return d

PILDORAS = [
 dict(n=1, area='Cómo decidimos', t1='Decidimos', t2='por atajos', idx='Decidimos por atajos', idx_corto='Atajos',
  idxp='El cerebro simplifica para ahorrar energía; eso no es culpa de nadie.',
  gancho='Cada semana tomas decenas de pequeñas decisiones sobre tu equipo. Casi todas las tomas rápido y sin darte cuenta, y eso no es un defecto: es cómo funciona el cerebro.',
  noT='Pensar que tener sesgos es un fallo personal o que solo les pasa a otras personas.',
  siT='Saber que el cerebro simplifica la realidad para ahorrar energía y que, si no comprobamos los hechos, podemos repetir el mismo error al decidir.',
  caso='Ves a un captador nuevo hablar con soltura en su primer turno y piensas «este va a llegar lejos». No lo has comprobado: has completado la historia con lo que ya sabías. Es un atajo útil para cruzar la calle y poco fiable para decidir a quién acompañas.',
  glos=[('Sistema 1', 'rápido, automático e intuitivo'), ('Sistema 2', 'lento, analítico y deliberado')],
  clab='¿Sistema 1 o Sistema 2?', clead='Marca con qué sistema se hace cada cosa.', rl=['Sistema 1', 'Sistema 2'],
  items=[I('Reconocer una cara conocida.', 'Piensa en si requiere esfuerzo.', 0, 'Sistema 1: rápido y automático.'),
         I('Comparar dos ofertas con una tabla de datos.', 'Piensa en si requiere esfuerzo.', 1, 'Sistema 2: lento y deliberado.'),
         I('Decidir a quién acompañas por la primera impresión.', 'Piensa en cuánto has analizado.', 0, 'Sistema 1: intuitivo. Útil para decidir deprisa, pero conviene comprobarlo.'),
         I('Revisar los últimos tres meses de resultados antes de dar feedback.', 'Piensa en el esfuerzo que supone.', 1, 'Sistema 2: más lento y más fiable para decidir sobre personas.')],
  extra='El material de la formación habla de decenas de miles de decisiones al día, casi todas automáticas, y de que procesamos de forma consciente solo una fracción mínima de lo que percibimos. Son cifras orientativas, no medidas exactas. La rapidez no explica todos los sesgos y deliberar tampoco garantiza objetividad. Según la Asociación Americana de Psicología, un sesgo implícito puede actuar antes de la intención consciente y no implica una conducta discriminatoria en cada caso.',
  error='Pensar que pensar más despacio basta. Hay que comprobar hechos concretos, no solo darle más vueltas.',
  plead='Piensa en una decisión reciente sobre alguien de tu equipo.',
  q=[('¿Qué decisión rápida has tomado esta semana sobre una persona de tu equipo?', 'Una real.', 'Decidí a quién acompañar el lunes por la mañana.'),
     ('¿Qué hecho concreto la sostenía?', 'Algo que otra persona podría comprobar.', 'Los resultados de las últimas cuatro semanas.')],
  acc='Antes de tomar una decisión sobre una persona de tu equipo, escribe en una línea el hecho que la sostiene.', chk='Ya escribí el hecho',
  rev='¿Pudiste escribirlo? Si no, ¿qué te faltaba por saber?', frase='Decidir deprisa no es lo mismo que decidir con datos.'),

 dict(n=2, area='Cómo decidimos', t1='Lo evidente', t2='no está comprobado', idx='Lo evidente no está comprobado', idx_corto='Comprobar',
  idxp='Un cuaderno, un bolígrafo y una respuesta que parece obvia.',
  gancho='Un cuaderno y un bolígrafo cuestan juntos 1,10 €. El cuaderno cuesta 1 € más que el bolígrafo. ¿Cuánto cuesta el bolígrafo? Antes de seguir, piensa tu primera respuesta y compruébala en silencio.',
  noT='Fiarte de la respuesta que te sale a la primera.',
  siT='Comprobar antes de dar por buena una respuesta, sobre todo cuando parece evidente.',
  caso='Si el bolígrafo costara 0,10 €, el cuaderno costaría 1,10 € y juntos serían 1,20 €. La solución es 0,05 €: el cuaderno cuesta 1,05 € y juntos son 1,10 €. Mucha gente responde 0,10 € sin comprobarlo.',
  clab='Compruébalo', clead='Marca si cada afirmación es cierta.', rl=['Cierto', 'Falso'],
  items=[I('El bolígrafo cuesta 0,10 €.', 'Haz la suma: cuaderno + bolígrafo.', 1, 'Falso: el cuaderno costaría 1,10 € y juntos sumarían 1,20 €.'),
         I('El bolígrafo cuesta 0,05 €.', 'Comprueba con el cuaderno a 1,05 €.', 0, 'Cierto: 1,05 € + 0,05 € = 1,10 € y el cuaderno cuesta 1 € más.'),
         I('Si una respuesta resulta evidente, ya está comprobada.', 'Piensa en lo que acabas de ver.', 1, 'Falso: que una respuesta parezca evidente no significa que esté comprobada.'),
         I('Con personas pasa igual: una impresión que parece evidente puede no estar comprobada.', 'Piensa en tu equipo.', 0, 'Cierto: las impresiones sobre personas también se completan solas.')],
  extra='Con las personas funciona igual que con el problema: lo que parece evidente es una respuesta rápida, no una respuesta comprobada. Comprobar no es desconfiar: es darte datos para decidir mejor.',
  error='Comprobar solo cuando dudas. El problema aparece cuando estás seguro.',
  plead='Piensa en una impresión que tengas sobre alguien de tu equipo.',
  q=[('¿Qué impresión tienes de una persona de tu equipo que te parece evidente?', 'Una frase sin nombres.', 'Que esa persona no tiene ganas de crecer.'),
     ('¿Cómo podrías comprobarla?', 'Con un dato o una pregunta.', 'Preguntándole qué le gustaría hacer en un año.')],
  acc='Elige una impresión que te parezca evidente sobre alguien de tu equipo y compruébala con un dato o una pregunta.', chk='Ya comprobé una impresión',
  rev='¿Cambió algo al comprobarla? Anota qué dato lo hizo.', frase='Que algo sea evidente no significa que esté comprobado.'),

 dict(n=3, area='Cómo decidimos', t1='Tu contexto', t2='te hace vulnerable', idx='El entorno que nos hace vulnerables', idx_corto='Tu contexto',
  idxp='Presión, información incompleta e historial previo.',
  gancho='Como RE trabajas con objetivos diarios, personas distintas y decisiones continuas. Es el entorno en el que más fácil es tratar una interpretación como si fuera un dato.',
  noT='Pensar que decidir con experiencia te protege.',
  siT='Reconocer tres factores del entorno: presión por resultados, información incompleta e historial previo.',
  caso='Es lunes, faltan días para cerrar el mes y un captador baja. Reaccionas rápido (presión), no sabes qué ha pasado en su turno (información incompleta) y recuerdas que «ya el mes pasado fue flojo» (historial). Resultado: lo explicas por su actitud sin haber hablado con él.',
  clab='Dato o interpretación', clead='Marca si la frase es un hecho comprobable o una interpretación.', rl=['Dato', 'Interpretación'],
  items=[I('«Este mes ha llegado tarde a dos turnos.»', 'Piensa en si otra persona podría comprobarlo.', 0, 'Dato: se puede comprobar.'),
         I('«Es poco profesional.»', 'Piensa en si se puede comprobar.', 1, 'Interpretación: es una etiqueta sobre la persona, no una conducta.'),
         I('«Ya el mes pasado fue flojo, así que es normal.»', 'Piensa en lo que ya pensabas.', 1, 'Interpretación: el historial condiciona lo nuevo.'),
         I('«Este mes ha hecho 22 socios y el pasado 26.»', 'Piensa en si lo comprueba el sistema.', 0, 'Dato: es un resultado. Falta el contexto: campaña, localización y acompañamiento.')],
  extra='Resultado de los tres factores juntos: podemos tratar como «evidencia» lo que en realidad es una interpretación. La presión por resultados es real y no se puede quitar; sí se puede parar un minuto a separar el dato de la explicación.',
  error='Pensar que si tienes poco tiempo no puedes comprobar nada. Basta con una pregunta: ¿qué sé y qué supongo?',
  plead='Piensa en un día de mucha presión.',
  q=[('¿Cuál de los tres factores te afecta más como RE?', 'Presión, información incompleta o historial.', 'La presión: a final de mes decido muy rápido.'),
     ('¿Qué harías en un minuto para separar el dato de la interpretación?', 'Una pregunta o un dato que mirar.', 'Mirar los últimos tres meses antes de decidir.')],
  acc='En la próxima decisión con prisa, tómate un minuto para separar lo que sabes de lo que supones.', chk='Ya separé dato e interpretación',
  rev='¿Cambió tu decisión? Anota qué dato te faltaba.', frase='Presión, poca información e historial: tres puertas para el automatismo.'),

 dict(n=4, area='Un caso: heredas un equipo', t1='Heredas', t2='este equipo', idx='Heredas este equipo: reparte los turnos', idx_corto='Heredas un equipo',
  idxp='Cinco captadores, cuatro turnos y una semana para cerrar el mes.',
  gancho='Es lunes. Queda una semana para cerrar el mes y todavía no has trabajado con estas personas. Tienes 5 captadores con contrato de 25 h y solo 4 turnos de acompañamiento esta semana. Puedes asignarlos ahora o dejar alguno en reserva.',
  noT='Buscar la respuesta correcta. No la hay: se trata de ver qué te hace decidir.',
  siT='Decidir con lo que sabes hoy, que es lo que te ha contado el anterior RE, y apuntar en qué te apoyas.',
  caso='Esto es un ejercicio: decide con lo que ves en las tarjetas. En la píldora siguiente recibirás información nueva y verás si cambias algo. Los nombres y los datos son ficticios.',
  casoL='Cómo funciona este caso',
  html_pre=tarjetas(),
  clab='Reparte tus turnos', clead='Marca a quién acompañas esta semana. No tienes que usar los cuatro.', rl=['Acompaño', 'No esta semana'],
  items=[T(n, '%s · calidad %s · últimos 3 meses %s · este mes %s' % (a_, c_, u_, m_), 'Apunta el dato en el que te apoyas: ¿está en la tabla o solo en el comentario?') for n, a_, u_, m_, c_, t_ in EQ],
  html_post='<div class="cnt" id="cv-cnt" role="status" aria-live="polite" data-over="0">Turnos asignados: 0 de 4. Quedan 4 en reserva.</div>',
  extra='No hay obligación de usar todos los turnos desde el lunes. Si dejas alguno en reserva, piensa qué tendría que pasar para decidir a quién darlo.',
  error='Decidir por el comentario del anterior RE sin mirar los datos. El comentario es su interpretación.',
  plead='Explica tu decisión con tus palabras.',
  q=[('¿A quién acompañas, a quién dejas fuera y por qué?', 'Una frase por persona.', 'Acompaño a Marcos y a Dani porque llevan menos tiempo; dejo fuera a Ana y a Sara por sus resultados estables.'),
     ('Si dejas un turno en reserva, ¿qué tendría que pasar para decidir a quién dárselo?', 'Un dato o una conversación.', 'Que a mitad de semana alguien baje de su nivel habitual.')],
  acc='Guarda tu reparto y no lo cambies hasta ver la información nueva de la píldora siguiente.', chk='Ya guardé mi reparto',
  rev='Si esto fuera real: ¿habrías preguntado a cada persona antes de repartir?', frase='Decide, apunta en qué te apoyas y compáralo después.'),

 dict(n=5, area='Un caso: heredas un equipo', t1='Ahora sabes', t2='algo más', idx='Ahora sabes algo más: ¿cambias el reparto?', idx_corto='Nueva información',
  idxp='Cinco datos nuevos. ¿Mantienes o cambias cada decisión?',
  gancho='Conoces mejor al equipo. ¿Cambia alguna de tus decisiones? El objetivo no era acertar, era descubrir qué estaba influyendo en tu decisión.',
  noT='Defender tu primer reparto porque ya lo habías decidido.',
  siT='Volver a los datos y cambiar de opinión ante nueva información, que es una muestra de rigor profesional.',
  caso='No podemos evitar tener sesgos. Sí podemos aprender a reconocer cuándo actúan y volver a los datos antes de decidir.',
  casoL='Qué se aprende de este caso',
  clab='Información nueva', clead='Marca si mantienes o cambias tu decisión sobre cada persona.', rl=['Mantengo', 'Cambio'],
  items=[
   T('Laura: lleva 3 meses por debajo de su rendimiento habitual y nadie ha trabajado con ella qué puede estar pasando.', '¿Mantienes tu decisión sobre Laura?',
     {0: 'Revisa: el comentario decía que no hacía falta estar encima, pero lleva tres meses por debajo de su nivel. Dar por hecho que no necesita apoyo era una suposición.', 1: 'Es un cambio con base en un dato: lo que parecía «un regalo» necesita una conversación. La confianza previa pudo ocultar la bajada.'}),
   T('Dani: su evolución es positiva, pero cuando trabaja sin acompañamiento su rendimiento baja. Su calidad sigue siendo mejorable.', '¿Mantienes tu decisión sobre Dani?',
     {0: 'Tiene base si le acompañas: su mejora existe y baja cuando trabaja solo. Si no le acompañabas, ¿qué dato lo justificaba?', 1: 'Es razonable si el dato te lo pide: el acompañamiento le sirve y la calidad aún se está consolidando.'}),
   T('Sara: le ha contado a una compañera que le gustaría crecer en Wesser, pero nunca se ha presentado a un proceso porque no sabe si está preparada. Ayuda habitualmente a las nuevas incorporaciones.', '¿Mantienes tu decisión sobre Sara?',
     {0: 'Puede que el reparto sea el mismo; lo que cambia es la conversación que tienes pendiente con ella sobre crecer. Preguntar es mejor que suponer.', 1: 'Si la dejaste fuera por «va haciendo», el dato nuevo muestra potencial sin explorar. Pregúntale qué necesita.'}),
   T('Marcos: parte de sus resultados coinciden con campañas y localizaciones de menor rendimiento y ha tenido menos acompañamiento efectivo que Dani. No hay datos que demuestren falta de ambición.', '¿Mantienes tu decisión sobre Marcos?',
     {0: 'Revisa: «falta de ambición» era una explicación, no un dato. Con el contexto, su 22 no la demuestra.', 1: 'Con el contexto, su resultado deja de ser prueba de falta de ambición. Separa el hecho de la causa que suponías.'}),
   T('Ana: sus ajustes de horario no han afectado a sus resultados ni a la disponibilidad acordada. Ha preguntado alguna vez por otros puestos y estaría interesada en crecer.', '¿Mantienes tu decisión sobre Ana?',
     {0: 'Tiene base si la dejaste fuera por ser fiable y estar bien. Pero ahora sabes algo que el comentario no recogía: quiere crecer.', 1: 'Sus horarios no han afectado a nada y le interesa crecer: ese dato no estaba en el comentario del anterior RE.'}),
  ],
  html_post='<div class="decir cso" id="cv-res" aria-live="polite"><small>Tu comparación</small><p>Primero reparte los turnos en la píldora 4: marca a quién acompañas.</p></div>'
            '<h2 class="lab" style="margin-top:22px">Los comentarios del anterior RE, uno a uno</h2><div class="faq">'
            '<div><b>«Laura es un regalo… no tienes que estar encima»</b><p>Interpretación basada en confianza heredada. Pregunta de control: ¿qué datos de los últimos tres meses la sostienen?</p></div>'
            '<div><b>«Dani es de la vieja escuela. Tiene hambre»</b><p>Expectativa de potencial. Pregunta de control: ¿qué conductas concretas ves?</p></div>'
            '<div><b>«Sara va haciendo. Para estar contenta necesita salir a las 13 h»</b><p>Suposición sobre su disponibilidad. Pregunta de control: ¿lo ha dicho ella?</p></div>'
            '<div><b>«Con Marcos tengo dudas… no muestra ambición»</b><p>Causa supuesta. Pregunta de control: ¿qué contexto hay detrás de su resultado?</p></div>'
            '<div><b>«Ana es muy fiable. Dale una campaña cada mes»</b><p>Etiqueta que encasilla: ser fiable no dice si quiere crecer. Pregunta de control: ¿se lo has preguntado?</p></div></div>',
  extra='Este caso no pretende que hayas acertado. Fíjate en qué cambió cuando apareció información nueva: eso es lo que tu primera decisión daba por cierto.',
  error='Pensar que cambiar de decisión es un fallo. Cambiar ante evidencias nuevas es rigor.',
  plead='Resume lo que has visto en este caso.',
  q=[('¿Qué decisión has cambiado y qué dato la cambió?', 'Una frase.', 'Cambié lo de Laura: llevaba tres meses bajando sin que nadie hablara con ella.'),
     ('¿Qué comentario del anterior RE era una interpretación y no un dato?', 'Elige uno.', '«No muestra ambición»: no había datos que lo apoyaran.')],
  acc='Antes de dar por buena una explicación sobre alguien, pregúntate «¿cómo lo sé?» y apunta el dato.', chk='Ya me hice la pregunta',
  rev='¿Qué explicaciones tuyas necesitaban un dato que no tenías?', frase='No era acertar: era descubrir qué influía.'),

 sesgo(6, 'Seis sesgos', 'El', 'metasesgo', 'Metasesgo', 'Creer que tus valoraciones son más objetivas que las de otros.',
  'Nos cuesta reconocer nuestros propios sesgos y creemos que nuestras valoraciones son más objetivas que las de otras personas. Cuanto más experiencia, más fácil es dejar de contrastar.',
  'Pensar que la experiencia te protege de los sesgos. La experiencia aporta valor, pero no garantiza que no los haya.',
  'Revisar qué hechos sostienen la decisión y pedir una segunda mirada, también cuando estás muy seguro.',
  'Un RE dice «conozco perfectamente a mi gente» y mantiene su valoración de Laura sin revisar cómo ha evolucionado en los últimos meses. La confianza sustituye a la comprobación.',
  ['Metasesgo', 'Decisión contrastada'],
  [I('«Conozco perfectamente a mi gente.» El RE mantiene su valoración de Laura sin revisar cómo ha evolucionado en los últimos meses.', 'Piensa en qué sustituye a la comprobación.', 0, 'Metasesgo: la confianza en conocer a alguien sustituye a revisar los datos.'),
   I('Una compañera RE propone contrastar su visión de una persona. El RE responde: «En mi caso no hace falta. Sé distinguir un mal día de una falta de actitud.»', 'Piensa en si acepta otra mirada.', 0, 'Metasesgo: se rechaza la segunda mirada por exceso de confianza.'),
   I('«Después de tantos años, sé quién puede crecer.» El RE recomienda una promoción sin explicar qué conductas apoyan su valoración.', 'Piensa en lo que apoya la recomendación.', 0, 'Metasesgo: la experiencia se usa en lugar de las conductas observables.'),
   I('Antes de recomendar a Ana, el RE repasa sus últimos seis meses y pide a otro RE que lea sus notas.', 'Piensa en qué contrasta.', 1, 'Decisión contrastada: revisa hechos y pide una segunda mirada.')],
  'No basta con que una decisión tenga consenso: conviene pedir evidencias y admitir información que pueda hacerla cambiar. La buena intención tampoco evita el sesgo.',
  'Pedir una segunda mirada solo cuando dudas. Es más útil cuando estás muy seguro.',
  [('¿En qué decisión sobre tu equipo estás más seguro de tener razón?', 'Una real, sin nombres.', 'En quién está listo para crecer.'),
   ('¿Quién podría darte una segunda mirada y qué le enseñarías?', 'Una persona y unos hechos.', 'A otro RE, mis notas de los últimos seis meses.')],
  'Pide a otra persona que revise los hechos de una decisión en la que estés muy seguro.', 'Ya pedí una segunda mirada',
  '¿Cambió algo? Si no cambió nada, ¿qué dato la reforzó?', 'Tu confianza no es un dato.', idx_corto='Metasesgo'),

 sesgo(7, 'Seis sesgos', 'Sesgo de', 'simpatía', 'Sesgo de simpatía', 'Lo agradable que resulta alguien mejora cómo valoras sus capacidades.',
  'La buena conexión personal con alguien mejora nuestra valoración de sus capacidades, aunque no tengamos evidencias suficientes. Lo agradable del trato ocupa el lugar de las evidencias.',
  'Pensar que tratar mejor a quien te cae bien es inocente. Puede cambiar la paciencia, el tiempo y la confianza que das.',
  'Valorar las conductas relevantes con criterios comunes y revisar si el agrado cambia tu respuesta ante un mismo hecho.',
  'Con Dani la conversación fluye y le dedicas más tiempo. Con Marcos, más reservado, terminas al acabar el turno. El agrado decide cuánto acompañas, no lo que cada uno necesita.',
  ['Simpatía', 'Sin sesgo'],
  [I('Con Dani la conversación fluye y el RE prolonga su acompañamiento para resolver dudas. Con Marcos, más reservado, termina al acabar el turno.', 'Piensa en qué decide el tiempo.', 0, 'Simpatía: el agrado decide cuánto tiempo se dedica a cada uno.'),
   I('Dani y Sara omiten el mismo paso del discurso. El RE lo describe como «un despiste» en Dani y como «falta de atención» en Sara.', 'Piensa en el mismo hecho, dos explicaciones.', 0, 'Simpatía: el mismo hecho recibe una explicación más benévola con quien cae mejor.'),
   I('El RE dice de Dani: «Da gusto trabajar con él, tiene mucho potencial». En sus notas no aparecen conductas que expliquen ese potencial.', 'Piensa en lo que respalda el potencial.', 0, 'Simpatía: el agrado ocupa el lugar de las evidencias.'),
   I('El RE dedica el mismo tiempo a Dani y a Marcos y anota, para cada uno, qué paso del discurso trabajaron.', 'Piensa en qué criterio usa.', 1, 'Sin sesgo visible: criterio común y evidencias anotadas.'),
   I('Dani y Sara omiten el mismo paso y el RE lo anota igual en ambos y lo corrige con la misma pregunta.', 'Piensa en si el trato cambia.', 1, 'Sin sesgo visible: mismo hecho, misma respuesta.')],
  'Diferencia con la afinidad: en la simpatía pesa que la persona nos resulte agradable; en la afinidad, que se parezca a nosotros. Pueden coincidir, pero no son lo mismo.',
  'Pensar que el remedio es dejar de ser cercano. Se trata de aplicar el mismo criterio, no de tratar a todos con frialdad.',
  [('¿Con quién de tu equipo es más fácil hablar y cómo lo notas en tu tiempo o tu paciencia?', 'Sin nombres.', 'Con una persona alargo los acompañamientos y con otra los acabo cuando termina el turno.'),
   ('¿Qué criterio común aplicarás a todas las personas?', 'Una conducta que mirar igual.', 'Cuánto tiempo dedico a cada persona según lo que necesita.')],
  'Esta semana, anota cuánto tiempo dedicas a cada persona de tu equipo y qué necesitaba cada una.', 'Ya anoté el tiempo de cada persona',
  '¿Qué diferencias hay entre el tiempo y lo que cada persona necesitaba?', 'El agrado no es una evidencia.', idx_corto='Simpatía'),

 sesgo(8, 'Seis sesgos', 'Sesgo de', 'rendimiento', 'Sesgo de rendimiento', 'El mismo resultado se valora distinto según lo que esperas de cada persona.',
  'Una misma actuación recibe una valoración distinta según las expectativas que ya tenemos sobre la persona. Las etiquetas previas cambian el nivel de exigencia.',
  'Pensar que valoras igual a todo el mundo porque lo haces con buena intención.',
  'Definir de antemano qué esperas del puesto y valorar resultados y conductas con esos criterios, considerando el contexto.',
  'Laura y Marcos terminan la semana con el mismo resultado. De Laura dices «ha tenido una mala racha» y de Marcos «sigue demostrando que le cuesta». Mismo dato, dos lecturas.',
  ['Rendimiento', 'Sin sesgo'],
  [I('Laura y Marcos terminan una semana con el mismo resultado. «Laura ha tenido una mala racha. Marcos sigue demostrando que le cuesta.»', 'Piensa en lo que cambia entre dos mismos resultados.', 0, 'Rendimiento: el mismo dato se disculpa en uno y confirma una impresión en el otro.'),
   I('Sara y Dani necesitan corregir el mismo paso del discurso. «Con Sara esperaba que ya estuviera resuelto. Dani lo aprenderá con práctica.»', 'Piensa en el nivel de exigencia.', 0, 'Rendimiento: la misma corrección se exige más a quien se espera más.'),
   I('Ana suele rendir bien, pero tiene un mes flojo. Al hablar de una promoción, el RE concluye «todavía no está preparada» basándose solo en ese mes.', 'Piensa en cuántos datos usa.', 0, 'Rendimiento: un único resultado reciente pesa más que toda su serie.'),
   I('Laura y Marcos terminan con el mismo resultado. El RE revisa para ambos los últimos meses y el contexto antes de valorar.', 'Piensa en qué hace igual para los dos.', 1, 'Sin sesgo visible: mismo criterio y mismo contexto para ambos.'),
   I('Ana tiene un mes flojo. El RE mira la serie de los últimos seis meses y se lo comenta a Ana antes de sacar conclusiones.', 'Piensa en cuántos datos usa.', 1, 'Sin sesgo visible: mira la serie y habla con la persona.')],
  'Las diferencias de juicio deben apoyarse en requisitos y contextos pertinentes, no en etiquetas. El tercer ejemplo también muestra el peso excesivo de la información más reciente: revisar una serie de datos evita decidir el futuro con un único resultado.',
  'Cambiar el criterio según la persona y llamarlo «adaptarse». Adaptar el apoyo es válido; adaptar el nivel de exigencia sin motivo, no.',
  [('¿A quién le exiges más o menos de lo que le pedirías a otra persona con el mismo resultado?', 'Sin nombres.', 'Exijo más a quien lleva más tiempo, aunque el resultado sea igual.'),
   ('¿Qué definirás antes de valorar el mes?', 'Qué esperas del puesto y cómo lo medirás.', 'Cuántos socios por turno y qué pasos del discurso, igual para todos.')],
  'Antes de valorar un mes, escribe qué esperas del puesto y aplícalo a todo el equipo.', 'Ya definí mis criterios',
  '¿Valoraste a todas las personas con los mismos criterios? Anota dónde dudaste.', 'El mismo dato merece la misma lectura.', idx_corto='Rendimiento'),

 sesgo(9, 'Seis sesgos', 'Sesgo de', 'atribución', 'Sesgo de atribución', 'Explicar un dato por cómo es la persona y no por sus circunstancias.',
  'Explicamos una conducta o un resultado por características de la persona sin considerar suficientemente las circunstancias. Atribuimos a la persona lo que puede deberse al contexto.',
  'Quitar mérito o justificar cualquier resultado. Una explicación sobre la persona puede ser correcta: hay que comprobarla.',
  'Separar el hecho de la explicación. Preguntar qué ha ocurrido y revisar el contexto antes de atribuir una causa.',
  'Marcos hace menos socios y piensas «le falta esfuerzo». No has mirado que ha trabajado en localizaciones de menor rendimiento ni cuánto acompañamiento ha tenido. Has pasado del dato a la causa sin comprobarla.',
  ['Atribución', 'Rendimiento', 'Sin sesgo'],
  [I('Marcos consigue menos socios. El RE lo atribuye a falta de esfuerzo sin revisar que ha trabajado en localizaciones de menor rendimiento.', 'Piensa en si explica por la persona o por el contexto.', 0, 'Atribución: se explica el dato por la persona sin revisar el contexto.'),
   I('Sara está más seria de lo habitual. El RE comunica al RP que «está desmotivada» sin haber hablado con ella.', 'Piensa en lo que se ha comprobado.', 0, 'Atribución: se supone una causa personal sin preguntar.'),
   I('Ana obtiene muy buenos resultados. El RE concluye que funcionaría igual en cualquier campaña sin revisar la ubicación o el apoyo recibido.', 'Piensa en lo que se da por hecho.', 0, 'Atribución: se atribuye todo a la persona y se ignora el contexto que ayudó.'),
   I('«Con Sara esperaba que ya estuviera resuelto. Dani lo aprenderá con práctica.»', 'Piensa en lo que se espera de cada uno.', 1, 'Rendimiento: aquí lo que cambia es la expectativa sobre cada persona, no la causa que se atribuye.'),
   I('Marcos consigue menos socios. El RE revisa campaña, localización y acompañamiento recibido y le pregunta cómo lo ha vivido.', 'Piensa en si pregunta antes de explicar.', 2, 'Sin sesgo visible: separa el dato de la explicación y comprueba el contexto.')],
  'Distingue rendimiento de atribución: en el rendimiento cambia la exigencia según la persona; en la atribución cambia la explicación del mismo dato (persona o contexto). Preguntar por localización, campaña, acompañamiento y otras circunstancias relevantes ayuda a comprobarlo.',
  'Dar siempre la explicación del contexto. Se trata de distinguir el dato de la causa que supones, no de justificar todo.',
  [('¿Qué dato de tu equipo estás explicando por la persona esta semana?', 'Sin nombres.', 'Que un captador haga menos socios porque no se esfuerza.'),
   ('¿Qué preguntarás antes de atribuir una causa?', 'Sobre contexto o sobre la persona.', 'En qué localización y con qué acompañamiento ha trabajado.')],
  'Antes de dar una explicación sobre un resultado, pregunta por el contexto: campaña, localización y acompañamiento.', 'Ya pregunté por el contexto',
  '¿Cambió tu explicación? Anota qué circunstancia no habías mirado.', 'No atribuyas a la persona lo que puede ser contexto.', idx_corto='Atribución',
  clead='Marca el sesgo que muestra cada ejemplo, o si no hay sesgo.'),

 sesgo(10, 'Seis sesgos', 'Sesgo de', 'afinidad', 'Sesgo de afinidad', 'Favorecer a quien se parece a ti o trabaja como tú.',
  'Favorecemos a personas que comparten nuestra trayectoria, intereses o forma de trabajar, porque esa semejanza nos resulta familiar.',
  'Pensar que tu estilo es la medida de un buen captador.',
  'Definir qué resultados y conductas requiere el puesto y comprobarlos también en personas con estilos diferentes al tuyo.',
  'Conectas con el discurso enérgico de Dani, parecido al tuyo, y te parece menos eficaz el estilo pausado de Sara, aunque sus resultados sean buenos. Tu estilo se ha convertido en la referencia.',
  ['Afinidad', 'Simpatía', 'Sin sesgo'],
  [I('El RE conecta con el discurso enérgico de Dani, parecido al suyo. Considera menos eficaz el estilo pausado de Sara, aunque sus resultados sean buenos.', 'Piensa en si pesa el parecido o el agrado.', 0, 'Afinidad: el estilo propio se convierte en la referencia.'),
   I('El RE practica más con quien aplica sus mismas técnicas. Dedica menos tiempo a explorar otra técnica que un captador usa con buenos resultados.', 'Piensa en qué técnicas prioriza.', 0, 'Afinidad: se prefiere lo familiar aunque otra técnica funcione.'),
   I('«Marcos me recuerda a mí cuando empecé.» Esa semejanza hace que el RE lo proponga para crecer antes de comparar las competencias del equipo.', 'Piensa en qué se compara antes.', 0, 'Afinidad: la semejanza con uno mismo pesa más que comparar competencias.'),
   I('Con Dani la conversación fluye y el RE prolonga su acompañamiento. Con Marcos, más reservado, termina al acabar el turno.', 'Piensa en si pesa el parecido o el agrado.', 1, 'Simpatía: pesa lo agradable del trato, no que se parezca a ti.'),
   I('El RE describe qué conductas exige el puesto y las comprueba en Sara y en Dani, aunque tengan estilos distintos.', 'Piensa en si el estilo importa.', 2, 'Sin sesgo visible: criterio por conductas, no por estilo.')],
  'Una técnica distinta puede ser válida si cumple los requisitos del trabajo. Revisa qué significa «encaje» y descríbelo con comportamientos profesionales, sin copiar un único perfil.',
  'Confundir afinidad con simpatía. Afinidad es preferencia por semejanza; simpatía, por agrado. Pueden coincidir.',
  [('¿Qué estilo de tu equipo te cuesta más valorar bien porque es distinto al tuyo?', 'Sin nombres.', 'El de quien habla más despacio que yo.'),
   ('¿Qué conductas y resultados exige el puesto, con independencia del estilo?', 'Dos o tres.', 'Explicar el contrato con claridad y cerrar con una pregunta.')],
  'Escribe tres conductas del puesto, sin hablar de estilo, y compruébalas en alguien muy distinto a ti.', 'Ya comprobé las conductas',
  '¿Qué has aprendido de un estilo distinto al tuyo?', 'Tu estilo no es la medida del puesto.', idx_corto='Afinidad',
  clead='Marca el sesgo que muestra cada ejemplo, o si no hay sesgo.'),

 sesgo(11, 'Seis sesgos', 'Maternidad', 'y paternidad', 'Sesgo de maternidad y paternidad', 'Suponer disponibilidad o compromiso por las responsabilidades de cuidado.',
  'Suponemos disponibilidad, compromiso o capacidad a partir de la maternidad, la paternidad o las responsabilidades de cuidado. Puede pasar también con buena intención.',
  'Pensar que proteger a alguien es siempre neutro. Dejar de ofrecer una oportunidad para ponérselo fácil también la limita.',
  'Explicar los requisitos reales y preguntar por disponibilidad e intereses en condiciones equivalentes, sin anticipar la respuesta.',
  'Sara y Dani tienen hijos y han confirmado la misma disponibilidad. Ante un cambio de turno, consultas primero a Dani porque crees que Sara lo tendrá más difícil. Has respondido por ella antes de preguntarle.',
  ['Sesgo', 'Sin sesgo'],
  [I('Sara y Dani tienen hijos y han confirmado la misma disponibilidad. Ante un cambio de turno, el RE consulta primero a Dani porque cree que Sara lo tendrá más difícil.', 'Piensa en lo que se supone.', 0, 'Sesgo: se supone una limitación que Sara no ha declarado.'),
   I('El RE propone a Dani para una campaña fuera de la ciudad. A Sara le reserva una opción cerca de casa «para ponérselo más fácil», sin preguntar qué prefiere.', 'Piensa en si pregunta.', 0, 'Sesgo: la protección bienintencionada limita la oportunidad sin preguntar.'),
   I('Ana ha mostrado interés por asumir más responsabilidad. El RE deja de proponerla porque supone que ahora «preferirá centrarse en su familia».', 'Piensa en lo que supone.', 0, 'Sesgo: se supone menor compromiso por sus responsabilidades de cuidado.'),
   I('Ante un cambio de turno, el RE pregunta a Sara y a Dani en el mismo orden y con las mismas condiciones, y respeta lo que cada uno responde.', 'Piensa en si pregunta igual.', 1, 'Sin sesgo visible: preguntas equivalentes y respuesta respetada.'),
   I('Sara le dice que esta semana no puede viajar por una razón familiar. El RE lo tiene en cuenta como dato declarado.', 'Piensa en quién lo ha dicho.', 1, 'Sin sesgo: una limitación declarada es un dato distinto de una limitación supuesta.')],
  'No asumas menor compromiso de una madre ni mayor disponibilidad de un padre. Comprueba horario, viajes y condiciones pertinentes con preguntas equivalentes. Una limitación declarada es un dato; una limitación supuesta, no. Los casos son ficticios.',
  'Dejar de preguntar para no incomodar. Preguntar igual a todas las personas es lo que evita suponer.',
  [('¿Qué oportunidad de tu equipo podrías estar dejando de ofrecer por suponer algo sobre la vida de alguien?', 'Sin nombres.', 'Una campaña fuera de la ciudad que no he propuesto a una persona.'),
   ('¿Qué pregunta equivalente harás a todo el equipo?', 'Una pregunta sobre disponibilidad e intereses.', '¿Te interesa esta campaña y qué necesitarías para hacerla?')],
  'La próxima vez que ofrezcas una oportunidad, haz la misma pregunta a todas las personas que cumplen los requisitos.', 'Ya hice la misma pregunta a todas',
  '¿Alguna respuesta te sorprendió? Anota qué habrías supuesto.', 'Pregunta, no supongas.', idx_corto='Maternidad y paternidad',
  clead='Marca si el ejemplo muestra el sesgo o no.', clab='¿Hay sesgo?'),

 dict(n=12, area='Para terminar', t1='Cuando una expectativa', t2='se cumple sola', idx='Cuando una expectativa se cumple sola', idx_corto='Para terminar',
  idxp='Cada decisión puede abrir o cerrar una oportunidad. Tu ficha de decisión.',
  gancho='Cada decisión que tomamos sobre una persona puede abrir o cerrar una oportunidad. Por eso, antes de decidir, merece la pena preguntarse: ¿qué sé y qué estoy suponiendo?',
  noT='Pensar que una expectativa es solo una opinión sin consecuencias.',
  siT='Ver el ciclo: expectativa, decisión, oportunidad y resultado. El resultado confirma la expectativa y parece que «ya lo sabías».',
  caso='«Tiene potencial» (expectativa) lleva a darle más tiempo, confianza y feedback (decisión), que le da más ocasiones de aprender y destacar (oportunidad), y mejora (resultado), lo que confirma la expectativa. Al revés: menos confianza, menos oportunidades, peor evolución y «ya lo sabía».',
  clab='Las piezas del ciclo', clead='Marca a qué pieza del ciclo corresponde cada frase.', rl=['Expectativa', 'Decisión', 'Resultado'],
  items=[I('«Tiene potencial.»', 'Piensa en si es un juicio previo.', 0, 'Expectativa: un juicio previo.'),
         I('Dedico más tiempo, confianza y feedback a esa persona.', 'Piensa en lo que haces tú.', 1, 'Decisión: lo que haces a partir de la expectativa.'),
         I('Mejora y confirma lo que yo esperaba.', 'Piensa en lo que ocurre al final.', 2, 'Resultado: confirma la expectativa, también por las oportunidades que diste.'),
         I('Le doy menos confianza y menos ocasiones de destacar.', 'Piensa en lo que haces tú.', 1, 'Decisión: la misma pieza, pero hacia el lado contrario.'),
         I('«Ya lo sabía.»', 'Piensa en lo que ocurre al final.', 2, 'Resultado: la evolución confirma la expectativa sin comprobar si las oportunidades fueron iguales.')],
  extra='Para terminar, estas cuatro ideas: la primera impresión es un punto de partida y se puede revisar; la experiencia aporta mucho valor, y contrastar tus interpretaciones la hace más útil; conocer a cada persona ayuda a descubrir capacidades que tus expectativas pueden ocultar; y cambiar de opinión ante nuevas evidencias demuestra rigor profesional.',
  error='Esperar a ver los resultados para saber si tenías razón. Los resultados también dependen de las oportunidades que diste.',
  plead='Prepara tu ficha de decisión.',
  q=[('¿Qué decisión sobre una persona de tu equipo tomarás esta semana?', 'Una real, sin nombres.', 'A quién propongo para acompañar a una persona nueva.'),
     ('¿Qué sabes con datos y qué estás suponiendo?', 'Dos listas cortas.', 'Sé: sus resultados de seis meses. Supongo: que no tiene tiempo.'),
     ('¿Qué dato te falta o quién te dará una segunda mirada?', 'Una de las dos cosas.', 'Le preguntaré qué le interesa y se lo contaré a otro RE.')],
  acc='Antes de la próxima decisión importante sobre una persona, rellena tu ficha: qué sé, qué supongo y qué me falta.', chk='Ya rellené mi ficha',
  rev='¿Cambió tu decisión? Anota qué suposición descubriste.', frase='¿Qué sé… y qué estoy suponiendo?', estricto=True),
]
