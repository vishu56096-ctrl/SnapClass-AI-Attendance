import streamlit as st

st.set_page_config(layout="wide", page_title="Snap Class", initial_sidebar_state="collapsed")

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen


def main() -> None:
    portal = st.query_params.get("portal")

    match portal:
        case "teacher":
            teacher_screen()
        case "student":
            student_screen()
        case _:
            home_screen()


main()
