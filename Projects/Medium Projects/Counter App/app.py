from flask import Flask, render_template

app = Flask(__name__)

# Initialize the count in the database
db = {'number': 0}

# Routes
@app.route('/')
def home():
    return render_template('home_page.html', count=db['number'])

@app.route('/increment')
def increment():
    db['number'] += 1
    return render_template('home_page.html', count=db['number'])

@app.route('/decrement')
def decrement():
    if db['number'] > 0:
        db['number'] -= 1
    return render_template('home_page.html', count=db['number'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)