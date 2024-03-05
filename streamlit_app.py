import base64
import os

import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

# Import style from CSS file
def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style/style.css")

@st.cache_data ()
def get_img_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get relative paths for images
main_img_path = os.path.join("images", "main1.jpeg")
left_img_path = os.path.join("images", "left1.jpeg")

# Convert images to base64
main_img = get_img_as_base64(main_img_path)
left_img = get_img_as_base64(left_img_path)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{main_img}");
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{left_img}");
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


add_page_title()
show_pages(
    [
        Page("streamlit_app.py", "main_info", "💻"),

        # # 2024 Content
        Section("2024", "🧙‍♂️"),
        Page("pages/PasswordStrength.py", "Password Strength", "📚", in_section=True),
        Page("pages/PasswordGenerator.py", "Password Generator", "📚", in_section=True),
    ]
)

st.markdown("#### 👨‍🔧 This webpage is having great features. please find below:")
st.markdown("""
- [Password Strength](#PasswordStrength)
- [Password Generator](#PasswordGenerator)
""", unsafe_allow_html=True)

hide_pages(["Thank you"])
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)