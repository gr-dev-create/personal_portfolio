import json
import requests
from streamlit_lottie import st_lottie

import streamlit as st
from forms.contact import contact_form

# --- ANIMATION ---


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_hello = load_lottiefile("./assets/hello.json")
lottie_coding = load_lottiefile("./assets/coding.json")

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
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        height=300,
        key="hello-lottie",
    )
    st.title("I'm, Grace Ann Villanueva", anchor=False)
    st.write(
        "A Java Engineer and Test Automation intern, aspiring to be a Full Stack Developer."

    )
    st.button("✉️ Contact Me", on_click=toggle_form)

# --- CONTACT FORM (toggle open/close) ---
if st.session_state.show_contact_form:
    contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("💼 Experience & Qualifications", anchor=False)

with st.expander("Java Backend Engineer & Test Automation - ING Hubs Philippines (6 months)"):
    st.markdown("""
- **Summary of Achievements:**
    - Completed Java Udemy course for PSS OM training
    - API Merak upgrade – 2 APIs (production-ready):
        > Checked migration guides  
        > Created local branch  
        > Ran pipelines [dev/tst/acc]  
        > Upgraded JDK 17 to 21  
        > Analyzed dependency and resolved conflicts  
        > Troubleshoot issues via sprint board and logs  
        > Requested support and sent BILA email  
        > Monitored beta logs via Elastic and Jumphost  
        > Replaced Polaris-tooling certificate  
        > Performed pull request review  
        > Sent changelog and Checkmarx docs  
        > Merged changes to master branch

- Utilized Azure DevOps tools: sprint board, repos, pipelines, artifacts  
- Member of innovatING PSS guild  
- Created user story for Innovation Week  
- Hosted sprint retrospective
    """, unsafe_allow_html=True)

with st.expander("Test Automation Achievements"):
    st.markdown("""
- Performed manual tests using Postman  
- Uploaded documentation and created team communication channels  
- Ran smoke and load tests

    """)

st.markdown("""
- Strong hands-on experience with Excel 
- Solid understanding of statistical principles and applications  
- Excellent team player with strong initiative
- Communicate well with peers, consumers, and stakeholders
""")


# --- HARD SKILLS ---
st.write("\n")
st.subheader("🧠 Hard Skills", anchor=False)

col1, col2 = st.columns([2, 1], gap="medium")

with col1:
    st.markdown("<div style='padding-top: 30px'>", unsafe_allow_html=True)
    st.markdown(
        """
        - **Programming Languages:** Python, Java, C++, C# , HTML, CSS, JavaScript  
        - **Data Visualization:**  MS Excel, Power BI  
        - **Databases:** MongoDB, MySQL, NoSQL, Cassandra  
        - **Testing:**  Postman, Karate, JMeter  
        - **Monitoring:** Elastic, Jumphost, Kibana, Grafana, Prometheus  
        - **Version Control:** GitHub, Jenkins  
        """
    )

with col2:
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",

        key="coding-lottie",
    )

# --- EDUCATION & CERTIFICATIONS ---
st.markdown('<h3 class="section-title"> 🎓 Education & Certifications</h3>',
            unsafe_allow_html=True)
st.write(
    """
    - Bachelor of Science in Information Technology (Far Eastern College - Silang)
    """
)
with st.expander("Certifications"):
    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/Java_udemy.jpg", width=350)
        st.image("assets/payments_basic_udemy.jpg", width=350)
        st.image("assets/intro_sql.jpg", width=350)
        st.image("assets/joining_data.jpg", width=350)

    with col2:
        st.image("assets/tech_reliab_udemy.jpg", width=350)
        st.image("assets/security_basic_udemy.jpg", width=350)
        st.image("assets/intermediate_sql.jpg", width=350)
        st.image("assets/llm.jpg", width=350)

# --- LANGUAGES ---
st.markdown('<h3 class="section-title">🌐 Languages</h3>',
            unsafe_allow_html=True)
st.write(
    """
    - English (Fluent)  
    - Filipino (Native)  
    """
)

# --- INTERESTS ---
st.markdown('<h3 class="section-title">💡 Interests</h3>',
            unsafe_allow_html=True)
st.write(
    """
    - Hiking and outdoor adventures  
    - Watching movies and TV shows  
    - Volunteering in community tech workshops   
    - Learning new things and expanding my knowledge
    """
)

# --- CONNECT ---
st.write("\n")
st.subheader("🔗 Connect with Me", anchor=False)
st.write("[📂 GitHub](https://github.com/gr-dev-create)")
st.write("[💼 LinkedIn](www.linkedin.com/in/grace-villanueva-xxxxx)")
