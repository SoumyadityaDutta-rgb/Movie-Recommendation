import streamlit as st
import pickle
import pandas as pd
import requests
import time

# -----------------------------
# Fetch poster function (robust)
# -----------------------------
def fetch_poster(movie_id):
    API_KEY = ""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "poster_path" in data and data["poster_path"]:
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        print(f"Poster fetch failed for {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"



# -----------------------------
# Recommendation function
# -----------------------------
def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        # Append movie title
        recommended_movies.append(movies.iloc[i[0]].original_title)

        # Fetch poster from TMDB API
        recommended_movies_posters.append(fetch_poster(movie_id))
        time.sleep(20)  # Adds a 50-millisecond delay

    return recommended_movies, recommended_movies_posters



# -----------------------------
# Load data
# -----------------------------
movies_dict = pickle.load(open("movie_list.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie you like:",
    movies['original_title'].values
)

if st.button("Recommend"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[idx])
            st.image(recommended_movie_posters[idx])

