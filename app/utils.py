import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def display_top_handsets(df):
    """Generate an interactive plot of the top 10 most-used handsets with unique colors."""
    # Get the top 10 most-used handsets
    top_10_handsets = df["Handset Type"].value_counts().head(10)

    # Convert to DataFrame for visualization
    top_10_handsets_df = top_10_handsets.reset_index()
    top_10_handsets_df.columns = ["Handset Type", "Count"]

    # Create the plot using Plotly with unique colors for each bar
    fig = px.bar(
        top_10_handsets_df,
        x="Count",
        y="Handset Type",
        orientation="h",
        title="Top 10 Most-Used Handsets",
        labels={"Count": "Count", "Handset Type": "Handset Type"},
        text="Count",
        color="Handset Type",
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        height=480,
        showlegend=False,
    )

    return fig


def display_top_3_manufacturers_bar(df):
    """Generate an interactive bar chart for the top 3 handset manufacturers."""
    # Group by 'Handset Manufacturer' and count occurrences
    top_3_manufacturers = df["Handset Manufacturer"].value_counts().head(3)

    # Convert to DataFrame for visualization
    # Group by 'Handset Manufacturer' and count occurrences
    top_3_manufacturers = df["Handset Manufacturer"].value_counts().head(3)

    # Convert to DataFrame for visualization
    top_3_manufacturers_df = top_3_manufacturers.reset_index()
    top_3_manufacturers_df.columns = ["Handset Manufacturer", "Count"]

    # Create the interactive bar chart
    fig = px.bar(
        top_3_manufacturers_df,
        x="Count",
        y="Handset Manufacturer",
        orientation="h",
        title="Top 3 Handset Manufacturers (Bar Chart)",
        labels={"Count": "Count", "Handset Manufacturer": "Handset Manufacturer"},
        text="Count",
        color="Handset Manufacturer",
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        height=400,
        showlegend=False,
    )

    return fig


def display_top_3_manufacturers_pie(df):
    """Generate an interactive pie chart for the top 3 handset manufacturers, including 'Others'."""
    # Group by 'Handset Manufacturer' and count occurrences
    top_3_manufacturers = df["Handset Manufacturer"].value_counts().head(3)
    other_manufacturers_count = df["Handset Manufacturer"].value_counts().iloc[3:].sum()

    # Add 'Others' category
    top_3_manufacturers["Others"] = other_manufacturers_count

    # Generate the color palette
    colors = px.colors.sequential.Viridis[: len(top_3_manufacturers)]

    # Create the interactive pie chart
    fig = go.Figure(
        data=[
            go.Pie(
                labels=top_3_manufacturers.index,
                values=top_3_manufacturers.values,
                textinfo="percent+label",
                hole=0.3,
                marker=dict(colors=colors),
            )
        ]
    )
    fig.update_layout(
        title="Top 3 Handset Manufacturers (Percentage)", title_font_size=20, height=400
    )

    return fig


def display_top_handsets_by_manufacturer(df):
    """Generate an interactive horizontal bar chart for the top 5 handsets of the top 3 manufacturers."""
    # Get the top 3 manufacturers
    top_3_manufacturers = df["Handset Manufacturer"].value_counts().head(3).index

    # Prepare data for plotting
    plot_data = []
    for manufacturer in top_3_manufacturers:
        top_5_handsets = (
            df[df["Handset Manufacturer"] == manufacturer]["Handset Type"]
            .value_counts()
            .head(5)
        )
        for handset, count in top_5_handsets.items():
            plot_data.append(
                {"Manufacturer": manufacturer, "Handset": handset, "Count": count}
            )

    plot_df = pd.DataFrame(plot_data)

    # Create the interactive bar chart
    fig = px.bar(
        plot_df,
        x="Count",
        y="Handset",
        color="Manufacturer",
        orientation="h",
        title="Top 5 Handsets per Top 3 Manufacturers",
        text="Count",
        color_discrete_sequence=px.colors.qualitative.Set1,
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title="Count",
        yaxis_title="Handset",
        height=500,
        showlegend=False,
    )

    return fig


def plot_engagement_scatter_interactive():
    """Generate an interactive 2D scatter plot of Total Traffic vs Total Session Duration with Cluster as hue."""
    # Load the data
    normalized_data = pd.read_csv(
        "C:/dev/Side-Projects/10 Acadamy/W2 Challenge/User Engagement and Satisfaction Analysis/data/streamlit_data/engagement_cluster_data.csv"
    )

    # Create the interactive scatter plot using Plotly
    fig = px.scatter(
        normalized_data,
        x="Total_Traffic",
        y="Total_Session_Duration",
        color="Cluster",
        title="K-Means Clustering: Total Traffic vs Total Session Duration",
        labels={
            "Total_Traffic": "Total Traffic",
            "Total_Session_Duration": "Total Session Duration",
        },
        color_continuous_scale=px.colors.qualitative.Set1,
        template="plotly",
    )

    # Update the layout to remove the color bar
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        height=400,
        showlegend=False,
        coloraxis_showscale=False,
    )

    return fig


import plotly.graph_objects as go


def plot_elbow_interactive():
    """Generate an interactive Elbow Method plot using Plotly."""
    k_values = list(range(1, 11))
    wcss = [
        1441.2847729772693,
        715.8046245825392,
        484.1252598695029,
        386.04931654440617,
        325.04113227033736,
        285.1383496018725,
        254.92665917891972,
        236.8345844164116,
        221.34939999179946,
        205.73188429463082,
    ]

    # Create the interactive line plot
    fig = go.Figure(
        data=[
            go.Scatter(
                x=k_values,
                y=wcss,
                mode="lines+markers",
                marker=dict(color="blue"),
                name="WCSS",
            )
        ]
    )

    # Update layout with titles and labels
    fig.update_layout(
        title="Elbow Method for Optimal K",
        title_font_size=20,
        xaxis_title="Number of Clusters (k)",
        yaxis_title="Within-Cluster Sum of Squares (WCSS)",
        xaxis=dict(tickmode="array", tickvals=k_values),
        template="plotly_dark",
    )

    return fig


import pandas as pd
import plotly.express as px


def plot_all_app_traffic():
    """
    Plot a bar chart showing total traffic for all applications.

    Returns:
        plotly.graph_objects.Figure: The generated Plotly figure.
    """
    # Load the data from the CSV file
    total_traffic_per_app = pd.read_csv(
        "C:/dev/Side-Projects/10 Acadamy/W2 Challenge/User Engagement and Satisfaction Analysis/data/streamlit_data/total_traffic_per_app_data.csv"
    )

    # Convert the data into a DataFrame
    total_traffic_per_app.columns = ["Application", "Total_Traffic"]

    # Create the bar chart
    fig = px.bar(
        total_traffic_per_app,
        x="Application",
        y="Total_Traffic",
        title="Most Used Applications by Total Traffic",
        labels={
            "Application": "Applications",
            "Total_Traffic": "Total Traffic (Bytes)",
        },
        color="Total_Traffic",
        color_continuous_scale="Blues",
    )

    # Update layout
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        # xaxis_tickangle=-45,
        height=400,
        showlegend=False,
    )

    return fig


def plot_top_3_app_traffic():
    """Plot a bar chart showing total traffic for the top 3 applications."""
    # Load the data from the CSV file
    total_traffic_per_app = pd.read_csv(
        "C:/dev/Side-Projects/10 Acadamy/W2 Challenge/User Engagement and Satisfaction Analysis/data/streamlit_data/total_traffic_per_app_data.csv"
    )
    total_traffic_per_app.columns = ["Application", "Total_Traffic"]

    # Sort and select the top 3 applications by total traffic
    top_3_apps_data = total_traffic_per_app.sort_values(
        by="Total_Traffic", ascending=False
    ).head(3)

    # Create the bar chart
    fig = px.bar(
        top_3_apps_data,
        x="Application",
        y="Total_Traffic",
        title="Top 3 Most Used Applications by Total Traffic",
        labels={
            "Application": "Applications",
            "Total_Traffic": "Total Traffic (Bytes)",
        },
        color="Total_Traffic",
        color_continuous_scale="Blues",
    )

    # Update layout
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        xaxis_tickangle=-45,
        height=400,
        showlegend=False,
    )

    return fig


def plot_avg_tcp_retransmission(df):
    # Calculate average TCP retransmission per handset type
    avg_tcp_retransmission_per_handset = (
        df.groupby("Handset Type")["Total TCP Retransmission"]
        .mean()
        .sort_values(ascending=False)
    )

    # Get the top 20 handset types
    top_20_handsets = avg_tcp_retransmission_per_handset.head(20)

    # Create the plot using Plotly Express
    fig = px.bar(
        top_20_handsets,
        x=top_20_handsets.values,
        y=top_20_handsets.index,
        orientation="h",
        labels={"x": "Average TCP Retransmission (Bytes)", "y": "Handset Type"},
        title="Average TCP Retransmission Per Handset Type (Top 20)",
        color=top_20_handsets.values,
        color_continuous_scale="Viridis",
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        xaxis_tickangle=-45,
        height=400,
        showlegend=False,
    )

    # Show the plot in Streamlit
    return fig


def plot_avg_throughput(df):
    # Calculate average throughput per handset type
    avg_throughput_per_handset = (
        df.groupby("Handset Type")["Total Throughput"]
        .mean()
        .sort_values(ascending=False)
    )

    # Get the top 20 handset types
    top_20_handsets = avg_throughput_per_handset.head(20)

    fig = px.bar(
        top_20_handsets,
        x=top_20_handsets.values,
        y=top_20_handsets.index,
        orientation="h",
        labels={
            "x": "Average Throughput (kbps)",
            "y": "Handset Type",
        },
        title="Average Throughput Per Handset Type (Top 20)",
        color=top_20_handsets.values,
        color_continuous_scale="Viridis",
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        xaxis_tickangle=-45,
        height=400,
        showlegend=False,
    )

    # Show the plot in Streamlit
    return fig


def plot_experience_scatter_interactive():
    # Load the data
    pca_data = pd.read_csv(
        "C:/dev/Side-Projects/10 Acadamy/W2 Challenge/User Engagement and Satisfaction Analysis/data/streamlit_data/experience_pca_data.csv"
    ).drop("Unnamed: 0", axis=1)

    # Create the interactive scatter plot using Plotly
    fig = px.scatter(
        pca_data,
        x="PCA1",
        y="PCA2",
        color="Cluster",
        title="Clusters of User Experience (PCA-reduced)",
        labels={
            "x": "PCA1",
            "y": "PCA2",
        },
        color_continuous_scale=px.colors.qualitative.Set1,
        template="plotly",
    )

    # Update the layout to remove the color bar
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        height=800,
        showlegend=False,
        coloraxis_showscale=False,
    )

    return fig


def plot_kmeans_clusters(df):
    # Create a scatter plot using Plotly
    fig = px.scatter(
        df,
        x="engagement_score",
        y="experience_score",
        color=df["satisfaction_cluster"],
        color_continuous_scale="viridis",
        title="K-means Clustering on Engagement and Experience Scores",
        labels={
            "x": "Engagement Score",
            "y": "Experience Score",
        },
        template="plotly_dark",
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        height=750,
        showlegend=True,
        coloraxis_showscale=True,
    )

    # Return the figure to be rendered in Streamlit or shown in an interactive window
    return fig
