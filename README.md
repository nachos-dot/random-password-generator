# Random Password Generator

This is a simple Streamlit-based password generator app that creates secure, random passwords based on user-specified criteria. It demonstrates basic Python programming concepts such as loops, conditionals, lists, and random selection, and it features an interactive user interface built with Streamlit.

## Features

- **Customizable Passwords:**  
  Choose the number of letters, symbols, and numbers you want in your password.
  
- **Random Generation:**  
  Uses Python's `random` module to randomly select characters and create a secure password.
  
- **Interactive UI:**  
  Built with Streamlit, the app provides a user-friendly interface that updates in real time.

## How It Works

1. **Character Lists:**  
   The app defines three lists containing possible characters: one for letters (both uppercase and lowercase), one for numbers, and one for symbols.

2. **User Input:**  
   The app uses Streamlit's input widgets (like number inputs and buttons) to gather the user's desired password criteria.

3. **Password Generation:**  
   For each type of character, the app uses a loop and `random.choice()` to select random characters from the appropriate list. All selected characters are combined, and `random.shuffle()` is used to further randomize the order before the final password is displayed.

## How to Use the App

1. **Access the App:**  
   Open the app in your web browser via the provided URL (if deployed) or run it locally.

2. **Input Criteria:**  
   - Enter the number of letters you want.
   - Enter the number of symbols you want.
   - Enter the number of numbers you want.

3. **Generate Password:**  
   Click the **"Generate Password"** button.  
   The app will display the generated password.

