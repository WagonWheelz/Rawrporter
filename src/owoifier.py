# owoifier.py
import random
import re

def owoify(text):
    faces = ["(・`ω´・)", ";;w;;", "owo", "UwU", ">w<", "^w^"]
    text = re.sub(r'[lr]', 'w', text)
    text = re.sub(r'[LR]', 'W', text)
    text = re.sub(r'n([aeiou])', r'ny\1', text)
    text = re.sub(r'N([aeiouAEIOU])', r'Ny\1', text)
    text = text.replace("ove", "uv")
    text += " " + random.choice(faces)
    print("[OwOifier] Local OwOified:", text)
    return text
