from bs4 import BeautifulSoup
import requests
import streamlit as st
import pandas as pd

link = '[GitHub](http://github.com)'
st.markdown(link, unsafe_allow_html=True)


df = pd.DataFrame.from_dict({'link': '<a href="https://www.google.com" id="ggl"> Google </a>', 'id': [1]})
st.write(df.to_html(escape=False, index=False, show_dimensions=True), unsafe_allow_html=True)