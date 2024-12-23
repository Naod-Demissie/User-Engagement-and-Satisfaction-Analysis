import seaborn as sns
import matplotlib.pyplot as plt


def generate_hist_box_plots(df, plot_data):
    """Generates histplots and boxplots for a list of dictionaries of title and column name."""
    num_cols = len(plot_data)
    fig, axes = plt.subplots(
        nrows=2,
        ncols=num_cols,
        figsize=(17, 5),
        # sharey="row",
        sharex="col",
        gridspec_kw={"height_ratios": [7, 0.4]},
    )

    for i in range(len(plot_data)):
        sns.histplot(df[plot_data[i]["column"]], kde=True, ax=axes[0, i])
        sns.boxplot(x=df[plot_data[i]["column"]], ax=axes[1, i], orient="h")
        axes[1, i].set_xlabel(plot_data[i]["label"], fontsize=11)
        axes[0, i].set_title(plot_data[i]["title"], fontsize=13)

    axes[0, 0].set_ylabel("Frequency", fontsize=11)
    axes[0, 1].set_ylabel("Frequency", fontsize=11)
    fig.tight_layout()
    plt.show()


def plot_boxplot(df, column):
    """
    Plot a boxplot for a specified column of a DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column (str): The column name to plot.
    """
    plt.figure(figsize=(6, 0.5))
    plt.boxplot(df[column], vert=False)
    plt.title(f"Boxplot for {column}")
    plt.show()
