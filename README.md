# Sentiment Analysis Web Application

A Flask-based web application that performs sentiment analysis on user-entered text using TextBlob. The application classifies text as positive, negative, or neutral and displays polarity and subjectivity scores.

## Features

- **Real-time Sentiment Analysis**: Analyze any text for emotional tone
- **Three-way Classification**: Positive, Negative, or Neutral sentiment
- **Detailed Scores**: Polarity (-1 to +1) and Subjectivity (0 to 1) scores
- **User-friendly Interface**: Clean, responsive web design
- **API Support**: JSON API endpoint for programmatic access

## Installation

1. **Clone or download the project**
2. **Navigate to the project directory**:
   ```bash
   cd sentiment_analysis_app
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download TextBlob corpora** (required for sentiment analysis):
   ```bash
   python -m textblob.download_corpora
   ```

## Usage

### Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Web Interface

1. Open your browser and navigate to `http://localhost:5000`
2. Enter text in the provided text area
3. Click "Analyze Sentiment" to see results

### API Usage

You can also use the API endpoint:

```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
```

## API Endpoints

- `GET /` - Main web interface
- `POST /analyze` - Web form submission
- `POST /api/analyze` - JSON API endpoint

## Response Format

The API returns JSON with the following structure:

```json
{
  "text": "The analyzed text",
  "polarity": 0.8,
  "subjectivity": 0.75,
  "sentiment": "Positive",
  "polarity_description": "Very Positive",
  "subjectivity_description": "Very Subjective (Opinion-based)"
}
```

## How It Works

1. **Text Processing**: User input is processed using TextBlob
2. **Sentiment Analysis**: TextBlob calculates polarity (-1 to +1) and subjectivity (0 to 1)
3. **Classification**: Based on polarity:
   - > 0.1: Positive
   - < -0.1: Negative
   - Otherwise: Neutral
4. **Results Display**: Scores and classifications are displayed with human-readable descriptions

## Technologies Used

- **Flask**: Web framework
- **TextBlob**: Sentiment analysis library
- **Bootstrap**: Frontend styling
- **Font Awesome**: Icons

