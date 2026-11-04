#!/usr/bin/env python3
"""Constructor genérico de series de píldoras Wesser.
Uso: python3 build_gen.py data_xxx.py salida.html
El módulo de datos define SERIE (dict) y PILDORAS (lista de dict)."""
import sys, json, html, importlib.util, os

HERE = os.path.dirname(os.path.abspath(__file__))
STYLES = open(os.path.join(HERE, 'styles_v3.html'), encoding='utf8').read() + open(os.path.join(HERE, 'styles_k.html'), encoding='utf8').read()
JSTPL = open(os.path.join(HERE, 'tpl_k.js'), encoding='utf8').read()
VALORES = '<div class="valores" role="note"><span><b>Compromiso ·</b> <b>Compañerismo ·</b> <b>Ambición por el progreso</b></span><span><b>Iniciativa y autonomía ·</b> <b>Afán de superación ·</b> <b>Orgullo</b></span></div>'
LOGO = open(os.path.join(HERE, 'logo.b64')).read().strip()

def svg(inner):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + inner + '</svg>')

IC = {
    'no': svg('<path d="M18 6 6 18" /> <path d="m6 6 12 12" />'),
    'si': svg('<path d="M20 6 9 17l-5-5" />'),
    'back': svg('<path d="m12 19-7-7 7-7" /> <path d="M19 12H5" />'),
    'next': svg('<path d="M5 12h14" /> <path d="m12 5 7 7-7 7" />'),
    'acc': svg('<circle cx="12" cy="12" r="10" /> <circle cx="12" cy="12" r="6" /> <circle cx="12" cy="12" r="2" />'),
    'clock': svg('<circle cx="12" cy="12" r="10" /> <path d="M12 6v6l4 2" />'),
    'plan': svg('<rect width="8" height="4" x="8" y="2" rx="1" ry="1" /> <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2" /> <path d="M12 11h4" /> <path d="M12 16h4" /> <path d="M8 11h.01" /> <path d="M8 16h.01" />'),
    'pdf': svg('<path d="M12 3v12" /> <path d="m7 10 5 5 5-5" /> <path d="M5 21h14" />'),
    'sos': svg('<path d="M12 9v4"/><path d="M12 17h.01"/><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>'),
    'wa': svg('<path d="M21 11.5a8.4 8.4 0 0 1-12.5 7.3L3 20.5l1.8-5.3A8.4 8.4 0 1 1 21 11.5Z" />'),
}

def e(s):
    return html.escape(str(s), quote=True)

def pad(n):
    return '%02d' % n

def build(mod_path, out_path):
    spec = importlib.util.spec_from_file_location('datos', mod_path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    S, P = m.SERIE, m.PILDORAS
    DUR = S.get('dur', '3 min')
    N = len(P)
    nombre = S['nombre1'] + ' ' + S['nombre2']
    pie = 'Formación y Desarrollo · Serie «%s»' % nombre
    plan = S['plan']
    plan_total = sum(len(g[1]) for g in plan)

    gen = []
    for p in P:
        k = len(p['items']); q = len(p['q']); h = 1
        gen.append({'n': p['n'], 'k': k, 'q': q, 'h': h, 'T': k + q + h, 'strict': bool(p.get('estricto')), 'grp': [{'i': g_[1], 'n': g_[2], 'r': g_[3]} for g_ in p.get('grupos', [])] or None,
                    'ans': [it[2] if len(it) > 2 and not isinstance(it[2], dict) else None for it in p['items']],
                    'opt': [it[2] if len(it) > 2 and isinstance(it[2], dict) else {} for it in p['items']],
                    'fb': [it[3] if len(it) > 3 else '' for it in p['items']]})
    views = {'inicio': ['SERIE', nombre, DUR + ' cada una'],
             'mi-kit': [S['plan_tag'], nombre, 'Solo para ti']}
    for p in P:
        views['pildora-%d' % p['n']] = ['PÍLDORA ' + pad(p['n']), p['area'], DUR]

    o = []
    o.append('<!doctype html><html lang="es"><head><meta charset="utf-8">'
             '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
             '<title>%s</title><meta name="claude:viewport-fit-sides" content="cover">'
             '<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Source+Sans+3:wght@400..700&display=swap">'
             '</head><body>' % e(nombre) + STYLES)
    if S.get('style_extra'): o.append('<style>%s</style>' % S['style_extra'])
    o.append('<header class="top"><div class="top-in"><div class="logo"><img alt="Wesser, un buen trabajo" src="data:image/png;base64,%s"></div>'
             '<div class="tag"><b id="tag-b">SERIE</b><span id="tag-a">%s</span><small>%s<span id="tag-s">%s cada una</span></small></div></div></header>'
             % (LOGO, e(nombre), IC['clock'], DUR))

    # ---------- inicio
    o.append('<div id="view-inicio" class="view"><main class="wrap">')
    o.append('<h1 tabindex="-1">%s<em>%s</em></h1><p class="sub">%s</p><p class="intro">%s</p>'
             % (e(S['nombre1']), e(S['nombre2']), e(S['sub']), e(S['intro'])))
    if S.get('aviso'):
        o.append('<p class="nota" style="margin-top:12px;color:var(--ink)">%s</p>' % e(S['aviso']))
    if S.get('sos_groups'):
        o.append('<button type="button" class="sos-btn" data-sos>%s<span><b>%s</b><small>%s</small></span></button>' % (IC['sos'], e(S.get('sos_btn','¡Estoy en plena racha!')), e(S.get('sos_btn_sub','Abrir la guía de 30 segundos'))))
    o.append('<section><h2 class="lab">De qué trata</h2><ul class="how tema">')
    for b, t in S['tema']:
        o.append('<li><div><b>%s</b>%s</div></li>' % (e(b), e(t)))
    o.append('</ul></section>')
    if S.get('glosario'):
        o.append('<section><h2 class="lab">Palabras que verás</h2><ul class="how tema">')
        for b_, t_ in S['glosario']:
            o.append('<li><div><b>%s</b>%s</div></li>' % (e(b_), e(t_)))
        o.append('</ul></section>')
    o.append('<section><h2 class="lab">Cómo funciona</h2><ol class="how">'
             '<li><span class="hn">1</span><div><b>Lee la idea</b>Una sola idea clave, con un caso para verla en tu día.</div></li>'
             '<li><span class="hn">2</span><div><b>Comprueba y responde</b>Una autoevaluación con su lectura y una mini-práctica de dos minutos. Lo que escribes lo ves solo tú.</div></li>'
             '<li><span class="hn">3</span><div><b>Da el paso de la semana</b>Uno solo, pequeño. No hace falta hacer uno por semana: haz el que toque y encadénalos a tu ritmo.</div></li></ol>'
             '<p class="nota" style="color:var(--ink)">Puedes hacerlas en el orden que quieras: cada una se entiende sola. Tu avance se guarda en este dispositivo.</p></section>')
    byn = {p['n']: p for p in P}
    o.append('<section><h2 class="lab">Si no sabes por dónde empezar</h2><p class="lead">Un recorrido corto de cinco píldoras, de 15 a 20 minutos en total.</p><div class="ruta">')
    chips = ['<a class="chip" href="#pildora-%d">%s %s</a>' % (n, pad(n), e(byn[n]['idx_corto'])) for n in S['ruta']]
    o.append('<i>›</i>'.join(chips) + '</div></section>')
    o.append('<section><h2 class="lab">Las %d píldoras</h2><div class="idx">' % N)
    for p in P:
        n = p['n']; g = gen[n - 1]
        o.append('<a class="card" href="#pildora-%d"><div class="card-top"><span class="num">%s</span><div><h3>%s</h3><small>%s · %s</small></div><span class="go">%s</span></div>'
                 '<p>%s</p><div class="st"><span id="idx-%d-txt">Sin empezar</span><output id="idx-%d-n">0 de %d</output></div><div class="bar"><i id="idx-%d-bar"></i></div></a>'
                 % (n, pad(n), e(p['idx']), e(p['area']), DUR, IC['next'], e(p['idxp']), n, n, g['T'], n))
    o.append('</div></section>')
    o.append('<section><h2 class="lab">Tu resultado</h2><a class="planc" href="#mi-kit"><b>%s%s</b><p>%s</p>'
             '<output id="plan-n">0 de %d apartados</output><div class="bar"><i id="plan-bar"></i></div></a></section>'
             % (IC['plan'], e(S['plan_nombre']), e(S['plan_card']), plan_total))
    o.append('<footer class="pie">%s<br>Tus respuestas se guardan solo en este dispositivo.</footer></main>' % e(pie) + VALORES + '</div>')

    # ---------- píldoras
    for p in P:
        n = p['n']; g = gen[n - 1]; pre = 'g%d' % n
        o.append('<div id="view-pildora-%d" class="view" hidden>' % n)
        o.append('<div class="prog" aria-live="polite"><div class="prog-in"><div class="prog-row"><span>Tu avance en esta píldora</span><output id="%s-prog-txt">0 de %d</output></div>'
                 '<div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="%d" aria-valuenow="0" id="%s-bar"><i id="%s-bar-i"></i></div></div></div>'
                 % (pre, g['T'], g['T'], pre, pre))
        o.append('<main class="wrap"><div class="backrow"><a class="back" href="#inicio">%sTodas las píldoras</a>%s</div>' % (IC['back'], ('<button type="button" class="sos-mini" data-sos>%s%s</button>' % (IC['sos'], e(S.get('sos_mini','Plena racha')))) if S.get('sos_groups') else ''))
        o.append('<h1 tabindex="-1" style="font-size:clamp(32px,9.6vw,54px)">%s<em>%s</em></h1>' % (e(p['t1']), e(p['t2'])))
        o.append('<div class="gancho">%s</div>' % e(p['gancho']))
        o.append('<div class="cols"><div class="col-a">')
        o.append('<section><h2 class="lab">La idea clave</h2><div class="duo">'
                 '<div class="no"><h3>%s%s</h3><p>%s</p></div>'
                 '<div class="si"><h3>%s%s</h3><p>%s</p></div></div>'
                 % (IC['no'], e(p.get('noL', 'Lo que no es')), e(p['noT']), IC['si'], e(p.get('siL', 'Lo que sí es')), e(p['siT'])))
        if p.get('caso'):
            o.append('<div class="decir cso"><small>%s</small><p>%s</p></div>' % (e(p.get('casoL', 'Así se ve en tu día')), e(p['caso'])))
        if p.get('glos'):
            o.append('<p class="nota" style="margin-top:12px;color:var(--ink)"><b>En esta píldora:</b> %s.</p>' % '; '.join('<b>%s</b>, %s' % (e(a_), e(b_)) for a_, b_ in p['glos']))
        o.append('</section>')
        if p.get('html_pre'): o.append(p['html_pre'])
        nl = len(p['rl'])
        def card(i, it):
            btns = ''.join('<button type="button" aria-pressed="false" data-i="%d" data-k="%d">%s</button>' % (i, kk, e(lab_)) for kk, lab_ in enumerate(p['rl']))
            return ('<div class="z-i" id="%s-r%d"><b%s>%s</b><span>%s</span><div class="ok2"%s>%s</div><p class="lect" id="%s-fb%d"></p></div>'
                    % (pre, i, (' class="sent"' if (it[0][0] in '«' or len(it[0]) > 34) else ''), e(it[0]), e(it[1]),
                       (' style="grid-template-columns:repeat(%d,minmax(0,1fr))"' % nl) if nl != 2 else '', btns, pre, i))
        if p.get('grupos'):
            for gt, gidx, gn, gr in p['grupos']:
                o.append('<section><h2 class="lab">%s</h2><div class="zs">' % e(gt))
                for i in gidx:
                    o.append(card(i, p['items'][i]))
                o.append('</div></section>')
            o.append('<section><h2 class="lab">Tu resultado</h2><div class="decir cso" id="%s-res"><small>Resultado del check-in</small><p>Marca los síntomas para ver tu resultado.</p></div>' % pre)
            if p.get('extra'):
                o.append('<p class="nota" style="margin-top:12px;color:var(--ink)">%s</p>' % e(p['extra']))
            o.append('</section>')
        else:
          o.append('<section><h2 class="lab">%s</h2><p class="lead">%s</p><div class="zs">' % (e(p['clab']), e(p['clead'])))
          for i, it in enumerate(p['items']):
            btns = ''.join('<button type="button" aria-pressed="false" data-i="%d" data-k="%d">%s</button>' % (i, kk, e(lab_)) for kk, lab_ in enumerate(p['rl']))
            o.append('<div class="z-i" id="%s-r%d"><b%s>%s</b><span>%s</span><div class="ok2"%s>%s</div>'
                     '<p class="lect" id="%s-fb%d"></p></div>'
                     % (pre, i, (' class="sent"' if (it[0][0] in '«' or len(it[0]) > 34) else ''), e(it[0]), e(it[1]),
                        (' style="grid-template-columns:repeat(%d,minmax(0,1fr))"' % nl) if nl != 2 else '', btns, pre, i))
          o.append('</div>')
          if p.get('extra'):
              o.append('<p class="nota" style="margin-top:12px;color:var(--ink)">%s</p>' % e(p['extra']))
          if p.get('error'):
              o.append('<div class="decir cso" style="margin-top:12px"><small>Error típico</small><p>%s</p></div>' % e(p['error']))
          if p.get('enlace'):
              o.append('<p style="margin-top:12px"><a class="btn" href="%s" target="_top">%s</a></p>' % (e(p['enlace'][1]), e(p['enlace'][0])))
          o.append('</section>')
        if p.get('html_post'): o.append(p['html_post'])
        o.append('<section><h2 class="lab">Mini-práctica · 2 minutos</h2><p class="lead">%s</p><div class="qs">' % e(p['plead']))
        for j, (lab, hint, ej) in enumerate(p['q']):
            o.append('<div class="q"><label for="%s-a%d"><span class="n">%d</span>%s</label><p class="h">%s</p><p class="eg">Ejemplo: «%s»</p>'
                     '<textarea id="%s-a%d" rows="3" placeholder="Escribe aquí tu respuesta"></textarea></div>'
                     % (pre, j, j + 1, e(lab), e(hint), e(ej), pre, j))
        o.append('</div><p class="save" id="%s-save"></p></section>' % pre)
        o.append('</div><div class="col-b">')
        o.append('<div class="accion"><h2>%sEsta semana</h2><p>%s</p><label class="chk" for="%s-hecho"><input type="checkbox" id="%s-hecho">%s</label></div>'
                 % (IC['acc'], e(p['acc']), pre, pre, e(p['chk'])))
        o.append('<div class="rev"><b>Dentro de una semana</b>%s</div><div class="frase">%s</div>' % (e(p['rev']), e(p['frase'])))
        o.append('</div></div>')
        prev = ('<a class="btn" href="#pildora-%d">%sPíldora %s</a>' % (n - 1, IC['back'], pad(n - 1))) if n > 1 else \
               ('<a class="btn" href="#inicio">%sInicio</a>' % IC['back'])
        nxt = ('<a class="btn next" href="#pildora-%d">Píldora %s%s</a>' % (n + 1, pad(n + 1), IC['next'])) if n < N else \
              ('<a class="btn next" href="#mi-kit">%s%s</a>' % (e(S['plan_nombre']), IC['next']))
        o.append('<nav class="navp" aria-label="Navegación entre píldoras">%s%s</nav>' % (prev, nxt))
        o.append('<footer class="pie">%s<div class="reset" id="%s-reset"></div></footer></main>' % (e(pie), pre) + VALORES + '</div>')

    # ---------- hoja final
    o.append('<div id="view-mi-kit" class="view" hidden><main class="wrap"><a class="back" href="#inicio">%sTodas las píldoras</a>' % IC['back'])
    o.append('<h1 tabindex="-1" style="font-size:clamp(32px,9.6vw,54px)">%s<em>%s</em></h1><p class="sub">%s</p><div class="gancho">%s</div>'
             % (e(S['plan1']), e(S['plan2']), e(S['plan_sub']), e(S['plan_gancho'])))
    o.append('<div class="prog" style="position:static;margin:18px 0 0;padding:0;border:0"><div class="prog-in"><div class="prog-row"><span>Apartados completados</span><output id="plan-prog-txt">0 de %d</output></div>'
             '<div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="%d" aria-valuenow="0" id="plan-pbar"><i id="plan-pbar-i"></i></div></div></div>' % (plan_total, plan_total))
    o.append('<div id="plan-body"></div><div class="copia"><div class="acts">'
             '<button class="btn" type="button" id="plan-pdf">%sGenerar PDF de mi plan</button>'
             '<a class="btn" id="plan-wa" href="https://wa.me/" target="_blank" rel="noopener">%sCompartir por WhatsApp</a></div>'
             '<p class="save" id="plan-msg" role="status"></p></div>' % (IC['pdf'], IC['wa']))
    o.append('<div class="rev"><b>La próxima vez</b>%s</div><div class="frase">%s</div>' % (e(S['plan_rev']), e(S['plan_frase'])))
    o.append('<nav class="navp" aria-label="Navegación"><a class="btn" href="#pildora-%d">%sPíldora %s</a><a class="btn" href="#inicio">Todas%s</a></nav>'
             % (N, IC['back'], pad(N), IC['next']))
    o.append('<footer class="pie">%s</footer></main>' % e(pie) + VALORES + '</div>')

    if S.get('sos_groups'):
        pn = ['<div id="sos" class="sos" hidden role="dialog" aria-modal="true" aria-labelledby="sos-t"><div class="sos-in"><div class="sos-h"><h2 id="sos-t">%s</h2><button type="button" class="btn" data-sos-close>Cerrar</button></div><p class="lead">%s</p>' % (e(S.get('sos_titulo','En plena racha')), e(S.get('sos_lead','30 segundos. No hace falta cambiar nada más.')))]
        for gi in S['sos_groups']:
            gt, rows = S['chuleta'][gi]
            pn.append('<section><h3>%s</h3>' % e(gt))
            for lab, tx in rows:
                pn.append('<div class="sos-r"><b>%s</b><p>%s</p></div>' % (e(lab), e(tx)))
            pn.append('</section>')
        pn.append('<p style="margin-top:22px"><a class="btn next" href="#mi-kit" data-sos-close>%s</a>' % e(S.get('sos_kit','Ver mi kit completo')) + '</p></div></div>')
        o.append(''.join(pn))
        o.append("<script>(function(){var P=document.getElementById('sos'),last=null;"
                 "function open(b){last=b||null;P.hidden=false;document.body.style.overflow='hidden';var c=P.querySelector('[data-sos-close]');if(c)c.focus();}"
                 "function close(){P.hidden=true;document.body.style.overflow='';}"
                 "document.addEventListener('click',function(ev){var t=ev.target.closest&&ev.target.closest('[data-sos]');if(t){ev.preventDefault();open(t);return;}"
                 "var c=ev.target.closest&&ev.target.closest('[data-sos-close]');if(c){close();if(last&&c.tagName==='BUTTON'){try{last.focus();}catch(e){}}}});"
                 "document.addEventListener('keydown',function(ev){if(ev.key==='Escape'&&!P.hidden)close();});"
                 "window.addEventListener('hashchange',function(){if(!P.hidden)close();});})();</script>")

    js = JSTPL.replace('__KEY__', json.dumps(S['key'])).replace('__GEN__', json.dumps(gen, ensure_ascii=False)) \
        .replace('__MISLAB__', json.dumps(S.get('plan_mis', 'Mis frases'), ensure_ascii=False)).replace('__CHULETA__', json.dumps(S.get('chuleta', []), ensure_ascii=False)).replace('__PLAN__', json.dumps(plan, ensure_ascii=False)).replace('__PLAN_TOTAL__', str(plan_total)) \
        .replace('__VIEWS__', json.dumps(views, ensure_ascii=False)).replace('__PLAN_TITLE__', json.dumps(S['plan_titulo_texto'], ensure_ascii=False)) \
        .replace('__SERIE_NOMBRE__', json.dumps(nombre, ensure_ascii=False))
    o.append('<script>%s</script>' % js)
    if S.get('script_extra'): o.append('<script>%s</script>' % S['script_extra'])
    o.append('</body></html>')
    out = '\n'.join(o)
    open(out_path, 'w', encoding='utf8').write(out)
    print('OK', out_path, len(out), 'bytes', N, 'píldoras')

if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
