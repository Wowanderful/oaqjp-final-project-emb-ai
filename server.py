from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    list = response[0]
    dom = response[2]

    if dom == None:
        return "Invalid text! Please try again!"
    else: 
        return "The given text has been identified as {} with a score of {}.".format(list, dom)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)