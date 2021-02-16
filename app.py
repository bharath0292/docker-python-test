from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return ("Hi Bharath")

if __name__ == "__main__" :
    uvicorn.run(app)

"""
@app.route('/',methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000) # running the app on the local machine on port 8000
"""