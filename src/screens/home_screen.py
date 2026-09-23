import streamlit as st

from src.ui.base_layout import style_home_layout


def home_screen() -> None:
    style_home_layout()
    st.markdown(
        """
        <div class="home-page">
            <div class="home-logo" aria-hidden="true">
                <svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
                    <rect x="3" y="3" width="74" height="74" rx="18" fill="#ffeb00" stroke="#1c2238" stroke-width="4"/>
                    <path d="M22 28.5 L40 20.5 L58 28.5 L40 36.5 Z" fill="#fff"/>
                    <rect x="36.2" y="28.5" width="7.6" height="5.2" fill="#fff"/>
                    <circle cx="58" cy="30.5" r="2.1" fill="#fff"/>
                    <circle cx="40" cy="48.5" r="10.5" fill="#fff"/>
                    <path d="M22 70 C24 58 32 54 40 54 C48 54 56 58 58 70 Z" fill="#fff"/>
                </svg>
            </div>
            <div class="home-title">SNAP<br>CLASS</div>
            <div class="portal-row">
                <div class="portal-card">
                    <div class="portal-heading">I'm<br>Student</div>
                    <div class="portal-icon">
                        <svg viewBox="0 0 180 150" xmlns="http://www.w3.org/2000/svg">
                            <ellipse cx="90" cy="142" rx="42" ry="6" fill="#d7dbf5"/>
                            <path d="M58 128 C62 96 74 86 90 86 C106 86 118 96 122 128 Z" fill="#1d3568"/>
                            <path d="M72 96 C78 90 102 90 108 96 L108 118 C102 112 78 112 72 118 Z" fill="#f4f6ff"/>
                            <rect x="84" y="96" width="12" height="24" fill="#1d3568"/>
                            <circle cx="90" cy="62" r="24" fill="#f3c7a8"/>
                            <path d="M68 58 C70 34 84 28 90 28 C100 28 114 36 114 56 C108 46 96 44 90 44 C80 44 72 50 68 58 Z" fill="#6ec8c4"/>
                            <path d="M66 62 C64 48 72 40 78 42" fill="none" stroke="#6ec8c4" stroke-width="8" stroke-linecap="round"/>
                            <path d="M114 62 C116 48 108 40 102 42" fill="none" stroke="#6ec8c4" stroke-width="8" stroke-linecap="round"/>
                            <path d="M80 68 Q90 74 100 68" fill="none" stroke="#2a3148" stroke-width="2.4" stroke-linecap="round"/>
                            <circle cx="82" cy="60" r="2.4" fill="#2a3148"/>
                            <circle cx="98" cy="60" r="2.4" fill="#2a3148"/>
                            <rect x="108" y="98" width="28" height="20" rx="3" fill="#3a4fa0" transform="rotate(-12 122 108)"/>
                            <rect x="111" y="101" width="22" height="14" rx="2" fill="#f7f8ff" transform="rotate(-12 122 108)"/>
                            <path d="M118 128 C128 110 142 108 150 116" fill="none" stroke="#f3c7a8" stroke-width="8" stroke-linecap="round"/>
                        </svg>
                    </div>
                    <a class="portal-button" href="?portal=student" target="_self">Student Portal ↗</a>
                </div>
                <div class="portal-card">
                    <div class="portal-heading">I'm<br>Teacher</div>
                    <div class="portal-icon">
                        <svg viewBox="0 0 180 150" xmlns="http://www.w3.org/2000/svg">
                            <ellipse cx="90" cy="142" rx="42" ry="6" fill="#d7dbf5"/>
                            <path d="M58 128 C62 96 74 86 90 86 C106 86 118 96 122 128 Z" fill="#e25b3a"/>
                            <path d="M72 96 C78 90 102 90 108 96 L108 118 C102 112 78 112 72 118 Z" fill="#f4f6ff"/>
                            <rect x="84" y="96" width="12" height="24" fill="#e25b3a"/>
                            <circle cx="90" cy="62" r="24" fill="#f3c7a8"/>
                            <path d="M68 58 C70 34 84 28 90 28 C100 28 114 36 114 56 C108 46 96 44 90 44 C80 44 72 50 68 58 Z" fill="#6ec8c4"/>
                            <path d="M66 62 C64 48 72 40 78 42" fill="none" stroke="#6ec8c4" stroke-width="8" stroke-linecap="round"/>
                            <path d="M114 62 C116 48 108 40 102 42" fill="none" stroke="#6ec8c4" stroke-width="8" stroke-linecap="round"/>
                            <path d="M80 68 Q90 74 100 68" fill="none" stroke="#2a3148" stroke-width="2.4" stroke-linecap="round"/>
                            <circle cx="82" cy="60" r="2.4" fill="#2a3148"/>
                            <circle cx="98" cy="60" r="2.4" fill="#2a3148"/>
                            <circle cx="132" cy="92" r="16" fill="none" stroke="#3a3f55" stroke-width="6"/>
                            <path d="M144 104 L158 122" stroke="#3a3f55" stroke-width="6" stroke-linecap="round"/>
                            <path d="M30 118 C42 104 58 100 70 108" fill="none" stroke="#f3c7a8" stroke-width="8" stroke-linecap="round"/>
                        </svg>
                    </div>
                    <a class="portal-button" href="?portal=teacher" target="_self">Teacher Portal ↗</a>
                </div>
            </div>
           
        """,
        unsafe_allow_html=True,
    )
    st.html(
        """
        <script>
            document.querySelectorAll("a.portal-button").forEach((link) => {
                link.setAttribute("target", "_self");
                link.removeAttribute("rel");
            });
        </script>
        """
    )
