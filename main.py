import streamlit as st
import pandas as pd
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# from streamlit_extras import switch_page

# Load the dataset
dataset = pd.read_csv('skills.csv')
dataset.dropna(inplace=True)
dataset.drop_duplicates(keep=False, inplace=True)
dataset['Responsibilities'] = dataset['Responsibilities'].apply(lambda x: x.split())
dataset['Category'] = dataset['Category'].apply(lambda x: [x.replace(" ", "")])
dataset['Responsibilities'] = dataset['Responsibilities'].apply(lambda x: [i.replace(" ", "") for i in x])
dataset['Company'] = dataset['Company'].apply(lambda x: [x.replace(" ", "")])
dataset['Location'] = dataset['Location'].apply(lambda x: [x.replace(" ", "")])
dataset['Preferred Qualifications'] = dataset['Preferred Qualifications'].apply(lambda x: [x.replace(" ", "")])
dataset['job_data'] = dataset['Company'] + dataset['Category'] + dataset['Location'] + dataset['Responsibilities'] + dataset['Preferred Qualifications']
mod_dataset = dataset[['Title', 'job_data']]
mod_dataset['job_data'] = mod_dataset['job_data'].apply(lambda x: " ".join(x))

cv = CountVectorizer(max_features=500, stop_words='english')
job_vectors = cv.fit_transform(mod_dataset['job_data']).toarray()

ps = PorterStemmer()

def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

mod_dataset['job_data'] = mod_dataset['job_data'].apply(stem)
similarity = cosine_similarity(job_vectors)

# Streamlit app
def main():
    st.set_page_config(
        page_title="Job Recommendation App",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
        body {
            background-color: #1E88E5;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .stApp {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border-radius: 10px;
            background-color: rgba(255, 255, 255, 0.8);
        }
        .stButton button {
            background-color: #FF5733;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #E63C1E;
        }
        .stSelectbox select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Job Recommendation App")
    
    image = "pic.jpg"  # Replace with the URL of your image
    st.image(image, use_column_width=True)

    st.markdown("Welcome to the Job Recommendation App!")
    st.markdown("This app helps you find job recommendations based on a selected job title.")

    job_option = st.selectbox("Select a job title:", mod_dataset['Title'])

    st.markdown("Click the 'Recommend' button to see job recommendations.")

    if st.button("Recommend"):
        st.subheader("Recommended Jobs:")
        recommend(job_option)

def recommend(job):
    job_index_fetch = mod_dataset[mod_dataset['Title'] == job].index[0]
    distances = similarity[job_index_fetch]
    job_fetch = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:5]
    for i in job_fetch:
        # Display all columns except 'job_data'
        st.write("Recommended Job Details:")
        st.write(f"Title: {dataset.iloc[i[0]]['Title']}")
        st.write(f"Company: {dataset.iloc[i[0]]['Company']}")
        st.write(f"Category: {dataset.iloc[i[0]]['Category']}")
        st.write(f"Location: {dataset.iloc[i[0]]['Location']}")
        st.write(f"Responsibilities: {', '.join(dataset.iloc[i[0]]['Responsibilities'])}")
        st.write(f"Preferred Qualifications: {', '.join(dataset.iloc[i[0]]['Preferred Qualifications'])}")
        st.write("---")  # Separator between recommendations

if __name__ == '__main__':
    main()