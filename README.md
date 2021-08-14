# Project-1
Data Analyst/Engineer/Scientist Job Analysis

## About the data
* Pulled from Kaggle.com
* Dataset name on Kaggle: Indeed Dataset (Data Scientist, Analyst, and Engineer)
* Link to dataset: [Indeed Dataset](https://www.kaggle.com/elroyggj/indeed-dataset-data-scientistanalystengineer?select=indeed_job_dataset.csv)
* Age of dataset: 11/02/2018
* The data was originally sourced from Indeed.
* Kaggle Usability Score: 3.5
* 43 Columns
* 5715 Rows

#### Presenters
* Shailza Rattu
* Lori Pepper
* Susana Villagrana
* Jennifer Rocha

### Presentation
To view the presentation, click below (This will require you to download the file, but it will have audio):

   ![Data Analyst Job Market](https://github.com/jennifermarie6sl/Project-1/blob/e5fed65a16d19056c854859958325d39fc344a75/Presentation/FINAL_Project%201_Indeed%20Data%20Analysis.ppsx "Data Analyst Job Market")
   
 To view a .pdf version of the slides, click below:
 
   ![Data Analyst Job Market.pdf](https://github.com/jennifermarie6sl/Project-1/blob/92b7ad80f14b48936a3f46913bbbb8e07a38e4c8/Presentation/FINAL_Project%201_Indeed%20Data%20Analysis.pdf)
   
 # Cleaning
* You can find our Jupyter Notebook and cleaned dataset in the !["Finalized Group Code"](https://github.com/jennifermarie6sl/Project-1/tree/main/Finalized%20Group%20Code) folder.
* Dropped columns: 'Link', 'Date Since Posted', and 'Description'.
* Adjusted data types when necessary
* Added latitude, longitude, and cost-of-living index for use with 'Location'
* Modified data format for use in visualizations
* Merged four, cleaned .csv files into one dataset for analysis and visualizations
   
# Presentation Summary   

Since everyone, or most of us, taking this bootcamp are planning to go into a data related field, we decided to present on our findings in the Data Analyst, Data Engineer, and Data Scientist job market. Below you will find a summary on our findings.

##  Overview
  
 ###### Figure 1: Top 10 most required skills in this field.
![Top skills needed for Data Analyst, Engineer, and Scientist positions](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Top_Skills.png)

###### Figure 2: Top five industries with job openings.
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Top_Industries.png)

###### Figure 3: Top 10 states with job openings.
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Top_States.png)

## Location Insights

###### Figure 4: Where are the higher paying jobs?
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Higher_paying_jobs_heatmap.png)

###### Figure 5: Cost of Living index by Salary
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Cost_of_living.png)

###### Figure 6: Are there areas of the country that require more data analytic's skills?
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Unique%20_skills_state.png)

## Employer Data

###### Figure 7: How happy are employees with their employer? (By position(s) with a vancancy)
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Company_Rating_by_Job_Types.png)

###### Figure 8: Which locations have happier employees? (By locations with a vancancy)
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Company_Rating_by_State.png)

###### Figure 9: Which industries have happier employees? (By industry with a vacancy)
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Company_Rating_by_Industry_Type.png)


## Salary Insight

###### Figure 10: Number of Skills Desired per Salary Range.
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/No_skill_salary_range.png)

###### Figure 11: Number of Represented as A Percentage of Job Opening.
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/No_skills_by_Job_Postings.png)

###### Figure 12: Salary based on Industry
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/No_skills_by_salary_bracket.png)

###### Figure 13: Salary Range Based on Company Revenue
![alt text](https://github.com/jennifermarie6sl/Project-1/blob/ed5a47a655b497b329e1e2adb06faf46f621032b/Presentation_Charts/Salary_by_company_revenue.png)

# Sources
* Search Function: ![Stack Overflow - Extract words surrounding a search word](https://stackoverflow.com/questions/17645701/extract-words-surrounding-a-search-word)
* Applying a Function to all rows: ![Geo-code - Applying a function to all rows of a column with pandas](http://chris35wills.github.io/apply_func_pandas/)
* Convert to array: ![Educative - How to convert a list to an array in Python](https://www.educative.io/edpresso/how-to-convert-a-list-to-an-array-in-python)
* Horizontal line: ![Matplotlib - Adding a horizontal line](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html)
* Sorting: ![Pandas - sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_values.html)
* Astype: ![Pandas - astype](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html?highlight=astype)
* Drop: ![Pandas - drop](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html?highlight=drop#pandas.DataFrame.drop)
* Drop Duplicates: ![Pandas - drop_duplicates](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates)
* Power point images: All images in out presentation came from the Powerpoint Design Tool or Online Pictures Tool. Except, the we created. These charts can be found ![here.](https://github.com/jennifermarie6sl/Project-1/tree/main/Presentation_Charts)
* Git hub markdown cheatsheet: ![Markdown Cheatsheet](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md)
