import streamlit as st
import pandas as pd

# Load the car data
@st.cache
def load_data():
    # Load the car data from a CSV file
    return pd.read_csv('cars.csv')

# Define the Streamlit app
def main():
    st.title('Car Recommendation System')

    # Load the car data
    df = load_data()

    # Input for net worth
    net_worth = st.number_input('Enter your net worth ($)', min_value=0, format="%d")

    # Show available car categories
    categories = df['Category'].unique()
    selected_category = st.selectbox('Select car category', categories)

    # Filter cars based on the selected category
    filtered_cars = df[(df['Category'] == selected_category) & (df['Price'] <= net_worth)]

    if not filtered_cars.empty:
        st.write(f"Based on your net worth of ${net_worth}, here are some cars you might consider in the {selected_category} category:")
        st.dataframe(filtered_cars[['Car Model', 'Price']])
    else:
        st.write("No cars available in this category within your budget.")

if __name__ == "__main__":
    main()
