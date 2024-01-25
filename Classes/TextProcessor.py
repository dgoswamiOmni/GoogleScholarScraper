import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import nltk

class TextProcessor:
    def __init__(self, text_column_name):
        self.text_column_name = text_column_name
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        # Tokenize and lemmatize
        words = word_tokenize(text.lower())
        words = [self.lemmatizer.lemmatize(word) for word in words if word.isalpha()]  # Keep only alphabetic words
        words = [word for word in words if word not in self.stop_words]
        return words

    def process_dataframe(self, df):
        # Apply preprocessing to the specified text column
        df['processed_text'] = df[self.text_column_name].apply(self.preprocess_text)

        # Flatten the list of processed words
        all_words = [word for sublist in df['processed_text'].tolist() for word in sublist]

        # Count the occurrences of each word
        word_counts = Counter(all_words)

        # Find the most common words and their frequencies
        most_common_words = word_counts.most_common()

        # Create a dictionary from the most common words
        most_common_dict = dict(most_common_words)

        return most_common_dict




# print(result_dict)
