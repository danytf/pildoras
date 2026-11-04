import os
# -*- coding: utf-8 -*-
import html
def e(s): return html.escape(s, quote=True)
def I(label, hint, ans, fb):
    return (label, hint, ans, fb)

KEY = 'wesser-serie-seleccion'

FASES = [('Fase 0', 'Preselección', 'Atracción del Talento'), ('Fase 1', 'Entrevista Zoom', 'Atracción del Talento'),
         ('Fase 2', 'Entrevista presencial', 'Responsable Provincial'), ('Fase 3', 'Formación inicial', 'Responsable Provincial')]
def fb(n):
    o = ['<div class="fb f4" role="group" aria-label="%s">' % ('Estás en la fase %d de 4' % n if n is not None else 'Las cuatro fases del proceso')]
    for i, (a, b, c) in enumerate(FASES):
        on = (i == n)
        o.append('<span%s%s><b>%s</b><small>%s</small><small>%s</small></span>' % (' class="on"' if on else '', ' aria-current="step"' if on else '', a, b, c))
    o.append('</div>')
    return ''.join(o)

def lista(titulo, filas, clase='faq'):
    o = ['<section><h2 class="lab">%s</h2><div class="%s">' % (e(titulo), clase)]
    for b, t in filas:
        o.append('<div><b>%s</b><p>%s</p></div>' % (e(b), e(t)))
    o.append('</div></section>')
    return ''.join(o)

STYLE = """.fb{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px;margin:16px 0 0}
.fb span{min-width:0;text-align:center;padding:8px 6px;border:2px solid var(--line);border-radius:var(--r);background:var(--surface);color:var(--ink)}
.fb b{display:block;font-family:var(--f-display);font-size:20px;text-transform:uppercase;letter-spacing:.6px;line-height:1.1}
.fb small{display:block;font-size:12.5px;font-weight:700;line-height:1.25;margin-top:2px;overflow-wrap:anywhere}
.fb .on{background:var(--red);border-color:var(--red);color:#fff}
.chq{background:var(--surface);border:2px solid var(--line);border-radius:var(--r);padding:10px 12px;margin-top:10px;min-width:0}
.chq p{margin:0 0 8px;font-weight:600;line-height:1.4}
.chr{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.chr label{display:flex;align-items:center;gap:8px;min-height:44px;padding:6px 10px;border:2px solid var(--line);border-radius:var(--r);font-weight:700;font-size:15px;line-height:1.25;cursor:pointer;min-width:0}
.chr input{width:20px;height:20px;flex:none;accent-color:var(--red)}
.chr label:has(input:checked){border-color:var(--red);background:var(--tint)}"""


TEST_ITEMS = [
 (17,'T','Prefiero que las cosas tengan orden y estructura.'),(12,'P','Cuando oigo una idea nueva, pienso enseguida cómo usarla en la práctica.'),
 (3,'A','Muchas veces actúo sin pensar demasiado en las consecuencias.'),(16,'R','Escucho más de lo que hablo.'),
 (4,'T','Me gusta resolver problemas paso a paso.'),(38,'P','Suelo valorar las ideas por si sirven en la realidad.'),
 (20,'A','Me motiva mucho probar cosas nuevas y diferentes.'),(18,'R','Antes de sacar conclusiones, intento entender bien la información.'),
 (50,'T','Creo que lo lógico y razonado debería imponerse.'),(57,'P','Antes de algo nuevo, prefiero comprobar si funciona.'),
 (27,'A','Suelo decir abiertamente cómo me siento.'),(31,'R','Suelo ser prudente antes de decidir algo.'),
 (71,'T','Me interesa entender la teoría o explicación detrás de lo que pasa.'),(73,'P','Si algo ayuda a que el trabajo salga bien, lo hago sin problema.'),
 (51,'A','Me gusta vivir experiencias nuevas.'),(63,'R','Me gusta pensar varias opciones antes de elegir.'),
]
TEST_HTML = ('<section><h2 class="lab">Tu test: CHAEA Express</h2><p class="lead">Son 16 frases del CHAEA Express. Marca más (+) si estás más de acuerdo que en desacuerdo, o menos (−) si estás más en desacuerdo. Tu resultado se guarda solo en este dispositivo.</p>'
             '<div id="ch-form" class="cht"></div><p class="nota" id="ch-cnt" role="status" aria-live="polite" style="color:var(--ink)">Respondidas: 0 de 16</p>'
             '<button type="button" class="btn next" id="ch-go">Ver mi resultado</button><div id="ch-out" aria-live="polite"></div></section>')
TIPS = {
 'A': ('Activo', 'Aprende haciendo', [('Empieza practicando pronto', 'Suele aprender con la experiencia directa. Si escucha mucho antes de actuar, puede desconectarse.'), ('Feedback rápido y concreto', 'Una sola mejora clara que aplicar en el siguiente intento.'), ('Objetivos cortos por turno', 'Los retos breves y medibles ayudan a mantener la motivación.'), ('Varía los estímulos', 'Cambiar de zona, enfoque o reto puede reactivar su atención.'), ('Corrige mostrando cómo hacerlo', 'La demostración seguida de repetición suele funcionar mejor que la teoría sola.')]),
 'R': ('Reflexivo', 'Aprende observando', [('Observación guiada', 'Mirar con una lista de cosas a observar enseña más que mirar sin foco.'), ('Una pausa para reflexionar', 'Tras cada intento, un momento para pensar lo vivido convierte la experiencia en aprendizaje.'), ('Ensayo controlado antes de subir el volumen', 'Practicar primero en un entorno seguro reduce el bloqueo.'), ('Coaching con preguntas', 'Las preguntas le ayudan a llegar solo a la conclusión.'), ('Calidad antes que velocidad', 'La presión de ritmo temprano puede generar errores. Primero precisión, luego velocidad.')]),
 'T': ('Teórico', 'Aprende comprendiendo', [('Explica la lógica del discurso', 'Necesita saber por qué existe cada paso para integrarlo.'), ('Relaciona cada frase con su función', 'Si entiende el propósito, puede adaptarlo en lugar de repetirlo.'), ('Usa esquemas claros', 'Los pasos numerados y los esquemas ordenan lo que aprende.'), ('Corrige señalando la regla', 'No basta con «esto está mal»: indica qué principio se ha roto.'), ('Que explique su razonamiento', 'Al contar el proceso, lo consolida.')]),
 'P': ('Pragmático', 'Aprende aplicando', [('Herramientas listas para usar', 'Frases exactas y guiones cortos le sirven más que la teoría.'), ('Problema, recurso y prueba', 'Situación real, solución concreta y aplicación inmediata.'), ('Indicadores simples', 'Necesita medidas claras para saber si algo funciona.'), ('Refuerza con resultados reales', 'Le convence ver que algo mejora lo que consigue.'), ('Plan final de acciones concretas', 'Terminar cada sesión con acciones evita que el aprendizaje se quede en intención.')]),
}
import json as _json
CH_SCRIPT = (open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'ch_tpl.js'), encoding='utf8').read()
             .replace('__IT__', _json.dumps([[a, b, c] for a, b, c in TEST_ITEMS], ensure_ascii=False))
             .replace('__TP__', _json.dumps({k: [v[0], v[1], [list(x) for x in v[2]]] for k, v in TIPS.items()}, ensure_ascii=False)))

SERIE = dict(
    key=KEY, dur='3 min',
    nombre1='Proceso de selección', nombre2='de personal',
    sub='Qué haces tú en la entrevista presencial y en la formación inicial, y qué ha vivido el candidato antes de llegar a ti',
    intro=('Esta serie va dirigida a Responsables Provinciales (RP). Recorre el modelo nacional de selección de Wesser, que es el mismo en todas las provincias: preselección, entrevista Zoom, entrevista presencial y formación inicial. '
           'Las dos primeras fases las hace el departamento de Atracción del Talento y se explican para que sepas qué ha vivido el candidato antes de llegar a ti; las dos últimas son tuyas. '
           'Son 13 píldoras de unos 3 minutos y cada una se entiende sola.'),
    aviso=('Es un resumen del modelo nacional. Los guiones y los tiempos son de referencia y no sustituyen tu criterio al entrevistar. '
           'Las condiciones se citan como figuran en el material de la formación; si cambian, manda la información vigente de Wesser. No se incluyen cifras de incentivos.'),
    glosario=[
        ('RP', 'Responsable Provincial: hace la entrevista presencial y la formación inicial y organiza las zonas de trabajo.'),
        ('Atracción del Talento', 'Departamento que preselecciona por teléfono y hace la entrevista Zoom antes de que el candidato llegue a ti.'),
        ('Recruitment Portal', 'Herramienta donde se pasa el feedback de cada candidato.'),
        ('Nevera', 'Candidatos que quedan en reserva y a los que no se cita todavía.'),
        ('Juego de roles', 'Simulación de una parada en la que el candidato practica su discurso contigo.'),
        ('CHAEA Express', 'Test breve de 16 frases que orienta sobre el estilo de aprendizaje de una persona.'),
        ('Estilo de aprendizaje', 'Forma en que cada persona aprende mejor: haciendo, observando, comprendiendo o aplicando. Orienta, no etiqueta.'),
        ('Formación inicial', 'Primer día de formación del nuevo captador: teoría por la mañana y práctica en la calle.'),
    ],
    tema=[
        ('El modelo', 'Un proceso nacional y unificado, las cuatro fases y quién hace cada una. Píldoras 1 y 2.'),
        ('Lo que pasa antes de ti', 'Qué ha vivido el candidato en la preselección y en la entrevista Zoom, y cómo pasas el feedback. Píldoras 3 y 4.'),
        ('Tu entrevista presencial', 'Estructura de 2,5 horas, condiciones, ONG, proceso de captación, speech y juego de roles, y la entrevista individual. Píldoras 5 a 9.'),
        ('Tu formación inicial', 'Teoría, test de estilo de aprendizaje, práctica en la calle y lista de comprobación para que el nuevo captador vuelva mañana. Píldoras 10 a 13.'),
    ],
    ruta=[2, 4, 5, 6, 13],
    chuleta=[
        ('Las cuatro fases', [
            ('Fase 0 · Preselección', 'Detectar candidatos con potencial. Atracción del Talento, por teléfono.'),
            ('Fase 1 · Entrevista Zoom', 'Atraer a los candidatos. Atracción del Talento, por videoentrevista. No se profundiza en las condiciones.'),
            ('Fase 2 · Entrevista presencial', 'Seleccionar a los candidatos. Tú, en oficina o sala de la ONG.'),
            ('Fase 3 · Formación inicial', 'Formar y motivar. Tú, en oficina o sala de la ONG (teoría) y en la calle (práctica).'),
        ]),
        ('Entrevista presencial: 2,5 horas', [
            ('10 min', 'Bienvenida y resolución de dudas.'),
            ('45 min', 'Bloque 1: ONG. Tres proyectos principales, datos relevantes y algún recurso multimedia.'),
            ('45 min', 'Bloque 2: proceso de captación. Perfil del socio, parada, discurso, cierre y rebatida principal.'),
            ('10 min', 'Bloque 3: preparación del speech y práctica rápida entre candidatos.'),
            ('5 min por candidato', 'Bloque 4: juego de roles.'),
            ('5 min por candidato', 'Bloque 5: entrevista individual, con última oportunidad para los dudosos, dudas, feedback y cierre.'),
        ]),
        ('Formación inicial: horario de referencia', [
            ('10:00 a 11:45', 'Teoría: contrato, tablet e Intranet, estilo de aprendizaje, calidad del socio, proyectos clave y repaso del speech.'),
            ('11:45 a 12:00', 'Desplazamiento y ubicación en la zona.'),
            ('12:00 a 13:50', 'Captación en la calle, con chaleco, acreditación y tablet.'),
            ('13:50 a 14:00', 'Feedback positivo, aspectos de mejora y cierre del día.'),
        ]),
        ('Los cuatro estilos de aprendizaje', [
            ('Activo', 'Aprende haciendo: práctica pronto, feedback corto y concreto.'),
            ('Reflexivo', 'Aprende observando: observación guiada, ensayo y preguntas.'),
            ('Teórico', 'Aprende comprendiendo: explica la lógica y señala la regla.'),
            ('Pragmático', 'Aprende aplicando: frases y herramientas listas para usar.'),
        ]),
        ('Antes de la formación inicial', [
            ('Contrato', 'Firmado.'),
            ('Tablet', 'Activada.'),
            ('Espacio', 'Reserva conjunta para la entrevista presencial y la formación inicial, con antelación.'),
            ('Recordatorio', 'Ese turno no cuenta para rendimientos y lo haces siempre tú.'),
        ]),
    ],
    plan=[
        ('Mi proceso', [('Qué se hace distinto en mi provincia', 1, 0), ('Qué fases hago yo y con qué frecuencia', 2, 0), ('Qué sé de lo que ya se le ha contado al candidato', 3, 0), ('Cómo paso el feedback de cada candidato', 4, 0)]),
        ('Mi entrevista presencial', [('Mi horario de los cinco bloques', 5, 0), ('Mis condiciones en tres frases', 6, 0), ('Cómo resumo los tres proyectos de la ONG', 7, 0), ('Cómo explico la parada en una frase', 7, 1), ('Qué miraré en cada juego de roles', 8, 1), ('Qué dirás a un candidato dudoso', 9, 0)]),
        ('Mi formación inicial', [('Qué parte del contrato explicaré con más cuidado', 10, 0), ('Cómo comprobaré que maneja la tablet', 10, 1), ('Mi estilo y mi opinión del resultado', 11, 0), ('Cómo usaré el resultado de un candidato', 11, 1), ('Feedback y mejora al cierre del turno', 12, 0), ('Tarea para casa', 12, 1), ('Qué me falta preparar', 13, 0), ('Qué haré para que vuelva mañana', 13, 1)]),
    ],
    plan_tag='MI LISTA', plan_nombre='Mi lista del proceso', plan_mis='Lo que has escrito',
    plan_card='Una hoja con las cuatro fases, la entrevista presencial, la formación inicial y lo que has escrito para tu provincia.',
    plan1='Mi lista', plan2='del proceso',
    plan_sub='Las cuatro fases, tus bloques y tu formación inicial en una sola hoja',
    plan_gancho='Arriba tienes las chuletas de consulta. Debajo se rellenan tus respuestas; lo que falta aparece como pendiente, con un enlace a la píldora donde se completa. Solo la ves tú.',
    plan_rev='Revisa esta hoja antes de tu próxima entrevista presencial: horario, condiciones, bloques y lista previa de la formación inicial.',
    plan_frase='Que vuelva mañana.',
    plan_titulo_texto='Mi lista del proceso · Proceso de selección de personal',
    style_extra=STYLE, script_extra=CH_SCRIPT,
)

def base(**k):
    k.setdefault('estricto', True)
    return k

PILDORAS = [
 base(n=1, area='El modelo', t1='Un modelo', t2='nacional y unificado', idx='Un modelo nacional y unificado', idx_corto='Modelo unificado',
  idxp='El mismo proceso en todas las provincias, con cada fase y su objetivo.',
  gancho='Wesser tiene un modelo de selección nacional, profesional y unificado: las mismas fases, con el mismo objetivo, en todas las provincias. Lo que cambia es la organización local, y esa parte es tuya.',
  noT='Pensar que cada provincia puede montar su propio proceso o saltarse una fase.',
  siT='Seguir el modelo en las dos fases que haces tú y organizar con criterio lo local: horarios, lugar y zonas.',
  caso='Dos candidatos llegan a una entrevista presencial, uno en tu provincia y otro en otra. Los dos han pasado por las mismas fases anteriores y esperan encontrar lo mismo: la bienvenida, las condiciones y la formación inicial.',
  casoL='Un ejemplo',
  clab='¿Igual o depende?', clead='Marca si es igual en todas las provincias o depende de la provincia.', rl=['Igual en todas', 'Depende de la provincia'],
  items=[I('Las cuatro fases y su orden.', 'Piensa en el modelo nacional.', 0, 'Igual en todas: preselección, Zoom, presencial y formación inicial.'),
         I('El objetivo de cada fase.', 'Piensa en qué se busca en cada una.', 0, 'Igual en todas: detectar, atraer, seleccionar y formar y motivar.'),
         I('Si el turno es de mañana o de tarde.', 'Piensa en el horario de trabajo.', 1, 'Depende de la provincia.'),
         I('Las zonas de trabajo.', 'Piensa en quién las organiza.', 1, 'Depende de la provincia: las organiza el RP y se asignan con antelación.'),
         I('El lugar de la entrevista presencial.', 'Piensa en oficina o sala de la ONG.', 1, 'Depende de la provincia: oficina o sala de la ONG, con reserva previa.')],
  extra='Unificar no es quitar criterio: el modelo marca qué se hace y en qué orden, y tú decides cómo organizarlo en tu provincia.',
  error='Saltarte una fase del modelo por falta de tiempo.',
  plead='Piensa en tu provincia.',
  q=[('¿Qué se hace distinto en tu provincia respecto al modelo?', 'Un ejemplo concreto.', 'La formación inicial se hace en una sala de la ONG y no en nuestra oficina.'),
     ('¿Qué parte del proceso te cuesta más sostener?', 'Una parte y por qué.', 'Reservar el espacio con antelación.')],
  acc='Escribe en una frase qué se hace distinto en tu provincia y comprueba si encaja con el modelo.', chk='Ya lo escribí',
  rev='¿Hay algo que debas ajustar para seguir el modelo?', frase='Mismo modelo, organización local.'),

 base(n=2, area='El modelo', t1='Las cuatro fases', t2='y quién las hace', idx='Las cuatro fases y quién hace cada una', idx_corto='Cuatro fases',
  idxp='Preselección, Zoom, presencial y formación inicial: cuáles son tuyas.',
  gancho='El proceso tiene cuatro fases. Las dos primeras las hace el departamento de Atracción del Talento y las dos últimas las haces tú. Conviene saberlo para no repetir lo que ya se ha hecho ni dejar de hacer lo tuyo.',
  noT='Pensar que todo el proceso es tuyo o que empieza el día de la entrevista presencial.',
  siT='Saber que seleccionas a los candidatos y los formas y motivas tú, y que antes ya se ha detectado y atraído a los candidatos.',
  html_pre=fb(None),
  clab='¿Quién lo hace?', clead='Marca quién hace cada fase o cada objetivo.', rl=['Atracción del Talento', 'Responsable Provincial'],
  items=[I('Preselección, por teléfono.', 'Piensa en la fase 0.', 0, 'Atracción del Talento: detecta candidatos con potencial.'),
         I('Entrevista Zoom, por videoentrevista.', 'Piensa en la fase 1.', 0, 'Atracción del Talento: atrae a los candidatos.'),
         I('Entrevista presencial, en oficina o sala de la ONG.', 'Piensa en la fase 2.', 1, 'Responsable Provincial: selecciona a los candidatos.'),
         I('Formación inicial, teoría y práctica.', 'Piensa en la fase 3.', 1, 'Responsable Provincial: forma y motiva a los candidatos.'),
         I('Objetivo: detectar candidatos con potencial.', 'Piensa en el primer filtro.', 0, 'Atracción del Talento, en la preselección.'),
         I('Objetivo: seleccionar a los candidatos.', 'Piensa en quién decide.', 1, 'Responsable Provincial, en la entrevista presencial.')],
  extra='Las fases 0 y 1 no son tuyas, pero lo que se diga en ellas condiciona lo que te encuentras: por eso las verás en las dos píldoras siguientes.',
  error='Volver a hacer en la presencial la preselección que ya se hizo por teléfono.',
  plead='Piensa en cómo trabajas hoy.',
  q=[('¿Qué fases haces tú en tu provincia y con qué frecuencia?', 'Fase y frecuencia.', 'Entrevista presencial dos veces por semana y formación inicial al día siguiente.'),
     ('¿Cómo coordinas con Atracción del Talento el paso de candidatos?', 'Un hecho concreto.', 'Me avisan cuando hay candidatos seleccionados en el Recruitment Portal.')],
  acc='Escribe qué fases haces tú y cómo recibes a los candidatos de las fases anteriores.', chk='Ya lo escribí',
  rev='¿Hay algún paso entre fases que se pierda?', frase='Las dos últimas fases son tuyas.'),

 base(n=3, area='Antes de ti', t1='Lo que ya ha vivido', t2='el candidato', idx='Lo que ya ha vivido el candidato', idx_corto='Antes de ti',
  idxp='La preselección y la entrevista Zoom: qué se le ha contado y qué no.',
  gancho='Cuando un candidato llega a tu entrevista presencial ya ha hablado por teléfono y ha pasado por una videoentrevista. Si sabes qué se le ha contado, no lo repites y dedicas tu tiempo a lo que falta.',
  noT='Empezar de cero como si el candidato no supiera nada de Wesser.',
  siT='Saber que ya conoce el puesto y la empresa a grandes rasgos, y que las condiciones no se han tratado en profundidad: eso lo haces tú en la presencial.',
  html_pre=lista('Qué se ha hecho antes de ti', [
    ('Preselección por teléfono', 'Se comprueba el interés y la disponibilidad para incorporarse, se recuerdan las condiciones básicas y se conoce su motivación y su forma de expresarse.'),
    ('Entrevista Zoom', 'Se presenta Wesser, qué es un captador de socios, las ONG con las que se trabaja y qué ofrecemos. No se profundiza en las condiciones.'),
    ('Cita para la presencial', 'Se le avisa por SMS y correo, con vídeos de la empresa, y se le pide que avise si hay cambios.')]),
  clab='¿Ya lo sabe o lo haces tú?', clead='Marca si el candidato ya lo sabe o te toca a ti.', rl=['Ya lo sabe', 'Lo haces tú'],
  items=[I('Qué es un captador de socios y en qué consiste el trabajo.', 'Piensa en lo que se explica por Zoom.', 0, 'Ya lo sabe: se presenta en la preselección y en la entrevista Zoom.'),
         I('Con qué ONG se trabaja.', 'Piensa en la presentación de Wesser.', 0, 'Ya lo sabe a grandes rasgos. Tú profundizas en los proyectos de la ONG.'),
         I('El detalle de las condiciones y las dudas sobre el contrato.', 'Piensa en dónde se profundiza.', 1, 'Lo haces tú: en la Zoom no se profundiza en las condiciones.'),
         I('Cómo se desenvuelve en una parada.', 'Piensa en quién lo puede observar.', 1, 'Lo haces tú: lo ves en el juego de roles de la presencial.'),
         I('Que el puesto es a pie de calle y con equipos.', 'Piensa en lo que ya se ha explicado.', 0, 'Ya lo sabe: forma parte de la oferta y de la presentación.'),
         I('Si de verdad encaja y está motivado.', 'Piensa en quién selecciona.', 1, 'Lo haces tú: lo decides al final de la presencial.')],
  extra='Si puedes, mira antes qué se anotó del candidato en las fases anteriores y asiste a una entrevista Zoom de tu provincia: así sabes lo que se cuenta.',
  error='Dar por hecho que ya conoce las condiciones porque pasó por la Zoom.',
  plead='Piensa en el último candidato que recibiste.',
  q=[('Antes de recibir a un candidato, ¿qué sabes de lo que ya se le ha contado?', 'Lo que consultas antes.', 'Reviso la anotación de la preselección y el feedback de la Zoom.'),
     ('¿Qué condiciones vas a explicar tú con detalle?', 'Dos o tres.', 'Contrato, horario y cómo se organizan las zonas.')],
  acc='Antes de tu próxima entrevista presencial, mira qué se ha anotado de cada candidato en las fases anteriores.', chk='Ya lo revisé',
  rev='¿Evitaste repetir algo que ya sabía?', frase='No empieces de cero.'),

 base(n=4, area='Antes de ti', t1='Feedback', t2='y candidatos en la nevera', idx='Feedback en el Recruitment Portal y candidatos en la nevera', idx_corto='Feedback y nevera',
  idxp='Cómo pasar bien el feedback y qué hacer con los candidatos en reserva.',
  gancho='El proceso funciona si todas las personas pasan bien el feedback desde el Recruitment Portal. Eso incluye a los candidatos que dejamos en la nevera: deben marcarse como seleccionados.',
  noT='Dejar el feedback para más tarde o comentarlo solo de palabra.',
  siT='Pasar el feedback desde el Recruitment Portal, marcar como seleccionados a los candidatos en la nevera y asistir cuanto antes a una entrevista Zoom de tu provincia.',
  glos=[('Nevera', 'candidatos que quedan en reserva sin citarlos todavía')],
  clab='¿Correcto o incorrecto?', clead='Marca si cada acción es correcta o incorrecta.', rl=['Correcto', 'Incorrecto'],
  items=[I('Marcar como seleccionado a un candidato que dejas en la nevera.', 'Piensa en lo que indica el modelo.', 0, 'Correcto: los candidatos en la nevera se marcan como seleccionados.'),
         I('Dejar sin marcar al candidato de la nevera hasta decidir.', 'Piensa en lo que debe constar.', 1, 'Incorrecto: debe marcarse como seleccionado.'),
         I('Pasar el feedback desde el Recruitment Portal.', 'Piensa en dónde debe quedar.', 0, 'Correcto: es fundamental pasarlo bien desde el portal.'),
         I('Comentar el feedback de palabra y no registrarlo.', 'Piensa en lo que se pierde.', 1, 'Incorrecto: el feedback debe quedar en el portal.'),
         I('Asistir lo antes posible a una entrevista Zoom de tu provincia.', 'Piensa en lo que ves.', 0, 'Correcto: todos los RP deben asistir a una.'),
         I('Explicar al detalle las condiciones durante la entrevista Zoom.', 'Piensa en dónde se profundiza.', 1, 'Incorrecto: en la Zoom no se profundiza en las condiciones; se hace en la presencial.')],
  extra='Un feedback bien pasado evita que un buen candidato se pierda entre fases.',
  error='Pensar que un candidato en la nevera no necesita constar como seleccionado.',
  plead='Piensa en tu forma de pasar el feedback.',
  q=[('¿Cómo pasas hoy el feedback de cada candidato?', 'Cuándo y dónde.', 'Lo paso en el portal al terminar la entrevista, el mismo día.'),
     ('¿Cómo vas a gestionar los candidatos que dejas en la nevera?', 'Una acción.', 'Los marcaré como seleccionados y revisaré la lista cada semana.')],
  acc='Revisa hoy el Recruitment Portal y comprueba que los candidatos en la nevera están marcados como seleccionados.', chk='Ya lo revisé',
  rev='¿Hay algún candidato sin feedback o mal marcado?', frase='Si no está en el portal, no ha pasado.'),

 base(n=5, area='Tu entrevista presencial', t1='Entrevista presencial:', t2='dos horas y media', idx='La entrevista presencial: estructura de 2,5 horas', idx_corto='Estructura',
  idxp='Seis bloques con su tiempo, de la bienvenida a la entrevista individual.',
  gancho='La entrevista presencial dura unas dos horas y media y tiene seis bloques. Con los tiempos claros evitas que la bienvenida se alargue y que los juegos de roles se queden sin tiempo.',
  noT='Improvisar el orden o dar más tiempo del previsto a lo que más te gusta explicar.',
  siT='Repartir la sesión en bienvenida, ONG, proceso de captación, preparación del speech, juego de roles y entrevista individual, con el tiempo de cada bloque.',
  html_pre=fb(2) + lista('Los bloques y su contenido', [
    ('Bienvenida y dudas', 'Presentación, repaso de condiciones y aclaración de dudas.'),
    ('Bloque 1: ONG', 'Tres proyectos principales, datos relevantes (valores y cifras potentes) y algún recurso multimedia.'),
    ('Bloque 2: proceso de captación de socios', 'Perfil del socio, parada, discurso, cierre y rebatida principal.'),
    ('Bloque 3: preparación del speech', 'Uniendo la información de los bloques 1 y 2, con práctica rápida entre candidatos.'),
    ('Bloque 4: juego de roles', 'Uno a uno con cada candidato.'),
    ('Bloque 5: entrevista individual', 'Última oportunidad con los dudosos, aclaración de dudas, feedback y cierre.')]),
  clab='¿Cuánto dura?', clead='Marca el tiempo de cada bloque.', rl=['10 minutos', '45 minutos', '5 min por candidato'],
  items=[I('Bienvenida y resolución de dudas.', 'Piensa en el arranque.', 0, '10 minutos.'),
         I('Bloque 1: ONG.', 'Piensa en los proyectos.', 1, '45 minutos.'),
         I('Bloque 2: proceso de captación de socios.', 'Piensa en la parada, el discurso y el cierre.', 1, '45 minutos.'),
         I('Bloque 3: preparación del speech.', 'Piensa en la práctica entre candidatos.', 0, '10 minutos.'),
         I('Bloque 4: juego de roles.', 'Piensa en cada candidato.', 2, '5 minutos por candidato.'),
         I('Bloque 5: entrevista individual.', 'Piensa en el cierre con cada uno.', 2, '5 minutos por candidato.')],
  extra='Los bloques 4 y 5 dependen de cuántos candidatos haya: cada candidato suma diez minutos. Con cuatro, la sesión cabe en las dos horas y media; con más, se alarga.',
  error='Alargar el bloque de la ONG y recortar los juegos de roles, que es donde ves cómo trabajará la persona.',
  plead='Prepara tu horario.',
  q=[('Escribe el horario de tu próxima entrevista presencial con los seis bloques.', 'Hora de inicio de cada bloque.', '10:00 bienvenida, 10:10 ONG, 10:55 proceso, 11:40 speech, 11:50 juego de roles, 12:10 individual (con cuatro candidatos).'),
     ('¿Qué bloque te suele llevar más tiempo del previsto?', 'Uno y por qué.', 'El de la ONG, porque me gusta contar los proyectos con detalle.')],
  acc='Escribe el horario de tu próxima entrevista presencial con la hora de inicio de cada bloque.', chk='Ya lo escribí',
  rev='¿Cumpliste los tiempos? ¿Qué bloque se te alargó?', frase='Cada bloque con su tiempo.'),

 base(n=6, area='Tu entrevista presencial', t1='Bienvenida', t2='y condiciones', idx='Bienvenida y repaso de condiciones', idx_corto='Condiciones',
  idxp='Qué condiciones repasas con el candidato y cómo no prometer de más.',
  gancho='En la bienvenida repasas las condiciones y aclaras dudas. En la entrevista Zoom no se ha profundizado, así que esta es la ocasión de dejarlas claras y sin sorpresas.',
  noT='Dar las condiciones por sabidas o prometer ingresos concretos.',
  siT='Explicar con claridad contrato, horario, equipos y zonas, y recordar que los incentivos dependen de llegar al objetivo marcado.',
  html_pre=lista('Las condiciones del contrato novel', [
    ('Contrato', 'Laboral indefinido, con alta en la Seguridad Social desde el primer día.'),
    ('Salario base', '915 euros brutos al mes por 24 horas semanales, más incentivos si se llega al objetivo marcado.'),
    ('Horario', '24 horas a la semana, en 6 turnos de lunes a sábado. El turno del sábado puede cambiarse en ocasiones por una tarde entre semana.'),
    ('Equipos y zonas', 'Equipos de 2 o 3 personas: no se trabaja solo. Las zonas se asignan con antelación y las organiza el RP. Se trabaja en toda la provincia.'),
    ('Objetivos iniciales', 'Primeras semanas: aprender a hacer socios. Objetivo de referencia: 2 socios por turno. Con 30 socios o más en el primer o segundo mes, se accede al contrato Senior, con un turno más al mes, mejor base y mejores incentivos.')]),
  clab='¿Correcto o incorrecto?', clead='Marca si cada afirmación sobre las condiciones es correcta.', rl=['Correcto', 'Incorrecto'],
  items=[I('El contrato es laboral indefinido, con alta en la Seguridad Social desde el primer día.', 'Piensa en el tipo de contrato.', 0, 'Correcto.'),
         I('El salario base es de 915 euros brutos al mes por 24 horas semanales.', 'Piensa en la parte fija.', 0, 'Correcto, más incentivos si se llega al objetivo.'),
         I('El horario son 24 horas a la semana, en 6 turnos de lunes a sábado.', 'Piensa en los turnos.', 0, 'Correcto: el turno del sábado puede cambiarse por una tarde entre semana.'),
         I('Cada persona trabaja sola en la zona que elige.', 'Piensa en quién organiza las zonas.', 1, 'Incorrecto: son equipos de 2 o 3 personas y las zonas las organiza el RP.'),
         I('Se trabaja siempre en el mismo barrio.', 'Piensa en el alcance.', 1, 'Incorrecto: se trabaja en toda la provincia.'),
         I('Con 30 socios o más en el primer o segundo mes se accede al contrato Senior.', 'Piensa en el objetivo inicial.', 0, 'Correcto: mejora de condiciones, con un turno más al mes.'),
         I('Puedes asegurar al candidato cuánto va a ganar.', 'Piensa en de qué depende el incentivo.', 1, 'Incorrecto: los incentivos dependen de llegar al objetivo marcado, así que no prometas ingresos concretos.')],
  extra='Explica las condiciones con el material vigente. Si el candidato pregunta algo que no sabes, apúntalo y respóndele después, en lugar de improvisar.',
  error='Hablar de ingresos como si estuvieran garantizados.',
  plead='Explica las condiciones con tus palabras.',
  q=[('Explica las condiciones del contrato en tres frases.', 'Contrato, horario y zonas.', 'Contrato indefinido de 24 horas en seis turnos. Se trabaja en equipo de dos o tres en toda la provincia. Los incentivos dependen del objetivo.'),
     ('¿Qué duda recibes más y cómo la responderás?', 'Una duda y tu respuesta.', 'Cuánto voy a ganar: depende del objetivo; el contrato Senior mejora las condiciones.')],
  acc='Antes de tu próxima presencial, repasa las condiciones con el material vigente y escribe tu explicación en tres frases.', chk='Ya la escribí',
  rev='¿Qué dudas te hicieron y cuáles no supiste responder?', frase='Condiciones claras, sin prometer de más.'),

 base(n=7, area='Tu entrevista presencial', t1='ONG y proceso', t2='de captación', idx='Bloque 1 y 2: la ONG y el proceso de captación', idx_corto='ONG y captación',
  idxp='Qué contar en los dos bloques de 45 minutos.',
  gancho='Los dos bloques más largos de la entrevista son la ONG y el proceso de captación. En el primero explicas por qué importa el trabajo; en el segundo, cómo se hace.',
  noT='Contar todo lo que sabes de la ONG o explicar la parada sin ejemplos.',
  siT='En el bloque de la ONG, tres proyectos principales, datos relevantes y algún recurso multimedia. En el de captación, el perfil del socio, la parada, el discurso, el cierre y la rebatida principal.',
  clab='¿A qué bloque pertenece?', clead='Marca en qué bloque va cada contenido.', rl=['Bloque 1: ONG', 'Bloque 2: captación'],
  items=[I('Los tres proyectos principales.', 'Piensa en la ONG.', 0, 'Bloque 1: ONG.'),
         I('Valores y cifras potentes.', 'Piensa en lo que emociona.', 0, 'Bloque 1: ONG. Usa solo datos vigentes y comprobados.'),
         I('Un vídeo o recurso multimedia.', 'Piensa en el apoyo visual.', 0, 'Bloque 1: ONG.'),
         I('El perfil del socio.', 'Piensa en a quién se habla.', 1, 'Bloque 2: proceso de captación.'),
         I('La parada.', 'Piensa en cómo empieza la conversación.', 1, 'Bloque 2: proceso de captación.'),
         I('El discurso y el cierre.', 'Piensa en lo que se dice.', 1, 'Bloque 2: proceso de captación.'),
         I('La rebatida principal.', 'Piensa en la objeción más habitual.', 1, 'Bloque 2: proceso de captación.')],
  extra='Cada bloque son 45 minutos. Deja tiempo para preguntas y usa el material más reciente de la ONG.',
  error='Memorizar cifras sin comprobar que están vigentes.',
  plead='Prepara tu explicación.',
  q=[('Resume en tres frases los tres proyectos principales de la ONG con la que vas a trabajar.', 'Un proyecto por frase.', 'Proyecto 1: a quién ayuda y qué consigue. Proyecto 2: lo mismo. Proyecto 3: lo mismo.'),
     ('Explica la parada en una frase.', 'Qué pasa en los primeros segundos.', 'Es parar a la persona en la calle con un saludo y una pregunta, para poder explicarle el proyecto.')],
  acc='Prepara el resumen de los tres proyectos con el material más reciente de la ONG y practícalo en voz alta.', chk='Ya lo practiqué',
  rev='¿Qué pregunta de los candidatos no supiste responder?', frase='Primero por qué, luego cómo.'),

 base(n=8, area='Tu entrevista presencial', t1='Speech y', t2='juego de roles', idx='Preparar el speech y el juego de roles', idx_corto='Speech y roles',
  idxp='Del bloque 3 al bloque 5: practicar, simular y decidir.',
  gancho='Después de explicar, los candidatos practican. Primero preparan su speech juntos y luego lo prueban contigo en un juego de roles. Es tu mejor oportunidad para ver cómo trabajaría la persona.',
  noT='Limitarte a escuchar un discurso sin observar cómo se expresa y cómo reacciona.',
  siT='Observar en el juego de roles cómo se expresa, cómo transmite ilusión y cómo reacciona ante una objeción, igual que en la llamada de preselección.',
  clab='¿En qué bloque ocurre?', clead='Marca el bloque que corresponde a cada actividad.', rl=['Bloque 3', 'Bloque 4', 'Bloque 5'],
  items=[I('Preparar el speech uniendo la ONG y el proceso de captación.', 'Piensa en la preparación.', 0, 'Bloque 3: preparación del speech.'),
         I('Practicar rápido entre candidatos.', 'Piensa en quién practica.', 0, 'Bloque 3: práctica rápida entre candidatos.'),
         I('Simular una parada contigo, uno a uno, durante 5 minutos.', 'Piensa en el uno a uno.', 1, 'Bloque 4: juego de roles.'),
         I('Dar una última oportunidad a quien te deja dudas.', 'Piensa en el cierre individual.', 2, 'Bloque 5: entrevista individual.'),
         I('Aclarar dudas, dar feedback y cerrar.', 'Piensa en el final con cada candidato.', 2, 'Bloque 5: entrevista individual.')],
  extra='En el juego de roles fíjate en cómo se expresa y en la ilusión que transmite. Si no transmite ilusión, no valen las palabras.',
  error='Corregirle durante el juego de roles en lugar de dejar que lo termine y luego darle feedback.',
  plead='Prepara tu observación.',
  q=[('¿Cómo vas a organizar la preparación del speech para que practiquen entre ellos?', 'Cómo los pones a practicar.', 'Los junto por parejas y cada uno practica la parada con el otro dos minutos.'),
     ('¿Qué vas a mirar en cada juego de roles?', 'Tres cosas concretas.', 'Cómo empieza la parada, cómo se expresa y cómo reacciona ante una objeción.')],
  acc='Escribe tres cosas que mirarás en cada juego de roles y úsalas en tu próxima entrevista presencial.', chk='Ya las escribí',
  rev='¿Qué te dieron de información útil?', frase='El juego de roles muestra cómo trabajará.'),

 base(n=9, area='Tu entrevista presencial', t1='La entrevista', t2='individual', idx='La entrevista individual y el feedback', idx_corto='Individual',
  idxp='Cinco minutos con cada candidato para aclarar, dar feedback y cerrar.',
  gancho='La entrevista individual dura cinco minutos por candidato. Es el cierre: la última oportunidad con los dudosos, la aclaración de dudas y el feedback.',
  noT='Despedir al candidato sin feedback o con la duda sin resolver.',
  siT='Usar los cinco minutos para aclarar dudas, dar feedback sobre cómo lo ha hecho, dar una última oportunidad a quien lo necesite y cerrar con claridad qué pasa después.',
  clab='¿Cabe en los cinco minutos?', clead='Marca si encaja en la entrevista individual.', rl=['Sí', 'No'],
  items=[I('Aclarar las dudas que le queden.', 'Piensa en lo que necesita saber.', 0, 'Sí: forma parte del bloque.'),
         I('Dar feedback sobre cómo lo ha hecho.', 'Piensa en el juego de roles.', 0, 'Sí: es parte del cierre.'),
         I('Dar una última oportunidad a quien te deja dudas.', 'Piensa en los dudosos.', 0, 'Sí: está pensado para eso.'),
         I('Volver a explicar todo el bloque de la ONG.', 'Piensa en el tiempo.', 1, 'No: ya se hizo en el bloque 1 y no cabe en cinco minutos.'),
         I('Cerrar con claridad qué pasa después.', 'Piensa en el siguiente paso.', 0, 'Sí: el candidato debe saber qué esperar.'),
         I('Volver a leer el contrato entero.', 'Piensa en lo ya hecho.', 1, 'No: las condiciones se repasaron en la bienvenida.')],
  extra='Tras la entrevista, registra el feedback de cada candidato en el Recruitment Portal, también el de quienes quedan en la nevera.',
  error='Dejar la decisión sin comunicar al candidato.',
  plead='Prepara lo que vas a decir.',
  q=[('¿Qué dirás a un candidato dudoso en sus cinco minutos?', 'Una frase.', 'Me gusta tu actitud, pero necesito ver más seguridad al cerrar. ¿Qué te parece si lo repasamos?'),
     ('¿Qué feedback dejarás en el portal?', 'Qué incluyes.', 'Puntos fuertes, aspectos a mejorar y mi decisión.')],
  acc='Prepara una frase para cada tipo de candidato: seleccionado, dudoso y no seleccionado.', chk='Ya las preparé',
  rev='¿Pudiste cerrar con todos y registrar su feedback?', frase='Ningún candidato se va sin saber qué pasa.'),

 base(n=10, area='Tu formación inicial', t1='Formación inicial:', t2='la teoría', idx='Formación inicial: parte teórica', idx_corto='Teoría',
  idxp='Contrato, tablet, estilo de aprendizaje y calidad del socio, antes de salir a la calle.',
  gancho='La formación inicial empieza en la oficina o en la sala de la ONG. Son casi dos horas de teoría para que el nuevo captador entienda su contrato, maneje la tablet y salga a la calle con el discurso afianzado.',
  noT='Dar la teoría como una charla larga sin comprobar que se ha entendido.',
  siT='Hacerla por temas, con material, y comprobar en cada uno que el nuevo captador ha comprendido el contrato, maneja la tablet y tiene claro qué es un socio de calidad.',
  html_pre=fb(3) + lista('Los temas de la mañana', [
    ('10:00 · Puntos clave del contrato', 'Anexo, cláusulas, condiciones y dudas. Con infografía y check-in en la tablet.'),
    ('10:25 · Tablet e Intranet', 'Liquidaciones, cierre de turno, vacaciones, códigos de zona y formularios de socios. Con la tablet ya activada.'),
    ('10:50 · Test de estilo de aprendizaje', 'Para detectar cómo aprende cada persona. Lo practicas en la píldora siguiente.'),
    ('11:00 · Calidad del socio', 'Perfil, edades, cuota y sensibilización, con una infografía del perfil del donante.'),
    ('11:15 · Repaso de proyectos clave', 'Proyectos principales y locales de la ONG.'),
    ('11:35 · Repaso del speech, negociación y cierre', 'Introducción, proyectos, importancia del socio, negociación de la cuota y cierre.')]),
  clab='¿De qué tema es?', clead='Marca el tema al que pertenece cada contenido.', rl=['Contrato', 'Tablet e Intranet', 'Calidad del socio'],
  items=[I('Anexo y cláusulas.', 'Piensa en el documento.', 0, 'Contrato.'),
         I('Liquidaciones y cierre de turno.', 'Piensa en lo que se hace con la tablet.', 1, 'Tablet e Intranet.'),
         I('Códigos de zona y formularios de socios.', 'Piensa en lo que se registra.', 1, 'Tablet e Intranet.'),
         I('Perfil del donante y edades.', 'Piensa en quién es un socio.', 2, 'Calidad del socio.'),
         I('Cuota y sensibilización.', 'Piensa en la importancia del socio.', 2, 'Calidad del socio.'),
         I('Dudas sobre las condiciones del puesto.', 'Piensa en lo que firma.', 0, 'Contrato.')],
  extra='Si la tablet no está activada o el contrato no está firmado, no se puede empezar con garantías: compruébalo antes.',
  error='Pasar rápido por el contrato para llegar a la práctica.',
  plead='Prepara la teoría.',
  q=[('¿Qué parte del contrato explicarás con más cuidado?', 'Una parte y por qué.', 'Las cláusulas del horario y de las zonas, porque generan más dudas.'),
     ('¿Cómo comprobarás que maneja la tablet?', 'Una comprobación.', 'Le pediré que haga el check-in y un formulario de prueba mientras lo miro.')],
  acc='Prepara una comprobación breve para cada tema de la teoría: contrato, tablet y calidad del socio.', chk='Ya las preparé',
  rev='¿Qué tema dejó más dudas?', frase='Que lo entienda, no que lo escuche.'),

 base(n=11, area='Tu formación inicial', t1='Estilos de', t2='aprendizaje', idx='Estilos de aprendizaje: test CHAEA Express y cómo enseñar a cada uno', idx_corto='Estilos',
  idxp='El CHAEA Express, de 16 frases, y cinco ideas para enseñar a cada estilo.',
  gancho='En la formación inicial se hace a los nuevos captadores un test de estilo de aprendizaje, el CHAEA Express. Hazlo tú primero: verás cómo funciona y qué ideas te da para enseñar a cada persona.',
  noT='Etiquetar a la persona nueva con un estilo y enseñarle solo de esa forma.',
  siT='Usar el resultado como una pista de por dónde empezar. Cada persona aprende con una mezcla de formas: lo importante es probar, observar cómo responde y ajustar.',
  caso='Dos personas oyen la misma explicación del discurso. Una quiere salir ya a probarlo; la otra prefiere ver antes cómo lo hace alguien. Ninguna es mejor: aprenden por caminos distintos.',
  casoL='Un ejemplo',
  html_pre=fb(3) + lista('Los cuatro estilos', [
    ('Activo · aprende haciendo', 'Impulsivo, enérgico, explorador y tolera el error.'),
    ('Reflexivo · aprende observando', 'Prudente, analítico, observador y seguro cuando comprende.'),
    ('Teórico · aprende comprendiendo', 'Lógico, estructurado, sistemático y orientado a entender.'),
    ('Pragmático · aprende aplicando', 'Práctico, resolutivo, orientado a resultados.')]),
  clab='¿Encaja con su estilo?', clead='Marca si cada forma de enseñar encaja con el estilo indicado.', rl=['Encaja', 'No encaja'],
  items=[I('A una persona de estilo activo le dejas practicar enseguida y le das una sola mejora clara.', 'Piensa en cómo aprende.', 0, 'Encaja: aprende con la experiencia directa y le sirve una corrección concreta.'),
         I('A una persona de estilo reflexivo le pides que haga muchas paradas desde el primer momento.', 'Piensa en lo que necesita antes de actuar.', 1, 'No encaja: necesita observar con foco y ensayar antes de subir el volumen.'),
         I('A una persona de estilo teórico le explicas por qué existe cada paso del discurso.', 'Piensa en lo que busca.', 0, 'Encaja: integra mejor lo que comprende.'),
         I('A una persona de estilo pragmático le das frases exactas y recursos listos para usar.', 'Piensa en lo que valora.', 0, 'Encaja: quiere herramientas aplicables enseguida.'),
         I('A una persona de estilo teórico solo le dices «esto está mal».', 'Piensa en qué necesita saber.', 1, 'No encaja: necesita saber qué regla o principio se ha roto.'),
         I('A una persona de estilo activo le haces escuchar una explicación larga antes de probar.', 'Piensa en cuánto aguanta sin actuar.', 1, 'No encaja: se puede desconectar si tarda en practicar.')],
  html_post=TEST_HTML,
  extra='Los estilos de aprendizaje son una herramienta de orientación, no un diagnóstico, y la investigación no ha encontrado pruebas sólidas de que enseñar solo según el estilo mejore los resultados. Úsalo para tener ideas y comprueba siempre cómo responde la persona.',
  error='Decidir cómo formar a alguien solo por el resultado de un test de dieciséis frases.',
  plead='Piensa en cómo vas a usarlo.',
  q=[('¿Qué estilo ha salido en tu test y qué opinas del resultado?', 'Una frase.', 'Me ha salido pragmático, y creo que es cierto porque me gusta tener frases listas.'),
     ('¿Cómo vas a usar el resultado de un candidato en su formación inicial?', 'Una idea concreta.', 'Si sale reflexivo, le daré una lista de cosas a observar antes de la primera parada.')],
  acc='Haz el test, lee los cinco consejos de tu resultado y elige uno para aplicar con el próximo nuevo captador.', chk='Ya elegí mi consejo',
  rev='¿Cómo respondió la persona? ¿Tuviste que cambiar de enfoque?', frase='El estilo orienta; la persona decide.'),

 base(n=12, area='Tu formación inicial', t1='Formación inicial:', t2='la calle', idx='Formación inicial: parte práctica en la calle', idx_corto='Calle',
  idxp='Paradas, discursos, rebatidas, feedback y cierre del día.',
  gancho='Después de la teoría, sales con el nuevo captador a la calle. El objetivo es que consiga el mayor número posible de paradas y discursos, aprenda a rebatir objeciones y, si puede, apunte su primer socio.',
  noT='Dejarle solo o hacerlo todo tú.',
  siT='Acompañarle en una calle con afluencia, con chaleco, acreditación y tablet, y cerrar el día con feedback positivo, aspectos de mejora y una tarea para casa.',
  html_pre=lista('El horario de la práctica', [
    ('11:45 · Desplazamiento y ubicación', 'Llegar a la zona de captación.'),
    ('12:00 · Captación en la calle', 'Con chaleco, acreditación y tablet, en una calle con afluencia. Mayor número de paradas y discursos hasta el cierre y la negociación. Aprender a rebatir objeciones. Deseable que apunte su primer socio.'),
    ('13:50 · Feedback', 'Feedback positivo y aspectos de mejora para el día siguiente, con una tarea para casa.'),
    ('14:00 · Cierre del día', 'Que tenga el conocimiento y la motivación para volver mañana.')]),
  clab='¿Antes o durante?', clead='Marca si va antes de salir a la calle o durante el turno de calle.', rl=['Antes de salir', 'En la calle'],
  items=[I('Comprobar que lleva chaleco, acreditación y tablet.', 'Piensa en el material.', 0, 'Antes de salir.'),
         I('Conseguir el mayor número de paradas posible.', 'Piensa en el objetivo del turno.', 1, 'En la calle.'),
         I('Aprender a rebatir las objeciones que surjan.', 'Piensa en lo que pasa en las paradas.', 1, 'En la calle.'),
         I('Dar feedback positivo y un aspecto de mejora.', 'Piensa en el final del turno.', 1, 'En la calle, al final del turno.'),
         I('Dejar una tarea para casa.', 'Piensa en el día siguiente.', 1, 'En la calle, en el cierre del turno.'),
         I('Comprobar que la tablet está activada.', 'Piensa en lo que se prepara antes.', 0, 'Antes de salir.')],
  extra='Este turno no cuenta para rendimientos: se trata de aprender, no de producir. Tu objetivo es que vuelva mañana.',
  error='Medir el turno por el número de socios y olvidar el feedback.',
  plead='Prepara el cierre del día.',
  q=[('¿Qué feedback positivo y qué mejora darás al cierre del turno?', 'Una cosa de cada.', 'Has aguantado los no sin parar. Mañana prueba a saludar con más calma.'),
     ('¿Qué tarea para casa darás?', 'Una tarea concreta.', 'Repasar la rebatida principal en voz alta.')],
  acc='Prepara el feedback positivo, la mejora y la tarea para casa del próximo turno de formación en la calle.', chk='Ya los preparé',
  rev='¿Salió motivado? ¿Volvió al día siguiente?', frase='Un turno para aprender, no para producir.'),

 base(n=13, area='Tu formación inicial', t1='Antes de empezar:', t2='lista y objetivo', idx='Lista previa y objetivo de la formación inicial', idx_corto='Lista previa',
  idxp='Contrato firmado, tablet activada y un solo objetivo: que vuelva mañana.',
  gancho='Antes de la formación inicial, hay cinco cosas que comprobar. Y un solo objetivo: que el nuevo captador tenga el conocimiento y la motivación necesarios para volver mañana.',
  noT='Empezar la formación sin el contrato firmado o sin tablet activada.',
  siT='Comprobar la lista previa, reservar el espacio con antelación y recordar que la formación inicial la haces siempre tú y que ese turno no cuenta para rendimientos.',
  clab='¿Correcto o incorrecto?', clead='Marca si cada afirmación es correcta.', rl=['Correcto', 'Incorrecto'],
  items=[I('El contrato debe venir firmado antes de empezar.', 'Piensa en lo imprescindible.', 0, 'Correcto.'),
         I('La tablet debe estar activada antes de empezar.', 'Piensa en lo que se usa en la mañana.', 0, 'Correcto.'),
         I('La formación inicial la puede hacer cualquier compañero.', 'Piensa en quién es responsable.', 1, 'Incorrecto: siempre la realiza el Responsable Provincial.'),
         I('El turno de la formación inicial cuenta para rendimientos.', 'Piensa en el objetivo del día.', 1, 'Incorrecto: este turno no cuenta para rendimientos.'),
         I('Se pide la reserva de espacio para la presencial y la formación a la vez, con antelación.', 'Piensa en la organización.', 0, 'Correcto: petición conjunta y con antelación suficiente.'),
         I('El objetivo principal es que tenga el conocimiento y la motivación para volver mañana.', 'Piensa en lo que buscas.', 0, 'Correcto: es el objetivo principal de la formación inicial.')],
  extra='Si algo de la lista no está listo, resuélvelo antes de empezar.',
  error='Medir el éxito de la formación inicial por los socios del día.',
  plead='Prepara tu próxima formación inicial.',
  q=[('¿Qué te falta preparar para tu próxima formación inicial?', 'Una cosa concreta.', 'Reservar la sala y comprobar que las tablets están activadas.'),
     ('¿Qué harás para que vuelva mañana?', 'Una acción.', 'Cerraré con un feedback positivo y le diré a qué hora empezamos mañana.')],
  acc='Revisa la lista previa de tu próxima formación inicial y completa lo que falte.', chk='Ya la revisé',
  rev='¿Volvió al día siguiente todo el que debía?', frase='Que vuelva mañana.', estricto=True),
]
