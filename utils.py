from transformers import AutoTokenizer,AutoModel, MT5ForConditionalGeneration, T5Tokenizer, T5Model
import pandas as pd
import requests
from transformers import pipeline

headline_init = pipeline(model = "czearing/article-title-generator")

class headline():
    def __init__(self,text):
        self.text = text

      
    def headline_generator(self):
        response=headline_init(self.text,max_length=500)
        self.temp = response
        print(self.temp)
    
    def clean_headlines(self):
        for i in self.temp:
         for self.temp,y in i.items():
             return y