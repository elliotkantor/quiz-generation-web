import streamlit as st
from question_generation.pipelines import pipeline
from quiz_gen import make_quiz

"# Text to questions and answers"
text_input = st.text_input("Text to make into quiz: ")


def display_questions(question_raw):
    for i, q in enumerate(question_raw):
        st.radio(label=f"{i+1}. {q['question']}", options=[q["answer"]])


if text_input:
    question_raw = make_quiz(text_input)
    display_questions(question_raw)
