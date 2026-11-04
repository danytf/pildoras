import os
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import data_cnv as O
SERIE=dict(O.SERIE)
SERIE.update(key='wesser-serie-cnv2', dur='3-4 min',
  intro=('Esta serie va dirigida a responsables de equipo. Las palabras no solo informan: también acercan o alejan. Aquí aprendes a hablar y a escuchar con la Comunicación No Violenta (CNV), un enfoque creado por Marshall Rosenberg: observar sin juzgar, nombrar lo que sientes y lo que necesitas, y pedir algo concreto. '
         'Recorre las cuatro piezas, una pausa para escucharte a ti y unas frases para comprobar cómo llega lo que dices. '
         'Son 12 píldoras de 3 a 4 minutos, con ejemplos y mini-tests, y cada una se entiende sola. Si tienes poco tiempo, haz la ruta de cinco.'),
  glosario=[('CNV', 'Comunicación No Violenta: forma de hablar y escuchar que cuida la conexión con la otra persona.'),
            ('Observación', 'Lo que una cámara podría grabar, sin valorarlo.'),
            ('Valoración', 'Etiqueta u opinión sobre la persona o el hecho.'),
            ('Necesidad', 'Lo que te importa y hay debajo de un sentimiento: claridad, orden, respeto…'),
            ('Estrategia', 'Una forma concreta de cubrir una necesidad, como «que me envíe el parte».'),
            ('Petición', 'Lo concreto y posible que pides; admite un «no». Si no admite un «no», es una exigencia.'),
            ('Autoempatía', 'Escucharte a ti mismo: cuerpo, sentimiento y necesidad.')],
  chuleta=[
   ('Las cuatro piezas en una frase', [
     ('Observación', '«Cuando el parte llega el martes…»'),
     ('Sentimiento', '«…me preocupo…»'),
     ('Necesidad', '«…porque necesito planificar con tiempo.»'),
     ('Petición', '«¿Puedes enviarlo el viernes antes de las 14 h?»')]),
   ('Del juicio a la pieza', [
     ('«Nunca te implicas»', 'Observación: qué hizo, cuándo y cuántas veces.'),
     ('«Me siento ignorado»', 'Sentimiento: tristeza, soledad, preocupación…'),
     ('«Que me den la razón»', 'Necesidad: respeto, ser escuchado…'),
     ('«Sé más responsable»', 'Petición: qué, cuándo y una pregunta al final.')]),
   ('Para cerrar comprobando', [
     ('Entendimiento', '«¿Qué has entendido de lo que te he dicho?»'),
     ('Obstáculos', '«¿Qué necesitas para poder hacerlo?»'),
     ('Otra vez', '«Voy a reformularlo.»'),
     ('Reacción', '«¿Cómo te llega esto?»')]),
   ('Si estás en modo chacal', [
     ('Para', 'Unos segundos antes de contestar.'),
     ('Pregúntate', '¿Qué siento? ¿Qué necesito yo aquí?'),
     ('Después', 'Observa, nombra lo que necesitas y pide.')]),
  ])
SERIE['plan_rev']='Revisa esta guía a las dos semanas: qué situaciones has trabajado, cómo respondieron y qué cambiarías.'
SERIE.setdefault('plan_frase','Observa, nombra lo que necesitas y pide.')
SERIE.setdefault('plan_titulo_texto','Mi guía de comunicación · Comunicación consciente en equipos')
SERIE.setdefault('plan_mis','Lo que has escrito')
P=[dict(p) for p in O.PILDORAS]
for p in P:
    p['clead']=p['clead'].replace('Paso 1. ','').replace('Paso 2. ','')
    p['plead']=p['plead'].replace('Paso 2. ','')
X={
 1:dict(caso='Antes: «Hay que mandar el parte ya, que siempre vamos con retraso.» Después: «El lunes necesito el parte para planificar los turnos; ¿puedes enviarlo?» La información es la misma, pero la primera cierra y la segunda abre.',
        error='Pensar que si el mensaje es correcto, el efecto da igual. El efecto lo decide quien escucha.'),
 2:dict(caso='Antes: «Estás siempre igual, así no se puede trabajar.» Después: «Esta semana han llegado dos partes tarde. Me preocupa no poder planificar. ¿Puedes enviarlos el viernes?» Mismo problema, dicho con las cuatro piezas.',
        error='Creer que la CNV consiste en ser amable. Se trata de ser claro sin culpar.',
        items=[('Observación','Lo que ves o lo que oyes, sin valorarlo.',{1:'Antes de hablar, escribe el hecho en una frase que una cámara pudiera grabar.'}),
               ('Sentimiento','Cómo te afecta lo que observas.',{1:'Elige una palabra sobre ti: preocupado, cansado, tranquilo.'}),
               ('Necesidad','Lo que hay detrás de ese sentimiento: lo que te importa.',{1:'Pregúntate «¿qué necesito yo aquí?» antes de decir nada.'}),
               ('Petición','Algo concreto y posible que pides ahora; la otra persona puede aceptarlo o no.',{1:'Termina con una pregunta que se pueda contestar con sí o no.'})]),
 3:dict(caso='Llega tarde el parte y respondes: «Ya estamos otra vez, así no hay quien trabaje» (chacal). Si paras unos segundos: «Me preocupa no poder planificar; ¿qué necesitáis de mí para tenerlo el viernes?» (jirafa).',
        error='Usar «chacal» como insulto para otros. Es un modo en el que todos entramos.',estricto=True),
 4:dict(caso='Antes: «Eres un desorganizado.» Después: «Este mes tres partes han llegado después del lunes.» La segunda se puede comprobar y deja espacio para hablar.',
        glos=[('observación','lo que una cámara podría grabar'),('valoración','etiqueta u opinión sobre la persona')],
        error='Pensar que observar es callarte lo que sientes. Primero el hecho, y después lo demás.',estricto=True),
 5:dict(caso='Antes: «Me siento ignorado» (supone lo que hace el otro). Después: «Me siento triste, porque eché de menos tu respuesta.» La segunda habla de ti y no acusa.',
        error='Poner «me siento» delante de un juicio. «Me siento utilizado» sigue siendo una acusación.',estricto=True),
 6:dict(caso='Antes: «Quiero que me envíes el parte antes del lunes» (estrategia). Después: «Necesito orden para planificar los turnos» (necesidad). Con la necesidad clara, hay varias maneras de cubrirla.',
        glos=[('necesidad','lo que te importa, como claridad u orden'),('estrategia','forma concreta de cubrir una necesidad')],
        error='Confundir lo que quieres con lo que necesitas. Lo que quieres es una forma de cubrirlo.',estricto=True),
 7:dict(caso='Antes: «Sé más responsable.» Después: «¿Puedes avisarme antes de las 18 h del día anterior si no vas a poder cubrir tu turno?» La segunda dice qué, cuándo y admite un «no».',
        glos=[('petición','lo que pides con un qué, un cuándo y la posibilidad de un «no»')],
        error='Pedir en negativo («que no llegues tarde»). Di qué quieres que ocurra.',estricto=True),
 8:dict(caso='Antes: «Me agobia que nunca avises.» Después: «Esta semana dos personas no avisaron del cambio; estoy preocupado porque necesito organizar los turnos. ¿Podéis avisarme el día antes?»',
        error='Recitar la fórmula como un guion. Con tus palabras suena más natural.',estricto=True),
 9:dict(caso='Quieres que alguien entregue el informe a tiempo y le dices: «Esto no puede seguir así». Tu intención era pedir puntualidad; a él le llegó que desconfías de su trabajo. Preguntar «¿qué te llegó?» saca a la luz la diferencia.',
        error='Defender la intención en cuanto el otro cuenta lo que le llegó. Primero escucha.',
        items=[('¿Qué quería conseguir realmente?','Tu intención, dicha en una frase.',{1:'Escríbela antes de entrar en la conversación.'}),
               ('¿Coincide con lo que ha recibido la otra persona?','Pregúntaselo y escucha.',{1:'Hazle la pregunta y espera, sin explicar.'}),
               ('¿Qué me sorprende?','Lo que no esperabas oír.',{1:'Apunta lo que no esperabas: es lo que más información da.'}),
               ('¿Qué impacto creía que iba a generar?','Y qué impacto ha tenido de verdad.',{1:'Compara lo que esperabas con lo que cuenta el otro.'})]),
 10:dict(caso='Antes de una reunión tensa, te tomas dos minutos: notas tensión en los hombros, nombras preocupación y reconoces que necesitas orden. Entras a la reunión sabiendo qué te pasa a ti, y escuchas mejor.',
        error='Hacerla solo cuando estás desbordado. Funciona mejor como hábito corto antes de conversaciones importantes.',
        items=[('Respira','Una o dos respiraciones profundas, soltando el aire despacio.',{1:'Prueba hoy con dos respiraciones antes de abrir un correo difícil.'}),
               ('Escanea el cuerpo','De los pies a la cabeza: tensión, peso, calor, cosquilleo o ninguna sensación.',{1:'Recorre el cuerpo de abajo arriba y quédate con la zona que más se nota.'}),
               ('Nombra el sentimiento','¿Qué emoción hay detrás de esas sensaciones?',{1:'Elige una palabra sobre ti, no sobre el otro.'}),
               ('Encuentra la necesidad','Descanso, claridad, apoyo, espacio… ¿qué necesitas ahora?',{1:'Mira la lista de la píldora 6 y elige una palabra.'}),
               ('Reconócela','Dite: «es importante para mí cubrir esta necesidad». Cierra con una última respiración.',{1:'Termina con una frase corta, sin juzgarte.'})]),
 11:dict(caso='Antes: «¿Entendido?» «Sí.» (y luego no ocurre). Después: «¿Qué necesitas de mí para tener el parte el viernes?» La respuesta te dice si hay un obstáculo.',
        error='Usar las frases como examen. Hazlas con curiosidad.',
        items=[('«¿Qué has entendido de lo que te he dicho?»','Comprueba el mensaje sin examinar.',{1:'Cámbiala por «¿cómo se lo contarías a otra persona?» si suena a examen.'}),
               ('«¿Qué necesitas para poder hacerlo?»','Detecta obstáculos antes de que aparezcan.',{1:'Ponla siempre tras una petición.'}),
               ('«Voy a reformularlo.»','Te ofreces a explicarlo de otra manera si no ha llegado.',{1:'Úsala cuando notes cara de duda.'}),
               ('«¿Cómo te llega esto?»','Abre espacio para su reacción.',{1:'Haz la pregunta y espera en silencio antes de seguir.'})]),
 12:dict(caso='Una persona de tu equipo lleva un mes sin implicarse. Observación: «Este mes no has respondido a tres avisos que mandé al equipo». Sentimiento y necesidad: «Me preocupa; necesito saber que cuento contigo». Petición: «¿Podemos hablar diez minutos mañana?»',
        error='Intentar aplicar las cuatro piezas a todo a la vez. Elige una situación y una pieza.',
        items=[('Alguien no llega a objetivos','Observa los hechos y pregunta qué necesita antes de proponer nada.',{1:'Esta semana, empieza con una pregunta abierta en vez de un consejo.'}),
               ('Permisos sin confirmar o sin pedir','Observa qué falta, nombra lo que necesitas y pide una acción concreta con una fecha.',{1:'Escribe la petición con qué y cuándo antes de hablar.'}),
               ('Falta de implicación','Nombra lo que ves y lo que necesitas, y haz una petición concreta.',{1:'Empieza por un hecho concreto, no por «te noto desinteresado».'}),
               ('Una conversación incómoda','Prepara tu sentimiento y tu necesidad antes de entrar.',{1:'Haz antes la pausa de la píldora 10.'}),
               ('Tensión en el equipo','Escucha las necesidades de cada parte antes de buscar una solución.',{1:'Pregunta a cada parte qué es lo más importante para ella, por separado.'})]),
}
def conv(items):
    out=[]
    for it in items:
        if len(it)==3 and isinstance(it[2],dict): out.append(it)
        else: out.append(tuple(it))
    return out
for p in P:
    x=X.get(p['n'],{})
    for k,v in x.items(): p[k]=v
    p['items']=conv(p['items'])
PILDORAS=P
