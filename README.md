# Telephone-interception
These codes are the Python code implementation of a machine learning phone interception project
## The Task
A mobile system based on Android that directly intercepts most users who hang up and classify them as harassing phone numbers. With the development of recommendation functions and the complexity of different types of marketing calls in real-world environments, we hope to update this feature. We decided to use the collected data of 10000 phone numbers containing multiple information for classification, and use machine learning models to divide the phone into harassing calls and partially effective marketing calls, distinguishing and intercepting harassing calls and some potentially useful marketing calls.
## Code Description
### data.py
In the data.py file, we preprocessed the input data by first setting labels for each piece of data, then encoding each non numeric attribute with one hot encoding, and finally encapsulating it into a function for calling the main function.
### plot.py
In the plot.py file, we designed the visualization section of our project code. Our visualization consists of two parts: one is the visualization confusion matrix, which is a 2x2 matrix with the x-axis representing predicted attributes and the y-axis representing actual attributes. Through the confusion matrix, recall, accuracy, specificity, accuracy, etc. can be conveniently measured. Another part is the visualization of the ROC curve, which calculates parameters such as AOC, We can clearly see the classification ability of our model, and all visualizations are saved in the eva folder.
### evaluate.py
For the convenience of function calls, we have encapsulated all the functions of the evaluation model in evaluate.py. By calling this function, we can calculate the accuracy, F1 score, interception rate, and interception success rate of the model.
### main.py
The main model is implemented in main.py. First, we instantiate various machine learning models, then call training functions to train the models, and finally evaluate and visualize the models. All visualization results can be queried in Eva folder.
