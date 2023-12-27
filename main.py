# impor tampilan web
import streamlit as st
from view.web import run_streamlit

# jalankan fungsi run_streamlit() untuk penggunaan pertama kali
if __name__ == "__main__":
    run_streamlit()

#background
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1483401757487-2ced3fa77952?ixlib=rb-4.0.3");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.markdown(
    """
    ---
    <p style='font-size:14px;'> Made with ❤️ by Kelompok 4C - TBO <br> </p>
    """,
    unsafe_allow_html=True
)