import streamlit as st

from src.ui.base_layout import style_dashboard_layout


def teacher_screen() -> None:
    style_dashboard_layout()
    st.title("Teacher Dashboard")
