# -*- coding: utf-8 -*-

from gluon.custom_import import track_changes
track_changes(True)

from highcharts import highcharts


def index():
    
   # Parametros para criação do Gráfico

    param = {'title':'Gráfico', 'tipo':'spline'}

    chart = highcharts()
    chart = chart.chart(param)
     

    a = html(chart)

    return a


# Gera HTML    

def html(strchart):


    html = HTML(
            HEAD   (

                    META(http_equiv='Content-Type',_content='text/html',_charset='utf-8'),
                    TITLE("graficos"),
                    SCRIPT(_src='/graficos/static/js/jquery.min.js'),
                    SCRIPT(_src='/graficos/static/js/highcharts.js'), 
                    SCRIPT(XML(strchart), _type='text/javascript'),
                   ),

            BODY    (
                        DIV(_id='container', _style='width: 1440px; height: 860px; margin: 0 auto'),
                        _bgcolor='FFFFFF',
                        _class='no-js'

                    )
                )
            
    return html


