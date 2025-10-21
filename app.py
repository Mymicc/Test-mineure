import streamlit as st
import pandas as pd
st.header("mon application")

nombre = [1, 2, 4, 7]
carré = [1**2, 2**2, 4**2, 7**2]

d = {"nombres": nombre, "carré": carré}
data = pd.DataFrame(d)

st.dataframe(data)
