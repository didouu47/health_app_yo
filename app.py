# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 15:07:38 2019

@author: Azemar David
"""
from os import X_OK
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State, MATCH, ALL
import dash_bootstrap_components as dbc
import dash_table 
from dash.exceptions import PreventUpdate
from dash_table import DataTable
from pandas.io.parquet import to_parquet
from sqlalchemy import create_engine
import dash_daq as daq
#from dash_extensions import Download
#from dash_extensions.snippets import send_data_frame
import dash_admin_components as dac
import dash_table.FormatTemplate as FormatTemplate
from dash_table.Format import Format, Scheme, Sign, Symbol
import locale
import pandas as pd
import base64
import numpy as np
import sqlite3
import math
import io
import json
from pandas.io.json import json_normalize
import time
from datetime import datetime
from datetime import timedelta, date


from waitress import serve
from dash_extensions import Download
from dash_extensions.snippets import send_data_frame
# =============================================================================
# Dash App and Flask Server
# =============================================================================

them = 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css'
app = dash.Dash(__name__,meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.config.suppress_callback_exceptions = True
server = app.server


# =============================================================================
# Data
# =============================================================================





# =============================================================================
# Plan your meal
# =============================================================================

cards_plan_meal = dac.TabItem(id='plan_your_meal',active=True, style={'display':'block'},
                              children=[
                                  html.Div([
                                    #   dbc.Row([
                                    #      dbc.Col([
                                    #                     dcc.Loading(dac.InfoBox(id='1',
                                    #                                 title = "Fruits",
                                    #                                 style= {'fontSize':18,'width':'700px'},
                                    #                                 color='success',
                                    #                                 icon = "lemon"
                                    #                                 )),   
                                    #               ],md=4),
                                    #      dbc.Col([
                                    #                     dcc.Loading(dac.InfoBox(id='2',
                                    #                                 title = "Fruits",
                                    #                                 style= {'fontSize':18,'width':'700px'},
                                    #                                 color='success',
                                    #                                 icon = "lemon"
                                    #                                 )),   
                                    #               ],md=4),
                                    #      dbc.Col([
                                    #                     dcc.Loading(dac.InfoBox(id='3',
                                    #                                 title = "Fruits",
                                    #                                 style= {'fontSize':18,'width':'700px'},
                                    #                                 color='success',
                                    #                                 icon = "lemon"
                                    #                                 )),   
                                    #               ],md=4)                                                                                                    
                                    #   ]),
                                    #   html.Br(),
                                    #   dbc.Row([
                                    #      dbc.Col([
                                    #                     dcc.Loading(dac.InfoBox(id='11',
                                    #                                 title = "Fruits",
                                    #                                 style= {'fontSize':18,'width':'700px'},
                                    #                                 color='success',
                                    #                                 icon = "lemon"
                                    #                                 )),   
                                    #               ],md=4),
                                    #      dbc.Col([
                                    #                     dcc.Loading(dac.InfoBox(id='22',
                                    #                                 title = "Fruits",
                                    #                                 style= {'fontSize':18,'width':'700px'},
                                    #                                 color='success',
                                    #                                 icon = "lemon"
                                    #                                 )),   
                                    #               ],md=4),
                                    #      dbc.Col([
                                    #                     dcc.Loading(dac.InfoBox(id='33',
                                    #                                 title = "Fruits",
                                    #                                 style= {'fontSize':18,'width':'700px'},
                                    #                                 color='success',
                                    #                                 icon = "lemon"
                                    #                                 )),   
                                    #               ],md=4)                                                                                                    
                                    #   ]), 
                                html.Br(),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col([
                                              dac.Box([
                                              dac.BoxHeader(title="Fruits",
                                                            style={'background':'bisque','font-family':'garamond',
                                                                   'color':'black'}),    
                                                 dac.BoxBody([ "example"  ])
                                                      ],width=12)
                                    ],md=4),
                                    dbc.Col([
                                              dac.Box([
                                              dac.BoxHeader(title="Vegetables Raw",
                                                            style={'background':'bisque','font-family':'garamond',
                                                                   'color':'black'}),    
                                                 dac.BoxBody([ "example"  ])
                                                      ],width=12)
                                    ],md=4),
                                    dbc.Col([
                                              dac.Box([
                                              dac.BoxHeader(title="Vegetables Cooked",
                                                            style={'background':'bisque','font-family':'garamond',
                                                                   'color':'black'}),    
                                                 dac.BoxBody([ "example"  ])
                                                      ],width=12)
                                    ],md=4)                                                                        
                                        ])                                         

                                  ])
                              ])                                     
                                      




# =============================================================================
# Layout
# =============================================================================



navbar = dac.Navbar(color = "dark grey", 
                    text="Healthy App",
                    skin='dark', 
                    fixed=True)

sidebar = dac.Sidebar(
	dac.SidebarMenu(
		[
			dac.SidebarHeader(children="Nutrition"),
			# dac.SidebarMenuItem(id='need_calculation', label='Calculate your need', icon='chart-bar'),                      
            dac.SidebarMenuItem(id='meal_plan', label='Plan your meal', icon='marker',style={'font-family':'garamond'}),
            # dac.SidebarMenuItem(id='tab_category', label='Category scorecard', icon='box'),
            # dac.SidebarMenuItem(id='tab_supplier', label='Supplier scorecard', icon='dolly'),
            # dac.SidebarMenuItem(id='tab_brand', label='Brand scorecard', icon='tags'),                        
			dac.SidebarHeader(children="Blog"),
			dac.SidebarMenuItem(id='beauty_article', label='Beauty articles', icon='gem'),
			dac.SidebarMenuItem(id='food_article', label='Food articles', icon='shopping-basket'),
			# dac.SidebarHeader(children="Gallery"),
			dac.SidebarMenuItem(id='living_article', label='Lifestyle articles', icon='spa'),  
			dac.SidebarMenuItem(id='sexual_article', label='Sexual relation articles', icon='heart'),                                           
			# dac.SidebarMenuItem(label='Galleries', icon='cubes', children=subitems),
		]
	),
    title='Healthy App',
    style={'fontweight':'bold'},
	skin="dark",
    color='info',
	brand_color="primary",
    # url="https://quantee.ai",
    #src="assets/bahrain_flag.png",
    elevation=3,
    opacity=0.8
)


footer = dac.Footer(
	html.A("©YoKimura",
		href = "https://twitter.com/quanteeai", 
		target = "_blank", 
	),)




body =  dac.Body(
        dac.TabItems([
            cards_plan_meal,
            # cards_store,
            # cards_stock_holding,
            # cards_min_max,
        dac.TabItem(html.P('Gallery 1 (You can add Dash Bootstrap Components!)'), 
                    id='content_gallery_1'),
        dac.TabItem(html.P('Gallery 2 (You can add Dash Bootstrap Components!)'), 
                    id='content_gallery_2'),
        ])
        )

app.title = "Healthy App"
app.layout = dac.Page(id="body_id",children=[navbar, sidebar, body, footer])





# =============================================================================
# App
# =============================================================================

if __name__ == '__main__':
    #app.run_server(debug=False)#,host='10.200.13.38',port='5000')
    app.run_server(debug=True)#,host='10.200.13.38',port='8051')
    # app.run_server(debug=False)
    # serve(app, host='0.0.0.0', port=8000)   
