from llama_cpp import Llama
import sys
import os
from texts import PROMPT

def generate_text(text: str, prompt: str):
    stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')
    
    llm = Llama(
        model_path="llama/ggml-model-Q4_K_M_RU.gguf",
        n_gpu_layers=-1,  # полностью на GPU
        n_ctx=2048,       # можно больше, если нужно (до 4096)
        verbose=False,
        verbosity=0
    )
    # print(f"{prompt}:\n{text}")
    output = llm.create_completion(
        prompt=f"{prompt}:\n{text}. Анкета: ",
        max_tokens=300,
        temperature=0.7,
        echo=False,
        stream=False
    )
    sys.stderr.close()
    sys.stderr = stderr
    return output["choices"][0]["text"]
