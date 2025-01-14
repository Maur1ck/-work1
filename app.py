from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.now().year
    return render_template('main.html', year=year)

if __name__ == '__main__':
    app.run(debug=True)
