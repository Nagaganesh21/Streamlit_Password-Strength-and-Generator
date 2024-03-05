import base64
import os
import streamlit as st
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

st.markdown("#### 👨‍🔧 My Projects list which are practiced in Streamlit:")
st.markdown("""
<br><a href="https://twittsentimentanalysis.streamlit.app/" >1️⃣ Twitterr Sentiment Analysis</a></br>
<br><a href="https://imdbreviewanalysis.streamlit.app/" >2️⃣ IMDB Review Analysis</a></br>
<br><a href="https://futurestockanalysis.streamlit.app/" >3️⃣ Stocks Future Price Prediction</a></br>
<br><a href="" >4️⃣ Image Classification</a></br>
<br><a href="https://apppassword-strength-and-generator.streamlit.app/" >5️⃣ Password Strength and Generator</a></br>
<br><a href="" >6️⃣ Fake News Detection</a></br>

""", unsafe_allow_html=True)
