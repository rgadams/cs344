# Load LSTM network and generate text
import sys
import numpy
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
df_pinkfloyd = df_pinkfloyd.apply(lambda x: x.astype(str).str.replace(r"\\n", ""))
df_pinkfloyd = df_pinkfloyd.apply(lambda x: x.astype(str).str.replace(r"\.\.\.", ""))
raw_text = ' '.join(map(str, df_pinkfloyd['text']))

# create mapping of unique chars to integers
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

# # summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

# # prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)

# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))

# normalize
X = X / float(n_vocab)
print(X.shape)

# one hot encode the output variable
y = np_utils.to_categorical(dataY)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, batch_input_shape=(1, X.shape[1], X.shape[2]), return_sequences=True, stateful=True))
model.add(Dropout(0.2))
model.add(LSTM(128, return_sequences=True, stateful=True))
model.add(Dropout(0.2))
model.add(LSTM(128, return_sequences=True, stateful=True))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# define the checkpoint
filepath="stateful/weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

# fit the model
model.fit(X, y, epochs=5, batch_size=1, callbacks=callbacks_list)