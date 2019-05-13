# Load LSTM network and generate text
import sys
import numpy
import string
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Flatten
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# load ascii text and covert to lowercase
filename = "data\\songdata.csv"
df_songs = pd.read_csv(filename)
df_pinkfloyd = df_songs.loc[df_songs['artist'] == 'Pink Floyd']
df_pinkfloyd = df_pinkfloyd.apply(lambda x: x.astype(str).str.lower())
df_pinkfloyd = df_pinkfloyd.apply(lambda x: x.astype(str).str.replace(r"\n", ""))
df_pinkfloyd = df_pinkfloyd.apply(lambda x: x.astype(str).str.replace(r"\.\.\.", ""))
raw_text = ' '.join(map(str, df_pinkfloyd['text']))
raw_text.translate(str.maketrans('', '', string.punctuation))

# create mapping of unique chars to integers
unique_words = list(set(raw_text.split()))
words = list(raw_text.split())

word_to_int = dict((c, i) for i, c in enumerate(unique_words))
int_to_word = dict((i, c) for i, c in enumerate(unique_words))

# summarize the loaded data
n_words = len(words)
print("Total Vocab: ", n_words)

# prepare the dataset of input to output pairs encoded as integers
seq_length = 6
dataX = []
dataY = []
for i in range(0, n_words - seq_length, 1):
	seq_in = words[i:i + seq_length]
	seq_out = words[i + seq_length]
	dataX.append([word_to_int[word] for word in seq_in])
	# print("x: ", [word_to_int[word] for word in seq_in])
	dataY.append(word_to_int[seq_out])
	# print("y: ", word_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)

# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))

# normalize
X = X / float(n_words)
print(X.shape)

# one hot encode the output variable
y = np_utils.to_categorical(dataY)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128, return_sequences=True))
model.add(Flatten())
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

# load the network weights
filename = "words\\weights-improvement-10-6.5060.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

# pick a random starting point
start = numpy.random.randint(0, len(dataX)-1)
pattern = dataX[start]

# generate characters
for i in range(100):
	x = numpy.reshape(pattern, (1, len(pattern), 1))
	x = x / float(n_words)
	prediction = model.predict(x, verbose=0)
	index = numpy.argmax(prediction)
	result = int_to_word[index]
	seq_in = [int_to_word[value] for value in pattern]
	sys.stdout.write(result + " ")
	pattern.append(index)
	pattern = pattern[1:len(pattern)]

print("\n\nDone.")