#IMPORTANT IMPORTS
import streamlit as st
import numpy as np
import pandas as pd
import streamlit.components.v1 as components
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
#TITLE
st.title("WELCOME TO  AUTO ANALYSIS APP")
st.subheader("Made by Aditya Bhatt")
#IMAGE
st.image(
            "https://cdn.pixabay.com/photo/2016/06/03/13/57/digital-marketing-1433427_960_720.jpg",
            width=700,
 )
#FILE UPLOADER
spectra = st.file_uploader("upload file", type={"csv"})
btn=st.button("Click here to get the EDA REPORT")
btn1=st.button("Click here for summary statistics")
if btn:
    if spectra is not None:
        def load_csv():
            csv = pd.read_csv(spectra)
            return csv
        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st_profile_report(pr)
if btn1:
    def load_csv():
        csv = pd.read_csv(spectra)
        return csv
    df = load_csv()
    z=pd.DataFrame(df.describe())
    st.table(z)






