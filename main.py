
from flask import Flask, render_template, Response
from recognizer import camera_stream
#from add_face_to_dataset import camera_stream2

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/info')
def info():

    return render_template('info.html')

@app.route('/faceapp')
def faceapp():

    return render_template('faceapp.html')

@app.route('/addface')
def addface():

    return render_template('addface.html')



def gen_frame():
    """Video streaming generator function."""
    while True:
        frame = camera_stream()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():

    return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='127.0.0.1', threaded=True)




