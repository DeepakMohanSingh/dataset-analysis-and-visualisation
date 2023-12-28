"""
Author Student ID: A00316036

Description: This module contains user-defined functions to generate visualisations using matplotlib.
"""

import matplotlib.pyplot as plt


def export_visualisation(figure, filename):
    """
    Export the generated matplotlib visualisation in the directory where the modules are being placed

    Parameters
    ----------
    figure : matplotlib.figure.Figure
        An object containing axes object(s) of visualisation generated
    filename : str
        The name of the visualisation to be exported

    Returns
    -------
    None - default
    """
    print(f"\nWould you like to export the {filename}?")
    print("------------------------------" + (len(filename) * "-"))
    is_visualisation_exported = False
    while True:
        try:
            option_selected = int(input(f"1. Export Visualisation {'again' if is_visualisation_exported else ''}\n2. Go back\nEnter the option (1 or 2): "))
            if option_selected == 1:
                figure.savefig(f"{filename}.png")
                print()
                print("--------------------------" + (len(filename) * "-"))
                print(f"| {filename} exported successfully |")
                print("--------------------------" + (len(filename) * "-"))
                print()
                is_visualisation_exported = True
            elif option_selected == 2:
                break
            else:
                print("\nWrong input!\n")
        except ValueError:
            print("\nWrong input!\n")


def draw_histogram(academic_reputation_scores, overall_scores):
    """
    Generate histograms of the given two lists of values corresponding to the two numerical columns - Academic reputation scores and Overall scores

    Parameters
    ----------
    academic_reputation_scores : list
        A list containing Academic Reputation Scores
    overall_scores : list
        A list containing Overall Scores

    Returns
    -------
    None - default
    """
    figure, axes = plt.subplots(1, 2, figsize=(12, 6))
    figure.suptitle("QS World University Rankings 2023 - Numerical Visualisation: Histograms")

    axes[0].set_title("Frequency of Academic Reputation Scores")
    axes[0].set_xlabel("Academic Reputation Score")
    axes[0].set_ylabel("Frequency")
    bins = range(0, int(max(academic_reputation_scores)) + 10, 10)
    axes[0].set_xticks(bins)
    axes[0].hist(academic_reputation_scores, bins=bins, color="orange", edgecolor="black")

    axes[1].set_title("Frequency of Overall scores")
    axes[1].set_xlabel("Overall Score")
    axes[1].set_ylabel("Frequency")
    bins = range(0, int(max(overall_scores)) + 10, 10)
    axes[1].set_xticks(bins)
    axes[1].hist(overall_scores, bins=bins, color="green", edgecolor="black")

    plt.show()
    export_visualisation(figure, "Numerical Visualisation - Histograms")


def draw_numerical_box_plot(academic_reputation_scores, overall_scores):
    """
    Generate box plot of the given two lists of values corresponding to the two numerical columns - Academic reputation scores and Overall scores

    Parameters
    ----------
    academic_reputation_scores : list
        A list containing Academic Reputation Scores
    overall_scores : list
        A list containing Overall Scores

    Returns
    -------
    None - default
    """
    figure, axes = plt.subplots(1, 2, figsize=(12, 6))
    figure.suptitle("QS World University Rankings 2023 - Numerical Visualisation: Box plots")

    axes[0].set_title("Academic reputation scores of Institutions")
    axes[0].set_ylabel("Academic reputation scores")
    axes[0].boxplot(academic_reputation_scores, showmeans=True, meanline=True, showfliers=False)

    axes[1].set_title("Overall scores of Institutions")
    axes[1].set_ylabel("Overall scores")
    axes[1].boxplot(overall_scores, showmeans=True, meanline=True, showfliers=False)

    plt.show()
    export_visualisation(figure, "Numerical Visualisation - Box plots")


def draw_scatter_plot(academic_reputation_scores, overall_scores):
    """
    Generate scatter plot of the given two lists of values corresponding to the two numerical columns - Academic reputation scores and Overall scores

    Parameters
    ----------
    academic_reputation_scores : list
        A list containing Academic Reputation Scores
    overall_scores : list
        A list containing Overall Scores

    Returns
    -------
    None - default
    """
    figure, axes = plt.subplots(figsize=(12, 6))
    figure.suptitle("QS World University Rankings 2023 - Numerical Visualisation: Scatter plot")

    axes.set_title("Top-ranked Institutions' scores")
    axes.set_xlabel("Overall score")
    axes.set_ylabel("Academic reputation score")
    axes.scatter(academic_reputation_scores, overall_scores, marker=".")

    plt.show()
    export_visualisation(figure, "Numerical Visualisation - Scatter plot")


def draw_pie_chart(region_frequency_dict):
    """
    Generate Pie chart of the categorical data along with its frequencies

    Parameters
    ----------
    region_frequency_dict : dict
        A dictionary with region sub-category as the key and the frequency as value

    Returns
    -------
    None - default
    """
    figure, axes = plt.subplots(figsize=(8, 6))
    figure.suptitle("QS World University Rankings 2023 - Categorical Visualisation: Pie chart")

    axes.set_title("Top-ranked Institutions by region")
    axes.pie(region_frequency_dict.values(), labels=region_frequency_dict.keys(), autopct="%.0f%%")

    plt.show()
    export_visualisation(figure, "Categorical Visualisation - Pie chart")


def draw_bar_chart(region_frequency_dict):
    """
    Generate Bar chart of the categorical data along with its frequencies

    Parameters
    ----------
    region_frequency_dict : dict
        A dictionary with region sub-category as the key and the frequency as value

    Returns
    -------
    None - default
    """
    figure, axes = plt.subplots(figsize=(12, 6))
    figure.suptitle("QS World University Rankings 2023 - Categorical Visualisation: Bar chart")

    axes.set_title("Top-ranked Institutions by region")
    axes.set_xlabel("Total number of top-ranked Institutions")
    axes.set_ylabel("Region")
    y_pos = [value for value in range(len(region_frequency_dict))]
    axes.set_yticks(y_pos)
    axes.set_yticklabels(region_frequency_dict.keys())
    for index, value in enumerate(region_frequency_dict.values()):
        axes.text(value, index - 0.1, str(value))

    axes.barh(y_pos, region_frequency_dict.values(), align="center")

    plt.show()
    export_visualisation(figure, "Categorical Visualisation - Bar chart")


def draw_categorical_box_plot(region_scores_dict):
    """
    Generate Box plot of the categorical data where region is the category and the corresponding scores of institutions in that region

    Parameters
    ----------
    region_scores_dict : dict
        A dictionary with region sub-category as the key and the list of Institutions' scores as value

    Returns
    -------
    None - default
    """
    figure, axes = plt.subplots(figsize=(10, 6))
    figure.suptitle("QS World University Rankings 2023 - Categorical Visualisation: Box plots")

    axes.set_title("Top-ranked Institutions by region")
    axes.set_xlabel("Region")
    axes.set_ylabel("Overall scores of Institutions")
    axes.boxplot(list(region_scores_dict.values()), showfliers=False, showmeans=True, meanline=True,
                 labels=region_scores_dict.keys())

    plt.show()
    export_visualisation(figure, "Categorical Visualisation - Box plots")
