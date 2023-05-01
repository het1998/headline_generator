import pandas as pd
import requests
from transformers import pipeline
# from utils import headline_generate_sam,headline_generator
from utils import headline
from flask import Flask,request
import os

app=Flask(__name__)

@app.route('/',methods=['POST'])

# text=input("Enter Your Article Here: ")

## Initialize transformer pipeline


def headline_generator():
    params=request.get_json(force=True)
    if (params is not None) and ('text' in params):

        text=params.get('text')
        print('printed_text>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',text)
        headline_temp=headline(str(text))
        headline_temp.headline_generator()
        generated_headline=headline_temp.clean_headlines()
        return {"status_code":200, "data":generated_headline}

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=int(os.environ.get("PORT",8080)))