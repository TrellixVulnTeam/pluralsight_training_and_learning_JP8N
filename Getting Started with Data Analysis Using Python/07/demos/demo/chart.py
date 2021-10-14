import pygal
from pygal.style import CleanStyle
from pygal.style import DarkGreenStyle

data1 = {}
data1[1]=10
data1[2]=20
data1[3]=30
data1[4]=25
data1[5]=17

data2 = {}
data2[1]=40
data2[2]=33
data2[3]=20
data2[4]=15
data2[5]=11

bar_chart = pygal.Bar(style=CleanStyle)
bar_chart.title = "Bar Chart"
bar_chart.x_labels = [1,2,3,4,5]  #List
bar_chart.add("data1" , data1)
bar_chart.add("data2" , data2)
# Save the svg to a file
bar_chart.render_to_file('bar_chart.svg')

line_chart = pygal.Line(style=CleanStyle)
line_chart.title = "Line Chart"
line_chart.x_labels = [1,2,3,4,5]  #List
line_chart.add("data1" , data1)
line_chart.add("data2" , data2)
# Save the svg to a file
line_chart.render_to_file('line_chart.svg')
