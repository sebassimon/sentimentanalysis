<h1>Analyzing E-commerce Customer Reviews</h1>

### [Medium Article Demonstration](https://medium.com/@sebastienwebdev/sentiment-analysis-on-e-commerce-reviews-c3c42edffb13)

<h2>Description</h2>
<p>This project employs sentiment analysis to explore customer reviews on e-commerce platforms like Amazon, offering insights into consumer behavior and satisfaction. It utilizes Natural Language Processing (NLP) to analyze emotions expressed in customer feedback.</p>

<h2>Environment & Utilities Used</h2>
<ul>
  <li><b>Python</b></li>
  <li><b>NLTK for NLP</b></li>
  <li><b>Pandas for data manipulation</b></li>
</ul>

<h2>Program Walk-through:</h2>

<h3>1. Data Preparation</h3>
<p>Using Python and libraries like pandas and NLTK to prepare and analyze text data.</p>

<h3>2. Sentiment Analysis</h3>
<pre><code>
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
</code></pre>

<h3>3. Download necessary NLTK resources </h3>
<pre><code>nltk.download('vader_lexicon') </code></pre>

<h3>4. Load data and preprocess</h3>
<pre><code>data['sentiment_scores'] = data['reviews'].apply(lambda x: SentimentIntensityAnalyzer().polarity_scores(x))
</code></pre>


<h3>5. Aggregate Sentiment Scores</h3>
<pre><code>
data['sentiment_type'] = data['sentiment_scores'].apply(lambda score: 'positive' if score['compound'] > 0 else 'negative')
sentiment_counts = data['sentiment_type'].value_counts()
</code></pre>


<h2>Conclusion</h2>
<p>The use of sentiment analysis helps e-commerce platforms enhance product development and customer service by understanding consumer preferences and satisfaction from their reviews.</p>
