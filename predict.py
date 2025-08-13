import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

def predict_message(message):
    message_vec = vectorizer.transform([message])
    prediction = model.predict(message_vec)[0]
    return "Spam" if prediction == 1 else "Ham"