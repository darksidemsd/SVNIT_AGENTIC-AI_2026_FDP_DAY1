import pickle

# Load saved model and vectorizer
model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

print("\n📩 Email Spam Detector")
print("Type a message and press Enter (or type 'exit' to quit)\n")

while True:
    msg = input("Enter message: ")

    if msg.lower() == "exit":
        print("Goodbye 👋")
        break

    msg_vec = vectorizer.transform([msg])
    prediction = model.predict(msg_vec)[0]

    if prediction == 1:
        print("🚨 SPAM detected!\n")
    else:
        print("✅ NOT spam\n")