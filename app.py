
import streamlit as st
import json

def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

def main():
    st.title("EngliChat: English Level Assessment")
    st.write("Answer the questions below to determine your English level (A1 to C2).")

    questions = load_questions()
    answers = {}
    level_scores = {level: 0 for level in questions.keys()}

    for level, qs in questions.items():
        st.header(f"Level {level}")
        for idx, q in enumerate(qs):
            if q["type"] == "text":
                answer = st.text_input(f"{level} Q{idx+1}: {q['question']}")
            elif q["type"] == "number":
                answer = st.number_input(f"{level} Q{idx+1}: {q['question']}", step=1)
            else:
                answer = None
            answers[f"{level}_{idx}"] = answer
            if answer:
                level_scores[level] += 1

    max_level = max(level_scores, key=level_scores.get)
    st.write(f"Your estimated English level is: **{max_level}**")

if __name__ == "__main__":
    main()
