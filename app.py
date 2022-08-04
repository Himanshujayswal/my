# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 01:50:20 2022

@author: antony.vibin
"""

#Smiley
#https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md


#!pip install flair

import streamlit as st
import pandas as pd # pip install pandas
#from matplotlib import pyplot as plt # pip install matplotlib
#import time

### Defining List
lst_chk = ["Name entity recognition(NER)","Medical Text Entity Recognition","Sentiment analysis","Question answering"]

sent_lst = ["Doctor in OHIO helped the covid patients to recover quickly"
"The patient has committed suicide due to high stress",
"Indian Research scientist found covaxin and saved all people",
"Students are affected with covid and are expected to die soon",
"Having high fever and not able to wake up"]

st.set_page_config(page_title="My WebPage", page_icon=":hugs:")



hom =st.sidebar.radio("Text Predictions",["Home","Text Prediction Models","Feedback"])


### Main Code
if hom == "Home":
    colm1 , colm2, colm3, colm4, colm5 = st.columns(5)
    with colm5:
        st.image("data//gavs_logo_v1.png", width = 100)
        
    col1 , col2 = st.columns([1,3])
    with col2:
        st.title("_OLIVE THE BOT_")
    #with col3:
        #st.write("[Gavs](https://www.gavstech.com/)")
    st.caption("")
    st.video("https://www.youtube.com/watch?v=_io1BzRwdWc")


if hom == "Text Prediction Models":
    st.sidebar.caption("")
    rad =st.sidebar.radio("Text Prediction Model",lst_chk)
        
    if rad == "Name entity recognition(NER)":
        st.write("Name entity recognition(NER)")
        
    if rad == "Sentiment analysis":
        st.write("Sentiment analysis") 

    if rad == "Medical Text Entity Recognition":
        st.write("Text generation")
        
    if rad == "Question answering":
        st.write("Question answering")
        

        
if hom == "Feedback":
    col3 , col4 = st.columns([1,4])
    with col4:
        st.subheader("Do let us know your Feedback :sunglasses:")

    st.caption("")
    name = st.text_input("Enter your Name")
    feedback = st.text_area("Enter your Feedback")
    if st.button("Submit"):
        to_add = {"Name":[name],"Feedback":[feedback]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data//feedback.csv",mode='a',header = False,index= False)
        st.success("Submitted")
        st.caption("")
    
    col5 , col6 = st.columns([1,4])
    with col6:
        st.caption("")
        if st.checkbox("View Previous Feedback"): 
            fb_csv = pd.read_csv("data//Feedback.csv")
            st.table(fb_csv)