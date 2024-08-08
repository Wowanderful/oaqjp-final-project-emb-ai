# Importing Flask
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

#Approute
@app.route("/emotionDetector")

# Main function
def em_detector():

    # Get the text to analyze from the query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)

    # Extract the list of emotions and the dominant emotion score
    li = response[0]
    dom = response[2]

    # Check if a valid emotion was detected
    if dom is None:
        return "Invalid text! Please try again!"
    # Return the detected emotion and score
    return f"The given text has been identified as {li} with a score of {dom}."

# approute
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
