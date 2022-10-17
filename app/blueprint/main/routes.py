from flask import Flask
app= Flask(__name__)


@app.route('/', methods=['GET'])

def homepage():
    return render_template('homepage.html.j2')

@app.route('/pokesearch', methods=['GET', 'POST'])
def pokesearch():
    pass 