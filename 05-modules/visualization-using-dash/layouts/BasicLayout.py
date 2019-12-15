import dash
import dash_core_components as dcc
import  dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dash Visualization - Layouts'),

    dcc.Graph(id='test-graph',figure={
        'data':[
            {'x':['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],'y':[10,11,23,1],'type':'bar', 'name':"Last Week"},
            {'x':['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],'y':[4,5,6,7],'type':'bar', 'name':"Before Last Week"}
        ],

        'layout':{
            'title':'Dash Data Visualization'
        }
    })
])
if __name__ == '__main__':
    app.run_server()