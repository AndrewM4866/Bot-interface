import time
import random
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def home():
    """Serves the dashboard's core layout shell."""
    return render_template("home.html")

@app.route('/baseline')
def baseline():
    # Renders your original telemetry stream panel
    return render_template('baseline.html')

@app.route('/vision')
def vision():
    # Renders your new multi-threaded camera container screen
    return render_template('vision.html')

@app.route('/video_feed')
def video_feed():
    # Points back to your existing multi-threaded frame generator pattern
    return Response(webcam_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_random_number():
    """
    Generator function serving as your telemetry pipeline.
    This loop continues as long as the browser window stays open.
    """
    while True:
        # Generate dummy data for your core AMR variables
        random_number = round(random.uniform(10.0, 200.0), 1)
        
        # SSE protocol strictly requires the payload to be prefixed with 'data: '
        # and terminated by two newlines ('\n\n')
        payload = f"data: {{\"randomNumber\": {random_number}}}\n\n"
        
        yield payload
        time.sleep(0.1)  # Streams updates at 10Hz (10 frames per second)

@app.route('/stream')
def stream():
    """Persistent HTTP connection endpoint for the live frontend telemetry."""
    return Response(generate_random_number(), mimetype='text/event-stream')

if __name__ == '__main__':
    # Configured on port 5001 to keep it accessible locally or via your SSH tunnels
    app.run(host='0.0.0.0', port=5001, debug=True)
