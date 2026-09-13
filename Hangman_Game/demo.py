import streamlit as st
import random

# Words the game can choose from
words = ["python", "computer", "programming", "student", "developer"]

# Set up the game when the page is first opened
if "word" not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.wrong_guesses = 0

word = st.session_state.word
guessed_letters = st.session_state.guessed_letters

st.title("🎯 Hangman Game")
st.write("Guess the hidden word one letter at a time!")

# Build the hidden word display
display = ""

for letter in word:
    if letter in guessed_letters:
        display += letter
    else:
        display += "_"

st.header(display)
st.write(f"Wrong guesses: {st.session_state.wrong_guesses} / 6")

# Check whether the player has won
if "_" not in display:
    st.success("🎉 You won!")
else:
    # Get a letter from the player
    guess = st.text_input("Enter a letter:", max_chars=1)

    if st.button("Guess"):
        if not guess.isalpha():
            st.warning("Please enter a letter.")
        elif guess.lower() in guessed_letters:
            st.warning("You already guessed that letter.")
        else:
            guess = guess.lower()
            guessed_letters.append(guess)

            if guess not in word:
                st.session_state.wrong_guesses += 1
                st.error("Wrong guess!")
            else:
                st.success("Correct guess!")

            st.rerun()

# Check whether the player has lost
if st.session_state.wrong_guesses >= 6:
    st.error("Game over!")
    st.write(f"The word was: **{word}**")

    if st.button("Play Again"):
        st.session_state.word = random.choice(words)
        st.session_state.guessed_letters = []
        st.session_state.wrong_guesses = 0
        st.rerun()