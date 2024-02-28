import streamlit as st
import pandas as pd

st.title("Amateur golf championship")

st.divider()
st.header("Results")

df = pd.read_csv("resultze.csv")

st.dataframe(df)

# manipulation des données : 
new_df = df[['Player','EVENTS_PLAYED','POINTS']]
sort_df = new_df.sort_values(by=['POINTS'])
sort_df['POINTS_PER_EVENT'] = sort_df['POINTS'] / sort_df['EVENTS_PLAYED']
sorted_df = sort_df.sort_values(by=['POINTS_PER_EVENT'])
st.title("Sorted by points per event")
st.dataframe(sorted_df)

st.title("Best players sorted by points")

st.dataframe(sort_df)

st.divider()
st.line_chart(sorted_df, x="Player", y="POINTS_PER_EVENT")