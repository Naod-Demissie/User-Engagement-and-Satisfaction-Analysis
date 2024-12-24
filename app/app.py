from utils import *
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

DATA_PATH = "C:/dev/Side-Projects/10 Acadamy/W2 Challenge/User Engagement and Satisfaction Analysis/data/final_telecom_data.csv"
df = pd.read_csv(DATA_PATH)

with st.sidebar:
    selected = option_menu(
        menu_title="TeleScope",
        options=[
            "User Overview",
            "User Engagement",
            "User Experience",
            "User Satisfaction",
        ],
        icons=[
            "bi-clipboard-data",
            "bi-magnet",
            "bi-hand-index-thumb",
            "bi-emoji-smile",
        ],
        menu_icon="bi-broadcast-pin",
        default_index=0,
    )


if selected == "User Overview":
    st.header("User Overview Analysis")

    # Create a row layout
    c1, c2 = st.columns([1, 1.2])
    c3, c4 = st.columns(2)

    with c1:
        fig1 = display_top_handsets(df)
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        fig2 = display_top_handsets_by_manufacturer(df)
        st.plotly_chart(fig2, use_container_width=True)

    with c3:
        fig3 = display_top_3_manufacturers_bar(df)
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        fig4 = display_top_3_manufacturers_pie(df)
        st.plotly_chart(fig4, use_container_width=True)


if selected == "User Engagement":
    st.header("User Engagement Analysis")
    # Create a row layout
    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    with c1:
        fig1 = plot_all_app_traffic()
        # fig1 = plot_top_3_app_traffic()

        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        fig2 = plot_top_3_app_traffic()
        st.plotly_chart(fig2, use_container_width=True)

    with c3:
        fig3 = plot_engagement_scatter_interactive()
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        fig4 = plot_elbow_interactive()
        st.plotly_chart(fig4, use_container_width=True)


if selected == "User Experience":
    st.header("User Experience Analysis")
    # Create a row layout
    c1, c2 = st.columns(2)
    # c3, c4 = st.columns(2)

    with c1:
        fig1 = plot_avg_tcp_retransmission(df)
        st.plotly_chart(fig1)

        fig2 = plot_avg_throughput(df)
        st.plotly_chart(fig2)

    with c2:
        fig3 = plot_experience_scatter_interactive()
        st.plotly_chart(fig3)


if selected == "User Satisfaction":
    st.header("User Satisfaction Analysis")
    st.plotly_chart(plot_kmeans_clusters(df))
