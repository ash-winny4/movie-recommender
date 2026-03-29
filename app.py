import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

col1, col2, col3 = st.columns([1,1.2,1])

with col2:
    st.title("WATCHMAXX")
st.divider()
st.markdown("<h4 style='text-align: center; color: violet;'>Content Based Movie Recommendation System</h4>",width='auto', unsafe_allow_html=True,text_alignment='center')

def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    top_movies = sim_scores[1:6] #skip the first cuz its the movie itself
    
    return [movies.iloc[i[0]].title for i in top_movies]


selected_movie = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    
    selected_movie_data = movies[movies['title'] == selected_movie].iloc[0]
    st.subheader(selected_movie_data.title)

    col1, col2 = st.columns([1,2])

    with col1:
        st.markdown(":violet[<u>Rating</u>]",unsafe_allow_html=True)
        st.metric("",round(selected_movie_data.vote_average,1), height="stretch",width="stretch",label_visibility="collapsed")

    with col2:
        st.markdown(":violet[<u>Synopsis</u>]",unsafe_allow_html=True)
        st.write(selected_movie_data.overview)
    
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies",divider="violet")

    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            st.write(recommendations[i])