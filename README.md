# 🎬 Movie Recommender System

A content-based Movie Recommender System built using **Python**, **Streamlit**, and the **TMDB API** that recommends movies similar to the one selected by the user and displays their posters.

---

## 📌 Project Overview

This project recommends movies based on content similarity. When a user selects a movie, the system finds similar movies using a precomputed similarity matrix and fetches movie posters using the TMDB API.

---

## 🚀 Features

* Recommend movies similar to the selected movie.
* Displays movie posters along with recommendations.
* Interactive web interface built with Streamlit.
* Uses TMDB API to fetch movie posters dynamically.
* Fast recommendations using a precomputed similarity matrix.

---

## 📂 Dataset

The project uses the TMDB Movie Dataset containing movie information such as:

* Movie Title
* Genres
* Keywords
* Cast
* Crew
* Overview

These features are combined to create movie tags used for generating recommendations.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* TMDB API

---

## 🧠 Recommendation Technique

This project uses **Content-Based Filtering**.

* Movie features are combined into tags.
* Text data is converted into vectors using vectorization techniques.
* Cosine similarity is calculated between movies.
* Movies with the highest similarity scores are recommended.

---

## 📁 Project Structure

```text
Movie-Recommender-System/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── poster fetching using TMDB API
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move to the project directory:

```bash
cd Movie-Recommender-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 How It Works

1. Select a movie from the dropdown menu.
2. Click the **Recommend** button.
3. The system finds similar movies using cosine similarity.
4. Posters are fetched using the TMDB API.
5. Recommended movies are displayed with their posters.

---

## 📷 Output

* Movie recommendations displayed in a grid layout.
* Posters fetched directly from TMDB.
* Simple and interactive user interface.

---

## 🔮 Future Improvements

* Add movie ratings and trailers.
* Implement collaborative filtering.
* Add genre-based filtering.
* Improve recommendation accuracy using hybrid models.

---

## 👨‍💻 Author

**Vinayak Raptulwar**

---


## 🌐 Live Demo

https://movie-recommender-zmt5e4yydcjbtbh4sfmsmf.streamlit.app/

---

## 🏷️ Internship/Portfolio Project

This project was developed to practice **Machine Learning**, **Recommendation Systems**, and **Streamlit deployment** and is suitable for showcasing in a portfolio or on LinkedIn.

