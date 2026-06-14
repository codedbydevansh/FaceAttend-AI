import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard , style_base_layout 
from src.components.footer import footer_dashboard

def teacher_screen():

    style_background_dashboard()
    style_base_layout()

    teacher_screen_login()



def teacher_screen_login():

    c1 , c2 = st.columns(2 , vertical_alignment='center' , gap='xxlarge')

    with c1:
        header_dashboard()

    with c2:
        if st.button('Go to back to Home', type='secondary' , key='loginbackbtn' , shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.rerun()

    st.header('Login using Password' , text_alignment='center')

    st.space()
    st.space()
    teacher_username = st.text_input("Enter username" , placeholder="username")
    teacher_pass = st.text_input("Enter Password" , type='password',placeholder="Password")

    btn1 , btn2 = st.columns(2)

    with btn1:
        st.button('Login' ,type="primary" ,icon=":material/passkey:" , shortcut="control+enter" , width='stretch')

    with btn2:
        st.button('Register Instead' , type="secondary" , icon=":material/passkey:" , width='stretch')

    footer_dashboard()


def teacher_screen_register():

    c1 , c2 = st.columns(2 , vertical_alignment='center' , gap='xxlarge')

    with c1:
        header_dashboard()

    with c2:
        if st.button('Go to back to Home', type='secondary' , key='loginbackbtn' , shortcut="control+backspace"):
            st.session_state['login_type']=None
            st.rerun()

    st.header('Register your teacher Profile')

    st.space()
    st.space()
    teacher_username = st.text_input("Enter username" , placeholder="username")
    teacher_pass = st.text_input("Enter Password" , type='password',placeholder="Password")

    btn1 , btn2 = st.columns(2)

    with btn1:
        st.button('Login' ,type="primary" ,icon=":material/passkey:" , shortcut="control+enter" , width='stretch')

    with btn2:
        st.button('Register Instead' , type="secondary" , icon=":material/passkey:" , width='stretch')

    footer_dashboard()

    