# `SMS Spam Prediction`

### Problem Statement :
Spam messages are a major problem for users of mobile phones and other messaging services. These messages can be annoying, unwanted, and sometimes even dangerous, as they can contain malicious links or other types of scams. Detecting spam messages is a challenging task that requires the use of advanced algorithms and natural language processing techniques.
The goal of this project is to develop an SMS spam detection system using machine learning algorithms. The system will be able to classify messages as either spam or non-spam based on their content. The accuracy of the system will be evaluated using a dataset of labeled messages.

### Description :
The SMS spam detection project is an NLP-based project that utilizes machine learning algorithms to detect spam messages. The project is built using Python programming language and several libraries, including TensorFlow, NumPy, Pandas, and Matplotlib.

### Data gathering : 
The project follows a chronology of steps in building the SMS spam detection system. Firstly, the data is gathered from Kaggle, The dataset used for this project contains two columns, text and spam_or_not, where the text column contains the message text, and the spam_or_not column contains the label indicating whether the message is spam or not.

### Data cleaning & feature engineering :
then the data is cleaned and feature engineering is performed using CountVectorizer and TfidfVectorizer techniques. 

### EDA : 
After feature engineering, exploratory data analysis (EDA) is performed to understand the distribution and patterns in the data.

### Data pre-processing : 
The next step involves data pre-processing, where the data is prepared for training the model. This includes converting the text to lowercase, tokenization, removing special characters, stop words and punctuation, and stemming.

### Model selection : 
After pre-processing, the dataset is split into training and testing sets. The machine learning algorithm used in this project is the Naive Bayes algorithm, which is a probabilistic algorithm that uses Bayes' theorem to calculate the probability of each message being spam or not. GaussianNB, MultinomialNB, and BernoulliNB algorithms are also applied, but the MultinomialNB algorithm is selected because it has the highest precision score of 1.
The model is then trained using the training dataset, and its performance is evaluated using the testing dataset. The accuracy of the model is calculated, and it is observed that the accuracy of the model is 97.1%, which is a good indication of its effectiveness in detecting spam messages.

### Model save & deployed on streamlit: 
After training and evaluation, the model is saved in pickle format for future use. A Streamlit website is then created, where users can enter their messages in a text box, and the model will predict whether the message is spam or not. The website is hosted and made available for free to the public.

### Conclusion : 
In conclusion, the SMS spam detection project is an NLP-based project that uses machine learning algorithms to detect spam messages. The project follows a chronology of steps in building the SMS spam detection system, including data gathering, cleaning, pre-processing, and model training. The final model has an accuracy of 97.1%, making it an effective tool for detecting spam messages.

### Visit website :
[https://spmpredict.streamlit.app](https://spmpredict.streamlit.app/)
