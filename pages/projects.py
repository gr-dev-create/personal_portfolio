import streamlit as st

st.title("Projects")

st.write("This is the projects page")

tab1, tab2, tab3 = st.tabs(["Capstone", "Game Development", "Owl"])

with tab1:
    st.header("[Hikeko](https://hikeko.vercel.app/)")
    st.image("assets/hikeko_hikersView.png", width=800)

    st.subheader("[Hikeko Super Admin](https://superadminhikeko.vercel.app/)")
    st.image("assets/superadmin_hikeko.png", width=800)

with tab2:
    st.header("Game development")
    # Google Drive Video Embed
    st.markdown("""
        <iframe src="https://drive.google.com/file/d/17X-a_tTE7fNbGEApCA5OPhm3GsZy2wP3/view?usp=sharing" width="800" height="480" allow="autoplay"></iframe>
    """, unsafe_allow_html=True)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
