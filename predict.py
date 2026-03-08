import joblib

model = joblib.load("phishing_model.pkl")

def detect_phishing(url):

    prediction = model.predict([url])[0]

    if prediction == 1:
        return "Phishing Website"
    else:
        return "Safe Website"
