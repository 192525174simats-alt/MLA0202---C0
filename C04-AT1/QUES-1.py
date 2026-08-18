print("Bayesian Network for Disease Prediction")

# Prior probabilities
P_Obesity = {
    "No": 0.7,
    "Yes": 0.3
}

P_HighSugar = {
    "No": 0.6,
    "Yes": 0.4
}

# Conditional Probability Table for Diabetes
P_Diabetes = {
    ("No", "No"): 0.01,
    ("No", "Yes"): 0.20,
    ("Yes", "No"): 0.10,
    ("Yes", "Yes"): 0.70
}

# Evidence
obesity = "Yes"
high_sugar = "Yes"

# Bayesian inference
probability = P_Diabetes[(obesity, high_sugar)]

print("\nBayesian Network:")
print("Obesity -> Diabetes")
print("High Blood Sugar -> Diabetes")

print("\nEvidence:")
print("Obesity =", obesity)
print("High Blood Sugar =", high_sugar)

print("\nPredicted Probability of Diabetes:")
print(probability)

print("Predicted Probability of Diabetes:", probability * 100, "%")
