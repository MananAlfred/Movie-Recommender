import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(
    page_title="Movie-Recommender",
    page_icon = "👌"
)

st.sidebar.success("Select a page from above")

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

def fetchPosterPath(movie_id):
    res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=fe0697d3e9e25a36cab128042a6a4822'.format(movie_id))
    data = res.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetchPosterPath(movie_id))
    return recommended_movies,recommended_movies_posters

st.title('Movie-Recommender-System')
selected_movie_name = st.selectbox(
    'Select a Movie !',
    movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    st.header("My Recommendations :-")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["1st", "2nd", "3rd","4th","5th"])

    with tab1:
        st.header(names[0])
        st.image(posters[0], use_column_width="auto")

    with tab2:
        st.header(names[1])
        st.image(posters[1], use_column_width="auto")

    with tab3:
        st.header(names[2])
        st.image(posters[2], use_column_width="auto")

    with tab4:
        st.header(names[3])
        st.image(posters[3], use_column_width="auto")

    with tab5:
        st.header(names[4])
        st.image(posters[4], use_column_width="auto")
