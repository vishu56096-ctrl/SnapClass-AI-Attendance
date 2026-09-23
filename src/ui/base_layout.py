import streamlit as st


def style_base_layout(background_color: str) -> None:
    st.html(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Lilita+One&family=Outfit:wght@400;500;600;700&display=swap');

            #MainMenu, footer, header, [data-testid="stHeader"],
            [data-testid="stToolbar"], [data-testid="stStatusWidget"],
            [data-testid="stAppDeployButton"],
            [data-testid="stHeaderActionElements"] {{
                display: none !important;
            }}

            [data-testid="stAppViewContainer"], [data-testid="stMain"],
            [data-testid="stApp"] {{
                background-color: {background_color};
            }}

            .block-container {{
                max-width: none !important;
                min-height: 100vh;
                padding: 0 !important;
            }}

            [data-testid="stVerticalBlock"] {{
                gap: 0 !important;
            }}

            [data-testid="stMarkdownContainer"] p {{
                margin: 0;
            }}

            .home-page {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                padding: 1.5rem 1rem 1.25rem;
                box-sizing: border-box;
            }}

            .home-title {{
                margin: 0 !important;
                color: #ffffff !important;
                font-family: 'Lilita One', 'Arial Black', Impact, sans-serif !important;
                font-size: clamp(3.8rem, 7.2vw, 5.8rem) !important;
                font-weight: 400 !important;
                letter-spacing: 0.06em !important;
                line-height: 0.86 !important;
                text-align: center !important;
                text-transform: uppercase !important;
            }}

            .home-logo {{
                display: flex;
                align-items: center;
                justify-content: center;
                width: 5.6rem;
                height: 5.6rem;
                margin: 0 auto 1.15rem;
                filter: drop-shadow(0 5px 0 rgba(28, 34, 56, 0.18));
            }}

            .home-logo svg {{
                width: 100%;
                height: 100%;
                display: block;
            }}

            .portal-row {{
                display: flex;
                justify-content: center;
                gap: 1.15rem;
                width: min(42rem, 92vw);
                margin: 1.7rem auto 0;
            }}

            .portal-card {{
                flex: 1;
                display: flex;
                flex-direction: column;
                min-height: 17.8rem;
                padding: 1.45rem 1.5rem 1.2rem;
                border-radius: 2.4rem;
                background: #eceeff;
                box-sizing: border-box;
                color: #22283a;
                text-align: left;
            }}

            .portal-heading {{
                margin: 0 !important;
                color: #1f2437 !important;
                font-family: 'Lilita One', 'Arial Black', Impact, sans-serif !important;
                font-size: clamp(2.15rem, 3.6vw, 2.85rem) !important;
                font-weight: 400 !important;
                letter-spacing: 0.01em !important;
                line-height: 0.88 !important;
            }}

            .portal-icon {{
                display: flex;
                align-items: center;
                justify-content: center;
                height: 8.6rem;
                margin: 0.2rem 0 0.55rem;
            }}

            .portal-icon svg {{
                width: 9.5rem;
                height: auto;
                display: block;
            }}

            .portal-button {{
                display: block;
                width: fit-content;
                margin: auto auto 0;
                padding: 0.72rem 1.25rem;
                border-radius: 999px;
                background: {background_color};
                color: #ffffff !important;
                font-family: 'Outfit', sans-serif;
                font-size: 0.92rem;
                font-weight: 600;
                text-decoration: none !important;
            }}

            .portal-button:hover {{
                filter: brightness(0.94);
                color: #ffffff !important;
            }}

            .credit {{
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.45rem;
                margin: 1.35rem 0 0;
                color: #ffffff;
                font-family: 'Outfit', sans-serif;
                font-size: 0.78rem;
                font-weight: 600;
                text-align: center;
            }}

            .apna-logo {{
                display: inline-block;
                color: #ff8a1f;
                font-family: 'Lilita One', sans-serif;
                font-size: 0.78rem;
                letter-spacing: 0.04em;
                line-height: 0.9;
                text-align: left;
            }}

            @media (max-width: 700px) {{
                .portal-row {{
                    flex-direction: column;
                    align-items: center;
                    margin-top: 1.8rem;
                }}

                .portal-card {{
                    width: min(22rem, 88vw);
                }}
            }}
        </style>
        """,
    )


def style_home_layout() -> None:
    style_base_layout("#5f6bff")


def style_dashboard_layout() -> None:
    style_base_layout("#e0e3ff")
