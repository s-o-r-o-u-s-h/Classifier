# Classifier
#### Current version: 0.1 dev
Basic software for classification a data set based on data mining concepts. This application just works with full categorical attributes and a data set without 
any missing values. Surely there are bugs in that and I'll trying to fix them. Stay tuned for updates!

## Requirements:

1. ***python 3.3+***: You can download it from [here](http:www.python.org)

2. ***Numpy***: You can download it from [here](http://sourceforge.net/projects/numpy/files/NumPy/1.9.1/)

3. ***PyQt4***: You can download it from [here](http://www.riverbankcomputing.com/software/pyqt/download)

## How to use:

As you see, there is a file called _data.txt_ in root folder of project, that's a sample data set you can use it to check application.

***Classifier v0.1*** consists of 4 steps, Each step is completely depicted below:

#### Step1:
In this step, you should choose a data set with _.txt_ format. this data set will be the cornerstone of your decision tree. I suggest you to see the
correct styling of a data set by looking at _data.txt_ file. As you'll see all records are in just one line without any divisor like parenthesis or brackets, Just 
commas. You are highly recommended to correct your data set styling if you want Classifier works fine.
#### Step2:
After choosing the data set, In this step you should can use your configuration for your data set such as which amount of data will be used as training data or how 
classifier should choose training data from the whole instances of data set. And you'll be able to choose which column(attribute) is your class attribute.
#### Step3:
In this step you will see summary of your training data and whole data specifications, If you are agree with that you can click on __start training__ button
to go on. In the terminal you can see a simple representation of created decision tree.
#### Step4:
After training your data, By clicking on __test it__ you can see the amount of errors in test data by percent. And of course in the Results area you can see
further details about predictive accuracy and standard error of test data. 

## On the next update:
1.dealing with missing values will be added

## More info:
For more documentation,please wait. I'm trying to build a page for this application on github.