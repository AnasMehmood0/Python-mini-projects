# Import necessary libraries
import streamlit as st
import random
import string
import time
import qrcode
from PIL import Image

# Set up the page configuration
st.set_page_config(
    page_title="Python Mini Projects", 
    page_icon="🚀", 
    layout="wide"
)

st.markdown("""
<style>
    /* Set a gradient background for the entire app */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e, #fbc2eb, #a6c1ee);
        font-family: 'Arial', sans-serif;
    }

    /* Style the main headings with a gradient effect */
    .stMarkdown h1 {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        animation: fadeIn 2s ease-in-out;
    }

    /* Style subheadings for better visibility */
    .stMarkdown h2 {
        color: #2c3e50;
        font-size: 2rem;
        font-weight: bold;
        animation: slideIn 1s ease-in-out;
    }

    /* Make all text bold and easy to read */
    .stMarkdown p, .stMarkdown div {
        color: #2c3e50;
        font-size: 1.2rem;
        font-weight: bold;
    }

    /* Add a gradient background to columns */
    .stColumn {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        padding: 20px;
        border-radius: 15px;
        margin: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        animation: slideIn 1s ease-in-out;
    }

    /* Style buttons with a gradient and hover effect */
    .stButton button {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.3s ease;
    }

    .stButton button:hover {
        transform: scale(1.1);
    }

    /* Style input fields for better visibility */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background: white;
        border: 2px solid #6a11cb;
        border-radius: 10px;
        padding: 10px;
        font-size: 1rem;
        font-weight: bold;
        color: black; /* Ensure text is visible */
    }

    /* Add animations for a polished look */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideIn {
        from { transform: translateY(50px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)
""", unsafe_allow_html=True)

# Add a sidebar for navigation
st.sidebar.title("Navigation")
project = st.sidebar.radio(
    "Choose a project", 
    [
        "Mad Libs", 
        "Guess the Number",  # Removed the trailing space
        "Password Generator", 
        "Countdown Timer", 
        "QR Code Generator", 
        "Rock, Paper, Scissors"
    ]
)

# Mad Libs Game
if project == "Mad Libs":
    st.title("Mad Libs Game 🎭")
    st.write("Fill in the blanks to create a fun story!")
    
    # Use columns to organize input fields
    col1, col2 = st.columns(2)
    with col1:
        adjective = st.text_input("Enter an adjective:")
    with col2:
        noun = st.text_input("Enter a noun:")
    with col1:
        verb = st.text_input("Enter a verb:")
    with col2:
        place = st.text_input("Enter a place:")
    
    # Generate the story when the button is clicked
    if st.button("Generate Story"):
        if adjective and noun and verb and place:
            story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} in {place}."
            st.success(story)
        else:
            st.error("Please fill in all the fields!")

# Guess the Number Game 
elif project == "Guess the Number":
    st.title("Guess the Number Game 🔢")
    st.write("Guess a number between 1 and 100!")
    
    # Store the target number and attempts in session state
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
    
    # Get the user's guess
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100)
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.number:
            st.warning("Too high! Try again.")
        else:
            st.success(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            # Reset the game
            del st.session_state.number
            del st.session_state.attempts

# Password Generator
elif project == "Password Generator":
    st.title("Password Generator 🔐")
    st.write("Generate a strong and secure password!")
    
    # Let the user choose the password length
    length = st.slider("Select password length:", 8, 32, 12)
    if st.button("Generate Password"):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        st.success(f"Your generated password is: `{password}`")

# Countdown Timer
elif project == "Countdown Timer":
    st.title("Countdown Timer ⏳")
    st.write("Set a countdown timer in seconds.")
    
    # Get the countdown duration from the user
    seconds = st.number_input("Enter time in seconds:", min_value=1, max_value=3600, value=10)
    if st.button("Start Timer"):
        with st.empty():
            for i in range(seconds, 0, -1):
                st.write(f"Time left: {i} seconds")
                time.sleep(1)
            st.success("Time's up!")

# QR Code Generator
elif project == "QR Code Generator":
    st.title("QR Code Generator 📲")
    st.write("Generate a QR code for any text or URL.")
    
    # Get the data for the QR code
    data = st.text_input("Enter text or URL:")
    if st.button("Generate QR Code"):
        if data:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save("qrcode.png")
            st.image("qrcode.png", caption="Generated QR Code", use_column_width=True)
            st.success("QR Code saved as 'qrcode.png'.")
        else:
            st.error("Please enter some text or URL!")

# Rock, Paper, Scissors
elif project == "Rock, Paper, Scissors":
    st.title("Rock, Paper, Scissors 🪨📄✂️")
    st.write("Play against the computer!")
    
    # Define the choices
    choices = ["rock", "paper", "scissors"]
    user_choice = st.selectbox("Choose your move:", choices)
    if st.button("Play"):
        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "You lose!"
        st.write(f"Computer chose `{computer_choice}`. **{result}**")
