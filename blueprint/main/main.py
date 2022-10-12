@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html.j2')

@app.route('/pokesearch', methods=['GET', 'POST'])
def pokesearch():