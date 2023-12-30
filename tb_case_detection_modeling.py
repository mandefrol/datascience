import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

df = pd.read_csv('./data/tb_detection_rate_by_region_dash.csv')

app = dash.Dash(external_stylesheets=[dbc.themes.LITERA])

app.head = [html.Link(rel='stylesheet', href='./assets/mystyle.css')]

regions = []
for region in df['Region'].unique():
    regions.append(region)

app.layout = html.Div([
    html.Div(id='title-text', children=[
        html.H1(children='Ethiopian Public Health Institute'),
        html.H2(children='National Data Management Center for Health'),
        html.H3(children='TB Case Detection Rate (All Forms)'),
    ], style={'background-color': '#4B84C5', 'width': '100%','text-align':'center','color':'#FFFFFF'}),
    html.Div(id='body-div', children=[
        html.Div(id='region-div', children=[
            dcc.Dropdown(id='region-picker',
                         options=regions,
                         value='National',
                         placeholder='Select Region'),
            html.P(id='line-break'),
            dcc.Dropdown(id='graph-type-picker',
                         options=['Line', 'Bar'],
                         value='Line',
                         placeholder='Choose Chart'),
            html.P(id='line-break2'),
            dbc.Checklist(id='national-forecast',
                          options=['National Forecast'],
                          style={'color':'MediumTurqoise', 'font-size':20})],
                 style={
                     'display': 'inline-block',
                     'margin': '0 auto',
                     'padding': '20px',
                     'width': '20%',
                     'float': 'left',
                 }),
        html.Div(id='graph-div', children=[
            dcc.Graph(id='graph-with-slider')],
                 style={
                     'display': 'inline-block',
                     'margin': '0 auto',
                     'padding': '20px',
                     'width': '80%',
                     'float': 'right'
                 })
        ],
        style={
            'background-color': '#2E8B57',
            'display': 'inline-block',
            'margin': '0 auto',
            'padding': '20px',
            'width':'100%'})
])


@app.callback(Output('graph-with-slider', 'figure'),
              [Input('region-picker', 'value'),
               Input('graph-type-picker', 'value'),
               Input('national-forecast','value')])
def update_graph(selected_region, selected_graph,national_forecast):
    filtered_df = df[df['Region'] == selected_region]

    if selected_graph == 'Bar':
        fig = px.bar(filtered_df,
                     x=filtered_df['Year'],  
                     y=filtered_df['Rate'],
                     title='TB Detection Rate: {}'.format(selected_region),
                     text=filtered_df['Rate'],

                     )
        fig.update_xaxes(title_font=dict(size=20,
                                         family='Verdana',
                                         color='#123C69'),
                         showgrid=False)
        fig.update_yaxes(title_font=dict(size=20,
                                         family='Verdana',
                                         color='#123C69'))
        fig.update_layout(title_font_color='#006400',
                          title_x=0.5,
                          title_font_size=20)
        return fig
    elif selected_graph == 'Line':
        fig = px.line(filtered_df,
                      x=filtered_df['Year'],
                      y=filtered_df['Rate'],
                      title='TB Detection Rate: {}'.format(selected_region),
                      markers='o',
                      text=filtered_df['Rate'],

                      )
        fig.update_xaxes(title_font=dict(size=20,
                                         family='Verdana',
                                         color='#123C69'),
                         showgrid=False)
        fig.update_yaxes(title_font=dict(size=20,
                                         family='Verdana',
                                         color='#123C69'))
        fig.update_traces(textposition="top center")
        fig.update_layout(title_font_color='#006400',
                          title_x=0.5,
                          title_font_size=20)
        return fig
    elif national_forecast == 'National Forecast':
        selected_region(disabled=True)

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
