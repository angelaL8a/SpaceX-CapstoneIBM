# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                             options=[
                                                 {'label': 'All Sites',
                                                     'value': 'ALL'},
                                                 {'label': 'CCAFS LC-40',
                                                     'value': 'CCAFS LC-40'},
                                                 {'label': 'VAFB SLC-4E',
                                                     'value': 'VAFB SLC-4E'},
                                                 {'label': 'KSC LC-39A',
                                                     'value': 'KSC LC-39A'},
                                                 {'label': 'CCAFS SLC-40',
                                                     'value': 'CCAFS SLC-40'}
                                             ],
                                             ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min=0,
                                                max=10000,
                                                step=1000,
                                                marks={
                                                    0: '0',
                                                    2500: '2500',
                                                    5000: '5000',
                                                    7500: '7500',
                                                    10000: '10000'
                                                },
                                                value=[min_payload, max_payload]),


                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(
                                    dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output


@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(
            filtered_df,
            values='class',
            names='Launch Site',
            title='Success Count for All Launch Sites',
            color_discrete_sequence=px.colors.sequential.Agsunset_r,  # Better color scheme
            hole=0.3  # Donut style for a modern look
        )
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(
            filtered_df,
            names='class',
            title=f'Success Count for Site {entered_site}',
            # Distinct color scheme for individual sites
            color_discrete_sequence=px.colors.sequential.Agsunset_r,
            hole=0.3  # Donut style for consistency
        )

    # Customize layout for better styling
    fig.update_traces(textinfo='percent',
                      pull=[0.05, 0], marker=dict(line=dict(color='#000000', width=2)))
    fig.update_layout(
        title_font_size=20,
        title_font_color='gray',
        annotations=[dict(text='Launches', x=0.5, y=0.5,
                          font_size=15, showarrow=False)],  # Custom center text
        legend_title_text='Launch Outcome',
        legend_title_font=dict(size=12, color='black'),
        legend_font=dict(size=10, color='black'),
        paper_bgcolor='whitesmoke',  # Improved background color
    )

    return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


@app.callback(
    Output(component_id='success-payload-scatter-chart',
           component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_chart(entered_site, payload_range):
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
        (spacex_df['Payload Mass (kg)'] <= payload_range[1])
    ]

    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]

    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category',
                     size=[10]*len(filtered_df),
                     title=f'Payload Success Rate for site {entered_site} from {
                         payload_range[0]} kg to {payload_range[1]} kg'
                     if entered_site != 'ALL' else
                     f'Payload Success Rate for All Sites from {
                         payload_range[0]} kg to {payload_range[1]} kg',
                     labels={'class': 'Success/Failure'}
                     )

    fig.update_layout(
        title_font_size=20,  # Larger title font
        xaxis_title="Payload Mass (kg)",
        yaxis_title="Launch Outcome (0 = Failure, 1 = Success)",
        font=dict(
            size=12  # Overall font size for labels and axes
        ),
        showlegend=True
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server()
