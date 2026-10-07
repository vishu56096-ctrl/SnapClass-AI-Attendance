import streamlit as st



def style_background_home():
    st.markdown("""
      
        <style>
              
            .stApp{
                  background: #5865F2 !important;
            }
            .stApp div[data-testid="stColumn"]{
                background-color:#E0E3FF !important;
                padding:2.5rem !important;
                border-radius: 5rem !important;

            }
            .stApp div[data-testid="stColumn"] h2{
                color: black !important;
            }

        </style>

                    """
                ,unsafe_allow_html=True)


def style_background_dashboard():
    st.html("""
      
        <style>
              
            .stApp{
                 background:#E0E3FF !important;
            }

            .stApp h2{
                 color: #15152E !important;
            }

            .stApp input{
                 background-color: white !important;
                 color: #15152E !important;
            }

            .stApp input::placeholder{
                 color: #15152E !important;
                 opacity: 1 !important;
            }

            .stApp [data-testid="stWidgetLabel"] p{
                 color: #15152E !important;
            }

        </style>

                    """
        )

    
def style_base_layout():
    st.html("""
      
        <style>
              @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');

             @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap'); 
              
            /*Hide Top bar of streamlit*/
                        #MainMenu, footer, header{
                             visibility : hidden;
                        }
                        .block-container{
                            padding-top:1.5rem !important;
                        }
            h1{
               font-family:'Climate Crisis', sans-serif !important;
               font-size:3rem !important;
               line-height:1.1 !important;
               margin-bottom:0rem !important;
               
            } 

            h2{
                           font-family:'Climate Crisis', sans-serif !important;
                           font-size:2rem !important;
                           line-height:0.9 !important;
                           margin-bottom:0rem !important;
                           

             } 

             h3,h4,p{
                 font-family: 'outfit', sans-serif;
             } 
             button{
                             border-radius: 1.5rem !important;
                             background: #5865F2 !important;
                             color: white !important;
                             padding: 10px 20px !important;
                             border: none !important;
                             transition: transform 0.25s ease-in-out !important;
            }  

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }    

            button[kind="tertiary"]{
                            border-radius: 1.5rem !important;
                            background: black !important;
                            color: white !important;
                            padding: 10px 20px !important;
                            border: none !important;
                            transition: transform 0.25s ease-in-out !important;
             } 

            button:hover{
                 transform:scale(1.05)
            }      

        </style>

                    """
        )
