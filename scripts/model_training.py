import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import joblib

def load_data(file_path):
    """Load cleaned data from CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded from {file_path}")
        print(f"Columns in DataFrame: {df.columns.tolist()}")
        return df
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None

def preprocess_data(df):
    """Preprocess the data by extracting features and labels, and converting text data to numerical features."""
    # Adjust column names based on the actual CSV
    if 'data' not in df.columns:
        raise ValueError("Dataframe must contain 'data' column.")
    
    # Assuming 'data' column contains the text for analysis, and we'll need a target column
    # For demonstration, we'll assume that 'data' is the text and we'll create dummy labels
    X = df['data']
    y = df.get('label', None)  # You need to have some label column for supervised learning; adjust accordingly
    
    # For now, let's assume y is not available and create dummy labels if needed
    if y is None:
        # Dummy labels (replace with actual labels if available)
        y = ['dummy_label'] * len(X)
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X)
    
    return X, y, vectorizer

def train_model(X_train, y_train):
    """Train a machine learning model."""
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model."""
    y_pred = model.predict(X_test)
    print("Model Evaluation:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

def save_model(model, vectorizer, model_file, vectorizer_file):
    """Save the trained model and vectorizer to files."""
    joblib.dump(model, model_file)
    joblib.dump(vectorizer, vectorizer_file)
    print(f"Model saved to {model_file}")
    print(f"Vectorizer saved to {vectorizer_file}")

# Main execution
if __name__ == "__main__":
    # File paths
    cleaned_data_file = 'cleaned_hospital_data.csv'
    model_file = 'model.pkl'
    vectorizer_file = 'vectorizer.pkl'
    
    # Load and preprocess data
    df = load_data(cleaned_data_file)
    if df is not None:
        X, y, vectorizer = preprocess_data(df)
        
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model
        model = train_model(X_train, y_train)
        
        # Evaluate the model
        evaluate_model(model, X_test, y_test)
        
        # Save the trained model and vectorizer
        save_model(model, vectorizer, model_file, vectorizer_file)
