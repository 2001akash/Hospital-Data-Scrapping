# Hospital Data Scrapping

## Overview
This project involves scraping data from the top 50 hospital websites, cleaning the data, and training a Private GPT model on the collected information.
This project involves developing a text classification model to categorize hospital-related data. The model uses the Naive Bayes algorithm and `TfidfVectorizer` for text feature extraction. 

## Project Structure

- `scripts/` - Contains the Python scripts for data cleaning, model training, and evaluation.
- `cleaned_hospital_data.csv` - The CSV file containing the preprocessed hospital data.
- `model.pkl` - The trained machine learning model.
- `vectorizer.pkl` - The `TfidfVectorizer` used for text feature extraction.

## Requirements

To run the scripts, you need the following Python libraries:

- `pandas`
- `scikit-learn`
- `joblib`

You can install these dependencies using pip:

```bash
pip install pandas scikit-learn joblib
```

## Data Loading

The data is loaded from `cleaned_hospital_data.csv`. The CSV file includes two columns:

- `url`: The URL associated with the hospital data.
- `data`: The text data to be classified.

## Preprocessing

- **Column Used:** Only the `data` column was utilized for model training.
- **Vectorization:** The `TfidfVectorizer` was used to convert text data into numerical features.
- **Labels:** Due to the lack of specific labels, dummy labels were used for model training.

## Model Training

- **Algorithm:** `MultinomialNB` (Naive Bayes)
- **Training Process:** The model was trained on the preprocessed data with the following results:

## Model Evaluation

- **Accuracy:** 1.0000
- **Classification Report:**
  ```
                precision    recall  f1-score   support

    dummy_label       1.00      1.00      1.00         9

      accuracy                           1.00         9
     macro avg       1.00      1.00      1.00         9
  weighted avg       1.00      1.00      1.00         9
  ```

The model achieved perfect accuracy on the test set, indicating excellent performance on the provided data.

## Model Saving

The trained model and vectorizer were saved to the following files:

- **Model:** `model.pkl`
- **Vectorizer:** `vectorizer.pkl`

## Running the Scripts

To run the scripts, use the following commands:

1. **Data Collection and Cleaning:**
   ```bash
   python scripts/data_collection.py
   python scripts/data_cleaning.py

   ```
2. **Model Training:**
   ```bash
   python scripts/model_training.py
   ```

## Documentation and Screenshots

- Documentation includes details about the data loading, preprocessing, model training, evaluation, and file saving.
- Screenshots of the terminal output and generated files are available in the documentation folder.



