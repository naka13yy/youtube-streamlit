import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0),width=500, height=500)
