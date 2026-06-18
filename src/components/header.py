import streamlit as st
from PIL import Image


def header_home():

    logo_url = "https://thumbs.dreamstime.com/z/digital-human-face-rendered-network-connected-blue-dots-dark-background-452962244.jpg?ct=jpeg"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url ="https://thumbs.dreamstime.com/z/digital-human-face-rendered-network-connected-blue-dots-dark-background-452962244.jpg?ct=jpeg"
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>FaceTrack<br/> AI</h1>
        </div>   
                
                """, unsafe_allow_html=True)