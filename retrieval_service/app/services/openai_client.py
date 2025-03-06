import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_subanswer(subquestion: str, documents: list):
    prompt = (
        f"Answer the following subquestion based on the context below.\n\n"
        f"Subquestion: {subquestion}\n"
        f"Documents: {documents}\n"
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
    )
    return response.choices[0].text.strip()

def generate_final_answer(original_query: str, subquestions: list, subanswers: dict):
    prompt = f"Using the following information, generate a comprehensive answer.\n\nOriginal Query: {original_query}\n"
    for subq in subquestions:
        prompt += f"Subquestion: {subq}\nAnswer: {subanswers.get(subq)}\n\n"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
    )
    return response.choices[0].text.strip()
