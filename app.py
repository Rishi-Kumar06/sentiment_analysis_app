from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import os

app = Flask(__name__)

def analyze_sentiment(text):
    """
    Analyze sentiment of the given text using TextBlob
    Returns polarity, subjectivity, and sentiment classification
    """
    if not text or text.strip() == "":
        return {
            'error': 'Please enter some text to analyze'
        }
    
    # Create TextBlob object
    blob = TextBlob(text)
    
    # Get polarity and subjectivity
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Classify sentiment based on polarity
    if polarity > 0.1:
        sentiment = 'Positive'
    elif polarity < -0.1:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return {
        'text': text,
        'polarity': round(polarity, 3),
        'subjectivity': round(subjectivity, 3),
        'sentiment': sentiment,
        'polarity_description': get_polarity_description(polarity),
        'subjectivity_description': get_subjectivity_description(subjectivity)
    }

def get_polarity_description(polarity):
    """Get human-readable description of polarity score"""
    if polarity > 0.5:
        return "Very Positive"
    elif polarity > 0.1:
        return "Positive"
    elif polarity > -0.1:
        return "Neutral"
    elif polarity > -0.5:
        return "Negative"
    else:
        return "Very Negative"

def get_subjectivity_description(subjectivity):
    """Get human-readable description of subjectivity score"""
    if subjectivity > 0.7:
        return "Very Subjective (Opinion-based)"
    elif subjectivity > 0.3:
        return "Moderately Subjective"
    else:
        return "Objective (Fact-based)"

@app.route('/')
def index():
    """Main page with sentiment analysis form"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """API endpoint for sentiment analysis"""
    if request.is_json:
        data = request.get_json()
        text = data.get('text', '')
    else:
        text = request.form.get('text', '')
    
    result = analyze_sentiment(text)
    
    if request.is_json:
        return jsonify(result)
    else:
        return render_template('result.html', result=result)

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    """JSON API endpoint for sentiment analysis"""
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    result = analyze_sentiment(data['text'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
