# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="Trelis/Meta-Llama-3-8B-Instruct-function-calling", device_map="auto")
pipe(messages)