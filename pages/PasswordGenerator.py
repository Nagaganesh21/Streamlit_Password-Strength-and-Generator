import base64
import os
import random
import string
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
def estimate_crack_time(password, characters):
    # Calculate the total number of possible combinations
    total_combinations = len(characters) ** len(password)
    # Assuming a certain number of attempts per second
    attempts_per_second = 10000000000000  # Adjust this value based on your estimation
    # Calculate seconds to crack
    seconds_to_crack = total_combinations / attempts_per_second
    # Convert seconds to days
    days_to_crack = seconds_to_crack / (60 * 60 * 24)

    # Convert days to years, months, days, and centuries
    years = days_to_crack // 365
    months = (days_to_crack % 365) // 30
    remaining_days = days_to_crack % 30
    centuries = years // 100
    years %= 100

    return int(centuries), int(years), int(months), int(remaining_days)

# Function to generate a random password
def generate_password(length, include_letters=True, include_symbols=True, include_numbers=True):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_symbols:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    if not characters:
        raise ValueError("###### At least one option should be selected for password generation.")

    password = ''.join(random.choice(characters) for _ in range(length))
    centuries, years, months, days = estimate_crack_time(password, characters)
    return password, centuries, years, months, days

def main():
    st.title("Generate Random Password")

    st.markdown("**Select the length of the password:**")
    length = st.slider("", 8, 15, 10)

    # Display slider value in bold using Markdown formatting
    st.markdown(f"**Selected length: {length}**")
    include_letters = st.checkbox("Include letters?")
    include_symbols = st.checkbox("Include symbols?")
    include_numbers = st.checkbox("Include numbers?")

    if st.button("Generate Password"):
        try:
            password, centuries, years, months, days = generate_password(length, include_letters, include_symbols, include_numbers)

            # Display generated password in red color
            st.write("###### Generated Password: " + f"<span style='color:red'><b>{password}</b></span>", unsafe_allow_html=True)

            # Display estimated time to crack in blue color
            st.write("###### Estimated time to crack: " + f"<span style='color:blue'><b>{centuries} centuries, {years} years, {months} months, {days} days</b></span>", unsafe_allow_html=True)

        except ValueError as e:
            st.error(e)

if __name__ == "__main__":
    main()