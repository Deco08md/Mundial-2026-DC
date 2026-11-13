import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.chart import LineChart, Reference
from openpyxl.comments import Comment

OUT=sys.argv[1]
wb=Workbook()
F='Arial'
f_title=Font(name=F,size=14,bold=True)
f_h=Font(name=F,size=10,bold=True,color='FFFFFF')
f_sec=Font(name=F,size=10,bold=True)
f_in=Font(name=F,size=10,color='0000FF')
f_link=Font(name=F,size=10,color='008000')
f_calc=Font(name=F,size=10,color='000000')
f_calcb=Font(name=F,size=10,bold=True)
f_note=Font(name=F,size=9,italic=True,color='555555')
fill_h=PatternFill('solid',fgColor='1F3FBF')
fill_sec=PatternFill('solid',fgColor='E4E9FB')
fill_key=PatternFill('solid',fgColor='FFFF00')
fill_tot=PatternFill('solid',fgColor='F2F2F2')
thin=Side(style='thin',color='BBBBBB')
USD='$#,##0;($#,##0);-'
USD2='$#,##0.00;($#,##0.00);-'
PCT='0.0%;(0.0%);-'
NUM='#,##0;(#,##0);-'

# ------------------------------------------------------------------ Supuestos
S=wb.active; S.title='Supuestos'
S['A1']='Cuadra · Modelo financiero 36 meses · Supuestos'; S['A1'].font=f_title
S['A2']='Cifras en USD, sin ITBMS. Texto azul = supuesto editable; fondo amarillo = supuesto clave. Cambia cualquier valor azul y todo el modelo se recalcula.'; S['A2'].font=f_note
S['A3']='Fuente: todos los valores son supuestos de trabajo acordados con David (sesión de diseño de Cuadra) o estimaciones propias marcadas en la columna Nota. Ninguno está validado con datos de mercado.'; S['A3'].font=f_note
hdr=['Supuesto','Unidad','Conservador','Medio','Agresivo','Nota']
for i,h in enumerate(hdr,1):
    c=S.cell(row=5,column=i,value=h); c.font=f_h; c.fill=fill_h; c.alignment=Alignment(horizontal='center' if i>2 else 'left')
A={}  # key -> row
r=6
def sec(t):
    global r
    for col in range(1,7): S.cell(row=r,column=col).fill=fill_sec
    S.cell(row=r,column=1,value=t).font=f_sec; r+=1
def inp(key,label,unit,vals,fmt,note='',key_fill=False):
    global r
    S.cell(row=r,column=1,value=label).font=f_calc
    S.cell(row=r,column=2,value=unit).font=f_note
    for j,v in enumerate(vals):
        c=S.cell(row=r,column=3+j,value=v); c.font=f_in; c.number_format=fmt
        if key_fill: c.fill=fill_key
    S.cell(row=r,column=6,value=note).font=f_note
    A[key]=r; r+=1

sec('Demanda')
inp('s0','Servicios completados en el mes 1','servicios/mes',[40,60,100],NUM,'Arranque tras el piloto de 90 días del brief (100-200 servicios acumulados).',True)
inp('g1','Crecimiento mensual de servicios · año 1','% mensual',[0.15,0.20,0.22],PCT,'Suposición. Año de tracción.',True)
inp('g2','Crecimiento mensual de servicios · año 2','% mensual',[0.06,0.08,0.10],PCT,'Suposición.')
inp('g3','Crecimiento mensual de servicios · año 3','% mensual',[0.03,0.04,0.05],PCT,'Suposición.')
inp('t0','Ticket promedio (año 1)','USD/servicio',[55,60,65],USD,'Brief: ticket de referencia $60.',True)
inp('tinf','Aumento anual del ticket','% anual',[0.03,0.03,0.03],PCT,'Suposición: inflación de precios de servicios.')
sec('Mezcla de trabajos y niveles')
inp('rep1','% de trabajos de clientes que repiten con el mismo profesional · año 1','% del total',[0.15,0.20,0.25],PCT,'Pagan 8%. Más repetición = más retención, menos comisión.',True)
inp('rep2','% de trabajos de clientes que repiten · año 2','% del total',[0.25,0.35,0.40],PCT,'')
inp('rep3','% de trabajos de clientes que repiten · año 3','% del total',[0.35,0.40,0.45],PCT,'')
inp('pl1','% de primeros trabajos hechos por profesionales Plata · año 1','% primeros trabajos',[0.0,0.05,0.10],PCT,'Plata: 10+ trabajos y 4.5+.')
inp('pl2','% primeros trabajos Plata · año 2','% primeros trabajos',[0.20,0.25,0.30],PCT,'')
inp('pl3','% primeros trabajos Plata · año 3','% primeros trabajos',[0.35,0.40,0.40],PCT,'')
inp('or1','% de primeros trabajos hechos por profesionales Oro · año 1','% primeros trabajos',[0.0,0.0,0.0],PCT,'Oro: 50+ trabajos, 4.7+ y verificado. Nadie llega en el año 1.')
inp('or2','% primeros trabajos Oro · año 2','% primeros trabajos',[0.05,0.10,0.15],PCT,'')
inp('or3','% primeros trabajos Oro · año 3','% primeros trabajos',[0.15,0.20,0.25],PCT,'')
sec('Comisiones e ingresos')
inp('cb','Comisión Bronce (primer trabajo con un cliente)','% del ticket',[0.18,0.18,0.18],PCT,'Acordado en el prototipo.',True)
inp('cp','Comisión Plata','% del ticket',[0.15,0.15,0.15],PCT,'Acordado en el prototipo.',True)
inp('co','Comisión Oro','% del ticket',[0.12,0.12,0.12],PCT,'Acordado en el prototipo.',True)
inp('cr','Comisión cliente que repite (cualquier nivel)','% del ticket',[0.08,0.08,0.08],PCT,'Acordado en el prototipo.',True)
inp('fee','Cargo por servicio cobrado al cliente','% del ticket',[0.0,0.0,0.0],PCT,'Hoy en 0% como en el prototipo. Palanca disponible: ver hoja Resumen.')
inp('mat','Ingreso por alianza de materiales (Cochez/Novey)','% del GMV',[0.0,0.005,0.01],PCT,'Suposición: comisión por referido sobre compras de materiales de los profesionales.')
inp('matm','Mes en que arranca la alianza de materiales','mes',[13,7,7],'0','')
sec('Costos variables')
inp('proc','Procesamiento de pagos (Yappy + tarjetas, mezcla)','% del GMV',[0.025,0.025,0.025],PCT,'Suposición: confirmar tarifas con el adquirente y con Yappy. Se cobra sobre todo el ticket, no solo la comisión.',True)
inp('gar','Fondo de garantía de 30 días','% del GMV',[0.015,0.01,0.008],PCT,'Suposición: reserva para rehacer trabajos fallidos.',True)
inp('sup','Soporte y verificación por servicio','USD/servicio',[1.5,1.0,0.8],USD2,'Suposición: llamadas, seguimiento, reclamos.')
sec('Adquisición')
inp('nw1','% de primeros trabajos que vienen de clientes nuevos a la plataforma · año 1','%',[0.70,0.70,0.65],PCT,'El resto son clientes existentes que prueban otro profesional.')
inp('nw2','% clientes nuevos · año 2','%',[0.55,0.50,0.45],PCT,'')
inp('nw3','% clientes nuevos · año 3','%',[0.45,0.35,0.30],PCT,'')
inp('cac','Costo de adquirir un cliente nuevo (CAC)','USD/cliente',[15,12,10],USD,'Suposición: pauta digital + referidos. Validar en el piloto.',True)
inp('cap','Servicios por profesional activo al mes','servicios',[6,8,10],NUM,'Suposición.')
inp('churn','Profesionales que se van cada mes','% mensual',[0.05,0.04,0.03],PCT,'Suposición.')
inp('onb','Costo de verificar y activar un profesional','USD/profesional',[25,25,25],USD,'Suposición: récord policivo + llamadas a referencias + sesión de activación.')
sec('Costos fijos mensuales')
inp('pay1','Nómina · año 1','USD/mes',[1500,2500,3500],USD,'Sin salario de fundadores. Año 1: operaciones y soporte.',True)
inp('pay2','Nómina · año 2','USD/mes',[3000,5000,8000],USD,'',True)
inp('pay3','Nómina · año 3','USD/mes',[4500,8000,14000],USD,'',True)
inp('cs','Cargas sociales y prestaciones sobre nómina','%',[0.25,0.25,0.25],PCT,'Suposición: CSS, seguro educativo, riesgos profesionales, décimo tercer mes y vacaciones. Validar con contador.')
inp('tec1','Tecnología y herramientas · año 1','USD/mes',[300,400,500],USD,'No-code, hosting, WhatsApp Business API.')
inp('tec2','Tecnología · año 2','USD/mes',[800,1500,2500],USD,'')
inp('tec3','Tecnología · año 3','USD/mes',[1500,2500,4000],USD,'')
inp('mkt','Marketing de marca (contenido, redes, activaciones)','USD/mes',[800,1500,3000],USD,'Adicional al CAC.')
inp('adm','Legal, contabilidad y administración','USD/mes',[500,600,800],USD,'')
sec('Inversión y caja')
inp('app','Desarrollo de app nativa (pago único)','USD',[15000,25000,40000],USD,'Suposición: cotizar. El MVP del brief es web/no-code.',True)
inp('appm','Mes de la inversión en app','mes',[13,10,7],'0','')
inp('cash0','Capital inicial','USD',[15000,15000,15000],USD,'Brief: $8,000-$15,000 para validar.',True)
S.column_dimensions['A'].width=66; S.column_dimensions['B'].width=18
for c in 'CDE': S.column_dimensions[c].width=14
S.column_dimensions['F'].width=80
S.freeze_panes='C6'

# ------------------------------------------------------------------ Model sheets
NM=36; C0=3  # first month column = C
months=[L(C0+i) for i in range(NM)]
first,last=months[0],months[-1]
SCEN=[('Conservador','C'),('Medio','D'),('Agresivo','E')]
ROWS={}
def build(name,col):
    ws=wb.create_sheet('Modelo '+name)
    a=lambda k:f"Supuestos!${col}${A[k]}"
    ws['A1']=f'Cuadra · Escenario {name} · 36 meses (USD)'; ws['A1'].font=f_title
    ws['A2']='Todas las celdas son fórmulas. Los supuestos (verde) vienen de la hoja Supuestos, columna '+name+'.'; ws['A2'].font=f_note
    rows=[]  # (key,label,unit,formula_fn(month_index, colletter, prevletter) or None for section, fmt, bold)
    def R(key,label,unit,fn,fmt=USD,bold=False): rows.append((key,label,unit,fn,fmt,bold))
    def SEC(t): rows.append((None,t,None,None,None,None))
    yr=lambda c:f"{c}$4"
    ch=lambda c,k1,k2,k3:f"CHOOSE({yr(c)},{a(k1)},{a(k2)},{a(k3)})"
    SEC('Demanda')
    R('g','Crecimiento mensual de servicios','%',lambda i,c,p: '=0' if i==0 else f"={ch(c,'g1','g2','g3')}",PCT)
    R('srv','Servicios completados','servicios',lambda i,c,p: f"={a('s0')}" if i==0 else f"={p}{{srv}}*(1+{c}{{g}})",NUM,True)
    R('tk','Ticket promedio','USD',lambda i,c,p: f"={a('t0')}*(1+{a('tinf')})^({yr(c)}-1)",USD2)
    R('gmv','GMV (valor transaccionado)','USD',lambda i,c,p: f"={c}{{srv}}*{c}{{tk}}",USD,True)
    SEC('Comisión efectiva')
    R('rep','% trabajos de clientes que repiten','%',lambda i,c,p: f"={ch(c,'rep1','rep2','rep3')}",PCT)
    R('pl','% primeros trabajos Plata','%',lambda i,c,p: f"={ch(c,'pl1','pl2','pl3')}",PCT)
    R('oro','% primeros trabajos Oro','%',lambda i,c,p: f"={ch(c,'or1','or2','or3')}",PCT)
    R('br','% primeros trabajos Bronce','%',lambda i,c,p: f"=1-{c}{{pl}}-{c}{{oro}}",PCT)
    R('take','Comisión efectiva sobre GMV','%',lambda i,c,p: f"={c}{{rep}}*{a('cr')}+(1-{c}{{rep}})*({c}{{br}}*{a('cb')}+{c}{{pl}}*{a('cp')}+{c}{{oro}}*{a('co')})",PCT,True)
    SEC('Ingresos')
    R('rcom','Ingresos por comisiones','USD',lambda i,c,p: f"={c}{{gmv}}*{c}{{take}}")
    R('rfee','Cargo por servicio al cliente','USD',lambda i,c,p: f"={c}{{gmv}}*{a('fee')}")
    R('rmat','Alianza de materiales','USD',lambda i,c,p: f"=IF({c}$3>={a('matm')},{c}{{gmv}}*{a('mat')},0)")
    R('rev','Ingresos totales','USD',lambda i,c,p: f"={c}{{rcom}}+{c}{{rfee}}+{c}{{rmat}}",USD,True)
    SEC('Costos variables')
    R('cproc','Procesamiento de pagos','USD',lambda i,c,p: f"=({c}{{gmv}}+{c}{{rfee}})*{a('proc')}")
    R('cgar','Fondo de garantía','USD',lambda i,c,p: f"={c}{{gmv}}*{a('gar')}")
    R('csup','Soporte y verificación','USD',lambda i,c,p: f"={c}{{srv}}*{a('sup')}")
    R('contrib','Margen de contribución','USD',lambda i,c,p: f"={c}{{rev}}-{c}{{cproc}}-{c}{{cgar}}-{c}{{csup}}",USD,True)
    R('cps','Margen de contribución por servicio','USD',lambda i,c,p: f"=IF({c}{{srv}}>0,{c}{{contrib}}/{c}{{srv}},0)",USD2)
    SEC('Adquisición')
    R('nw','Clientes nuevos','clientes',lambda i,c,p: f"={c}{{srv}}*(1-{c}{{rep}})*{ch(c,'nw1','nw2','nw3')}",NUM)
    R('cmk','Marketing de adquisición (CAC)','USD',lambda i,c,p: f"={c}{{nw}}*{a('cac')}")
    R('pros','Profesionales activos','profesionales',lambda i,c,p: f"={c}{{srv}}/{a('cap')}",NUM)
    R('newp','Profesionales nuevos a verificar','profesionales',lambda i,c,p: f"={c}{{pros}}" if i==0 else f"=MAX(0,{c}{{pros}}-{p}{{pros}})+{p}{{pros}}*{a('churn')}",NUM)
    R('conb','Verificación y activación de profesionales','USD',lambda i,c,p: f"={c}{{newp}}*{a('onb')}")
    SEC('Costos fijos')
    R('fpay','Nómina con cargas','USD',lambda i,c,p: f"={ch(c,'pay1','pay2','pay3')}*(1+{a('cs')})")
    R('ftec','Tecnología','USD',lambda i,c,p: f"={ch(c,'tec1','tec2','tec3')}")
    R('fmkt','Marketing de marca','USD',lambda i,c,p: f"={a('mkt')}")
    R('fadm','Legal, contabilidad y administración','USD',lambda i,c,p: f"={a('adm')}")
    R('fix','Total costos fijos','USD',lambda i,c,p: f"={c}{{fpay}}+{c}{{ftec}}+{c}{{fmkt}}+{c}{{fadm}}",USD,True)
    SEC('Resultado y caja')
    R('ebitda','EBITDA','USD',lambda i,c,p: f"={c}{{contrib}}-{c}{{cmk}}-{c}{{conb}}-{c}{{fix}}",USD,True)
    R('capex','Inversión en app nativa','USD',lambda i,c,p: f"=IF({c}$3={a('appm')},{a('app')},0)")
    R('flow','Flujo de caja del mes','USD',lambda i,c,p: f"={c}{{ebitda}}-{c}{{capex}}",USD,True)
    R('cash','Caja acumulada','USD',lambda i,c,p: (f"={a('cash0')}+{c}{{flow}}" if i==0 else f"={p}{{cash}}+{c}{{flow}}"),USD,True)
    R('pos','EBITDA positivo (1 = sí)','',lambda i,c,p: f"=IF({c}{{ebitda}}>0,1,0)",'0')
    # header rows
    ws['A3']='Mes'; ws['A4']='Año'
    for i,c in enumerate(months):
        ws[f'{c}3']=i+1; ws[f'{c}4']=f'=ROUNDUP({c}3/12,0)'
        for rr in (3,4):
            ws[f'{c}{rr}'].font=f_h; ws[f'{c}{rr}'].fill=fill_h; ws[f'{c}{rr}'].alignment=Alignment(horizontal='center')
    for rr in (3,4):
        ws[f'A{rr}'].font=f_h; ws[f'A{rr}'].fill=fill_h; ws[f'B{rr}'].fill=fill_h
    rr=6; keyrow={}
    for key,label,unit,fn,fmt,bold in rows:
        if key: keyrow[key]=rr
        rr+=1
    rr=6
    for key,label,unit,fn,fmt,bold in rows:
        if key is None:
            for cc in range(1,C0+NM): ws.cell(row=rr,column=cc).fill=fill_sec
            ws.cell(row=rr,column=1,value=label).font=f_sec
        else:
            ws.cell(row=rr,column=1,value=label).font=f_calcb if bold else f_calc
            ws.cell(row=rr,column=2,value=unit).font=f_note
            for i,c in enumerate(months):
                p=months[i-1] if i else None
                fx=fn(i,c,p)
                for k,v in keyrow.items(): fx=fx.replace('{'+k+'}',str(v))
                cell=ws[f'{c}{rr}']; cell.value=fx; cell.number_format=fmt
                cell.font=Font(name=F,size=10,bold=bool(bold),color='008000' if ('Supuestos!' in fx and '{' not in fx and fx.count('Supuestos!')>=1 and all(t not in fx for t in ['*','+','-','/']) ) else '000000')
                if bold: cell.fill=fill_tot
        rr+=1
    ws.column_dimensions['A'].width=44; ws.column_dimensions['B'].width=13
    for c in months: ws.column_dimensions[c].width=11
    ws.freeze_panes='C5'
    ROWS[name]=keyrow
    return ws
models={n:build(n,c) for n,c in SCEN}

# ------------------------------------------------------------------ Resumen
R_=wb.create_sheet('Resumen',0)
R_['A1']='Cuadra · Resumen del modelo a 36 meses'; R_['A1'].font=f_title
R_['A2']='Todo se calcula desde las hojas Modelo; edita solo la hoja Supuestos. USD, sin ITBMS ni impuesto sobre la renta.'; R_['A2'].font=f_note
yrs=[(1,months[0],months[11]),(2,months[12],months[23]),(3,months[24],months[35])]
# header
R_['A4']='Métrica'
col=2; hdrpos={}
for n,_ in SCEN:
    R_.cell(row=3,column=col,value=n).font=f_h
    for k in range(3): R_.cell(row=3,column=col+k).fill=fill_h
    for k,(y,_,_) in enumerate(yrs):
        c=R_.cell(row=4,column=col+k,value=f'Año {y}'); c.font=f_sec; c.alignment=Alignment(horizontal='center'); c.fill=fill_sec
    hdrpos[n]=col; col+=3
R_['A4'].font=f_sec; R_['A4'].fill=fill_sec
def ref(n,key,c): return f"'Modelo {n}'!{c}{ROWS[n][key]}"
metrics=[
 ('Servicios completados en el año',lambda n,a,b:f"=SUM({ref(n,'srv',a)}:{b}{ROWS[n]['srv']})",NUM),
 ('Servicios en el último mes del año',lambda n,a,b:f"={ref(n,'srv',b)}",NUM),
 ('GMV del año',lambda n,a,b:f"=SUM({ref(n,'gmv',a)}:{b}{ROWS[n]['gmv']})",USD),
 ('Ingresos del año',lambda n,a,b:f"=SUM({ref(n,'rev',a)}:{b}{ROWS[n]['rev']})",USD),
 ('Comisión efectiva (comisiones / GMV)',lambda n,a,b:f"=IFERROR(SUM({ref(n,'rcom',a)}:{b}{ROWS[n]['rcom']})/SUM({ref(n,'gmv',a)}:{b}{ROWS[n]['gmv']}),0)",PCT),
 ('Margen de contribución del año',lambda n,a,b:f"=SUM({ref(n,'contrib',a)}:{b}{ROWS[n]['contrib']})",USD),
 ('Margen de contribución por servicio',lambda n,a,b:f"=IFERROR(SUM({ref(n,'contrib',a)}:{b}{ROWS[n]['contrib']})/SUM({ref(n,'srv',a)}:{b}{ROWS[n]['srv']}),0)",USD2),
 ('Marketing de adquisición del año',lambda n,a,b:f"=SUM({ref(n,'cmk',a)}:{b}{ROWS[n]['cmk']})",USD),
 ('Costos fijos del año',lambda n,a,b:f"=SUM({ref(n,'fix',a)}:{b}{ROWS[n]['fix']})",USD),
 ('EBITDA del año',lambda n,a,b:f"=SUM({ref(n,'ebitda',a)}:{b}{ROWS[n]['ebitda']})",USD),
 ('Caja al cierre del año',lambda n,a,b:f"={ref(n,'cash',b)}",USD),
 ('Profesionales activos al cierre',lambda n,a,b:f"={ref(n,'pros',b)}",NUM),
]
r=5
for label,fn,fmt in metrics:
    R_.cell(row=r,column=1,value=label).font=f_calc
    for n,_ in SCEN:
        for k,(y,a_,b_) in enumerate(yrs):
            c=R_.cell(row=r,column=hdrpos[n]+k,value=fn(n,a_,b_)); c.number_format=fmt; c.font=f_link
            if label.startswith('EBITDA'): c.fill=fill_tot; c.font=Font(name=F,size=10,bold=True,color='008000')
    r+=1
r+=1
R_.cell(row=r,column=1,value='Indicadores clave por escenario').font=f_sec
for n,_ in SCEN:
    R_.cell(row=r,column=hdrpos[n],value=n).font=f_sec
for cc in range(1,11): R_.cell(row=r,column=cc).fill=fill_sec
r+=1
kpis=[
 ('Primer mes con EBITDA positivo',lambda n:f"=IFERROR(MATCH(1,{ref(n,'pos',first)}:{last}{ROWS[n]['pos']},0),\"No en 36 meses\")",'0'),
 ('Caja mínima en 36 meses',lambda n:f"=MIN({ref(n,'cash',first)}:{last}{ROWS[n]['cash']})",USD),
 ('Capital adicional necesario (sobre el inicial)',lambda n:f"=MAX(0,-B{{min}})".replace('B',''),USD),
 ('EBITDA del mes 36',lambda n:f"={ref(n,'ebitda',last)}",USD),
 ('Costos fijos del mes 36',lambda n:f"={ref(n,'fix',last)}",USD),
 ('Servicios al mes para cubrir fijos + CAC del mes 36',lambda n:f"=IFERROR(({ref(n,'fix',last)}+{ref(n,'cmk',last)}+{ref(n,'conb',last)})/{ref(n,'cps',last)},0)",NUM),
 ('Servicios reales en el mes 36',lambda n:f"={ref(n,'srv',last)}",NUM),
]
kr={}
for label,fn,fmt in kpis:
    R_.cell(row=r,column=1,value=label).font=f_calc
    kr[label]=r
    for n,_ in SCEN:
        colL=L(hdrpos[n])
        fx=fn(n)
        if 'Capital adicional' in label: fx=f"=MAX(0,-{colL}{kr['Caja mínima en 36 meses']})"
        c=R_.cell(row=r,column=hdrpos[n],value=fx); c.number_format=fmt; c.font=f_link if 'Modelo' in fx else f_calc
        if 'Capital adicional' in label or 'Primer mes' in label: c.fill=fill_key; c.font=Font(name=F,size=10,bold=True,color='008000' if 'Modelo' in fx else '000000')
    r+=1

# Levers (Medio, month 36)
r+=1
R_.cell(row=r,column=1,value='Palancas: efecto en el EBITDA del mes 36, escenario Medio').font=f_sec
for cc in range(1,11): R_.cell(row=r,column=cc).fill=fill_sec
r+=1
R_.cell(row=r,column=1,value='Cada fila cambia una sola cosa y deja todo lo demás igual. Los valores azules de esta tabla se pueden editar.').font=f_note; r+=1
n='Medio'; m=lambda k:ref(n,k,last); sup=lambda k:f"Supuestos!$D${A[k]}"
R_.cell(row=r,column=1,value='Palanca').font=f_sec; R_.cell(row=r,column=2,value='Valor').font=f_sec; R_.cell(row=r,column=3,value='Cambio en EBITDA del mes').font=f_sec; R_.cell(row=r,column=4,value='EBITDA del mes resultante').font=f_sec; r+=1
base_r=r
R_.cell(row=r,column=1,value='Base: EBITDA del mes 36 (Medio)').font=f_calc
c=R_.cell(row=r,column=4,value=f"={m('ebitda')}"); c.number_format=USD; c.font=f_link; r+=1
levers=[
 ('Cargo por servicio al cliente (% del ticket)',0.05,PCT,lambda v:f"={m('gmv')}*{v}*(1-{sup('proc')})"),
 ('Comisión a clientes que repiten (en vez del supuesto)',0.10,PCT,lambda v:f"={m('gmv')}*{m('rep')}*({v}-{sup('cr')})"),
 ('Aumento del ticket promedio (USD)',15,USD,lambda v:f"={m('srv')}*{v}*({m('take')}+{sup('mat')}-{sup('proc')}-{sup('gar')})"),
 ('Procesamiento de pagos (en vez del supuesto)',0.02,PCT,lambda v:f"={m('gmv')}*({sup('proc')}-{v})"),
 ('Reducción del CAC (USD por cliente)',4,USD,lambda v:f"={m('nw')}*{v}"),
]
for label,val,fmt,fn in levers:
    R_.cell(row=r,column=1,value=label).font=f_calc
    v=R_.cell(row=r,column=2,value=val); v.font=f_in; v.number_format=fmt
    c=R_.cell(row=r,column=3,value=fn(f"B{r}")); c.number_format=USD; c.font=f_calc
    c=R_.cell(row=r,column=4,value=f"=$D${base_r}+C{r}"); c.number_format=USD; c.font=f_calc
    r+=1
R_.cell(row=r,column=1,value='Todas las palancas juntas').font=f_calcb
c=R_.cell(row=r,column=3,value=f"=SUM(C{base_r+1}:C{r-1})"); c.number_format=USD; c.font=f_calcb
c=R_.cell(row=r,column=4,value=f"=$D${base_r}+C{r}"); c.number_format=USD; c.font=f_calcb; c.fill=fill_key
r+=2

# Sensitivity of take rate to repeat share
R_.cell(row=r,column=1,value='Comisión efectiva según % de clientes que repiten (mezcla de niveles del año 3, escenario Medio)').font=f_sec
for cc in range(1,11): R_.cell(row=r,column=cc).fill=fill_sec
r+=1
R_.cell(row=r,column=1,value='% de trabajos de clientes que repiten').font=f_calc
R_.cell(row=r+1,column=1,value='Comisión efectiva sobre GMV').font=f_calcb
for k,v in enumerate([0,0.1,0.2,0.3,0.4,0.5,0.6]):
    cc=R_.cell(row=r,column=2+k,value=v); cc.font=f_in; cc.number_format='0%'
    colL=L(2+k)
    fx=f"={colL}{r}*{sup('cr')}+(1-{colL}{r})*((1-{sup('pl3')}-{sup('or3')})*{sup('cb')}+{sup('pl3')}*{sup('cp')}+{sup('or3')}*{sup('co')})"
    cc=R_.cell(row=r+1,column=2+k,value=fx); cc.number_format=PCT; cc.font=f_calcb
r+=3
chart_row=r
R_.column_dimensions['A'].width=58
for k in range(2,11): R_.column_dimensions[L(k)].width=14
R_.freeze_panes='B5'

# Charts
lc=LineChart(); lc.title='Caja acumulada por escenario (USD)'; lc.y_axis.title='USD'; lc.x_axis.title='Mes'; lc.height=8; lc.width=22
for n,_ in SCEN:
    ws=models[n]; rr=ROWS[n]['cash']
    ref_=Reference(ws,min_col=C0-1,max_col=C0+NM-1,min_row=rr)
    lc.add_data(ref_,from_rows=True,titles_from_data=True)
lc.series[0].tx=None
from openpyxl.chart.series import SeriesLabel
for s,(n,_) in zip(lc.series,SCEN): s.tx=SeriesLabel(v=n)
lc.set_categories(Reference(models['Medio'],min_col=C0,max_col=C0+NM-1,min_row=3))
R_.add_chart(lc,f'A{chart_row}')
lc2=LineChart(); lc2.title='EBITDA mensual por escenario (USD)'; lc2.height=8; lc2.width=22
for n,_ in SCEN:
    ws=models[n]; rr=ROWS[n]['ebitda']
    lc2.add_data(Reference(ws,min_col=C0-1,max_col=C0+NM-1,min_row=rr),from_rows=True,titles_from_data=True)
for s,(n,_) in zip(lc2.series,SCEN): s.tx=SeriesLabel(v=n)
lc2.set_categories(Reference(models['Medio'],min_col=C0,max_col=C0+NM-1,min_row=3))
R_.add_chart(lc2,f'A{chart_row+17}')

from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.drawing.line import LineProperties
COLS=['8A8F9E','1F3FBF','F5B728']
for ch_ in (lc,lc2):
    ch_.x_axis.delete=False; ch_.y_axis.delete=False
    ch_.x_axis.tickLblPos='low'; ch_.y_axis.number_format='$#,##0;($#,##0)'
    ch_.legend.position='b'
    for s_,col_ in zip(ch_.series,COLS):
        s_.smooth=False
        s_.graphicalProperties.line.solidFill=col_
        s_.graphicalProperties.line.width=28000

# ------------------------------------------------------------------ Suscripción Cuadra+
U=wb.create_sheet('Suscripción',1)
U['A1']='Cuadra+ · Suscripción mensual para clientes'; U['A1'].font=f_title
U['A2']='Principio: beneficios que suenan ilimitados pero se usan poco o le cuestan poco a Cuadra. El precio se fija para que el usuario más intenso quede cerca de cero y el promedio deje margen. Texto azul = editable.'; U['A2'].font=f_note
U['A3']='Todos los valores son supuestos de trabajo (Suposición) salvo los vinculados en verde, que vienen del modelo. Validar uso real en el piloto.'; U['A3'].font=f_note
for i,h in enumerate(['Supuesto','Unidad','Cuadra+ Hogar','Cuadra+ Total','Nota'],1):
    c=U.cell(row=5,column=i,value=h); c.font=f_h; c.fill=fill_h
UR={}
r=6
def urow(key,label,unit,vals,fmt,note='',kind='in',keyfill=False):
    global r
    U.cell(row=r,column=1,value=label).font=f_calc
    U.cell(row=r,column=2,value=unit).font=f_note
    for j,v in enumerate(vals):
        if v is None: continue
        c=U.cell(row=r,column=3+j,value=v); c.number_format=fmt
        c.font={'in':f_in,'link':f_link,'calc':f_calc}[kind]
        if keyfill: c.fill=fill_key
    U.cell(row=r,column=5,value=note).font=f_note
    UR[key]=r; r+=1
def usec(t):
    global r
    for cc in range(1,6): U.cell(row=r,column=cc).fill=fill_sec
    U.cell(row=r,column=1,value=t).font=f_sec; r+=1
usec('Precio')
urow('pm','Precio mensual','USD/mes',[9.99,19.99],USD2,'Hogar al nivel de NEXO Essential ($9.99) para que la comparación sea fácil.',keyfill=True)
urow('pa','Precio anual (prepago)','USD/año',[99,199],USD2,'Equivale a ~2 meses gratis. Trae caja por adelantado.',keyfill=True)
urow('fa','% de miembros que paga anual','%',[0.4,0.4],PCT,'')
urow('pe','Ingreso mensual efectivo por miembro','USD/mes',[f"=C{UR['fa']}*C{UR['pa']}/12+(1-C{UR['fa']})*C{UR['pm']}",f"=D{UR['fa']}*D{UR['pa']}/12+(1-D{UR['fa']})*D{UR['pm']}"],USD2,'Mezcla de pago mensual y anual.',kind='calc')
urow('mi','Mantenimientos de split incluidos al año','visitas',[0,3],'0','Total: el aire en Panamá necesita servicio cada 3-4 meses. Valor al público ~3 × $45.')
urow('mc','Lo que Cuadra le paga al profesional por mantenimiento incluido','USD',[38,38],USD,'Cerca de lo que el profesional recibe neto en un mantenimiento normal.')
usec('Costos de los beneficios (aplican a ambos planes)')
urow('tk','Ticket promedio','USD',[f"=Supuestos!$D${A['t0']}",None],USD2,'Del escenario Medio.',kind='link')
urow('fee','Cargo de servicio que pagan los no miembros (y los miembros no)','% del ticket',[0.04,None],PCT,'El plan necesita este cargo: sin él, "sin cargo de servicio" no vale nada.',keyfill=True)
urow('take','Comisión efectiva de Cuadra (año 3, Medio)','%',["=Resumen!G9",None],PCT,'Del Resumen.',kind='link')
urow('urg','Recargo de urgencia que Cuadra absorbe por cada urgencia de un miembro','USD',[15,None],USD,'El profesional sigue cobrando su recargo; lo paga Cuadra.')
urow('dg','Costo de una visita de diagnóstico que el miembro no termina contratando','USD',[20,None],USD,'Si contrata el trabajo, el diagnóstico ya se descontaba de todas formas.')
urow('gx','Costo de la garantía extendida a 90 días','% del valor de sus trabajos',[0.005,None],PCT,'Adicional al fondo de garantía normal.')
urow('pp','Cobro de la suscripción (tarjeta o Yappy)','% del precio',[0.03,None],PCT,'')
urow('up','Aumento de uso por ser miembro','%',[0.4,None],PCT,'Sin cargo y con urgencias sin recargo, el miembro usa más la app y se fuga menos.')
r+=1
# usage profiles
pr0=r
for i,h in enumerate(['Perfil de uso','% de miembros','Trabajos al año','Urgencias al año','Diagnósticos sin contratar al año','Mantenimientos que usaría al año'],1):
    c=U.cell(row=r,column=i,value=h); c.font=f_h; c.fill=fill_h; c.alignment=Alignment(wrap_text=True,vertical='center')
U.row_dimensions[r].height=30
r+=1
PROF=[('Ligero',0.5,2,0.2,0.2,1),('Promedio',0.35,4,1,0.5,2),('Intenso',0.15,8,3,2,3)]
prow={}
for name,share,jobs,urgn,diag,mant in PROF:
    U.cell(row=r,column=1,value=name).font=f_calc
    for j,(v,fmt) in enumerate([(share,PCT),(jobs,'0.0'),(urgn,'0.0'),(diag,'0.0'),(mant,'0.0')]):
        c=U.cell(row=r,column=2+j,value=v); c.font=f_in; c.number_format=fmt
    prow[name]=r; r+=1
U.cell(row=r,column=1,value='Total (debe sumar 100%)').font=f_note
c=U.cell(row=r,column=2,value=f'=SUM(B{pr0+1}:B{r-1})'); c.number_format=PCT; c.font=f_calc
r+=2
# results per plan and profile
res0=r
for i,h in enumerate(['Resultado por miembro al mes','Plan','Ligero','Promedio','Intenso','Promedio ponderado'],1):
    c=U.cell(row=r,column=i,value=h); c.font=f_h; c.fill=fill_h
r+=1
RES={}
C=lambda k:f"$C${UR[k]}"
for plan,col in (('Hogar','C'),('Total','D')):
    P=lambda k:f"${col}${UR[k]}"
    lines=[
     ('cost','Costo de los beneficios',lambda pr:f"=(B_JOBS*{C('tk')}*{C('fee')}+B_URG*{C('urg')}+B_DIAG*{C('dg')}+B_JOBS*{C('tk')}*{C('gx')}+MIN(B_MANT,{P('mi')})*{P('mc')})/12+{P('pe')}*{C('pp')}"),
     ('marg','Margen de la suscripción',lambda pr:f"={P('pe')}-COST"),
     ('extra','Comisión extra por mayor uso',lambda pr:f"=(B_JOBS-B_JOBS/(1+{C('up')}))*{C('tk')}*{C('take')}/12"),
     ('tot','Aporte total del miembro',lambda pr:"=MARG+EXTRA"),
    ]
    for key,label,fn in lines:
        U.cell(row=r,column=1,value=label).font=f_calcb if key=='tot' else f_calc
        U.cell(row=r,column=2,value='Cuadra+ '+plan).font=f_note
        for j,name in enumerate(['Ligero','Promedio','Intenso']):
            pr=prow[name]; colL=L(3+j)
            fx=fn(pr).replace('B_JOBS',f'$C${pr}').replace('B_URG',f'$D${pr}').replace('B_DIAG',f'$E${pr}').replace('B_MANT',f'$F${pr}')
            fx=fx.replace('COST',f'{colL}{RES.get((plan,"cost"),0)}').replace('MARG',f'{colL}{RES.get((plan,"marg"),0)}').replace('EXTRA',f'{colL}{RES.get((plan,"extra"),0)}')
            c=U.cell(row=r,column=3+j,value=fx); c.number_format=USD2; c.font=f_calcb if key=='tot' else f_calc
        c=U.cell(row=r,column=6,value=f"=$B${prow['Ligero']}*C{r}+$B${prow['Promedio']}*D{r}+$B${prow['Intenso']}*E{r}"); c.number_format=USD2; c.font=f_calcb
        if key=='tot':
            for cc in range(1,7): U.cell(row=r,column=cc).fill=fill_tot
        RES[(plan,key)]=r; r+=1
    # weighted jobs per member per year
    U.cell(row=r,column=1,value='Trabajos al año por miembro (ponderado)').font=f_note
    c=U.cell(row=r,column=6,value=f"=SUMPRODUCT($B${pr0+1}:$B${pr0+3},$C${pr0+1}:$C${pr0+3})"); c.number_format='0.00'; c.font=f_calc
    RES[(plan,'jobs')]=r; r+=2
# margin of the heaviest user as % of price
U.cell(row=r,column=1,value='Margen del usuario intenso como % del precio (Hogar / Total)').font=f_calc
c=U.cell(row=r,column=3,value=f"=IFERROR(E{RES[('Hogar','marg')]}/$C${UR['pe']},0)"); c.number_format=PCT; c.font=f_calcb
c=U.cell(row=r,column=4,value=f"=IFERROR(E{RES[('Total','marg')]}/$D${UR['pe']},0)"); c.number_format=PCT; c.font=f_calcb
U.cell(row=r,column=5,value='El principio del car wash: el más intenso queda cerca de cero, el promedio deja margen.').font=f_note
r+=2
# impact on month 36, Medio
usec('Efecto en el mes 36 del escenario Medio')
ML="'Modelo Medio'!"+last
urow('hj','Trabajos al año de un hogar típico (no miembro)','trabajos',[2.5,None],'0.0','Suposición: para estimar cuántos hogares distintos usan la app.')
urow('ha','Hogares activos al mes 36','hogares',[f"={ML}{ROWS['Medio']['srv']}*12/C{UR['hj']}",None],NUM,'Servicios del mes 36 × 12 ÷ trabajos por hogar.',kind='calc')
urow('pen','Penetración de la suscripción','% de hogares activos',[0.10,0.03],PCT,'',keyfill=True)
urow('mem','Miembros','miembros',[f"=C{UR['ha']}*C{UR['pen']}",f"=C{UR['ha']}*D{UR['pen']}"],NUM,'',kind='calc')
urow('ap','Aporte mensual de la suscripción','USD/mes',[f"=C{UR['mem']}*F{RES[('Hogar','tot')]}",f"=D{UR['mem']}*F{RES[('Total','tot')]}"],USD,'',kind='calc')
urow('mj','Trabajos al mes hechos por miembros','trabajos',[f"=C{UR['mem']}*F{RES[('Hogar','jobs')]}/12",f"=D{UR['mem']}*F{RES[('Total','jobs')]}/12"],NUM,'',kind='calc')
urow('fr','Ingreso por cargo de servicio a no miembros','USD/mes',[f"=MAX(0,{ML}{ROWS['Medio']['srv']}-C{UR['mj']}-D{UR['mj']})*C{UR['tk']}*C{UR['fee']}*(1-Supuestos!$D${A['proc']})",None],USD,'Los no miembros pagan el cargo; el cobro del banco se descuenta.',kind='calc')
urow('eb','EBITDA del mes 36 sin suscripción ni cargo','USD/mes',[f"={ML}{ROWS['Medio']['ebitda']}",None],USD,'Del modelo Medio.',kind='link')
urow('eb2','EBITDA del mes 36 con suscripción y cargo','USD/mes',[f"=C{UR['eb']}+C{UR['ap']}+D{UR['ap']}+C{UR['fr']}",None],USD,'Sin contar ingresos por prepago anual ni menor fuga.',kind='calc',keyfill=True)
U.column_dimensions['A'].width=62; U.column_dimensions['B'].width=22
for cc in 'CDEF': U.column_dimensions[cc].width=16
U.column_dimensions['E'].width=18
U.freeze_panes='C6'

# fonts default for any unset cell values
for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            if c.value is not None and c.font.name!=F:
                c.font=Font(name=F,size=10,bold=c.font.bold,color=c.font.color)
wb.save(OUT); print('saved',OUT)
