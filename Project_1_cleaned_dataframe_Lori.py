#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Cleaning the data - split up the columns by teammate, clean assigned data, create final dataframe by merging the separate clean dataframes


# In[ ]:


import pandas as pd
import numpy as np

data_file = "indeed_job_dataset.csv"

original_df = pd.read_csv(data_file)
original_df.head()


# In[ ]:


data_to_clean = original_df[["Job_Title", "Link", "Queried_Salary", "Job_Type", "Skill", "No_of_Skills", "Company", "No_of_Stars", "Date_Since_Posted"]]

data_to_clean.head() 


# In[ ]:


clean_df = data_to_clean.drop(columns=["Link", "Date_Since_Posted"])

clean_df


# In[ ]:


#check columns for values that need cleaning
clean_df["Job_Title"].value_counts()


# In[ ]:


clean_df["Job_Type"].value_counts()


# In[ ]:


clean_df["Queried_Salary"].value_counts()


# In[ ]:


clean_df["No_of_Stars"].value_counts()


# In[ ]:


# replace NaN with 0 in No_of_Stars column
clean_df["No_of_Stars"] = clean_df["No_of_Stars"].fillna(0)

clean_df


# In[ ]:


#round No_of_Stars column to whole numbers
clean_df["No_of_Stars"] = clean_df["No_of_Stars"].round().astype("int")

clean_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




