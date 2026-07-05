from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room

# Flask automatically monitors the /static directory for asset delivery
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-server-key-12345'
socketio = SocketIO(app, cors_allowed_origins="*")

USERS = {}
SID_TO_USER = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('register')
def handle_register(data):
    username = data.get('username')
    public_key = data.get('public_key')
    if not username or not public_key:
        return
    USERS[username] = {"sid": request.sid, "public_key": public_key, "status": "online"}
    SID_TO_USER[request.sid] = username
    join_room(request.sid)
    send_updated_user_list()

@socketio.on('get_public_key')
def handle_get_public_key(data):
    target_user = data.get('target_user')
    if target_user in USERS:
        emit('receive_public_key', {
            "target_user": target_user,
            "public_key": USERS[target_user]['public_key']
        }, room=request.sid)

@socketio.on('send_encrypted_msg')
def handle_encrypted_msg(data):
    receiver = data.get('receiver')
    msg_id = data.get('msg_id')
    sender = SID_TO_USER.get(request.sid)
    if not sender: return

    if receiver in USERS:
        emit('receive_encrypted_msg', data, room=USERS[receiver]['sid'])
        emit('msg_status_update', {"msg_id": msg_id, "status": "delivered"}, room=request.sid)
    else:
        emit('msg_status_update', {"msg_id": msg_id, "status": "sent"}, room=request.sid)

@socketio.on('msg_read_receipt')
def handle_read_receipt(data):
    sender = data.get('sender')
    if sender in USERS:
        emit('msg_status_update', {"msg_id": data.get('msg_id'), "status": "read"}, room=USERS[sender]['sid'])

@socketio.on('typing_status')
def handle_typing_status(data):
    target_user = data.get('target_user')
    sender = SID_TO_USER.get(request.sid)
    if target_user in USERS and sender:
        emit('peer_typing', {"sender": sender, "is_typing": data.get('is_typing')}, room=USERS[target_user]['sid'])

@socketio.on('disconnect')
def handle_disconnect():
    disconnected_user = SID_TO_USER.pop(request.sid, None)
    if disconnected_user:
        USERS.pop(disconnected_user, None)
        send_updated_user_list()

def send_updated_user_list():
    payload = [{"username": u, "status": m["status"]} for u, m in USERS.items()]
    emit('user_list', payload, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)