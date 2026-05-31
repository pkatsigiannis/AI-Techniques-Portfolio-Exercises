import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Claculated Entropy
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy_value = -np.sum([
        (counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts))
        for i in range(len(elements))
    ])
    return entropy_value


# Calculates IG
def information_gain(data, feature, target="Class"):
    total_entropy = entropy(data[target])
    values, counts = np.unique(data[feature], return_counts=True)

    weighted_entropy = np.sum([
        (counts[i] / np.sum(counts)) *
        entropy(data[data[feature] == values[i]][target])
        for i in range(len(values))
    ])

    return total_entropy - weighted_entropy


# Creates Decision Tree recursively
def id3(data, original_data, features, target="Class", parent_node_class=None):

    if len(np.unique(data[target])) == 1:
        return np.unique(data[target])[0]

    if len(data) == 0:
        return np.unique(original_data[target])[np.argmax(
        np.unique(original_data[target], return_counts=True)[1])]

    if len(features) == 0:
        return parent_node_class
    
    parent_node_class = np.unique(data[target])[np.argmax(
    np.unique(data[target], return_counts=True)[1])]

    gains = [information_gain(data, feature, target) for feature in features]
    best_feature = features[np.argmax(gains)]

    tree = {best_feature: {}}
    features = [f for f in features if f != best_feature]

    for value in np.unique(data[best_feature]):
        subset = data[data[best_feature] == value]
        subtree = id3(subset, original_data, features, target, parent_node_class)
        tree[best_feature][value] = subtree

    data = pd.DataFrame({...})
    features = list(data.columns[:-1])
    tree = id3(data, data, features)
    print(tree)