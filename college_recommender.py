import streamlit as st
import pandas as pd

# Load the college data
@st.cache
def load_data():
    return pd.read_csv('colleges.csv')

# Define the Streamlit app
def main():
    st.title('College Recommendation System based on JEE Score')

    # Load the college data
    df = load_data()

    # Input for JEE score
    jee_score = st.number_input('Enter your JEE score', min_value=0, format="%d")

    # Show available categories
    categories = df['Category'].unique()
    selected_category = st.selectbox('Select college category', categories)

    # Filter colleges based on the selected category and JEE score
    filtered_colleges = df[
        (df['Category'] == selected_category) &
        (df['Minimum JEE Score'] <= jee_score) &
        (df['Maximum JEE Score'] >= jee_score)
    ]

    if not filtered_colleges.empty:
        st.write(f"Based on your JEE score of {jee_score}, here are some colleges you might consider in the {selected_category} category:")
        st.dataframe(filtered_colleges[['College Name', 'Minimum JEE Score', 'Maximum JEE Score']])
    else:
        st.write("No colleges available in this category within your JEE score range.")

if __name__ == "__main__":
    main()
