print("Hidden Markov Model for Weather Prediction")

states = ["Sunny", "Cloudy", "Rainy"]

observations = ["Dry", "Wet", "Wet", "Dry"]

transition = {
    "Sunny": {
        "Sunny": 0.7,
        "Cloudy": 0.2,
        "Rainy": 0.1
    },
    "Cloudy": {
        "Sunny": 0.3,
        "Cloudy": 0.4,
        "Rainy": 0.3
    },
    "Rainy": {
        "Sunny": 0.2,
        "Cloudy": 0.3,
        "Rainy": 0.5
    }
}

emission = {
    "Sunny": {
        "Dry": 0.8,
        "Wet": 0.2
    },
    "Cloudy": {
        "Dry": 0.5,
        "Wet": 0.5
    },
    "Rainy": {
        "Dry": 0.1,
        "Wet": 0.9
    }
}

initial = {
    "Sunny": 0.5,
    "Cloudy": 0.3,
    "Rainy": 0.2
}

probability = {}
path = {}

for state in states:
    probability[state] = (
        initial[state] *
        emission[state][observations[0]]
    )
    path[state] = [state]

for i in range(1, len(observations)):

    new_probability = {}
    new_path = {}

    for current_state in states:

        best_probability = 0
        best_previous_state = ""

        for previous_state in states:

            p = (
                probability[previous_state] *
                transition[previous_state][current_state] *
                emission[current_state][observations[i]]
            )

            if p > best_probability:
                best_probability = p
                best_previous_state = previous_state

        new_probability[current_state] = best_probability

        new_path[current_state] = (
            path[best_previous_state] +
            [current_state]
        )

    probability = new_probability
    path = new_path

best_state = max(probability, key=probability.get)

print("\nObservations:")
print(observations)

print("\nPredicted Hidden Weather States:")
print(path[best_state])
