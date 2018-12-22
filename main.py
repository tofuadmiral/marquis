from iexfinance.stocks import Stock
from flask import Flask
from flask_socketio import SocketIO, send






app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)


@socketio.on('message')



def handleMessage(msg): 
        msg=[msg]
        msg.append('TOSHI: Welcome my name is TOSHI')
        send(msg, broadcast=True)
       

        

if __name__ == '__main__':
        from bot import *
        socketio.run(app)


