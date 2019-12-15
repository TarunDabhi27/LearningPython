import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

app.layout = html.Div(children=[
    
        html.H1(children="Dash Visualization"),
        dcc.Graph(
            id="test-id",
            figure={
                "data": [
                    {
                        "x": ["Mon", "Tue", "Wed", "Thus", "Fri", "Sat", "Sun"],
                        "y": [10, 20, 5, 15, 32, 41, 21],
                        "type": "bar",
                        "name": "Last Week"
                    }
                ],
                "layout": {"title": "Example Visualization"}
                }
            )
    ])


if __name__ == '__main__':
    app.run_server()