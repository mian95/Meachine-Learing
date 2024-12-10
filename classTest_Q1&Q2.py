"""
Q1: Import diabetes dataset and split data into training and testing sets for the following ratios: 50/50, 60/40, 70/30, 90/10, Report number of instances in training and testing sets for each ratio.

Q2: Import wine dataset and split data into training and testing sets for the following ratios: 50/50, 60/40, 70/30, 90/10. Report number of instances in training and testing sets for each ratio.
"""

# Importing models
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split


x,y = load_wine(return_X_y=True)

print("For the Wine Dataset")
split_ratios = [0.5, 0.4, 0.3, 0.1]  # Test sizes for 50/50, 60/40, 70/30, 90/10 splits

for test_size in split_ratios:
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    print(f"\nFor {int((1-test_size)*100)}/{int(test_size*100)} split_size:")
    print(f"Testing Set Size: {len(x_test)} Instances")
    print(f"Training Set Size: {len(x_train)} Instances")

