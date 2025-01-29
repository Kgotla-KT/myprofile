# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:09:32 2025

@author: kkmasibi
"""

import streamlit as st
import random
import json

def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_leaderboard(data):
    with open("leaderboard.json", "w") as f:
        json.dump(data, f)

def main():
    st.set_page_config(page_title="Fun Learning for Grade 4", page_icon="📚", layout="wide")
    st.title("🎉 Welcome to Grade 4 Interactive Learning! 🎨")
    
    st.sidebar.title("👤 Enter Your Details")
    name = st.sidebar.text_input("Enter your name:")
    age = st.sidebar.number_input("Enter your age:", min_value=7, max_value=12)
    grade = st.sidebar.selectbox("Select your grade:", ["Grade 3", "Grade 4", "Grade 5"])
    avatar = st.sidebar.radio("Choose an avatar:", ["🐱 Cat", "🐶 Dog", "🐵 Monkey", "🦊 Fox"])
    
    if name and age and grade:
        st.sidebar.success(f"Welcome, {name}! {avatar} Let's start learning!")
    
    st.sidebar.title("📌 Select a Subject")
    choice = st.sidebar.radio("Choose a subject:", ["Mathematics", "Science", "English", "Afrikaans", "Coding"])
    
    if choice == "Mathematics":
        math_section(name)
    elif choice == "Science":
        science_section()
    elif choice == "English":
        english_section()
    elif choice == "Afrikaans":
        afrikaans_section()
    elif choice == "Coding":
        coding_section()
    
    st.sidebar.title("🏆 Leaderboard")
    leaderboard = load_leaderboard()
    if leaderboard:
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        for rank, (player, score) in enumerate(sorted_leaderboard, start=1):
            st.sidebar.write(f"{rank}. {player}: {score} points")
    else:
        st.sidebar.write("No scores yet! Be the first to earn points!")

def update_score(name, points):
    if not name:
        return
    leaderboard = load_leaderboard()
    leaderboard[name] = leaderboard.get(name, 0) + points
    save_leaderboard(leaderboard)

def math_section(name):
    st.header("📊 Mathematics Fun Zone!")
    st.write("Solve this simple math question:")
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    correct_answer = num1 + num2
    answer = st.number_input(f"What is {num1} + {num2}?", min_value=0, step=1)
    if st.button("Submit Answer"):
        if answer == correct_answer:
            st.success("🎉 Correct! Well done!")
            update_score(name, 10)
        else:
            st.error(f"❌ Incorrect! The correct answer is {correct_answer}.")

def science_section():
    st.header("🔬 Fun with Science!")
    st.write("Did you know? Water boils at **100°C** at sea level! 🫗")
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/7f/Boiling_water_in_kettle.jpg", width=300)
    st.write("### Quick Quiz: What gas do plants take in for photosynthesis?")
    answer = st.radio("Select an option:", ["Oxygen", "Carbon Dioxide", "Nitrogen"])
    if st.button("Submit Answer"):
        if answer == "Carbon Dioxide":
            st.success("✅ Correct! Plants need CO₂.")
        else:
            st.error("❌ Try again!")

def english_section():
    st.header("📖 Learn English Words!")
    words = {"Apple": "A fruit 🍏", "Book": "Something you read 📚", "Sun": "Gives us light ☀️"}
    word = st.selectbox("Choose a word:", list(words.keys()))
    st.write(f"**{word}** means: {words[word]}")
    st.write("### Quick Challenge: Form a sentence using the word!")
    sentence = st.text_area("Type your sentence here:")
    if st.button("Check Sentence") and sentence:
        st.success("👍 Good job!")

def afrikaans_section():
    st.header("🗣 Learn Afrikaans!")
    translations = {"Hello": "Hallo", "Goodbye": "Totsiens", "Thank you": "Dankie"}
    word = st.selectbox("Choose an English word:", list(translations.keys()))
    st.write(f"In Afrikaans, **{word}** is **{translations[word]}** 🇿🇦")
    st.write("### Quick Challenge: Translate 'Please' into Afrikaans!")
    answer = st.text_input("Your answer:")
    if st.button("Check Answer"):
        if answer.lower() == "asseblief":
            st.success("✅ Correct! 'Please' in Afrikaans is 'Asseblief'.")
        else:
            st.error("❌ Try again!")

def coding_section():
    st.header("💻 Let's Learn Coding!")
    st.write("A simple Python print statement:")
    st.code("print('Hello, world!')", language="python")
    st.write("### Quick Challenge: What will this print?\n\n```python\nx = 5\nprint(x * 2)```")
    answer = st.text_input("Your answer:")
    if st.button("Check Answer"):
        if answer == "10":
            st.success("✅ Correct! The output is 10.")
        else:
            st.error("❌ Try again!")

if __name__ == "__main__":
    main()