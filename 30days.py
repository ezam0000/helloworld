#30 days of streamlit

# import streamlit as st

# st.header('st.button')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

#example 1 
st.write('Hello, *My fellow americans* :sunglasses:')
#example 2
st.write(1234)
# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

#Slider

from datetime import time, datetime

st.header('st.slider')

#slider 1
st.subheader('Slider')

age = st.slider('How old are you ?', 0, 130, 25)

st.write("I'm", age, 'years old')

#slider 2
st.subheader('Range Slider')

values = st.slider(
    'Select range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values: ', values)

#slider 3

st.subheader('Range time slider')

appointment =  st.slider(
    "Schedule your appointment: ",
    value = (time(11,30), time(12,45)))
st.write("You're scheduled for: ", appointment)

#slider 4

st.subheader('Date Slider')

start_time = st.slider(
    "When do you start?",
    value = datetime(2020, 1, 1, 9, 30),
    format = 'MM/DD/YY - hh:mm')
st.write("Start time: ", start_time)

# DAy 9

st.subheader('Day 9')

import streamlit as st
import pandas as pd
import numpy as np

st.subheader('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Day 10

st.header('Select Box')

option = st.selectbox(
    "What's your favorite color",
    ('Blue', 'Red', 'Green'))

st.write('Your favorite color is', option)

#Day 11

st.header('Multi Select')

options = st.multiselect(
    'What are your favorite colors?',
    ['Green', 'Yellow', 'Red', 'Blue'], 
    ['Yellow', 'Red'])

st.write ('You selected', option)

#Day 12 

st.header('Checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

#Day 13
import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`Streamlit pandas profiling')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)