# Name: Khoger Dosky
# File Name: Python Web Page Code
# Date: June 29, 2020
# Course: SDEV 300 6380 Building Secure Python Applications (2205)
# Prof. Muhammad Khan


from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')


def Home():
    return render_template('Home.html', time = datetime.datetime.now())

if __name__ == '__main__':
    app.run(debug = True)


