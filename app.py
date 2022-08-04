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
lst_chk = ["PHI Masking","Disease & Drug Extraction","Question Answering"]

sent_lst = ["Doctor in OHIO helped the covid patients to recover quickly"
"The patient has committed suicide due to high stress",
"Indian Research scientist found covaxin and saved all people",
"Students are affected with covid and are expected to die soon",
"Having high fever and not able to wake up"]

st.set_page_config(page_title="My WebPage", page_icon=":hugs:")



hom =st.sidebar.radio("Text Predictions",["Home","Text Prediction Models","Feedback"])


### Main Code
if hom == "Home":
    #colm1 , colm2, colm3, colm4, colm5 = st.columns(5)
    #with colm5:
    #    st.image("data//Goofy.jpg", width = 100)
        
    col1 , col2 = st.columns([1,3])
    with col2:
        st.title("GOOFY THE ASSIST :male-doctor:")
        # :male-doctor:,  :person_doing_cartwheel:
    #with col3:
        #st.write("[Gavs](https://www.gavstech.com/)")
    st.caption("")
    st.video("https://www.youtube.com/watch?v=_io1BzRwdWc")


if hom == "Text Prediction Models":
    st.sidebar.caption("")
    rad =st.sidebar.radio("Text Prediction Model",lst_chk)

##### PHI Masking        
    if rad == "PHI Masking":
        
        phi_masking_input = ["SURGICAL KIT PROCEDURE COVER FOR HENRY FORD HEALTH SYSTEMS",
"PACK SURGICAL PROCEDURE CUSTOM OPERATING ROOM VASCULAR F/ALLEGIANCE HEALTH HOSPITAL",
"BIT SECURESPAN DRILL BIT F/DR.GUIDE FG868R",
"PACK SURGICAL PROCEDURE NASAL LATEX-FREE AIS 252 SAN JOAQUIN COMM HOSPITAL",
"PACK SURGICALPROCEDURE TOTAL HIP REPLACEMENT F/UHHS RICHMOND HEIGHT HOSPITAL"]
        
        st.header("PHI Masking")
        
        sb1 = st.radio("Choose Data",["Choose From Sample","Upload Data"],index = 0)
        
        if sb1 == "Choose From Sample": 
            sb2 = st.selectbox("Select Input Data",phi_masking_input,index = 0)
            ip_txt = sb2
            if st.button("Clear"):
                ip_txt = ""
            txt_input1 = st.text_area("Your text input is ",ip_txt)            
            if st.button("Submit"):
                st.text_area("Output",ip_txt)
                st.success("The output has been generated")
                
            
        if sb1 == "Upload Data":
            img = st.file_uploader("Upload a file")
            if img:
                df = pd.read_excel(img)
                st.table(df)
                if st.button("Submit"):
                    st.table(df)
                    st.success("The output has been generated")


##### Disease & Drug Extraction 
    if rad == "Disease & Drug Extraction":
        phi_masking_input = ["SURGICAL KIT PROCEDURE COVER FOR HENRY FORD HEALTH SYSTEMS",
"PACK SURGICAL PROCEDURE CUSTOM OPERATING ROOM VASCULAR F/ALLEGIANCE HEALTH HOSPITAL",
"BIT SECURESPAN DRILL BIT F/DR.GUIDE FG868R",
"PACK SURGICAL PROCEDURE NASAL LATEX-FREE AIS 252 SAN JOAQUIN COMM HOSPITAL",
"PACK SURGICALPROCEDURE TOTAL HIP REPLACEMENT F/UHHS RICHMOND HEIGHT HOSPITAL"]
        
        st.header("Disease & Drug Extraction")
        
        sb1 = st.radio("Choose Data",["Choose From Sample","Upload Data"],index = 0)
        
        if sb1 == "Choose From Sample": 
            sb2 = st.selectbox("Select Input Data",phi_masking_input,index = 0)
            ip_txt = sb2
            if st.button("Clear"):
                ip_txt = ""
            txt_input1 = st.text_area("Your text input is ",ip_txt)            
            if st.button("Submit"):
                st.text_area("Output",ip_txt)
                st.success("The output has been generated")
                
            
        if sb1 == "Upload Data":
            img = st.file_uploader("Upload a file")
            if img:
                df = pd.read_excel(img)
                st.table(df)
                if st.button("Submit"):
                    st.table(df)
                    st.success("The output has been generated")

    

##### Question Answering 
    if rad == "Question Answering":
        phi_masking_input = ["SURGICAL KIT PROCEDURE COVER FOR HENRY FORD HEALTH SYSTEMS",
"PACK SURGICAL PROCEDURE CUSTOM OPERATING ROOM VASCULAR F/ALLEGIANCE HEALTH HOSPITAL",
"BIT SECURESPAN DRILL BIT F/DR.GUIDE FG868R",
"PACK SURGICAL PROCEDURE NASAL LATEX-FREE AIS 252 SAN JOAQUIN COMM HOSPITAL",
"PACK SURGICALPROCEDURE TOTAL HIP REPLACEMENT F/UHHS RICHMOND HEIGHT HOSPITAL"]
        
        st.header("Question Answering")
        
        sb1 = st.radio("Choose Data",["Choose From Sample","Upload Data"],index = 0)
        
        if sb1 == "Choose From Sample": 
            sb2 = st.selectbox("Select Input Data",phi_masking_input,index = 0)
            ip_txt = sb2
            if st.button("Clear"):
                ip_txt = ""
            txt_input1 = st.text_area("Your text input is ",ip_txt)            
            if st.button("Submit"):
                st.text_area("Output",ip_txt)
                st.success("The output has been generated")
                
            
        if sb1 == "Upload Data":
            img = st.file_uploader("Upload a file")
            if img:
                df = pd.read_excel(img)
                st.table(df)
                if st.button("Submit"):
                    st.table(df)
                    st.success("The output has been generated")
        

        
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