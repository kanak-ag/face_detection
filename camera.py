from flask import Flask, render_template, Response
from camera import Video 
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video')
def video():
    return Response(Video)

app.run(debug=True)


