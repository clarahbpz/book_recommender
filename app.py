import streamlit as st
from src.recommender_model import BookRecommender

# Page Configuration
st.set_page_config(page_title="AI Book Advisor", page_icon="📚")

st.title("📚 NextRead AI")
st.markdown("### Find your next favorite book based on what you already love.")

# Cache the engine so it only loads once
@st.cache_resource
def load_engine():
    return BookRecommender()

try:
    engine = load_engine()
    
    # Get all unique titles for the autocomplete dropdown
    book_list = engine.df_books['title'].unique().tolist()
    
    # User Input
    selected_book = st.selectbox(
        "Search for a book you've read:",
        options=[""] + sorted(book_list),
        index=0,
        help="Type to filter titles..."
    )

    if st.button("Get Recommendations"):
        if selected_book:
            with st.spinner('Calculating similarities...'):
                recs = engine.get_recommendations(selected_book)
            
            if isinstance(recs, str):
                st.error(recs)
            else:
                st.success(f"Since you liked **{selected_book}**, you might enjoy:")
                
                # Display results in a clean grid
                for title, score in recs.items():
                    match_pct = round(score * 100, 1)
                    st.write(f"📖 **{title}**")
                    st.caption(f"Match Score: {match_pct}%")
                    st.progress(float(score))
                    st.divider()
        else:
            st.warning("Please select a book title first.")

except Exception as e:
    st.error("Make sure your data is generated and paths are correct.")
    st.info(f"Technical error: {e}")