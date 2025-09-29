import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.table(dataframe)
