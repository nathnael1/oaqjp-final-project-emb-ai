from flask import Flask,request,render_template
import requests
from EmotionDetection.emotion_detection import emotion_detector 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/emotionDetector")
def emotion_detector_route():
    text = request.args.get("textToAnalyze")
    if text == None:
        return "Invalid text! Please try again!.\n"
    emotion = emotion_detector(text)
    prevalue = "For the given statement, the system response is "
    emotions = f"'anger': {emotion['anger']}, 'disgust': {emotion['disgust']},'fear': {emotion['fear']}, 'joy': {emotion['joy']}, 'sadness': {emotion['sadness']}"
    dominant_emotion = f"The dominant emotion is {emotion['dominant_emotion']}."
 
        
    return f"{prevalue}{emotions} {dominant_emotion} \n"
if __name__ == "__main__":
    app.run(debug=True)