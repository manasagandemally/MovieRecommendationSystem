import streamlit as st
import pandas as pd
import wdmproject  # Ensure 'wdmproject.py' is available

# Load data
df_movies = pd.read_csv('processed_movies.csv')
cosine_sim = pd.read_csv('cosine_similarity.csv').values  # Convert to numpy array

# Set page config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .stButton>button {
            background-color: black !important;  /* Black color */
            color: white !important;
            border-radius: 10px;
            font-size: 20px;
            padding: 12px;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #333333 !important;  /* Slightly lighter black */
        }
        .recommendation-box {
            background-color: #f8f9fa;
            padding: 8px;
            border-radius: 8px;
            margin: 4px auto;
            color: #333;
            font-size: 18px;
            width: 40%;  /* Smaller box width */
            text-align: left; /* Left align */
        }
        .default-movie-box {
            background-color: #dedede;
            padding: 40px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# Title with increased font size using HTML and inline CSS
st.markdown('<h1 style="text-align: center; font-size: 60px; color: #ff4b4b; font-weight: bold;">🎬 Movie Recommendation System 🍿</h1>', unsafe_allow_html=True)

# Movie selection dropdown
selected_movie = st.selectbox("🔍 Select a movie:", df_movies['title'].values)

# Fetch movie details
movie_info = df_movies[df_movies['title'] == selected_movie].iloc[0]

# Movie details section (without the poster)
st.markdown(f'<p class="movie-title">{selected_movie}</p>', unsafe_allow_html=True)
st.write(f"🎭 **Genres:** {movie_info['genres']}" if 'genres' in df_movies.columns else "")
st.write(f"⭐ **Rating:** {movie_info['rating']}" if 'rating' in df_movies.columns else "")
st.write("📖 **Overview:**", movie_info['overview'] if 'overview' in df_movies.columns else "No description available.")

# Recommend Button
if st.button("🎥 Get Recommendations"):
    recommendations = wdmproject.get_recommendations(selected_movie, df_movies, cosine_sim)

    st.subheader("✨ Top 5 Recommended Movies:")
    for movie in recommendations:
        st.markdown(f'<div class="recommendation-box">{movie}</div>', unsafe_allow_html=True)
