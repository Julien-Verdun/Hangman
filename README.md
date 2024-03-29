# Hangman

This project includes an implementation of the famous game Hangman, programmed with the graphical interface Tkinter on Python.

This project was implemented in November 2017 by Julien Verdun. It is part of a school project (first year of engineer school) that aims at learning object oriented programming.

Two versions of the game was implemented :

- the first one is the basic version, with only the game and nothing else. It was the goal of the school project.
- the second one is a more advanced version, with other possibilities (create a player profile and monitor his score).

You can play the game by running with python either "Hangman_simple_version.py" or "Hangman_complex_version.py". If you don't have python installed, you can run the executables included on both folders "Hangman_simple_version" and "Hangman_complex_version". 

## The simple version

The rules of the games are pretty simple. 
Start a new game, a word is randomly generated, the goal is to find this word by pressing the letters with less than the number of mistakes allowed : 8 mistakes.
Whenever a mistake is done, the drawing of the hangman is updated and a new member of his body is drawn on the window. 


This version uses shapes created on Tkinter (circles, rectangles, squares and so one).


## The advanced version



This version uses the same game logic but here the hangman is displayed by means of images (instead of shapes).

On this version you can sign up by fill in your name and your scre will be registered. 


## Demonstration of the game

#### The simple version :

![simple_version_demo](simple_version_demo.PNG)

#### The improved version :

![improved_version_demo](improved_version_demo.PNG)


By the way, the words to guess are French words, sorry for that !

Good luck and have fun !! 



