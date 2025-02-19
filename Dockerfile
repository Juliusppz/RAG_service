FROM python:3.9-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoModelForCausalLM.from_pretrained('mistralai/Mistral-7B-Instruct', trust_remote_code=True); AutoTokenizer.from_pretrained('mistralai/Mistral-7B-Instruct', trust_remote_code=True)"

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
