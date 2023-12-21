import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    # Check if the value is NaN
    if pd.isnull(text):
        return ''
    
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
output_file_path = 'preprocessed_data_with_tfidf.csv'

# Assuming 'Email Text' is the correct column name for email content
# and 'Email Type' is the correct column name for the label
df = pd.read_csv(input_file_path)

# Apply preprocessing to each email content
df['Processed_Content'] = df['Email Text'].apply(lambda x: clean_text(x))
df['Processed_Content'] = df['Processed_Content'].apply(lambda x: tokenize_text(x))
df['Processed_Content'] = df['Processed_Content'].apply(lambda x: remove_stopwords(x))
df['Processed_Content'] = df['Processed_Content'].apply(lambda x: lemmatize_tokens(x))

# Convert processed content to text
df['Processed_Content_Text'] = df['Processed_Content'].apply(lambda x: ' '.join(x))

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust max_features as needed
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Processed_Content_Text'])

# Convert the TF-IDF matrix to a DataFrame
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

# Concatenate TF-IDF matrix with the original labels
final_data = pd.concat([tfidf_df, df['Email Type']], axis=1)

# Save the final processed data with numerical features to a new CSV file
final_data.to_csv(output_file_path, index=False)

print(f"Final processed data saved to: {output_file_path}")
