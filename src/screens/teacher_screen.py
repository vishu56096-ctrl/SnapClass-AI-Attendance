
import streamlit as st

from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.database.db import check_teacher_exists, create_teacher, teacher_login, get_teacher_subjects,get_attendance_for_teacher
from src.components.subject_card import subject_card
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog
from src.pipelines.face_pipline import predict_attendance
import numpy as np
from datetime import datetime
import pandas as pd
from src.database.config import supabase
from src.components.dialog_attendance_results import attendance_result_dialog
from src.components.dialog_voice_attendance import voice_attendance_dialog




def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()

def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    column_left, column_right = st.columns(
            2,
            vertical_alignment="center",
            gap="large",
        )
    
    with column_left:
            header_dashboard()
    
    with column_right:
            st.subheader(f"""
                    Welcome, {teacher_data['name']}
            """)
            if st.button(
                "Logout",
                type="secondary",
                key="teacher_login_back",
            ):
                st.session_state['is_logged_in'] = False
                st.session_state["teacher_login_type"] = "login"
                del st.session_state.teacher_data
                st.rerun()

    st.space()
    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    tab1, tab2, tab3 = st.columns(3) 

    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendance' else "tertiary"
        if st.button('Take Attendance',type=type1,width='stretch', icon=':material/ar_on_you:'):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
            type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
            if st.button('Manage Subjects',type=type2,width='stretch', icon=':material/book_ribbon:'):
                st.session_state.current_teacher_tab = 'manage_subjects'
                st.rerun()

    with tab3:
            type3 = "primary" if st.session_state.current_teacher_tab == 'attendance_records' else "tertiary"
            if st.button('Attendance Records',type=type3,width='stretch', icon=':material/assignment:'):
                st.session_state.current_teacher_tab = 'attendance_records'
                st.rerun() 
    st.divider()                              
                      
    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()
    if st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records()

def teacher_tab_take_attendance():
    teacher_id = st.session_state.teacher_data['teacher_id']
    st.header('Take AI Attendance')   
    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []
    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning('You havent created any subjects yet! Plwase create one to begin!')
        return
    subject_options = {f"{s['name']}-{s['subject_code']}": s['subject_id'] for s in subjects}

    col1, col2 = st.columns([3,1], vertical_alignment='bottom')
    with col1:
        selected_subject_label = st.selectbox('Select Subject', options=list(subject_options.keys()))
    selected_subject_id = subject_options[selected_subject_label]

    st.divider()

    has_photos = bool(st.session_state.attendance_images)
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button('Use Voice Attendance', type='primary', width='stretch', icon=':material/mic:'):
            voice_attendance_dialog(selected_subject_id)

    with c2:
        if st.button('Add Photos', type='primary', icon=':material/photo_prints:', width='stretch'):
            add_photos_dialog()

    with c3:
        if st.button('Clear all photos', width='stretch', type='tertiary', icon=':material/delete:', disabled=not has_photos):
            st.session_state.attendance_images = []
            st.rerun()

    if st.session_state.attendance_images:
        st.header('Add Photos')
        gallery_cols = st.columns(4)

        for idx,img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img,width='stretch', caption=f'Photo{idx+1}')
        if st.button('Run Face Analysis', width='stretch', type='secondary', icon=':material/analytics:'):
            with st.spinner('Deep scanning classroom photos...'):
                all_detected_ids ={}

                for idx, img in enumerate(st.session_state.attendance_images):
                    img_np = np.array(img.convert('RGB'))
                    detected, _, _= predict_attendance(img_np)

                    if detected:
                        for sid in detected.keys():
                            student_id = int(sid)
                            all_detected_ids.setdefault(student_id, []).append(f"Photo{idx+1}")
                enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id',selected_subject_id).execute()
                enrolled_students = enrolled_res.data

                if not enrolled_students:
                    st.warning('No students in this course')
                    return
                else:
                    results, attendance_to_log = [],[]
                    current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                    for node in enrolled_students:
                        student = node['students']
                        sources = all_detected_ids.get(int(student['student_id']), [])
                        is_present = len(sources)>0

                        results.append({
                            "Name" : student['name'],
                            "ID" : student['student_id'],
                            "Source" : ", ".join(sources) if is_present else "_",
                            "Status": "✅ Present" if is_present else "❌ Absent"
                        })
                        attendance_to_log.append({
                            'student_id': student['student_id'],
                            'subject_id':selected_subject_id,
                            'timestamp':current_timestamp,
                            'is_present':bool(is_present)
                        })
                attendance_result_dialog(pd.DataFrame(results), attendance_to_log)











def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data['teacher_id']
    col1, col2 = st.columns(2)
    with col1:
        st.header('Manage Subject', width='stretch')

    with col2:
        if st.button('Create New Subject', width='stretch'):
            create_subject_dialog(teacher_id)

    # list all subjects
    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("🧑‍🏫", "Students", sub["total_students"]),
                ("⏱️", "Classes", sub['total_classes']),
            ]
            def share_btn():
                if st.button(f"Share Code:{sub['name']}", key=f"share_{sub['subject_code']}", icon=":material/share:"):
                    share_subject_dialog(sub['name'], sub['subject_code'])
                st.space()

            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=stats,
                footer_callback=share_btn
            )
    else:
        st.info("NO SUBJECTS FOUND, CREATE ONE ABOVE")          


        
      
def teacher_tab_attendance_records():
    st.header('Attendance Records') 
    teacher_id = st.session_state.teacher_data['teacher_id']
    records = get_attendance_for_teacher(teacher_id)
    if not records:
        st.info('No attendance records found.')
        return
    data = []

    for r in records:
        ts = r.get('timestamp')

        data.append({
            "ts_group": ts,
            "Time": datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N'A",
            "Subject": r['subjects']['name'],
            "Subject Code": r['subjects']['subject_code'],
            "is_present":bool(r.get('is_present', False))
        })

    df = pd.DataFrame(data) 

    summary = (
        df.groupby(['ts_group', 'Time', 'Subject','Subject Code'])
        .agg(
            Present_Count = ('is_present', 'sum'),
            Total_Count = ('is_present', 'count')
        ).reset_index()
    ) 

    summary['Attendance Stats'] = (
        "✅" + summary['Present_Count'].astype(str) + "/" + summary['Total_Count'].astype(str) + ' students'    )  
    display_df = (summary.sort_values(by='ts_group', ascending=False)
                  [['Time','Subject', 'Subject Code','Attendance Stats' ]]
                  )

    st.dataframe(display_df, width='stretch', hide_index=True)
    



def login_teacher(username,password):
    if not username or not password:
        return False
    teacher =teacher_login(username, password)

    if teacher:
        st.session_state.user_role='teacher'
        st.session_state.teacher_data=teacher 
        st.session_state.is_logged_in=True
        return True
    return False

def teacher_screen_login():
    column_left, column_right = st.columns(
        2,
        vertical_alignment="center",
        gap="large",
    )

    with column_left:
        header_dashboard()

    with column_right:
        if st.button(
            "Go back to Home",
            type="secondary",
            key="teacher_login_back",
        ):
            st.session_state["login_type"] = None
            st.session_state["teacher_login_type"] = "login"
            st.rerun()

    st.header("Login using password")
    if "teacher_message" in st.session_state:
        st.success(st.session_state.pop("teacher_message"))
    st.space()
    st.space()

    teacher_username = st.text_input("Enter username", placeholder="username")
    teacher_pass = st.text_input("Enter Password", type="password", placeholder="Enter password")
    st.divider()

    login_column, register_column = st.columns(2)

    with login_column:
        if st.button("Login", icon=":material/passkey:", width="stretch"):
            if login_teacher(teacher_username, teacher_pass):
                st.toast(f"Welcome back!")
                import time
                time.sleep(1)
                st.rerun()
            else:
                 st.error("Invalid username and password")
            

    with register_column:
        if st.button("Register", type="primary", icon=":material/passkey:", width="stretch"):
            st.session_state["teacher_login_type"] = "register"
            st.rerun()

def register_teacher(teacher_username, teacher_name, teacher_pass,teacher_pass_confirm):
    teacher_username = teacher_username.strip()
    teacher_name = teacher_name.strip()
    missing = []
    if not teacher_username:
        missing.append("username")
    if not teacher_name:
        missing.append("name")
    if not teacher_pass:
        missing.append("password")
    if not teacher_pass_confirm:
        missing.append("password confirmation")
    if missing:
        return False, "Please fill in: " + ", ".join(missing) + "."
    if teacher_pass != teacher_pass_confirm:
        return False , "Password doesn't match"
    try:
       if check_teacher_exists(teacher_username):
           return False, "Username already taken"
       create_teacher(teacher_username, teacher_pass, teacher_name)
       return True, "Successfully created! Login now"
    except Exception as e:
        return False, f"Registration failed because of a database error: {e}"
def teacher_screen_register():
    column_left, column_right = st.columns(
        2,
        vertical_alignment="center",
        gap="large",
    )

    with column_left:
        header_dashboard()

    with column_right:
        if st.button(
            "Go back to Home",
            type="secondary",
            key="teacher_register_back",
        ):
            st.session_state["login_type"] = None
            st.session_state["teacher_login_type"] = "login"
            st.rerun()

    st.header("Register your teacher profile")
    st.space()
    st.space()

    with st.form("teacher_registration_form"):
        teacher_username = st.text_input("Enter username", placeholder="username")
        teacher_name = st.text_input("Enter name", placeholder="Your name")
        teacher_pass = st.text_input("Enter Password", type="password", placeholder="Enter password")
        teacher_pass_confirm = st.text_input("Confirm your Password", type="password", placeholder="Enter password")
        st.divider()
        register = st.form_submit_button("Register now", icon=":material/passkey:", width="stretch", type="primary")

    if register:
        success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
        if success:
            st.session_state["teacher_message"] = message
            st.session_state["teacher_login_type"] = "login"
            st.rerun()
        else:
            st.error(message)

    if st.button("Login", icon=":material/passkey:", width="stretch", key="teacher_register_login"):
        st.session_state.teacher_login_type = "login"
        st.rerun()
