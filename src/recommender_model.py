import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class BookRecommender:
    def __init__(self, books_path='data/processed/books.csv', ratings_path='data/processed/ratings.csv'):
        """
        Initializes the engine. 
        Note: The 'on_bad_lines' parameter handles formatting issues in real datasets.
        """
        print("⚙️  Booting up the Professional Recommendation Engine...")
        self.books_path = books_path
        self.ratings_path = ratings_path
        self.similarity_df = None
        self.df_books = None
        self._build_engine()

    def _build_engine(self):
        try:
            # 1. Load Real Data
            self.df_books = pd.read_csv(self.books_path, on_bad_lines='skip')
            df_ratings = pd.read_csv(self.ratings_path)

            # 2. Pre-process: Merge ratings with book titles
            # Using 'bookID' from your file and 'book_id' from our generated ratings
            df_merged = pd.merge(df_ratings, self.df_books[['bookID', 'title']], left_on='book_id', right_on='bookID')

            # 3. Create Pivot Table
            print("📊  Generating User-Item Matrix...")
            user_item_matrix = df_merged.pivot_table(index='title', columns='user_id', values='rating').fillna(0)

            # 4. Mathematical Similarity (Cosine)
            print("🧮  Computing Similarity Matrix...")
            similarity_matrix = cosine_similarity(user_item_matrix)
            
            # Store in a DataFrame for easy indexing
            self.similarity_df = pd.DataFrame(
                similarity_matrix, 
                index=user_item_matrix.index, 
                columns=user_item_matrix.index
            )
            print("✅  Engine is ready with real-world data!")
            
        except Exception as e:
            print(f"❌  Initialization Error: {e}")

    def get_recommendations(self, book_title, top_n=5):
        """
        Finds recommendations using normalized string matching to avoid 'Not Found' errors.
        """
        if self.similarity_df is None:
            return "Error: Engine not initialized."
        
        # Normalize input: remove extra spaces and lowercase
        search_term = book_title.strip().lower()
        
        # Normalize the index for comparison
        index_norm = self.similarity_df.index.str.strip().str.lower()
        
        # Find partial matches
        matches = self.similarity_df.index[index_norm.str.contains(search_term, regex=False)]
        
        if len(matches) == 0:
            return f"The book '{book_title}' was not found. Try a different keyword!"
        
        # Use the first match found
        actual_title = matches[0]
        print(f"🔍  Match found: {actual_title}")
        
        # Get scores, sort, and skip the first one (the book itself)
        scores = self.similarity_df[actual_title].sort_values(ascending=False)[1:top_n+1]
        return scores

if __name__ == "__main__":
    recommender = BookRecommender()
    # Test with a snippet of a title
    test_query = "Harry Potter" 
    results = recommender.get_recommendations(test_query)
    
    if isinstance(results, str):
        print(results)
    else:
        print(f"\nRecommendations for '{test_query}':")
        for title, score in results.items():
            print(f"👉 {title} (Match: {round(score * 100, 2)}%)")