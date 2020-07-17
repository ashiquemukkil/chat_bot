from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = False
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    socketio.run(app,port=8000)