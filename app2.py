# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 02:02:25 2022

@author: antony.vibin
"""

import streamlit as st
import pandas as pd 
import pickle
import flair
from flair.data import Sentence
from flair.models import SequenceTagger
import regex as re

#### Defining Functions

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
        
    col1 , col2 = st.columns([0.8,3])
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
        
        phi_masking_input = ["DR. RAMANUJAM FROM AMAR LEELA HOSPITALS, HYDERABAD REQUIRES A PACK OF SURGICAL PROCEDURE COVER",
"POLYDIOXANONE MONOFILAMENT SUTURE PRESCRIBED PATIENT NAME PHILIPS ADMITTED AT APEX HOSPITALS, JAIPUR",
"SURGICAL KIT PACKED DELIVERED TO ASIAN HEART INSTITUTE ON 12/11/21",
"FORMER PRESIDENT OF INDIA ZAKIR HUSAIN ADMITTED AT CITY HOSPITAL, DELHI DATED 03-MAY-1969",
"HOSPITAL RELATED QUERIES CAN BE SENT TO CHORDHOSP@GMAIL.COM"]

        tagger = SequenceTagger.load("flair/ner-english-ontonotes-large")
        st.header("PHI Masking")
        
        sb1 = st.radio("Choose Data",["Choose From Sample","Upload Data"],index = 0)
        
        if sb1 == "Choose From Sample": 
            sb2 = st.selectbox("Select Input Data",phi_masking_input,index = 0)
            ip_txt = sb2
            if st.button("Clear"):
                ip_txt = ""
            txt_input1 = st.text_area("Your text input is ",ip_txt)            
            if st.button("Submit"):
##### Hugging Face Model
              lst_org = []
              lst_date = []
              lst_person = []
              lst_gpe = []

              def listToString(s): 
                  str1 = " ; " 
                  return (str1.join(s))

              sentence = Sentence(txt_input1)
              tagger.predict(sentence)

              out_txt = txt_input1
              for entity in sentence.get_spans('ner'):
                str_len = len(str(entity.text)) 
                out_txt = out_txt.replace(str(entity.text), "*"*str_len)
                if entity.tag == "ORG":
                  lst_org.append(entity.text)
                elif entity.tag == "DATE":
                  lst_date.append(entity.text)
                elif entity.tag == "PERSON":
                  lst_person.append(entity.text)
                elif entity.tag == "GPE":
                  lst_gpe.append(entity.text)

              lst_mail = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", txt_input1)

              details = {
                  'TEXT' : txt_input1,
                  'ORG' : listToString(lst_org),
                  'DATE' : listToString(lst_date),
                  'PERSON' : listToString(lst_person),
                  'LOCATION' : listToString(lst_gpe),
                  'MAIL' : listToString(lst_mail),
              }
              phi_df = pd.DataFrame([details])

              st.text_area("Output",out_txt)
              st.table(phi_df)
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
        phi_masking_input = ["DR. RAMANUJAM FROM AMAR LEELA HOSPITALS, HYDERABAD REQUIRES A PACK OF SURGICAL PROCEDURE COVER",
"POLYDIOXANONE MONOFILAMENT SUTURE PRESCRIBED PATIENT NAME PHILIPS ADMITTED AT APEX HOSPITALS, JAIPUR",
"SURGICAL KIT PACKED DELIVERED TO ASIAN HEART INSTITUTE ON 12/11/21",
"FORMER PRESIDENT OF INDIA ZAKIR HUSAIN ADMITTED AT CITY HOSPITAL, DELHI DATED 03-MAY-1969",
"HOSPITAL RELATED QUERIES CAN BE SENT TO CHORDHOSP@GMAIL.COM"]
        
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
