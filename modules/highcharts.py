# -*- coding: utf-8 -*-

class highcharts:

    def __init__(self):
        self.arg = 'arg'

       


    def chart(self, param):

        strchart = '''
    
        var chart1; // globally available
        $(document).ready(

        function() {
        chart1 = new Highcharts.Chart({
         
       ''' + self._chart(param.get('tipo')) +  self._title(param.get('title')) +  self._xAxis() + self._yAxis() + self._series() + '''
        
         }); }); '''

        return strchart

    def _title(self, param):
            
        string = '''title: {text:' ''' + param + '''' },'''

        return string


    def _xAxis(self):

        string = ''' xAxis: { categories: ['Apples', 'Bananas', 'Oranges']},'''

        return string


    def _yAxis(self):
        
        string = ''' yAxis: { title: { text: 'Fruit eaten' } }, '''

        return string

    def _chart(self, param):

        string = ''' chart: {renderTo: 'container', type: ''' + "'" + param + "'" + ''' }, '''

        return string

    def _series(self):

        string = ''' series: [{ name: 'Jane', data: [1, 0, 4] }, { name: 'John', data: [5, 7, 3] }] '''

        return string