from keras.datasets import boston_housing
import numpy

((train_data, train_labels), (test_data, test_labels)) = boston_housing.load_data()

def print_structures():
    print(
        'training data \
            \n\tcount:', len(train_data),
            '\n\tdimensions:', train_data.ndim,
            '\n\tshape:', train_data.shape,
            '\n\tdata type:', train_data.dtype, '\n\n',
        'training labels \
            \n\tcount:', len(train_labels),
            '\n\tdimensions:', train_labels.ndim,
            '\n\tshape:', train_labels.shape,
            '\n\tdata type:', train_labels.dtype, '\n\n',
        'test data \
            \n\tcount:', len(test_data),
            '\n\tdimensions:', test_data.ndim,
            '\n\tshape:', test_data.shape,
            '\n\tdata type:', test_data.dtype, '\n\n',
        'testing labels \
            \n\tcount:', len(test_labels),
            '\n\tdimensions:', test_labels.ndim,
            '\n\tshape:', test_labels.shape,
            '\n\tdata type:', test_labels.dtype, '\n\n',
    )
print_structures()
