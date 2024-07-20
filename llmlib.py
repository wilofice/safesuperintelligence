# from langchain_huggingface import HuggingFaceEndpoint
#
# llm = HuggingFaceEndpoint(
#     repo_id="meta-llama/Meta-Llama-3-70B-Instruct",
#     task="text-generation",
#     max_new_tokens=512,
#     do_sample=False,
#     repetition_penalty=1.03,
# )

# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="Trelis/Llama-2-7b-chat-hf-function-calling-v3")
pipe(messages)