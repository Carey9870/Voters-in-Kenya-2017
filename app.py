import streamlit as st
import pandas as pd
import numpy as np
import preprocessor, helper
import plotly.express as px
import openpyxl

voters = pd.read_excel('votersconstituency-2.xlsx')

# load preprocessor.py
voters = preprocessor.preprocess(voters)

# sidebar ui
st.sidebar.title('Voters in Kenya Per 2017 General Election Analysis')

# sidebar components
user_menu = st.sidebar.radio(
    'Select an Option', (
        'Number of Constituencies per County', 'Total Number of Voters per Constituency', 'Number of Polling Stations per Constituencies'
))

if user_menu == 'Number of Constituencies per County':
    st.title('Number of Constituencies per County')
    vpc = helper.VotersPerConstituency(voters)
    st.table(vpc)
    
    # a bar graph
    st.subheader('A Bar Graph showing Number of Constituencies per County')
    fig = px.bar(voters.COUNTY_NAME.value_counts(), color_discrete_sequence=['#771933'])
    st.plotly_chart(fig)
    
    # violin plot
    st.subheader('A violin plot showing Number of Constituencies per County')
    fig = px.violin(voters, y=voters.COUNTY_NAME.value_counts(), box=True, points='all', color_discrete_sequence=['yellowgreen'])
    st.plotly_chart(fig)

if user_menu == 'Total Number of Voters per Constituency':
    cnv = voters.groupby('CONSTITUENCY_NAME')[['VOTERS']].sum().reset_index()
    st.table(cnv)
    
    # line Graph
    st.subheader("Bar Graph")
    fig = px.line(voters, y='VOTERS', x='CONSTITUENCY_NAME', color_discrete_sequence=['red'])
    st.plotly_chart(fig)
    
    # density heatmap
    st.subheader('Density Heatmap')
    fig = px.density_heatmap(voters, y='VOTERS', x='CONSTITUENCY_NAME', z='COUNTY_CODE', color_continuous_scale='viridis')
    st.plotly_chart(fig)

if user_menu == 'Number of Polling Stations per Constituencies':
    vpx = voters.groupby(['COUNTY_NAME','CONSTITUENCY_NAME'])['NO. OF POLLING STATIONS'].sum().reset_index()
    st.table(vpx)
    
    fig = px.line(voters, x='CONSTITUENCY_NAME', y='NO. OF POLLING STATIONS', color_discrete_sequence=['yellow'])
    st.plotly_chart(fig)