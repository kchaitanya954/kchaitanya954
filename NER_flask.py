from flask import Flask, render_template, request, Blueprint
import spacy
from spacy import displacy
from flaskext.markdown import Markdown
import wikipedia

nlp=spacy.load('en_core_web_sm')

app=Flask(__name__)
Markdown(app)

simple_page = Blueprint('simple_page', __name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ner', methods=["GET", "POST"])
def extract():
    if request.method == 'POST':
        if request.form['submit_button'] == 'NER Submit':
            rawtext = request.form['rawtext']
            docx = nlp(rawtext)
            html = displacy.render(docx, style='ent')
            result = html
        elif request.form['submit_button'] == 'NER wiki Submit':
            rawtext = wikipedia.summary(request.form['rawtext'])
            docx = nlp(rawtext)
            html = displacy.render(docx, style='ent')
            result = html

    return render_template('results.html', rawtext=rawtext, result=result)




if __name__ == '__main__':

    app.run(debug=True)
