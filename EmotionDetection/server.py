"""
Module này triển khai server Flask cho ứng dụng phát hiện cảm xúc.
Nó cung cấp các endpoint để phân tích văn bản và hiển thị giao diện web.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Phân tích văn bản đầu vào và trả về chuỗi kết quả định dạng cho người dùng.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Xử lý trường hợp đầu vào trống (Question 13)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Trả về kết quả hiển thị trên giao diện
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Hiển thị trang giao diện chính của ứng dụng.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
