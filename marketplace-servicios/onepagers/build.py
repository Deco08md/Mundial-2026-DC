"""Genera los 3 one-pagers de Cuadra (HTML tamaño carta). Uso: python3 build.py <carpeta_salida>"""
import sys, os
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
CONTACTO = "[WhatsApp e Instagram de Cuadra · por definir]"   # <- reemplazar cuando exista

MARK = '<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M10 36V10h26" fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><path d="M54 28v26H28" fill="none" stroke="#F5B728" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><circle cx="32" cy="32" r="5" fill="#F5B728"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12 4.5 4.5L19 7" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

CSS = """
@page{size:Letter;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
:root{--c:#1F3FBF;--cd:#162E8F;--y:#F5B728;--ink:#131833;--ink2:#535B78;--line:#DCE0EC;--soft:#F3F5FB;--ysoft:#FDF1D3}
html,body{width:8.5in;height:11in;background:#fff;color:var(--ink);font-family:"Figtree","Segoe UI",Arial,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:8.5in;height:11in;overflow:hidden;display:flex;flex-direction:column;position:relative}
.top{flex:none;background:var(--c);color:#fff;padding:.4in .55in .34in;position:relative;overflow:hidden}
.top::after{content:"";position:absolute;right:-.55in;top:-.55in;width:1.9in;height:1.9in;border:.2in solid rgba(255,255,255,.1);border-radius:.08in}
.brand{display:flex;align-items:center;gap:.1in;font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:800;font-size:22pt;letter-spacing:-.02em}
.brand svg{width:.36in;height:.36in}
.aud{display:inline-block;margin-left:auto;background:var(--y);color:#1B1406;font-weight:800;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;padding:.05in .12in;border-radius:99px}
.toprow{display:flex;align-items:center}
h1.s{font-size:25pt}
h1{font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:800;font-size:30pt;line-height:1.04;letter-spacing:-.025em;margin-top:.22in;max-width:6.6in}
h1 em{font-style:normal;color:var(--y)}
.sub{margin-top:.12in;font-size:12pt;line-height:1.4;opacity:.92;max-width:6.4in}
.body{flex:1 1 auto;min-height:0;overflow:hidden;padding:.26in .55in .06in;display:flex;flex-direction:column;gap:.15in}
h2{font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:800;font-size:15pt;letter-spacing:-.01em;margin-bottom:.09in}
h2 small{font-family:"Figtree",Arial,sans-serif;font-weight:600;font-size:9.5pt;color:var(--ink2);margin-left:.06in;letter-spacing:0}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:.14in}
.step{background:var(--soft);border-radius:.12in;padding:.13in .14in;display:flex;gap:.1in;align-items:flex-start}
.step i{flex:none;width:.3in;height:.3in;border-radius:.07in;background:var(--y);color:#1B1406;font-style:normal;font-weight:800;font-size:12pt;display:grid;place-items:center;font-family:"Bricolage Grotesque",Arial,sans-serif}
.step b{display:block;font-size:10.5pt;margin-bottom:.02in}
.step span{font-size:9pt;color:var(--ink2);line-height:1.35}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:.1in .22in}
.ben{display:flex;gap:.09in;align-items:flex-start}
.ben .ck{flex:none;width:.22in;height:.22in;border-radius:50%;background:var(--c);color:#fff;display:grid;place-items:center;margin-top:.01in}
.ben .ck svg{width:.13in;height:.13in}
.ben b{display:block;font-size:10.5pt}
.ben span{font-size:9pt;color:var(--ink2);line-height:1.35}
.cta{flex:none;background:var(--ink);color:#fff;padding:.2in .55in;display:flex;align-items:center;gap:.25in}
.cta b{font-family:"Bricolage Grotesque",Arial,sans-serif;font-size:15pt;font-weight:800;letter-spacing:-.01em;display:block}
.cta span{font-size:9.5pt;opacity:.8}
.cta .ct{margin-left:auto;border:1.5px dashed var(--y);color:var(--y);border-radius:.08in;padding:.08in .14in;font-weight:700;font-size:9.5pt;max-width:2.8in;text-align:center}
.cats{display:flex;flex-wrap:wrap;gap:.07in}
.cat{background:var(--soft);border:1px solid var(--line);border-radius:99px;padding:.04in .13in;font-size:9.5pt;font-weight:700}
.cat.soon{color:var(--ink2);font-weight:600;border-style:dashed;background:#fff}
.ladder{display:grid;grid-template-columns:repeat(3,1fr);gap:.12in;align-items:end}
.lv{border-radius:.12in;padding:.13in .14in;display:flex;flex-direction:column;gap:.04in;border:1px solid var(--line)}
.lv .nm{font-size:9pt;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
.lv .pc{font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:800;font-size:26pt;line-height:1}
.lv .pc small{font-size:9pt;font-family:"Figtree",Arial,sans-serif;font-weight:600;color:var(--ink2)}
.lv .rq{font-size:9pt;font-weight:700}
.lv ul{list-style:none;font-size:8.6pt;color:var(--ink2);display:flex;flex-direction:column;gap:.02in;margin-top:.02in}
.lv.b{background:#F6E6DA;border-color:#E7CDB8;min-height:1.3in}.lv.b .nm{color:#7A4520}
.lv.p{background:#E8EBF3;border-color:#CED4E4;min-height:1.45in}.lv.p .nm{color:#46506E}
.lv.o{background:var(--ysoft);border-color:#F0D9A0;min-height:1.6in}.lv.o .nm{color:#7A5300}
.arrow{font-size:9pt;color:var(--ink2);margin-top:.06in}
.rep{display:flex;gap:.16in;align-items:center;background:var(--c);color:#fff;border-radius:.12in;padding:.12in .18in;margin-top:.1in}
.rep .pc{font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:800;font-size:28pt;color:var(--y);line-height:1}
.rep b{font-size:11pt;display:block}
.rep span{font-size:9pt;opacity:.9;line-height:1.35}
.math{display:grid;grid-template-columns:1.15fr 1fr;gap:.18in}
table{border-collapse:collapse;width:100%;font-size:9.5pt}
td,th{padding:.045in .08in;border-bottom:1px solid var(--line);text-align:left}
th{font-size:8.5pt;text-transform:uppercase;letter-spacing:.06em;color:var(--ink2)}
td.n,th.n{text-align:right;font-variant-numeric:tabular-nums}
tr.hl td{font-weight:800;background:var(--ysoft)}
.vs{background:var(--soft);border-radius:.12in;padding:.12in .15in;font-size:9pt;line-height:1.4;display:flex;flex-direction:column;gap:.05in}
.vs b{font-size:10.5pt}
.vs .x{color:#B0302A;font-weight:700}
.req{display:flex;flex-wrap:wrap;gap:.06in .16in;font-size:9pt;color:var(--ink2)}
.req span::before{content:"■ ";color:var(--y)}
.twocol{display:grid;grid-template-columns:1fr 1fr;gap:.2in}
.col{border:1px solid var(--line);border-radius:.14in;padding:.16in .18in;display:flex;flex-direction:column;gap:.09in}
.col .tag{align-self:flex-start;font-size:8.5pt;font-weight:800;letter-spacing:.08em;text-transform:uppercase;padding:.03in .1in;border-radius:99px;background:var(--c);color:#fff}
.col .tag.y{background:var(--y);color:#1B1406}
.col h3{font-family:"Bricolage Grotesque",Arial,sans-serif;font-size:14pt;font-weight:800;line-height:1.1}
.pillars{display:grid;grid-template-columns:repeat(5,1fr);gap:.1in}
.pil{background:var(--soft);border-radius:.1in;padding:.1in;text-align:center;font-size:8.6pt;color:var(--ink2);line-height:1.3}
.pil b{display:block;color:var(--ink);font-size:9.6pt;margin-bottom:.02in}
.note{font-size:8pt;color:var(--ink2)}
"""

def page(title, aud, h1, sub, body, cta_title, cta_sub, h1cls=''):
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;600;700;800&display=swap">
<style>{CSS}</style></head><body><div class="page">
<header class="top"><div class="toprow"><div class="brand">{MARK}cuadra</div><span class="aud">{aud}</span></div><h1 class="{h1cls}">{h1}</h1><p class="sub">{sub}</p></header>
<main class="body">{body}</main>
<footer class="cta"><div><b>{cta_title}</b><span>{cta_sub}</span></div><div class="ct">{CONTACTO}</div></footer>
</div></body></html>"""

def bens(items):
    return '<div class="grid">' + ''.join(f'<div class="ben"><span class="ck">{CHECK}</span><div><b>{a}</b><span>{b}</span></div></div>' for a, b in items) + '</div>'
def bens4(items):
    return '<div class="grid" style="grid-template-columns:repeat(4,1fr);gap:.1in .14in">' + ''.join(f'<div class="ben"><span class="ck">{CHECK}</span><div><b>{a}</b><span>{b}</span></div></div>' for a, b in items) + '</div>'
def steps(items):
    return '<div class="steps">' + ''.join(f'<div class="step"><i>{i+1}</i><div><b>{a}</b><span>{b}</span></div></div>' for i, (a, b) in enumerate(items)) + '</div>'
CATS = '<div class="cats">' + ''.join(f'<span class="cat">{c}</span>' for c in ['Plomería','Electricidad','Limpieza','Aires acondicionados','Pintura']) + ''.join(f'<span class="cat soon">{c} · pronto</span>' for c in ['Belleza','Mascotas','Tutorías']) + '</div>'

# ---------------- CLIENTES ----------------
clientes = page("Cuadra para clientes", "Para clientes",
 "¿A quién le abres la puerta de tu casa? <em>Lo cuadras con gente de confianza.</em>",
 "Plomeros, electricistas, técnicos de aires, pintores y personal de limpieza verificados en Ciudad de Panamá. Eliges tú, ves el precio antes y pagas solo cuando el trabajo quedó bien.",
 f"""<section><h2>Así de fácil</h2>{steps([
   ("Busca por el problema","Escribe \"fuga en el baño\" o \"el aire no enfría\" y ves quién puede resolverlo."),
   ("Elige con información","Reseñas con fotos de clientes reales, referencias verificadas y precio antes de reservar."),
   ("Paga protegido","Yappy o tarjeta. El dinero se libera al profesional solo cuando confirmas.")])}</section>
 <section><h2>Lo que no tienes en un grupo de WhatsApp</h2>{bens([
   ("Profesionales verificados","Revisamos cédula, récord policivo e idoneidad antes de darles el sello."),
   ("Reseñas solo de clientes reales","Solo califica quien contrató y pagó por Cuadra, con fotos del trabajo."),
   ("Referencias que llamamos","Cada referencia de un profesional se confirma por teléfono antes de publicarse."),
   ("Precio claro antes de reservar","Sin cotizaciones eternas. Y si no sabes qué tiene, reservas una visita de diagnóstico de $20 que se descuenta del trabajo."),
   ("Garantía de 30 días","Si algo falla, lo rehacemos sin costo. Tu pago queda retenido si reportas un problema."),
   ("Urgencias en 2 horas","Para una fuga o un apagón: profesionales que llegan hoy, con recargo de $15 visible antes de pagar."),
   ("Código de llegada","El profesional solo empieza cuando le das tu código de 4 dígitos en la puerta."),
   ("Chat protegido","Coordinas por la app sin compartir tu número. Todo queda registrado por si hace falta.")])}</section>
 <section><h2>Categorías</h2>{CATS}</section>""",
 "Lanzamiento en Ciudad de Panamá", "Únete a la lista y sé de los primeros en usarla.")

# ---------------- PROFESIONALES ----------------
profes = page("Cuadra para profesionales", "Para profesionales",
 "Más clientes, cobro seguro y <em>cada trabajo bien hecho baja tu comisión.</em>",
 "Clientes en tu zona sin pagar publicidad. Inscribirte es gratis y solo pagas comisión cuando cobras.",
 f"""<section><h2>Tu comisión baja mientras más trabajas bien</h2>
  <div class="ladder">
   <div class="lv b"><span class="nm">Bronce</span><span class="pc">18%<small> primer trabajo</small></span><span class="rq">Al inscribirte</span><ul><li>Pago en 3 días hábiles</li><li>Impulso de visibilidad mientras llegan tus primeras reseñas</li></ul></div>
   <div class="lv p"><span class="nm">Plata</span><span class="pc">15%<small> primer trabajo</small></span><span class="rq">10 trabajos validados · 4.5★ o más</span><ul><li>Pago en 48 horas</li><li>Más arriba en las búsquedas</li></ul></div>
   <div class="lv o"><span class="nm">Oro</span><span class="pc">12%<small> primer trabajo</small></span><span class="rq">50 trabajos validados · 4.7★ o más · verificado</span><ul><li>Pago el mismo día</li><li>Primero en las búsquedas</li><li>Sello Oro en tu perfil</li></ul></div>
  </div>
  <p class="arrow">Trabajo validado = cobrado por la app y confirmado por el cliente.</p>
  <div class="rep"><span class="pc">8%</span><div><b>Cuando un cliente te vuelve a contratar por Cuadra, pagas solo 8%. En cualquier nivel, siempre.</b><span>Tus clientes de siempre te salen más baratos dentro de la app que el costo de perder el cobro asegurado, la garantía y las reseñas que te suben de nivel.</span></div></div>
 </section>
 <section><h2>Haz la cuenta <small>Ejemplo: un trabajo de $60</small></h2>
  <div class="math"><table><thead><tr><th>Tu situación</th><th class="n">Comisión</th><th class="n">Recibes</th></tr></thead><tbody>
   <tr><td>Bronce, cliente nuevo</td><td class="n">$10.80</td><td class="n">$49.20</td></tr>
   <tr><td>Plata, cliente nuevo</td><td class="n">$9.00</td><td class="n">$51.00</td></tr>
   <tr><td>Oro, cliente nuevo</td><td class="n">$7.20</td><td class="n">$52.80</td></tr>
   <tr class="hl"><td>Cliente que te repite</td><td class="n">$4.80</td><td class="n">$55.20</td></tr></tbody></table>
  <div class="vs"><b>¿Y si cobras por fuera?</b><span>Te ahorras $4.80 una vez, pero ese trabajo:</span>
   <span class="x">✕ no tiene cobro asegurado</span><span class="x">✕ no tiene garantía si el cliente reclama</span><span class="x">✕ no te da reseña ni cuenta para subir de nivel</span>
   <span>Llegar a Oro te ahorra $3.60 en cada cliente nuevo, para siempre.</span></div></div>
 </section>
 <section><h2>Lo que te da Cuadra</h2>{bens4([
   ("Ves el neto antes de aceptar","Tú decides qué trabajos tomas."),
   ("Cobro asegurado","El cliente paga al reservar."),
   ("Tú pones tus precios","Por cada servicio que ofreces."),
   ("Urgencias con recargo","$15 extra por llegar en 2 horas.")])}</section>
""",
 "Inscríbete gratis en 10 minutos", "Ten a mano: cédula, récord policivo de menos de 90 días, idoneidad (electricidad y aires), 2 referencias y fotos de tus trabajos.", "s")

# ---------------- GENERAL ----------------
general = page("Cuadra", "Panamá",
 "Donde se encuentran <em>la necesidad y la persona correcta.</em>",
 "Cuadra conecta a quien necesita resolver algo en casa con profesionales verificados y recomendados.",
 f"""<section><div class="twocol">
   <div class="col"><span class="tag">Para clientes</span><h3>Lo que no te atreverías a contratar con un desconocido.</h3>{bens([
     ("Eliges con información","Reseñas con fotos, referencias verificadas y precio antes de reservar."),
     ("Pagas protegido","Yappy o tarjeta; se libera solo cuando confirmas."),
     ("Garantía de 30 días","Si algo falla, lo rehacemos sin costo."),
     ("Urgencias en 2 horas","Para lo que no puede esperar.")]).replace('class="grid"','class="grid" style="grid-template-columns:1fr"')}</div>
   <div class="col"><span class="tag y">Para profesionales</span><h3>Más clientes, cobro seguro y una reputación que trabaja por ti.</h3>{bens([
     ("Clientes en tu zona","Sin pagar publicidad. Inscribirte es gratis."),
     ("Cobro asegurado","El cliente paga al reservar."),
     ("Tu comisión baja","18% al empezar, 15% en Plata y 12% en Oro, según trabajos validados y calificaciones."),
     ("8% con clientes que repiten","Tus clientes de siempre, más baratos dentro de la app.")]).replace('class="grid"','class="grid" style="grid-template-columns:1fr"')}</div>
 </div></section>
 <section><h2>Cómo se gana la confianza</h2><div class="pillars">
   <div class="pil"><b>Verificación</b>Cédula, récord policivo e idoneidad</div>
   <div class="pil"><b>Reseñas reales</b>Solo de quien contrató, con fotos</div>
   <div class="pil"><b>Referencias</b>Confirmadas por llamada</div>
   <div class="pil"><b>Pago protegido</b>Se libera al confirmar</div>
   <div class="pil"><b>Código de llegada</b>Sin código no empieza el trabajo</div></div></section>
 <section><h2>Cómo funciona</h2>{steps([
   ("El cliente busca y elige","Por el problema, viendo reseñas, referencias y precio."),
   ("El profesional acepta y llega","Con código de llegada y chat protegido."),
   ("Se confirma y se cobra","El cliente confirma, el profesional cobra y ambos se califican.")])}</section>
 <section><h2>Lanzamiento en Ciudad de Panamá</h2>{CATS}</section>""",
 "Lo cuadras con gente de confianza.", "Clientes: únete a la lista. Profesionales: inscríbete gratis.", "s")

for name, html in [("cuadra-onepager-clientes", clientes), ("cuadra-onepager-profesionales", profes), ("cuadra-onepager-general", general)]:
    with open(os.path.join(OUT, name + ".html"), "w") as f:
        f.write(html)
print("ok")
