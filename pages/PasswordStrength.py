import streamlit as st
import random
import string
import pickle
import os
import base64

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

# Define character-level tokenizer function
def tokenize_chars(text):
    return [ch for ch in text]

# Load tokenizer and model
tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
clf = pickle.load(open('model.pkl', 'rb'))

# Function to check password strength using the model
def check_password_strength(password):
    # Preprocess the password
    X_input = tokenizer.transform([password])
    # Predict the strength
    predicted_strength = clf.predict(X_input)[0]
    return ["Weak", "Medium", "Strong"][predicted_strength]

# Main function to run the Streamlit app
def main():
    st.title("Check Password Strength")
    password = st.text_input("Enter the password to check its strength:")
    if st.button("Check Strength"):
        if password:
            strength = check_password_strength(password)
            st.write("###### Password strength: " + f"<span style='color:red'><b>{strength}</b></span>", unsafe_allow_html=True)
        else:
            st.warning("###### Please enter a password.")

if __name__ == "__main__":
    main()
