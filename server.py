"""
Emotion detection module.

This module analyzes text and returns emotion scores
for anger, disgust, fear, joy, and sadness.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyze the user-provided text and return emotion scores.

    Retrieves the text from the 'textToAnalyze' query parameter,
    invokes the emotion detector, and returns the detected emotion
    scores along with the dominant emotion. If the input text is
    invalid or no dominant emotion can be determined, an error
    message is returned.

    Returns:
        str: A formatted string containing emotion scores and the
        dominant emotion, or an error message for invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return (
    f"For the given statement, the system response is "
    f"'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, "
    f"'joy': {response['joy']} and "
    f"'sadness': {response['sadness']}. "
    f"The dominant emotion is "
    f"{response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the application's home page.

    Returns:
        str: The rendered index.html template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=500)
