# CS 344 Final Project -- Lyrics Generator

This project aims to generate lyrics based off of Pink Floyd's work.

I used two resources that I based my code off of:  
https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/  
https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/8.1-text-generation-with-lstm.ipynb  

The dataset I am using comes from https://www.kaggle.com/mousehead/songlyrics and contains 57650 songs. I am only using the ones with Pink Floyd as the artist. songdata.csv must be stored in a folder named "data".

## Project Structure

This project contains 8 files. Four of these files are dedicated to training various models:  
  - build_char_model.py: This file trains a character model based on the machinelearningmastery tutorial mentioned above
  - build_char_model_stateful.py: This is the exact same as build_char_model.py but trains a stateful version of the LSTM
  - build_model.py: My attempt at converting to a word-generating system from a character-generating system
  - build_chollet_model.py: This file trains a model akin to Chollet's model in Chapter 8.1 of Deep Learning with Python.
The other four files are dedicated to running these models and are named according to the model file it accompanies.

In addition to the files, there are four folders that hold the weights for the four network models. I have included only one example weights file for testing purposes, but the training files will generate one per epoch.

## Python Version

To run this project I am using Python 3.7 with the requirements.txt found in this repository's head directory.


