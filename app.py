# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 03:01:34 2024

@author: Tumisang.Lemao
"""
"""MODEL INTEGRATION CODE

convert model from ipynb to plk

model = pickle.load(open('/Text-to-Speech_Working Doc.plk'))
"""

!pip install flask SpeechRecognition
!pip install translate
!pip install pyttsx3

from flask import Flask, render_template, request, send_file
import pyttsx3
from translate import Translator
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

#File upload and convert into mp3 file 
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    text_content = file.read().decode("utf-8")
    mp3_file = convert_text_to_speech(text_content)
    

    return render_template('index1.html', mp3_file=mp3_file)
#------------------------------------------------------------------------------

#Input text into text box and convert into mp3.
@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text_content = request.form['text_content']
    mp3_file = convert_text_to_speech(text_content)

    return render_template('index1.html', mp3_file=mp3_file)
#------------------------------------------------------------------------------

#input text into text box and translate to desired language via mp3 file

@app.route('/download', methods=['GET'])
def download():
    mp3_file = request.args.get('mp3_file', '')
    return send_file(mp3_file, as_attachment=True, attachment_filename='output.mp3')

def convert_text_to_speech(text):
    engine = pyttsx3.init()
    mp3_file = 'output.mp3'
    engine.save_to_file(text, mp3_file)
    engine.runAndWait()
    return mp3_file

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

!python untitled0.py
