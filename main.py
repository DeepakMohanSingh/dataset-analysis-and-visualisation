"""
Author Student ID: A00316036

Description: This module provides an interactive menu for users to perform either Numerical Analysis and Visualization
or Categorical Analysis and Visualization based on a selected dataset "QS World Rankings - 2023".
"""

from analysis_and_visualisation import analyse_and_visualise_numerical_data, analyse_and_visualise_categorical_data

if __name__ == '__main__':
    academic_reputation_scores = []
    overall_scores = []
    region_scores_dict = {}
    region_frequency_dict = {}

    try:
        # Reading the dataset file to add required columns to perform analysis/visualisation
        with open("dataset.csv") as data_file:
            data_file.readline()

            for line in data_file:
                try:
                    rank, institution, country, region, size, academic_reputation, employer_reputation, citations_per_faculty, international_faculty_ratio, international_students_ratio,  employment_outcomes, overall_score = line.strip().split(',')
                except ValueError:
                    print("Error splitting line:", line)

                try:
                    rank = int(rank)
                except ValueError:
                    print("Error parsing Rank to int:", rank)
                try:
                    academic_reputation = float(academic_reputation)
                except ValueError:
                    if academic_reputation == "":
                        academic_reputation = 0
                    else:
                        print("Error parsing Academic Reputation Score to float:", academic_reputation)
                try:
                    employer_reputation = float(employer_reputation)
                except ValueError:
                    if employer_reputation == "":
                        employer_reputation = 0
                    else:
                        print("Error parsing Employer Reputation to float:", employer_reputation)
                try:
                    citations_per_faculty = float(citations_per_faculty)
                except ValueError:
                    if citations_per_faculty == "":
                        citations_per_faculty = 0
                    else:
                        print("Error parsing Citations per faculty to float:", citations_per_faculty)
                try:
                    international_faculty_ratio = float(international_faculty_ratio)
                except ValueError:
                    if international_faculty_ratio == "":
                        international_faculty_ratio = 0
                    else:
                        print("Error parsing International Faculty Ratio to float:", international_faculty_ratio)
                try:
                    international_students_ratio = float(international_students_ratio)
                except ValueError:
                    if international_students_ratio == "":
                        international_students_ratio = 0
                    else:
                        print("Error parsing to International Students Ratio to float:", international_students_ratio)
                try:
                    employment_outcomes = float(employment_outcomes)
                except ValueError:
                    if employment_outcomes == "":
                        employment_outcomes = 0
                    else:
                        print("Error parsing Employment Outcomes to float:", employment_outcomes)
                try:
                    overall_score = float(overall_score)
                except ValueError:
                    if overall_score == "":
                        overall_score = 0
                    else:
                        print("Error parsing Overall Score to float:", overall_score)

                # Adding the Academic Reputation Score column's values to list
                academic_reputation_scores.append(academic_reputation)
                # Adding the Overall Score column's values to list
                overall_scores.append(overall_score)
                # Adding the Overall Score column's values to dictionary with key being the Region
                if region_scores_dict.get(region) is None:
                    region_scores_dict[region] = [overall_score]
                else:
                    region_scores_dict[region].append(overall_score)
                # Calculating and assigning Region frequency in dictionary with key being the Region
                region_frequency_dict[region] = region_frequency_dict.get(region, 0) + 1

    except FileNotFoundError:
        print("File not found")

    while True:
        print("*****************************************************************")
        print("| Exploratory Data Analysis - QS World University Rankings 2023 |")
        print("*****************************************************************")
        print()
        print("What would you like to perform?")
        print("-------------------------------")
        print("1. Numerical Analysis and Visualisation")
        print("2. Categorical Analysis and Visualisation")
        print("3. Quit")
        try:
            option_selected = int(input("Enter the option (1, 2 or 3): "))
            if option_selected == 1:
                # Perform analysis and visualisation of numerical data
                analyse_and_visualise_numerical_data(academic_reputation_scores, overall_scores)
            elif option_selected == 2:
                # Perform analysis and visualisation of categorical data
                analyse_and_visualise_categorical_data(region_scores_dict, region_frequency_dict)
            elif option_selected == 3:
                break
            else:
                print("Wrong input!\n")
        except ValueError:
            print("Wrong input!\n")
    print()
    print("***********************************")
    print("| Thank you! I hope you liked it. |")
    print("***********************************")
