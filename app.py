import streamlit as st
import pandas as pd
import numpy as np

## Title of the applicationn
## Important components

st.title("Hello Data Science Batch 2")

## Display a simple text
st.write("This is my favourite Class")

## create a simple DataFrame

df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

# Display the Dataframe
st.write("Here is the Dataframe")
st.write(df)

## create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)
