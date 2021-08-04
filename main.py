import streamlit as st
from question_generation.pipelines import pipeline

"# Text to questions and answers"
text_input = st.text_input("Text to make into quiz: ")


@st.cache
def make_quiz(text_input):
    qg = pipeline("question-generation")
    return qg(text_input)


def display_questions(question_raw):
    for i, q in enumerate(question_raw):
        st.radio(label=f"{i+1}. {q['question']}", options=[q["answer"]])


if text_input:
    question_raw = make_quiz(text_input)

    display_questions(question_raw)
