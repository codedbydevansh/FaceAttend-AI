import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():

    st.set_page_config(
        page_title='FaceTrack AI - Making Attendance faster using AI',
        page_icon="https://chatgpt.com/backend-api/estuary/content?id=file_000000009e8471fb82074a2e856a3220&ts=494944&p=fs&cid=1&sig=750ac3fe2904f8439d97f12ceff6ce4790a12d34877006448d0d793ba0b91de0&v=0"
    )
    
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case None:
            home_screen()


    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()

        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
            

main()