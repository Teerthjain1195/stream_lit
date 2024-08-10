import streamlit as st

# Define a dictionary of colleges with their minimum JEE score requirements
colleges = {
    'IIT Bombay': 250,
    'IIT Delhi': 240,
    'IIT Kanpur': 230,
    'IIT Kharagpur': 220,
    'IIT Madras': 210,
    'NIT Trichy': 200,
    'NIT Warangal': 190,
    'NIT Surathkal': 180,
    'BIT Mesra': 170,
    'VIT Vellore': 160
}

def recommend_colleges(score):
    recommended = []
    for college, min_score in colleges.items():
        if score >= min_score:
            recommended.append(college)
    return recommended

# Streamlit app
def main():
    st.title("College Recommendation Based on JEE Score")

    st.write("Enter your JEE score to get recommendations on which colleges you might be eligible for.")

    # Input for JEE score
    score = st.number_input("Enter your JEE score:", min_value=0, max_value=300, step=1)

    if st.button("Get Recommendations"):
        if score > 0:
            recommendations = recommend_colleges(score)
            if recommendations:
                st.write("Based on your score, you might be eligible for the following colleges:")
                for college in recommendations:
                    st.write(f"- {college}")
            else:
                st.write("Sorry, no recommendations available for your score.")
        else:
            st.write("Please enter a valid JEE score.")

if __name__ == "__main__":
    main()
