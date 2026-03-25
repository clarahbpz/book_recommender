# AI-Powered Book Recommendation Engine

A collaborative filtering recommendation system built with Python, utilizing the Goodreads dataset to suggest books based on user preference patterns and vector similarity.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](https://seu-app.streamlit.app)

## Project Overview
This project implements an item-based collaborative filtering algorithm. It processes the included Goodreads dataset and simulates user interactions to build a mathematical model capable of identifying similar items in a multi-dimensional space. The solution is encapsulated in an Object-Oriented (OOP) architecture to ensure scalability and memory efficiency.

## Technical Architecture
The engine operates through a three-stage pipeline:
1. **Data Processing**: The included `books.csv` is cleaned and merged with generated user ratings. A User-Item matrix is generated where rows represent book titles and columns represent unique users.
2. **Similarity Computation**: The system utilizes Cosine Similarity to calculate the distance between book vectors.
3. **In-Memory Retrieval**: The similarity matrix is pre-calculated and stored during class initialization, allowing for fast retrieval times during user queries.

## Key Features
* **Normalized Search**: Implements string normalization (case-insensitivity and whitespace stripping) to prevent lookup errors.
* **Fuzzy Matching**: Capable of finding book titles through partial keyword matches.
* **Web Interface**: Built with Streamlit to provide an interactive dashboard for end-users.
* **Object-Oriented Design**: The `BookRecommender` class manages data state and prevents redundant matrix re-computations.

## Repository Structure
```text
book_recommender/
├── data/
│   └── processed/           
├── src/
│   ├── data_generator.py   
│   └── recommender_model.py 
├── app.py                 
├── requirements.txt       
└── README.md                     
```
## Installation and Usage
**1. Environment Setup**
Ensure you have Python 3.8+ installed. It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```
**2. Data Preparation**
The books.csv is already included in data/processed/. Run the generator to create the user interaction database:
    ```bash
    python src/data_generator.py
    ```
**3. Launching the Application** 
To run the web-based interface:
    ```bash
    streamlit run app.py
    ```
## Technologies Used
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn
* **UI Framework:** Streamlit

**Author**: Clara Hilbert Polizel
