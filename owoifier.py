# owoifier.py
import random
import re

def owoify(text):
    faces = ["(・`ω´・)", ";;w;;", "owo", "UwU", ">w<", "^w^", "hehe", "^w^"]
    text = re.sub(r'[lr]', 'w', text)
    text = re.sub(r'[LR]', 'W', text)
    text = re.sub(r'n([aeiou])', r'ny\1', text)
    text = re.sub(r'N([aeiouAEIOU])', r'Ny\1', text)
    text = text.replace("ove", "uv")
    text = text.replace("love", "wuv")
    text = text.replace("mr", "mistuh")
    text = text.replace("dog", "doggo")
    text = text.replace("cat", "kitteh")
    text = text.replace("hello", "henwo")
    text = text.replace("hell", "heck")
    text = text.replace("fuck", "fwick")
    text = text.replace("fuk", "fwick")
    text = text.replace("shit", "shoot")
    text = text.replace("friend", "fwend")
    text = text.replace("stop", "stawp")
    text = text.replace("god", "gosh")
    text = text.replace("dick", "peepee")
    text = text.replace("penis", "peepee")
    text = text.replace("damn", "darn")    
    text += " " + random.choice(faces)
    print("[OwOifier] Local OwOified:", text)
    return text
