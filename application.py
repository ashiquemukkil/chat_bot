from flask import Flask, render_template
from flask_socketio import SocketIO
from eventlet import wsgi
import eventlet

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
# app.config['DEBUG'] = False
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('home.html')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


if __name__ == '__main__':
    wsgi.server(eventlet.listen(('', 443)), app)
