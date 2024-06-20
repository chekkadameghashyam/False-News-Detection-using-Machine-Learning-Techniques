Title :  Utilizing Machine Learning For The Identification of False News

Project consists of 2 Phases
1. Static Phase
2. Dynamic Phase

Overview :

•	Two sections of the system are developed. They are Static Implementation and Dynamic Implementation. Static implementation, which uses machine learning methods, is the first element. Here's what we just take the pre processed dataset and extract its characteristics. After collecting the characteristics, they are input into four distinct classifiers: Support Vector Machine, Random Forest Classifier, Logistic Regression, and Passive-Aggressive Classifier. Next, these classifiers are used to fit the model. Following model fitting, the researchers evaluate the accuracy differences between the classifiers. To determine the performance of the model, a confusion matrix is used. In the second component, dynamic implementation, the keyword or text found in the news articles from the dataset is utilized. 

•	This component likely involves deploying the trained model to make real time predictions on new news articles or texts, allowing for the dynamic classification of news as fake or real.

•	The framework and system design parts go into great detail about the architecture and operation of the system, even down to the code level. These sections cover the fundamental ideas of the system and how the design embodies them, in addition to discussing how the system is implemented.

•	They give a thorough rundown of the system's architecture, constituent parts, and interrelationships, elucidating how each works together to support the system's overall goals and functionality. Readers can better grasp the inner workings of the system and the reasoning behind its design choices by closely analyzing the framework and system architecture.

Dataset :

The dataset that our project uses is an easy-to-use and realistic dataset that contains 10000 news articles simply classified as Fake or Real , where 5000 are false news and 5000 were true news.
The attributes of the dataset are:

Subject : Description about type of news article

Title : Article Headline 

Text : Article textual content 

Class Label : Fake and Real

Date : Date identification for article

Conclusion : 

The field of fake news detection research contains a vast dataset and many potential applications.
We compare our model with the current dataset. Results indicates that the Maximum Accuracy of Support-Vector Machine algorithms is up to 92.8%.Thus, we developed our classification model for false news detectors using this classifier. The user can verify the news credibility by entering a phrase or keyword on the webpage.We intend to develop our own dataset in the future that will be current and contain all the news pertinent to it.The database will be updated with the most recent data and real-time news.The next step is to train the model and analyze how its accuracy changes in light of the new data in order to enhance and refine it.Dynamic Phase of the project is made by using python-Django Web Frame Works. Here by only files that we made changes in an usual django new project were provided and regression.py file to make a link between the machine learning to web is used. Data Csv files are also provided other than all the django files. Web application Snap is also provided.Go through the review pdf for outcomes.

Run :

In Static phase, run the .ipynb file

Whereas in  Dynamic Phase after making required changes in Django project run command line as ‘py manage.py runserver project_name ‘

Thank You.
