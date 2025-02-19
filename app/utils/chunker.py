from transformers import AutoTokenizer


def split_text(text: str, chunk_size: int = 200):
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct", trust_remote_code=True)

    tokens = tokenizer.encode(text)

    return [tokenizer.decode(tokens[i:i + chunk_size]) for i in range(0, len(tokens), chunk_size)]
