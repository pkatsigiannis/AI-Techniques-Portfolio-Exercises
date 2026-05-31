import pandas as pd
import numpy as np


# Calculates Entropy
def entropy(target_col):
    classes, counts = np.unique(target_col, return_counts=True)
    total = np.sum(counts)

    entropy_value = -np.sum([
        (counts[i] / total) * np.log2(counts[i] / total)
        for i in range(len(classes))
    ])

    return entropy_value


# Calculates Information Gain
def information_gain(data, feature, target="Pass?"):
    total_entropy = entropy(data[target])

    values, counts = np.unique(data[feature], return_counts=True)
    total = np.sum(counts)

    weighted_entropy = np.sum([
        (counts[i] / total) *
        entropy(data[data[feature] == values[i]][target])
        for i in range(len(values))
    ])

    return total_entropy - weighted_entropy


# Builds the ID3 decision tree recursively
def id3(data, original_data, features, target="Pass?", parent_node_class=None):

    # If all examples have the same class, return that class
    if len(np.unique(data[target])) == 1:
        return np.unique(data[target])[0]

    # If the subset is empty, return the majority class from the original dataset
    if len(data) == 0:
        classes, counts = np.unique(original_data[target], return_counts=True)
        return classes[np.argmax(counts)]

    # If no attributes remain, return the majority class of the parent node
    if len(features) == 0:
        return parent_node_class

    # Determine the majority class of the current node
    classes, counts = np.unique(data[target], return_counts=True)
    parent_node_class = classes[np.argmax(counts)]

    # Calculate Information Gain for each available attribute
    gains = [information_gain(data, feature, target) for feature in features]

    # Select the attribute with the highest Information Gain
    best_feature = features[np.argmax(gains)]

    # Create the tree node
    tree = {best_feature: {}}

    # Remove the selected attribute from the remaining attributes
    remaining_features = [f for f in features if f != best_feature]

    # Create one branch for each value of the selected attribute
    for value in np.unique(data[best_feature]):
        subset = data[data[best_feature] == value]

        subtree = id3(
            subset,
            original_data,
            remaining_features,
            target,
            parent_node_class
        )

        tree[best_feature][value] = subtree

    return tree


# Dataset from Portfolio Exercise 5.2
data = pd.DataFrame({
    "Study Hours": [
        "High", "High", "High", "High",
        "Medium", "Medium", "Medium", "Medium", "Medium",
        "Low", "Low", "Low", "Low",
        "Medium"
    ],
    "Attendance": [
        "Regular", "Regular", "Irregular", "Irregular",
        "Regular", "Regular", "Irregular", "Irregular", "Regular",
        "Regular", "Regular", "Irregular", "Regular",
        "Irregular"
    ],
    "Sleep Quality": [
        "Good", "Poor", "Good", "Poor",
        "Good", "Poor", "Good", "Good", "Good",
        "Good", "Poor", "Poor", "Good",
        "Poor"
    ],
    "Revision Done": [
        "Yes", "Yes", "Yes", "No",
        "Yes", "No", "No", "Yes", "No",
        "Yes", "No", "No", "No",
        "Yes"
    ],
    "Pass?": [
        "Yes", "Yes", "Yes", "No",
        "Yes", "No", "No", "Yes", "Yes",
        "No", "No", "No", "No",
        "No"
    ]
})


features = list(data.columns[:-1])

print("Initial Entropy:")
print(entropy(data["Pass?"]))

print("\nInformation Gain for each attribute:")
for feature in features:
    print(feature, ":", information_gain(data, feature, "Pass?"))

tree = id3(data, data, features, target="Pass?")

print("\nFinal Decision Tree:")
print(tree)
