import numpy as np
import pandas as pd
from keras.datasets import boston_housing

# Acquire the data from keras.datasets
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

'''
Targets are the median values of the houses at a location, so our synthetic feature must be valuable towards that goal.
I found the features here: https://mc.ai/boston-housing-prediction-using-keras/
For my feature I focused on transportation. I looked at DIS: weighted distances to five Boston employment centers and 
RAD: index of accessibility to radial highways. My feature took the ratio of RAD / DIS. I believe this could help with 
determining median house value as the harder it is to get to a place of work can be compounded by a long distance.
'''
cols = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']

train_data = pd.DataFrame(train_data)
train_data.columns = cols

train_data['RAD-DIS'] = train_data['RAD'] / train_data['DIS']

test_x = pd.DataFrame(test_data)
test_x.columns = cols

# Create the synthetic feature RAD-DIS
test_x['RAD-DIS'] = test_x['RAD'] / test_x['DIS']

# Create a random mask that sets aside 30% of the training data for validation
mask = np.random.rand(train_data.shape[0]) < 0.7

# Apply the mask to separate training data from validation data
train_x = train_data[mask]
train_y = train_targets[mask]

validation_x = train_data[~mask]
validation_y = train_targets[~mask]

print("Training data shape:", train_x.shape)
print("Training labels shape:", train_y.shape)
print("Validation data shape:", validation_x.shape)
print("Validation labels shape:", validation_y.shape)
print("Testing data shape:", test_x.shape)
print("Testing labels shape:", test_targets.shape)


