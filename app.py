import streamlit as st 
import pickle
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

try:
    # Load the model from the file
    with open('model/spam_detection_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error("Error: Model file not found. Please make sure the model file is available.")
    st.stop()

try:
    # Load vectorizer model from the file
    with open('model/vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
except FileNotFoundError:
    st.error("Error: Vectorizer file not found. Please make sure the vectorizer file is available.")
    st.stop()

st.set_page_config(
    page_title="Spam emails detection",
    page_icon="images/spam.png"
)

st.title("📧 Spam Email Detection App 📧")

st.markdown("<div style='padding: 30px'></div>", unsafe_allow_html=True)
st.subheader("Welcome to Our Trained Spam Detection Model")
st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)
st.markdown("""Test if your email is spam or not! Enter the text of your email and
                get the prediction from our trained model.""")
st.markdown("""
    The model utilizes a TF-IDF vectorizer and a Multinomial Naive Bayes classifier for spam detection.
    Enter the text of your email and click the submit button to get the prediction.
""")

st.markdown("<div style='padding: 20px'></div>", unsafe_allow_html=True)
st.subheader("Enter the text of your email: ")
st.markdown("<div style='padding: 10px'></div>", unsafe_allow_html=True)

email_text = st.text_area("Type or paste your email text here:")
st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)

st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)

predict = st.button("Predict")

st.markdown("<div style='padding: 20px'></div>", unsafe_allow_html=True)

# text cleaning and preprocessing (e.g., removing stopwords, punctuation, lowercase conversion)
def preprocess_text(text):
    # remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    # remove stopwords
    text = ' '.join([word for word in text.split() if word.lower() not in stopwords.words('english')])
    # convert to lowercase
    text = text.lower()
    return text

if predict:
    if not email_text:
        st.warning("Warning: Please enter some text before clicking Predict.")
        st.stop()
    # Preprocess the email text
    preprocessed_email = [preprocess_text(email_text) ]
    vectorized_email = vectorizer.transform(preprocessed_email)

    try:
        prediction = model.predict(vectorized_email)
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        st.stop()
    
    if prediction[0] > 0.5:
        st.subheader("The email is a spam.")
        st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)
    else:
        st.subheader("The email is not a spam. ")
        st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)



