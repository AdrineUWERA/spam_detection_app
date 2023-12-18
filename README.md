# Spam Detection Model

## Description

The Spam Detection App is a web application that utilizes a machine learning model to predict whether an email is spam or not. The model is trained on a dataset of labeled emails using a TF-IDF vectorizer and a Multinomial Naive Bayes classifier. The app has been deployed on Streamlit.

Demo Links: 

Deployed version of the web pages [Here](https://adrine-uwera-spam-detection-app.streamlit.app/)


Demo video: [Here](https://drive.google.com/file/d/1CVIBN5sn25RPekYZ3xsZfk3_g6h4eoz8/view?usp=sharing)

## Notebooks and dataset

- [Dataset 1](https://www.kaggle.com/datasets/marcelwiechmann/enron-spam-data?select=enron_spam_data.csv)

- [Dataset 2](https://www.kaggle.com/datasets/bayes2003/emails-for-spam-or-ham-classification-trec-2007?select=email_text.csv)

- [Files used](https://drive.google.com/drive/u/0/folders/1p2vodU-5SIgVTkOjio21KY4tSHHC-Sji)

- [Classification model](https://colab.research.google.com/drive/1E5Ppr3Qm3xZ3mej6LODIuBYFaI3giq0T#scrollTo=EAhJI8XPNkXq)


## Features
- Email Input: Users can input the text of an email for spam detection.
- Prediction: After entering the email text, users can click the "Predict" button to get the model's prediction regarding whether the email is spam or not.

## Packages Used

This project has used some packages such as numpy, pandas, scikit-learn, which have to be installed to run this web app locally present in `requirements.txt` file. 

## Installation

To run the project locally, there is a need to have Visual Studio Code (vs code) installed on your PC:

- **[vs code](https://code.visualstudio.com/download)**: It is a source-code editor made by Microsoft with the Electron Framework, for Windows, Linux, and macOS.

## Usage

1. Clone the project 

``` bash
git clone https://github.com/AdrineUWERA/spam_detection_app.git

```

2. Open the project with vs code

``` bash
cd spam_detection_app
code .
```

3. Install the required dependencies

``` bash
pip install -r requirements.txt
```


4. Run the project

``` bash
streamlit run app.py
```

5. Use the link printed in the terminal to visualise the app. (Usually `http://localhost:8501`)

## Model Files

- spam_detection_model.pkl: The main spam detection model trained on a dataset of labeled emails.
- vectorizer.pkl: The TF-IDF vectorizer used for text vectorization during inference.

## Important Notes
- The app is designed to work specifically with only text for spam detection.

## Authors and Acknowledgment

- Adrine Uwera 

## License
[MIT](https://choosealicense.com/licenses/mit/)
