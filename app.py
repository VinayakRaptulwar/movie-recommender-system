import streamlit as st
import pickle
import requests
import os
import gdown

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a496a810b8aa784a1f734d0b16a2fa6b&language=en-US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w400/" + data['poster_path']




def recommend(movie):

    movie_index = movies[movies['title'] == movie ].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1 : 11]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster



movies = pickle.load(open('movies.pkl', 'rb'))


if not os.path.exists("similarity.pkl"):
    file_id = "PASTE_YOUR_FILE_ID_HERE"
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, "similarity.pkl", quiet=False)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title(':blue[Movie] Recommender System')


option = st.selectbox(
"What would you like to see?",
movies['title'].values,
)

if st.button("Recommend"):
    names,posters = recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.caption(names[0])
        st.image(posters[0])

    with col2:
        st.caption(names[1])
        st.image(posters[1])

    with col3:
        st.caption(names[2])
        st.image(posters[2])

    with col4:
        st.caption(names[3])
        st.image(posters[3])

    with col5:
        st.caption(names[4])
        st.image(posters[4])

    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.caption(names[5])
        st.image(posters[5])

    with col7:
        st.caption(names[6])
        st.image(posters[6])

    with col8:
        st.caption(names[7])
        st.image(posters[7])

    with col9:
        st.caption(names[8])
        st.image(posters[8])

    with col10:
        st.caption(names[9])
        st.image(posters[9])




