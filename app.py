from flask import Flask, render_template

app = Flask(__name__)

url = 'images/tennis01.jpg'  # Replace with your desired URL

@app.route('/')
def index():
    return render_template('index.html', url=url)

if __name__ == '__main__':
    app.run()