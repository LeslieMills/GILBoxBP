import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_uploader as du
import plotly.graph_objects as go
from app import app

du.configure_upload(app,"uploads",use_upload_id=False)

def get_upload_component(id):
    return du.Upload(
        id=id,
        pause_button=True,
        text_completed='Uploaded: ',
        max_file_size=1800,  # 1800 Mb
        filetypes=['csv', 'json'],
    )

main_layout = html.Div([
                dbc.Container([
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            html.H2("Boosterpack sample", style={"textAlign":"center"}, className="col-md-12 text-white"),
                            width=12,className="navbar navbar-expand-lg navbar-light bg-primary")
                            ],
                        className="text-center"),
                    html.Hr(),
                    dbc.Row([
                        dbc.Col([
                            html.Hr(),
                            html.Div([
                                dcc.Dropdown(id="dynamic-dropdown",options=[{'label':'Demo file','value':'202004-divvy-tripdata'}], placeholder="Select a dataset", className="form-select")
                                     ], 
                                className="form-group",style={'color':'black'}),
                            html.Div(id='dd-output-container',style={'textAlign':'center'}),
                            html.Hr(),
                            html.Button('Load', id='initiate', n_clicks=0,
                                        className="btn btn-lg btn-success", style={'width': '100%', 'offset':1}
                                        ),
                            dcc.Loading(
                                id="loading-1",
                                type="circle",
                                fullscreen=True,
                                children=html.Div(id="loading-output-1", style={'textAlign':'center'})
                                ),
                            dcc.Loading(
                                id="loading-3",
                                type="circle",
                                fullscreen=True,
                                children=html.Div(id="loading-output-3", style={'textAlign':'center'})
                                ),
                            html.Hr(),
                            html.Button('Download CSV', id='btn_csv', n_clicks=0, 
                                            className="btn btn-lg btn-warning", 
                                        ),
                            html.Hr(),
                            html.Div(dcc.Download(id="download-dataframe-csv")),
                            html.Div([
                                    get_upload_component(id='dash-uploader'),
                                ],
                                className='card text-white bg-primary mb-3',
                                #style={'justify':'center'}
                                style={  # wrapper div style
                                #     'textAlign': 'center',
                                #     'width': '200px',
                                    'padding': '10px',
                                #     'display': 'inline-block'
                                },
                                ),
                            html.Ul(id="file-list",children=[]),
                            html.Hr(), 
                            dcc.DatePickerRange(
                                    id='my-date-picker-range', className="form-select", style={'textAlign':'center'}
                                    ),
                            html.Div(id='output-container-date-picker-range', children=[],className='text-warning',style={'textAlign':'center'}),
                            html.Div(id='output-container-max-date-range', children=[],className='text-warning',style={'textAlign':'center'}),
                            html.Hr(),
                            html.Button('Analyze', id='analyze', n_clicks=0, hidden = True,
                                        className="btn btn-lg btn-danger", style={'width': '100%', 'offset':1}
                                    ),
                            dcc.Loading(
                                    id="loading-2",
                                    type="circle",
                                    fullscreen=True,
                                    children=html.Div(id="loading-output-2"),style={'textAlign':'center'}
                                    ),
                            dcc.Loading(
                                    id="loading-4",
                                    type="circle",
                                    fullscreen=True,
                                    children=html.Div(id="loading-output-4"),style={'textAlign':'center'}
                                    ),
                            dcc.Loading(
                                    id="loading-5",
                                    type="circle",
                                    fullscreen=True,
                                    children=html.Div(id="loading-output-5"),style={'textAlign':'center'}
                                    ),
                            html.Hr(),
                                ],
                                className='card text-dark bg-light mb-3',width=2),
                        dbc.Col([html.Div(html.H3("Map appears here post selection and loading of dataset"),id="map_placeholder", style={'textAlign':'center'}),
                            dcc.Graph(
                                id='map', className="tab-pane fade show active",
                                config={
                                    'displayModeBar': 'hover',
                                    'modeBarButtonsToAdd':['select2d'],
                                },
                                figure={
                                    'data': [],
                                    'layout': go.Layout(
                                        xaxis={
                                            'showticklabels': False,
                                            'ticks': '',
                                            'showgrid': False,
                                            'zeroline': False
                                        },
                                        yaxis={
                                            'showticklabels': False,
                                            'ticks': '',
                                            'showgrid': False,
                                            'zeroline': False
                                        },
                                        paper_bgcolor='rgba(0,0,0,0)',
                                        plot_bgcolor='rgba(0,0,0,0)',
                                        )}
                                )],className='card text-dark bg-light mb-3',width=7),
                        dbc.Col([
                            html.Div(html.H3("Horizontal bar graph appears here post clicking a point on the map"),id="graph_placeholder", style={'textAlign':'center'}),                
                            dcc.Graph(
                                id="graph",
                                config={
                                'displayModeBar': 'hover'
                                },
                                figure={
                                    'data': [],
                                    'layout': 
                                        go.Layout(
                                        xaxis={
                                            'showticklabels': False,
                                            'ticks': '',
                                            'showgrid': False,
                                            'zeroline': False
                                        },
                                        yaxis={
                                            'showticklabels': False,
                                            'ticks': '',
                                            'showgrid': False,
                                            'zeroline': False
                                        },
                                        paper_bgcolor='rgba(0,0,0,0)',
                                        plot_bgcolor='rgba(0,0,0,0)',
                                        )
                                    }
                                    )
                                ],className='card text-black bg-light mb-3', width=3,)
                            ],justify="center"),
                            dbc.Row([dbc.Col([html.Div(html.H3("Post AI processing map appears here"),id="postAI_placeholder", style={'textAlign':'center'}),                
                                dcc.Graph(
                                    id="cluster",
                                    config={
                                    'displayModeBar': 'hover'
                                    },
                                    figure={
                                        'data': [],
                                        'layout': 
                                            go.Layout(
                                            xaxis={
                                                'showticklabels': False,
                                                'ticks': '',
                                                'showgrid': False,
                                                'zeroline': False
                                            },
                                            yaxis={
                                                'showticklabels': False,
                                                'ticks': '',
                                                'showgrid': False,
                                                'zeroline': False
                                            },
                                            paper_bgcolor='rgba(0,0,0,0)',
                                            plot_bgcolor='rgba(0,0,0,0)',
                                            )
                                        }
                                    )
                                ],className='card text-black bg-light mb-3', width=6)],justify="center")],className=""),
                                        ],fluid=True)])

login_layout = html.Div([
                    html.H2('''Please log in to continue:''', id='h1'), 
                    dcc.Input(placeholder='Enter your username',
                                value = "",
                                type='text',
                                id='uname-box'), 
                    dcc.Input(placeholder='Enter your password',
                                type='password',
                                value="",
                                id='pwd-box'), 
                    html.Button('Login',
                                n_clicks=0,
                                id='login-button'), 
                    html.Div(children='', id='output-state')
                ])

login_failed = html.Div([ 
                    html.Div([
                        html.H2('Log in Failed. Please try again.'), 
                        html.Br(), 
                        html.Div([login_layout]), 
                        html.Br(), 
                        html.Button(id='back-button', children='Go back', n_clicks=0)
                    ]) 
                ])

logout = html.Div([
            html.Br(), 
            html.Div([
                html.H2('You have been logged out - Please login')]), 
            html.Br(), 
            html.Div([login_layout]), 
            html.Button(id='back-button', children='Go back', n_clicks=0)
        ])
