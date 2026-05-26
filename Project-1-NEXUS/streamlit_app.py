import streamlit as st

st.set_page_config(
    page_title="NEXUS Personal OS",
    layout="centered"
)

st.title("NEXUS Personal OS")

st.markdown(
    "### Cyberpunk Productivity Terminal"
)

command = st.text_input(
    "Enter Command"
)

if command:

    st.success(
        f"Command received: {command}"
    )

    if command == "help":

        st.write("""
        help
        task add
        show tasks
        mood log
        motivate
        focus start
        brief today
        matrix
        self destruct
        """)