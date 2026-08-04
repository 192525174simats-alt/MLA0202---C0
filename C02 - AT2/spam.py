from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

emails = [
    "Win a free prize now",
    "Congratulations you won a lottery",
    "Claim your free money",
    "You are a lucky winner",
    "Get a free gift today",
    "Please attend the meeting tomorrow",
    "Submit your assignment by Monday",
    "Your project report is ready",
    "The class starts at 10 AM",
    "Please send the project file"
]

labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(emails)

model = LogisticRegression()

model.fit(X, labels)

new_email = input("Enter a new email: ")

new_email_features = vectorizer.transform([new_email])

prediction = model.predict(new_email_features)

print("\n================================")
print("       EMAIL CLASSIFICATION")
print("================================")
print("Email:", new_email)

if prediction[0] == 1:
    print("Result: SPAM")
else:
    print("Result: NON-SPAM")

print("================================")
