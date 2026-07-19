import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def plot_pollutant_bar_chart(pollutants_dict):
    df = pd.DataFrame(list(pollutants_dict.items()), columns=['Pollutant', 'Concentration'])
    fig = px.bar(df, x='Pollutant', y='Concentration', 
                 color='Concentration', color_continuous_scale='Reds')
    fig.update_layout(
        title={'text': 'Current Pollutant Levels (µg/m³)', 'font': {'color': '#1E293B'}},
        xaxis={'title': {'font': {'color': '#475569'}}, 'tickfont': {'color': '#475569'}},
        yaxis={'title': {'font': {'color': '#475569'}}, 'tickfont': {'color': '#475569'}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def plot_pollutant_pie_chart(pollutants_dict):
    df = pd.DataFrame(list(pollutants_dict.items()), columns=['Pollutant', 'Concentration'])
    # Filter out 0 values for better visualization
    df = df[df['Concentration'] > 0]
    fig = px.pie(df, values='Concentration', names='Pollutant',
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(
        title={'text': 'Pollutant Distribution', 'font': {'color': '#1E293B'}},
        legend={'font': {'color': '#334155'}},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

def plot_aqi_gauge(predicted_aqi):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = predicted_aqi,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Predicted Tomorrow AQI", 'font': {'color': '#1E293B'}},
        number = {'font': {'color': '#1E293B'}},
        gauge = {
            'axis': {'range': [None, 500], 'tickwidth': 1, 'tickcolor': "#475569", 'tickfont': {'color': '#475569'}},
            'bar': {'color': "rgba(0,0,0,0)"}, # hide the bar
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': "#00E400"},
                {'range': [51, 100], 'color': "#FFFF00"},
                {'range': [101, 200], 'color': "#FF7E00"},
                {'range': [201, 300], 'color': "#FF0000"},
                {'range': [301, 500], 'color': "#8F3F97"}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': predicted_aqi}
        }
    ))
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=50, b=20),
        height=300
    )
    return fig
