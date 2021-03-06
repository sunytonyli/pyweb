from pyweb import app
from flask import Flask, url_for, render_template
import time

@app.route('/')
def index():
	return render_template('index.html', time = time.strftime('%Y-%m-%d %H-%M-%S'), month = time.strftime('%m'))

@app.route('/demo')
def demo():
	return render_template('kartik/examples/index.html')

@app.route('/ckeditor')
def ckeditor():
	return render_template('ckeditor.html');

@app.route('/ckeditor/examples')
def ckeditor_demo():
	return render_template('ckeditor/samples/index.html');