"""
Author Student ID: A00316036

Description: This module provides user-defined functions to calculate and display Numerical and Categorical Analysis
and their Visualizations based on the user's choice.
"""

from math import sqrt
from matplotlib_visualisations import draw_histogram, draw_numerical_box_plot, draw_scatter_plot, draw_pie_chart, draw_bar_chart, draw_categorical_box_plot


def get_mean(values_list):
    """
    Calculates the Mean of the list of values

    Parameters
    ----------
    values_list : list
        A list containing numeric values

    Returns
    -------
    float
        The mean of the provided list of values
    """
    return sum(values_list) / len(values_list)


def get_median(values_list):
    """
    Calculates the Median of the list of values

    Parameters
    ----------
    values_list : list
        A list containing numeric values

    Returns
    -------
    float
        The median of the provided list of values
    """
    sorted_list = sorted(values_list)
    mid_index = int(len(sorted_list) / 2)
    if len(sorted_list) % 2 != 0:
        return sorted_list[mid_index]
    else:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2


def get_mode(values_list):
    """
    Calculates the Mode of the list of values

    Parameters
    ----------
    values_list : list
        A list containing numeric values

    Returns
    -------
    float
        The mode of the provided list of values
    """
    distinct_values = list(set(values_list))
    frequencies = [values_list.count(value) for value in distinct_values]
    return distinct_values[frequencies.index(max(frequencies))]


def get_range(values_list):
    """
    Calculates the Range of the list of values

    Parameters
    ----------
    values_list : list
        A list containing numeric values

    Returns
    -------
    float
        The range of the provided list of values
    """
    return max(values_list) - min(values_list)


def get_inter_quartile_range(values_list):
    """
    Calculates the Inter Quartile range of the list of values

    Parameters
    ----------
    values_list : list
        A list containing numeric values

    Returns
    -------
    float
        The Inter quartile range of the provided list of values
    """
    sorted_list = sorted(values_list)
    mid_index = int(len(sorted_list) / 2)
    lower_half = sorted_list[:mid_index]
    if len(sorted_list) % 2 != 0:
        upper_half = sorted_list[mid_index + 1:]
    else:
        upper_half = sorted_list[mid_index:]
    return get_median(upper_half) - get_median(lower_half)


def get_standard_deviation(values_list):
    """
    Calculates the Standard Deviation of the list of values

    Parameters
    ----------
    values_list : list
        A list containing numeric values

    Returns
    -------
    float
        The standard deviation of the provided list of values
    """
    mean = get_mean(values_list)
    squared_deviations = [(value - mean) ** 2 for value in values_list]
    return sqrt(sum(squared_deviations) / (len(values_list) - 1))


def get_mode_skewness(values_list):
    """
    Calculates the Mode Skewness of the list of values

    Parameters
    ----------
    values_list : list
        A list containing numeric values

    Returns
    -------
    float
        The mode skewness of the provided list of values
    """
    return (get_mean(values_list) - get_mode(values_list)) / get_standard_deviation(values_list)


def get_median_skewness(values_list):
    """
    Calculates the Median Skewness of the list of values

    Parameters
    ----------
    values_list : list
        A list containing numeric values

    Returns
    -------
    float
        The median skewness of the provided list of values
    """
    return (3 * (get_mean(values_list) - get_median(values_list))) / get_standard_deviation(values_list)


def display_numerical_analysis(title, values_list):
    """
    Performs numerical analysis on the given list of values corresponding to a numerical column

    Parameters
    ----------
    title : str
        The title of the numerical column whose values are to be analysed
    values_list : list
        A list containing numeric values

    Returns
    -------
    None - default
    """
    print(title)
    print("-" * len(title))
    print(f"Number of scores: {len(values_list)}")
    print(f"Average: {sum(values_list) / len(values_list):.2f}")
    print(f"Minimum: {min(values_list)}")
    print(f"Maximum: {max(values_list)}")
    print(f"Mean: {get_mean(values_list):.2f}")
    print(f"Median: {get_median(values_list):.2f}")
    print(f"Mode: {get_mode(values_list)}")
    print(f"Range: {get_range(values_list)}")
    print(f"Inter-quartile range: {get_inter_quartile_range(values_list):.2f}")
    print(f"Standard deviation: {get_standard_deviation(values_list):.2f}")
    print(f"Mode Skewness: {get_mode_skewness(values_list):.2f}")
    print(f"Median Skewness: {get_median_skewness(values_list):.2f}")


def get_correlation(x_values, y_values):
    """
    Calculates the Correlation between the two lists of values

    Parameters
    ----------
    x_values : list
        A list containing numeric values
    y_values : list
        A list containing numeric values

    Returns
    -------
    float
        The correlation between the two provided lists of values
    """
    x_mean = get_mean(x_values)
    y_mean = get_mean(y_values)
    x_deviations = [(x - x_mean) for x in x_values]
    y_deviations = [(y - y_mean) for y in y_values]
    xy_deviations = [x * y for (x, y) in zip(x_deviations, y_deviations)]
    x_squared_deviations = [x ** 2 for x in x_deviations]
    y_squared_deviations = [y ** 2 for y in y_deviations]
    return sum(xy_deviations) / (sqrt(sum(x_squared_deviations)) * sqrt(sum(y_squared_deviations)))


def display_correlation(academic_reputation_scores, overall_scores):
    """
    Calculates and displays the correlation between two numerical columns using their lists of values

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
    print(
        f"Correlation between Academic Reputation Scores and Overall Scores: {get_correlation(academic_reputation_scores, overall_scores):.3f}")


def analyse_numerical_data(academic_reputation_scores, overall_scores):
    """
    Perform numerical analysis on the two numerical columns using their lists of values

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
    print()
    print("---------------------------")
    print("| Numerical Data Analysis |")
    print("---------------------------")
    print()

    display_numerical_analysis("Academic reputation (Score)", academic_reputation_scores)
    print()
    display_numerical_analysis("Overall (Score)", overall_scores)
    print()
    display_correlation(academic_reputation_scores, overall_scores)

    while True:
        try:
            option_selected = int(input("\nEnter 1 to go back: "))
            if option_selected == 1:
                break
            print("Wrong input!")
        except ValueError:
            print("Wrong input!")


def visualise_numerical_data(academic_reputation_scores, overall_scores):
    """
    Perform numerical visualisation based on user input on the two numerical columns using their lists of values

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
    print()
    print("--------------------------------")
    print("| Numerical Data Visualisation |")
    print("--------------------------------")

    while True:
        print()
        print("How do you like to visualise the numerical data?")
        print("------------------------------------------------")
        print("1. Histograms")
        print("2. Box plots")
        print("3. Scatter plot")
        print("4. Go back")
        try:
            option_selected = int(input("Enter the option: "))
            if option_selected == 1:
                draw_histogram(academic_reputation_scores, overall_scores)
            elif option_selected == 2:
                draw_numerical_box_plot(academic_reputation_scores, overall_scores)
            elif option_selected == 3:
                draw_scatter_plot(academic_reputation_scores, overall_scores)
            elif option_selected == 4:
                break
            else:
                print("Wrong input!")
        except ValueError:
            print("Wrong input!")


def analyse_and_visualise_numerical_data(academic_reputation_scores, overall_scores):
    """
    Analyse and Visualise the numerical columns using their lists of values

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

    while True:
        print()
        print("---------------------------------------------")
        print("| Numerical Data Analysis and Visualisation |")
        print("---------------------------------------------")
        print()
        print("What would you like to perform?")
        print("-------------------------------")
        print("1. Analyse numerical data")
        print("2. Visualise numerical data")
        print("3. Go back")
        try:
            option_selected = int(input("Enter the option (1, 2 or 3): "))
            if option_selected == 1:
                analyse_numerical_data(academic_reputation_scores, overall_scores)
            elif option_selected == 2:
                visualise_numerical_data(academic_reputation_scores, overall_scores)
            elif option_selected == 3:
                print()
                break
            else:
                print("Wrong input!")
        except ValueError:
            print("Wrong input!")


def get_maximum_and_minimum_frequency(region_frequency_dict):
    """
    Calculate and display the regions with maximum and minimum frequency

    Parameters
    ----------
    region_frequency_dict : dict
        A dictionary with region sub-category as keys and its frequency as values

    Returns
    -------
    None - default
    """
    region_with_maximum_frequency = max(region_frequency_dict, key=region_frequency_dict.get)
    print(
        f"Region with most top-ranked Institutions: {region_with_maximum_frequency} ({region_frequency_dict[region_with_maximum_frequency]})")
    region_with_minimum_frequency = min(region_frequency_dict, key=region_frequency_dict.get)
    print(
        f"Region with fewest top-ranked Institutions: {region_with_minimum_frequency} ({region_frequency_dict[region_with_minimum_frequency]})")


def get_maximum_and_minimum_average(region_scores_dict):
    """
    Calculate and display the regions with maximum and minimum average overall score

    Parameters
    ----------
    region_scores_dict : dict
        A dictionary with region sub-category as keys and the list of Institutions' scores as values

    Returns
    -------
    None - default
    """
    average_scores_per_region = [sum(scores) / len(scores) for scores in region_scores_dict.values()]
    highest_average_score = max(average_scores_per_region)
    lowest_average_score = min(average_scores_per_region)
    regions = list(region_scores_dict.keys())
    region_with_highest_average_score = regions[average_scores_per_region.index(highest_average_score)]
    region_with_lowest_average_score = regions[average_scores_per_region.index(lowest_average_score)]
    print(f"Region with highest average score: {region_with_highest_average_score} ({highest_average_score:.3f})")
    print(f"Region with lowest average score: {region_with_lowest_average_score} ({lowest_average_score:.3f})")


def analyse_categorical_data(region_frequency_dict, region_scores_dict):
    """
    Performs categorical analysis on the given dictionaries corresponding to a categorical column and its associated numerical values

    Parameters
    ----------
    region_scores_dict : dict
        A dictionary with region sub-category as keys and the list of Institutions' scores as values
    region_frequency_dict : dict
        A dictionary with region sub-category as keys and its frequency as values

    Returns
    -------
    None - default
    """
    print()
    print("-----------------------------")
    print("| Categorical Data Analysis |")
    print("-----------------------------")
    print()
    print(f"Number of Regions: {len(region_frequency_dict)}")
    get_maximum_and_minimum_frequency(region_frequency_dict)
    get_maximum_and_minimum_average(region_scores_dict)

    while True:
        try:
            option_selected = int(input("\nEnter 1 to go back: "))
            if option_selected == 1:
                break
            print("Wrong input!")
        except ValueError:
            print("Wrong input!")


def visualise_categorical_data(region_frequency_dict, region_scores_dict):
    """
    Perform categorical visualisation based on user input using the given dictionaries corresponding to a categorical column and its associated numerical values

    Parameters
    ----------
    region_scores_dict : dict
        A dictionary with region sub-category as keys and the list of Institutions' scores as values
    region_frequency_dict : dict
        A dictionary with region sub-category as keys and its frequency as values

    Returns
    -------
    None - default
    """
    print()
    print("----------------------------------")
    print("| Categorical Data Visualisation |")
    print("----------------------------------")

    while True:
        print()
        print("How do you like to visualise the categorical data?")
        print("--------------------------------------------------")
        print("1. Pie chart")
        print("2. Bar chart")
        print("3. Box plots")
        print("4. Go back")
        try:
            option_selected = int(input("Enter the option: "))
            if option_selected == 1:
                draw_pie_chart(region_frequency_dict)
            elif option_selected == 2:
                draw_bar_chart(region_frequency_dict)
            elif option_selected == 3:
                draw_categorical_box_plot(region_scores_dict)
            elif option_selected == 4:
                break
            else:
                print("Wrong input!")
        except ValueError:
            print("Wrong input!")


def analyse_and_visualise_categorical_data(region_scores_dict, region_frequency_dict):
    """
    Analyse and Visualise the categorical data along with its associated numerical data using its dictionaries

    Parameters
    ----------
    region_scores_dict : dict
        A dictionary with region sub-category as keys and the list of Institutions' scores as values
    region_frequency_dict : dict
        A dictionary with region sub-category as keys and its frequency as values

    Returns
    -------
    None - default
    """
    while True:
        print()
        print("-----------------------------------------------")
        print("| Categorical Data Analysis and Visualisation |")
        print("-----------------------------------------------")
        print()
        print("What would you like to perform?")
        print("-------------------------------")
        print("1. Analyse categorical data")
        print("2. Visualise categorical data")
        print("3. Go back")
        try:
            option_selected = int(input("Enter the option (1, 2 or 3): "))
            if option_selected == 1:
                analyse_categorical_data(region_frequency_dict, region_scores_dict)
            elif option_selected == 2:
                visualise_categorical_data(region_frequency_dict, region_scores_dict)
            elif option_selected == 3:
                print()
                break
            else:
                print("Wrong input!")
        except ValueError:
            print("Wrong input!")
