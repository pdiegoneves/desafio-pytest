import streamlit as st

from components.header import header
from components.tasks import add_task, tasks

st.set_page_config(page_icon="🎯", page_title="Cliente para consumo da API")


def main():
    header()
    add_task()
    tasks()


if __name__ == "__main__":
    main()
