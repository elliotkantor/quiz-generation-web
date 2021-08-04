from question_generation.pipelines import pipeline


def make_quiz(text_input):
    qg = pipeline("question-generation")
    return qg(text_input)
