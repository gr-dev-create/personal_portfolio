import streamlit as st
from forms.contact import contact_form

# --- Initialize toggle state ---
if "show_contact_form" not in st.session_state:
    st.session_state.show_contact_form = False

# --- Function to toggle form visibility ---


def toggle_form():
    st.session_state.show_contact_form = not st.session_state.show_contact_form


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/grace_profile.png", width=400)

with col2:
    st.title("Grace Ann Villanueva", anchor=False)
    st.write(
        "Java Engineer, assisting enterprises by supporting data-driven decision-making."
    )
    st.button("✉️ Contact Me", on_click=toggle_form)

# --- CONTACT FORM (toggle open/close) ---
if st.session_state.show_contact_form:
    contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 6 months experience as a Java/DevOps Engineer  
    - Strong hands-on experience and knowledge in Python and Excel  
    - Good understanding of statistical principles and their respective applications  
    - Excellent team-player and displaying a strong sense of initiative on tasks  
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA  
    - Data Visualization: PowerBi, MS Excel, Plotly  
    - Modeling: Logistic regression, linear regression, decision trees  
    - Databases: Postgres, MongoDB, MySQL  
    """
)
