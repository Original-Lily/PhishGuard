import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    return text

def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens

def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

# Read Excel file
input_file_path = 'Archive/Phishing_Email.csv'
output_file_path = 'preprocessed_data.csv'

df = pd.read_excel(input_file_path)

# Apply preprocessing to each email content
df['Processed_Content'] = df['Email_Content'].apply(lambda x: clean_text(x))
df['Processed_Content'] = df['Processed_Content'].apply(lambda x: tokenize_text(x))
df['Processed_Content'] = df['Processed_Content'].apply(lambda x: remove_stopwords(x))
df['Processed_Content'] = df['Processed_Content'].apply(lambda x: lemmatize_tokens(x))

# Save preprocessed data to a new CSV file
df.to_csv(output_file_path, index=False)

print(f"Preprocessed data saved to: {output_file_path}")
