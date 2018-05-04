import dash
import dash_daq as daq
import dash_html_components as html

app=dash.Dash()

server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app_style = dict(
    background='#000',
    color='#FFF',
    fontFamily='sans-serif',
    textAlign='center',
    height='100vh',
    width='100%',
    paddingTop='100px',
)

app.layout = html.Div(
    id='container',
    children=[
        daq.DarkThemeProvider(
            theme=dict(dark=True), 
            children=[
                html.Link(rel='stylesheet', href='http://codepen.io/plotly/pen/mLMoGg.css'),
                html.Div(
                    style=dict(
                        background='#2a3f5f',
                        padding='10px',
                        width='40px',
                        borderRadius='4px',
                        margin='0 auto'
                    ),
                    children=[
                        daq.Indicator(
                            id="led",
                            label="LED",
                            color="red",
                            value=True
                        )
                    ]
                ),
                html.Br(),
                daq.ColorPicker(
                    id="color-picker",
                    label="Color Picker",
                    value=dict(hex="#FF0000"),
                    size=164,
                )
            ]
        )
    ]
)

@app.callback(
    dash.dependencies.Output('led', 'color'),
    [dash.dependencies.Input('color-picker', 'value')])
def set_led_color(color):    
    return color['hex']

@app.callback(
    dash.dependencies.Output('container', 'style'),
    [dash.dependencies.Input('color-picker', 'value')])
def set_led_color(color):
    app_style['backgroundColor'] = color['hex']
    return app_style

if __name__ == '__main__':
    app.run_server(debug=True)
