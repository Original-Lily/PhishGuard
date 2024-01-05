# PhishGuard

## Key Features pre-Learning

Phish Guard uses the following stages in order to predict the safety of an email:

- **DataCollection:** Emails to train and test from are sourced for free from [kaggle](https://www.kaggle.com/datasets/subhajournal/phishingemails)!

- **Data Interpretation & Pre-processing:** involving tasks such as removing irrelevant characters, handling misspellings, and tokenizing the text into words.

- **Feature extraction:** Converting the text data into numerical features that can be used as input for machine learning models. TF-IDF (Term Frequency-Inverse Document Frequency) was employed for this stage.

## Accuracy & Training

- **Logistic Regression** was employed via the sciKit-learn module in order to intake this data and make predictions

- The dataset imported is split into an 80% training portion and a 20% testing portion
- As shown below this model is able to make correct predictions roughly 96.75
- Precision for 'Phishing Email': 95% (of the instances predicted as phishing, 95% are correct).
- Precision for 'Safe Email': 98% (of the instances predicted as safe, 98% are correct).

        Accuracy: 0.967024128686327
        Classification Report:
                        precision    recall  f1-score   support
        
        Phishing Email       0.95      0.96      0.96      1457
            Safe Email       0.98      0.97      0.97      2273
        
              accuracy                           0.97      3730
             macro avg       0.96      0.97      0.97      3730
          weighted avg       0.97      0.97      0.97      3730


## Setup and Running Yourself

1. Clone the repository:

    ```bash
    git clone git://github.com/Original-Lily/PhishGuard.git
    ```
    
2. Begin program in full via:

   ```bash
    python main.py "{string input}"
    ```
    <i>ensure the string input is accompanied by quotations ""</i>
   
3. (Optional) Ensure your modules are installed/ up-to-date:

    ```bash
    Do you want to install dependencies? (y/n): y
    Collecting nltk==3.6.3 (from -r requirements.txt (line 1))
    Collecting pandas==1.3.3 (from -r requirements.txt (line 2))
    etc...
    ```
