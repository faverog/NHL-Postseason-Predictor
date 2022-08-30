# NHL-Postseason-Predictor

### An Introductory Machine Learning Project
Gian Favero, 2021

This Machine Learning based Python script aims to predict the winner of a 7 game NHL series based on the game/team data compiled and a Support Vector Machine algorithm using the SciKit Learn, Pandas, and NumPy libraries. Team data was compiled over the course of the 2021 NHL season. 

A SVM model is used to categorize team performances into a typical "Win" or "Loss", such that when two teams meet in the playoffs, the result of the series can be decided based on if the opponents' stats fell into the "Win" or "Loss" category. This is a preliminary model, which had slim success according to the real data.

## Getting Started
First, clones this repository. 

The runnable program lies in a single script, `SVM Script.py`. In here, Lines 70-71 can be adjusted to predict a the winner of a series between two NHL teams. A sample series between the Edmonton Oilers and the Tampa Bay Lightning is provided. In this case, the program outputs a 'W', indicating that Edmonton is the predictable winner of the series.
