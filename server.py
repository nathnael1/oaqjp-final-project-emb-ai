'''This is Ai developed flask application using watson API'''
from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route("/")
def index():
    """
    return template
    """
    return render_template("index.html")
@app.route("/emotionDetector")
def emotion_detector_route():
    """
    return emotion values and dominant emotion
    """
    text = request.args.get("textToAnalyze")
    if text is None:
        return "Invalid text! Please try again!.\n"
    emotion = emotion_detector(text)
    prevalue = "For the given statement, the system response is "
    emotions = ', '.join(
        f"'{key}': {emotion[key]}" for key in ['anger', 'disgust', 'fear', 'joy', 'sadness']
    )
    dominant_emotion = f"The dominant emotion is {emotion['dominant_emotion']}."
    return f"{prevalue}{emotions} {dominant_emotion} \n"
if __name__ == "__main__":
    app.run(debug=True)
