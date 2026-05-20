import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

tv_vector = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

## preprocessing
## ---------------------------
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:] 
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y) 

##----------------------------------

st.title("Email /SMS Spam Classifier ✉️")
st.markdown("*:blue[Vansh Pandey 🤗]*")
st.divider()

input_message = st.text_area("Enter ur message here:")
if st.button("Predict"):
    st.write(input_message)

##----------------------------------------
    # preprocess
    transformed_message = transform_text(input_message)

    # vectorize
    vector_input = tv_vector.transform([transformed_message])

    # model predict
    result = model.predict(vector_input)[0]

    # Display
    if result == 1:
        st.header("SPAM 🔴")
    else :
        st.header("NOT SPAM 🟢")