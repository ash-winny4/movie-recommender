# WATCHMAXX

A content-based movie recommendation system built using Python and Streamlit that suggests similar movies based on metadata like genres, cast, keywords, and director.

-------------------------------------------------------

## Live Demo

https://movie-recommender-mkxqv78yqynf4buoldu57d.streamlit.app/

-------------------------------------------------------

## Working and Concept

This project uses a content-based filtering approach.

* Combines movie features like:

  * Genres
  * Keywords
  * Cast
  * Director
* Converts them into text data ("tags")
* Uses CountVectorizer to transform text into numerical vectors
* Applies Cosine Similarity to find similar movies

---------------------------------------------------------------

## Features

When the User selects a movie, 
1) Displays the Poster and Synopsis of the selected movie
2) Minimalist and Functional UI using Streamlit
3) Similarity Matrix calculated only once (data cached) for each movie

----------------------------------------------------------------

## Tech Stack

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**

--------------------------------------------------------------------

## Installation & Setup

1) Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/movie-recommender.git
cd movie-recommender
```

2) Install dependencies:

```
pip install -r requirements.txt
```

3) Run the app:

```
streamlit run app.py
```

-----------------------------------

## Dataset

* TMDB Movie Metadata dataset from Kaggle
  Contains information about movies including genres, cast, crew, and ratings

------------------------------------------------------------------------------

## Future Improvements

1) Search Functionality
2) Improve recommendations using advanced models
3) Continue to grow the app as I learn more intermediate level stuff in ML :)

-------------------------------------------------------------------------------



## Author

Ashwin Nair
GitHub : https://github.com/ash-winny4
LinkedIn : https://www.linkedin.com/in/ashwin-nair-a97b81371/
