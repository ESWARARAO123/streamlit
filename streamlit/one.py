import streamlit as st
import pandas as pd
import numpy as np
st.title("my app")

x=st.text_input("new movie")
st.write(f"hello my favourite movie is {x}")
button=st.button("click")
st.divider()
st.markdown("hello ** world**")
st.text("eswar")
c=pd.DataFrame(np.random.randn(20,3),columns=["a",'b','c'])
st.bar_chart(c)
st.line_chart(c)
st.caption("i am doing the streamlit")
st.link_button("download",url='http://localhost:8501/k')