import streamlit as st

# -- PAGE CONFIGS ---

about_page = st.Page(
    page="pages/about_me.py",
    title="About Me",
    icon="👨‍🎓",
    default=True,
)

project_1_page = st.Page(
    page="pages/sales_dashboard.py",
    title="Sales Dashboard",
    icon="📈",
)

project_2_page = st.Page(
    page="pages/chatbot.py",
    title="Chat Bot",
    icon="💬",
)


# -- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# -- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)
# --SHARED ON ALL PAGES ---
st.logo("assets/grr.png")
st.sidebar.text("Made with ♡ by grr.vi")
# -- RUN NAVIGATION ---
pg.run()
