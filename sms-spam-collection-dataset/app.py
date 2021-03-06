import streamlit as st 
import pickle
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
import urllib.request
#nltk.download('all') # uncomment when, ntlk not downloaded on your system

#tfidf = pickle.load(urllib.request.urlopen('https://drive.google.com/uc?export=download&id=12Xg7xNbR9jpLFJetr0aC8o1JVOg735L7'))
#model = pickle.load(urllib.request.urlopen('https://drive.google.com/uc?export=download&id=1wgZVx-eYLALXpg4ijq9h7kqN3Ipip--x'))


tfidf = pickle.load(urllib.request.urlopen('https://www.googleapis.com/drive/v3/files/12Xg7xNbR9jpLFJetr0aC8o1JVOg735L7?alt=media&key=AIzaSyCUpIPtvM6lJw65WnZoM-Xxn7Xo6xytJ3k'))
model = pickle.load(urllib.request.urlopen('https://www.googleapis.com/drive/v3/files/1wgZVx-eYLALXpg4ijq9h7kqN3Ipip--x?alt=media&key=AIzaSyCUpIPtvM6lJw65WnZoM-Xxn7Xo6xytJ3k'))



def transform_text(text):
    #Lower case
    text = text.lower()
    
    #Tokenization
    text = nltk.word_tokenize(text) 
    
    #Removing special characters
    y = []
    for i in text:
        if i.isalnum(): 
            y.append(i)
    
    #Removing stop words and punctuation
    text = y[:] 
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    #Stemming (convert similar words to a specif word like dancing,dance,danced conver to danc)
    text = y[:] 
    y.clear()   
    
    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))
    

    return " ".join(y)



st.title('SMS Spam Classifer')

input_sms = st.text_area('Enter the SMS')


if st.button('predict'):
    if len(input_sms.strip()) != 0: 
        # preprocessing
        transformed_sms = transform_text(input_sms)
        # vectorizer
        vector_input = tfidf.transform([transformed_sms])
        # predict
        result = model.predict(vector_input)[0]
        # display
        if result == 1:
            st.header('Spam')
        else:
            st.header('Not Spam')
    else:
        st.header('TextArea is Blank')
