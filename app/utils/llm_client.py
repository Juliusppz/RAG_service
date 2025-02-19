from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from app.config import settings


tokenizer = AutoTokenizer.from_pretrained(settings.llm_model_name)
model = AutoModelForCausalLM.from_pretrained(
    settings.llm_model_name, torch_dtype=torch.float16, device_map="auto"
)

def generate_response(query: str, context_chunks: list):
    prompt = query + "\nContext:\n" + "\n".join(context_chunks)
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(model.device)

    output = model.generate(**inputs, max_new_tokens=150)
    return tokenizer.decode(output[0], skip_special_tokens=True)
