# import model here
import numpy as np
# Use a pipeline as a high-level helper
from transformers import pipeline

path = "./model"
pipe = pipeline("summarization", model=path)
# tokenizer = AutoTokenizer.from_pretrained(path)
# print("Loaded tokenizer...")
# model = AutoModelForSeq2SeqLM.from_pretrained(path)
# print("Loaded model...")

def summarize_text(text):
    output = pipe(text)
    return output[0]['summary_text']
