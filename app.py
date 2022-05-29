# from crypt import methods
from cgitb import html

from unicodedata import name
from flask import Flask, render_template, Response, request, json,jsonify
from flask_cors import CORS
# from requests import request
from camera import Video
from flask import send_file

app=Flask(__name__)

@app.route("/" , methods=["GET"])
def api():
    return render_template('index.html')          #rendering index.html here

@app.route('/', methods=["POST"])          #function for adding new registerations to backend
def reg():
    name = request.form["name"] 
    imagefile= request.files['imagefile']
    image_path = "C:/Users/dell/OneDrive/Desktop/Microsoft-engage/face_verify/images./" +name+".jpeg"
    imagefile.save(image_path)
    return render_template('index.html')



def gen(camera):                    #accessing camera function
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')
         

@app.route('/video')                  #this function returns response of final encoded images
def video():
    return Response(gen(Video()),       #gen() function is called here
    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_csv') #for adding name and time in attendance.csv file
def plot_csv():
    return send_file('Attendance.csv',
                     mimetype='text/csv',
                     attachment_filename='Attendance.csv',
                     as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)