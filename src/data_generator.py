import os
import pandas as pd
import numpy as np
import random

def generate_synthetic_ratings():
    # 1. Load your real books dataset
    # Make sure books.csv is in 'data/processed/' or adjust path
    input_path = 'data/processed/books.csv'
    
    if not os.path.exists(input_path):
        print(f"❌ Error: {input_path} not found. Move the uploaded file there.")
        return

    df_books = pd.read_csv(input_path, on_bad_lines='skip')
    book_ids = df_books['bookID'].unique()
    
    print(f"📖 Loaded {len(book_ids)} real books from Goodreads dataset.")

    # --- CONFIGURATION ---
    NUM_USERS = 1000  # Increased for more realism
    AVG_RATINGS_PER_USER = 15

    # 2. Generate Ratings
    ratings = []
    for user_id in range(1, NUM_USERS + 1):
        num_ratings = max(3, int(np.random.normal(AVG_RATINGS_PER_USER, 5)))
        books_rated = random.sample(list(book_ids), min(num_ratings, len(book_ids)))
        
        for b_id in books_rated:
            # Random rating between 1 and 5
            rating = int(max(1, min(5, round(np.random.normal(4, 1)))))
            ratings.append([user_id, b_id, rating])

    df_ratings = pd.DataFrame(ratings, columns=['user_id', 'book_id', 'rating'])
    
    # 3. Save
    output_path = 'data/processed/ratings.csv'
    df_ratings.to_csv(output_path, index=False)
    print(f"✅ 'ratings.csv' generated with {len(df_ratings)} rows using REAL book IDs.")

if __name__ == "__main__":
    generate_synthetic_ratings()