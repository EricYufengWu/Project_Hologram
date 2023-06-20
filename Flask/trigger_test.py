import socketio

# Connect to the Flask-SocketIO server
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

def trigger_image_update():
    # Trigger the 'update_image' event on the server
    sio.emit('update_image')

# Start the WebSocket connection
sio.connect('http://localhost:5000')

# Call the function to trigger the image update
trigger_image_update()

# Wait for a few seconds to allow the server to process the event
sio.sleep(2)

# Disconnect from the server
sio.disconnect()