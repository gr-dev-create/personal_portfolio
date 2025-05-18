import streamlit as st

st.set_page_config(
    page_title="grr portfolio",
    page_icon="assets/grr.png",
    layout="wide"
)
# -- PAGE CONFIGS ---

about_page = st.Page(
    page="pages/about_me.py",
    title="About Me",
    icon="👨‍🎓",
    default=True,
)
project_1_page = st.Page(
    page="pages/projects.py",
    title="Projects",
    icon="👨‍💻",
)
project_2_page = st.Page(
    page="pages/sales_dashboard.py",
    title="Sales Dashboard",
    icon="📈",
)

project_3_page = st.Page(
    page="pages/chatbot.py",
    title="Chat Bot",
    icon="💬",
)

# -- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[about_page, project_1_page,
                   project_2_page, project_3_page])

# -- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page],
    }
)
# --SHARED ON ALL PAGES ---
st.logo("assets/grr.png")
st.sidebar.text("Made with ♡ by grr.vi")
# -- RUN NAVIGATION ---
pg.run()
