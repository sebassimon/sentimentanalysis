import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Load the TSV file
file_path = '/Users/Desktop/folder/weather/amazon.tsv'
data = pd.read_csv(file_path, sep='\t')

# Preprocessing function
def preprocess_text(text):
    if not isinstance(text, str):
        return ''  # If text is not a string (e.g., NaN), return an empty string
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    tokens = word_tokenize(text)  # Tokenize
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return ' '.join(tokens)

# Apply the preprocessing function to review texts
data['cleaned_reviews'] = data['verified_reviews'].apply(preprocess_text)

# Sentiment Analysis with VADER
sia = SentimentIntensityAnalyzer()

# Assign a sentiment score to each review
data['sentiments'] = data['cleaned_reviews'].apply(lambda x: sia.polarity_scores(x))
data['compound'] = data['sentiments'].apply(lambda score_dict: score_dict['compound'])
data['sentiment_type'] = data['compound'].apply(lambda c: 'positive' if c > 0 else ('negative' if c < 0 else 'neutral'))

# Aggregate sentiment scores for analysis
sentiment_counts = data['sentiment_type'].value_counts(normalize=True)
print(sentiment_counts)

# Export the data with sentiment scores for visualization
output_file = 'processed_amazon_reviews.csv'
data.to_csv(output_file, index=False)
print(f"Processed data saved to {output_file}")
