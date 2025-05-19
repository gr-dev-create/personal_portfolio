import streamlit as st

st.title("Projects")
st.write("Welcome to my project portfolio! Below are some of the key projects I've developed in the fields of web application development and game development. Click on the tabs to explore more details.")

user_manual = "https://drive.google.com/file/d/1l0WH3e6qGnO1_4YwFICRAIYjH612IUaw/view?usp=sharing"
tab1, tab2 = st.tabs(["Capstone", "Game Development"])

with tab1:
    st.header("[HikeKo - Hiker Reservation Platform](https://hikeko.vercel.app/)")
    st.markdown("""
        <iframe src="https://drive.google.com/file/d/1P1cvVo_Qh-m-lmYcqpFX0aHvGMfDju4F/preview" width="800" height="480" allow="autoplay"></iframe>
    """, unsafe_allow_html=True)
    st.image("assets/hikeko_hikersView.png", width=800)
    st.write("""
        HikeKo is a capstone project designed to streamline hiking trip reservations and event coordination for hikers and travel agencies in the Philippines.
        It features booking, subscription, and event management capabilities, along with a community discussion, and a reward system to enhance user engagement. 
        The platform is developed using modern web technologies including ReactJS, MongoDB, and Tailwind CSS.
    """)

    st.subheader(
        "[HikeKo Super Admin Panel](https://superadminhikeko.vercel.app/)")
    st.image("assets/superadmin_hikeko.png", width=800)
    st.write("""
        The Super Admin module allows for managing travel agency subscriptions, monitoring user activity, 
        and maintaining mountain and event data. This separate portal ensures effective system control 
        and administration over the entire HikeKo platform.
    """)

    st.subheader("User Manual")
    st.write("This user manual provides step-by-step guidance on how to use the HikeKo platform effectively.")
    st.markdown(
        f"""
        <iframe src="{user_manual}" width="100%" height="600px" frameborder="0" allowfullscreen></iframe>
        """, unsafe_allow_html=True,
    )

with tab2:
    st.header("Game Development Projects")

    st.subheader("TamaRun - Educational Platformer Game")
    st.write("""
        TamaRun is a 2D platformer game designed to make learning fun by combining gameplay mechanics with educational challenges. 
        The player must answer quiz questions correctly to continue progressing through levels while avoiding obstacles.
        Developed using Unity, it emphasizes player engagement and interactive learning.
    """)
    st.markdown("""
        <iframe src="https://drive.google.com/file/d/17X-a_tTE7fNbGEApCA5OPhm3GsZy2wP3/preview" width="800" height="480" allow="autoplay"></iframe>
    """, unsafe_allow_html=True)

    st.subheader("2D Infinite Runner")
    st.write("""
        This game is a 2D side-scrolling infinite runner where the player navigates through obstacles, 
        collecting coins and avoiding traps to achieve high scores. Built in Unity, it features smooth 
        animations, power-ups, and an increasing difficulty curve for replayability.
    """)
    st.markdown("""
        <iframe src="https://drive.google.com/file/d/17X-a_tTE7fNbGEApCA5OPhm3GsZy2wP3/preview" width="800" height="480" allow="autoplay"></iframe>
    """, unsafe_allow_html=True)
