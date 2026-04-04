import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pickle.load(open('movies.pkl', 'rb'))

TMDB_API_KEY = "419d25d49d49799a74b716be042eeef0"  

@st.cache_resource
def compute_similarity(movies):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    return cosine_similarity(vectors)

similarity = compute_similarity(movies)

def fetch_poster(movie_id):
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_movies = sim_scores[1:6]

    titles = []
    posters = []
    for i in top_movies:
        movie_row = movies.iloc[i[0]]
        titles.append(movie_row.title)
        posters.append(fetch_poster(movie_row.movie_id))  
    return titles, posters


col1, col2, col3 = st.columns([1, 1.2, 1])
with col2:
    st.title("WATCHMAXX")
st.divider()
st.markdown(
    "<h4 style='text-align: center; color: violet;'>Content Based Movie Recommendation System</h4>",
    unsafe_allow_html=True
)

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    selected_movie_data = movies[movies['title'] == selected_movie].iloc[0]

   
    st.subheader(selected_movie_data.title)
    col_poster, col_info = st.columns([1, 2])

    with col_poster:
        poster_url = fetch_poster(selected_movie_data.movie_id) 
        st.image(poster_url, use_container_width=True)

    with col_info:
        st.markdown(":violet[<u>Rating</u>]", unsafe_allow_html=True)
        st.metric("", round(selected_movie_data.vote_average, 1), label_visibility="collapsed")
        st.markdown(":violet[<u>Synopsis</u>]", unsafe_allow_html=True)
        st.write(selected_movie_data.overview)

    
    st.subheader("Recommended Movies", divider="violet")
    titles, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.image(posters[i], use_container_width=True)
            st.caption(titles[i])