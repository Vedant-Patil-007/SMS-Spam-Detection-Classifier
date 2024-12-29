import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    # converting to lower
    text = text.lower()
    # tokenization
    text = nltk.word_tokenize(text)
    # removing special characters
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    # stopword and punctutions
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    # stemming
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter the message")

if st.button('Predict'):

    #1. PreProcessing
    transform_sms = transform_text(input_sms)
    #2. Vectorizing
    vector_input = tfidf.transform([transform_sms])
    #3. Predicting
    result  = model.predict(vector_input)[0]
    #4. Display
    if result ==  1:
        st.header("Spam")
    else:
        st.header("Ham")
