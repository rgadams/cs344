import keras
import numpy as np
import pandas as pd
from keras import layers
from keras.callbacks import ModelCheckpoint
import string
import random
import sys

# path = keras.utils.get_file(
#     'nietzsche.txt',
#     origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt')
# text = open(path).read().lower()
filename = "data\\songdata.csv"
df_songs = pd.read_csv(filename)
df_pinkfloyd = df_songs.loc[df_songs['artist'] == 'Pink Floyd']
df_pinkfloyd = df_pinkfloyd.apply(lambda x: x.astype(str).str.lower())
# df_pinkfloyd = df_pinkfloyd.apply(lambda x: x.astype(str).str.replace(r"\n", ""))
df_pinkfloyd = df_pinkfloyd.apply(lambda x: x.astype(str).str.replace(r"\.\.\.", ""))
text = ' '.join(map(str, df_pinkfloyd['text']))
# text.translate(str.maketrans('', '', string.punctuation))
print('Corpus length:', len(text))

# Length of extracted character sequences
maxlen = 60

# We sample a new sequence every `step` characters
step = 3

# This holds our extracted sequences
sentences = []

# This holds the targets (the follow-up characters)
next_chars = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('Number of sequences:', len(sentences))

# List of unique characters in the corpus
chars = sorted(list(set(text)))
print('Unique characters:', len(chars))
# Dictionary mapping unique characters to their index in `chars`
char_indices = dict((char, chars.index(char)) for char in chars)

# Next, one-hot encode the characters into binary arrays.
print('Vectorization...')
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

model = keras.models.Sequential()
model.add(layers.LSTM(128, input_shape=(maxlen, len(chars))))
model.add(layers.Dense(len(chars), activation='softmax'))

optimizer = keras.optimizers.RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

for epoch in range(1, 20):
    print('epoch', epoch)
    filepath="chollet/weights-improvement-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    # Fit the model for 1 epoch on the available training data
    model.fit(x, y,
              batch_size=128,
              epochs=1,
              callbacks=callbacks_list)
