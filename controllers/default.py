# -*- coding: utf-8 -*-

from gluon.custom_import import track_changes
track_changes(True)

import highcharts_thema

from highcharts import clock
from highcharts import chart


def index():
    
    #chart1 = grafico.chart('column', 'container01')

    chart1 = clock('gauge', 'container00')
    chart2 = chart('area', 'container01')

    
    a = html(chart1, chart2)

    return a

def html(strchart1, strchart2):

    largura = 1440
    altura = 860

    nmlinhas = 1
    nmcolunas = 2

    largcel = largura / nmcolunas
    altcel = altura / nmlinhas


    strtd = criacolunas(largcel, altcel, 0, strchart1, strchart2, nmcolunas)    
    
    trlinha = (TR(strtd,_style=': 1px; height:' + str(altcel) + 'px; margin: 0 auto'), )

    for l in xrange(1,nmlinhas):
        
        strtd = criacolunas(largcel, altcel, l, strchart1, strchart2, nmcolunas)

        trlinha = trlinha + (TR(strtd,_style=': 1px; height:' + str(altcel) + 'px; margin: 0 auto'), )
    
    tabela = TABLE(trlinha, _border='0')

    html = HTML(
            HEAD(
                META(_charset='utf-8'),
                TITLE("graficos"),
                META(_name='application-name',_content=''),
                META(_name='google-site-verification',_content=''),
                META(_name='viewport',_content='width=device-width, initial-scale=1.0, user-scalable=yes'),
            SCRIPT(_src='/graficos/static/js/jquery.min.js'),
            tabela,
    
            SCRIPT(_language='javascript', _type='text/javascript')
            ),
            BODY(SCRIPT(_src='/graficos/static/js/highcharts.js'), SCRIPT(_src='/graficos/static/js/highcharts-more.js'),_bgcolor='FFFFFF'),
            #DIV(_id='container', _style='width:2px; height: 1px; margin: 1 auto'),
             _class='no-js')
            
    return html




def criacolunas(largcel, altcel, nmlinha, strchart1, strchart2, nmcolunas):

    # primeira coluna da tabela
    colunas = (TD(SCRIPT(XML(strchart1),_type='text/javascript'),
                _id='container' + str(nmlinha) + '0',_style='width:' + str(largcel) + 'px; height: ' + str(altcel) + 'px; margin: 0 auto'), )

    for c in xrange(1,nmcolunas):

        # adiciona colunas a linha até a quantidade selecionada

        colunas =  colunas + (TD(SCRIPT(XML(strchart2),_type='text/javascript'),
                              _id='container' + str(nmlinha) + str(c),_style='width:' + str(largcel) + 'px; height: ' + str(altcel) + 'px; margin: 0 auto'), )

    return colunas


def extra():
    html = HTML(
            HEAD(
                META(_charset='utf-8'),
                TITLE("graficos"),
                META(_name='application-name',_content=''),
                META(_name='google-site-verification',_content=''),
                META(_name='viewport',_content='width=device-width, initial-scale=1.0, user-scalable=yes'),
            SCRIPT(_src='/graficos/static/js/jquery.min.js'),
            #tabela,
    
            SCRIPT(_language='javascript', _type='text/javascript')
            ),
            BODY(SCRIPT(_src='/graficos/static/js/highcharts.js'), SCRIPT(_src='/graficos/static/js/highcharts-more.js'),_bgcolor='FFFFFF'),
            #DIV(_id='container', _style='width:2px; height: 1px; margin: 1 auto'),
             _class='no-js')
            
    return html