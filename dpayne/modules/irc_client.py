import socketio

def main():
    sio = socketio.Client()

    @sio.on('irc_message')
    def on_message(data):
        print(f"[{data['user']}] {data['message']}")

    nickname = input("Enter your nickname: ")
    room = input("Enter room name (default): ") or "default"

    sio.connect('http://localhost:5000')  # Adjust the server address as needed

    sio.emit('join_irc', {'nickname': nickname, 'room': room})
    try:
        while True:
            message = input(f"[{nickname}] > ")
            if message.lower() == "/quit":
                sio.emit('leave_irc', {'room': room})
                break
            sio.emit('send_irc_message', {'message': message, 'room': room})
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Exiting IRC chat...")
        sio.emit('leave_irc', {'room': room})
        pass
    finally:
        sio.disconnect()