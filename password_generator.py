import streamlit as st
import random

# Lists of characters to use in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# App title and description
st.title("Password Generator")
st.write("Welcome to the Password Generator! Customize your password by selecting the number of letters, symbols, and numbers you want in your password.")

# User inputs for password criteria using Streamlit number_input
nr_letters = st.number_input("How many letters would you like in your password?", min_value=0, value=4, step=1)
nr_symbols = st.number_input("How many symbols would you like?", min_value=0, value=2, step=1)
nr_numbers = st.number_input("How many numbers would you like?", min_value=0, value=2, step=1)

# Button to trigger password generation
if st.button("Generate Password"):
    password_list = []

    # Append random letters
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    # Append random symbols
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    # Append random numbers
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # Shuffle the list to randomize the order
    random.shuffle(password_list)

    # Convert the list of characters into a string
    password = ""
    for char in password_list:
        password += char

    # Alternatively, you can join the list in one line:
    # password = "".join(password_list)

    st.success(f"Your password is: {password}")
