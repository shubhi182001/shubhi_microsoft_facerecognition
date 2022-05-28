# from crypt import methods
from cgitb import html

from unicodedata import name
from flask import Flask, render_template, Response, request, json,jsonify
from flask_cors import CORS
# from requests import request
from camera import Video

app=Flask(__name__)

@app.route("/" , methods=["GET"])
def api():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def reg():
    name = request.form["name"] 
    imagefile= request.files['imagefile']
    image_path = "C:/Users/dell/OneDrive/Desktop/Microsoft-engage/face_verify/images./" +name+".jpeg"
    imagefile.save(image_path)
    return render_template('index.html')

# def kcu():
#     if "Implement ml" in request.form:
#         return render_template ('camera.html')
#     elif "Register" in request.form:
#         return render_template('register.html')


# @app.route('/register')
# def register():
#     name = request.form["name"]
#     imagefile= request.files['imagefile']
#     image_path = "C:/Users/dell/OneDrive/Documents/MY PROJECTS/flask-react/flask-server/ImagesAttendance./" + name+ ".jpeg"
#     imagefile.save(image_path)


def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')
         
# @app.route('/video', methods=["GET"])
# def vi():
#     return render_template("camera.html")

@app.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == "__main__":
    app.run(debug=True)