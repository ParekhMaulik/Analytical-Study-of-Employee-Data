import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



df_original = pd.read_csv("original_file.csv")
df = pd.read_csv('original_file.csv')
df = pd.DataFrame(df)
print(df)

print(df.info())


cleaned_file = "cleaned_data.csv"
df = pd.read_csv('cleaned_data.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] 
df.to_csv(cleaned_file, index=False)


# Modify data of department 
df_modify = df.dropna(subset=['Department'])
df.dropna(subset=['Department'], inplace=True)
df_modify.to_csv(cleaned_file,index=False)



# for department 
df['Department'] = df['Department'].astype(str)  # Ensure column is string
df_exploded = df['Department'].str.split(',').explode()  # Split & expand
department_counts = df_exploded.value_counts()  # Count occurrences
print(department_counts)

# for working hours per week 
df_modify = pd.read_csv('cleaned_data.csv',index_col=False)
x = df_modify['Working_Hours_per_Week'].median(0)
df_modify['Working_Hours_per_Week'].fillna(x,inplace=True)
df_modify.to_csv(cleaned_file,index=False)


# for gender
gender_counts = df['Gender'].value_counts()
df_geneder = pd.read_csv('cleaned_data.csv',index_col=False)
df_geneder['Gender'].fillna("Not selected",inplace=True)
df_geneder.to_csv(cleaned_file,index=False)



# for job level 
df_job = pd.read_csv("cleaned_data.csv",index_col=False)
df_job['Job_Level'].fillna("fresers",inplace=True)
df_job.to_csv(cleaned_file,index=False)



# for bonus
# Using NumPy 
df['Bonus'].fillna(np.nanmedian(df['Bonus']), inplace=True)

# for remote work percentage  
df_remort = pd.read_csv("cleaned_data.csv",index_col=False)
x = df_remort['Remote_Work_Percentage'].median()
df_remort['Remote_Work_Percentage'].fillna(x,inplace=True)
df_remort.to_csv(cleaned_file,index=False)


# for bonus
# Using NumPy 
# df['Bonus'].fillna(np.nanmedian(df['Bonus']), inplace=True)
df_bonus = pd.read_csv("cleaned_data.csv",index_col=False)
x = df_bonus['Bonus'].median()
df_bonus['Bonus'].fillna(x,inplace=True)
df_bonus.to_csv(cleaned_file,index=False)



# Open  file in Excel
os.startfile("original_file.csv")    # Original file
os.startfile(cleaned_file)           # new file 



#  matplotlib
# Fill missing values
df['Department'] = df['Department'].astype(str)
df['Job_Level'].fillna("fresers", inplace=True)
df['Bonus'].fillna(df['Bonus'].median(), inplace=True)
df['Remote_Work_Percentage'].fillna(df['Remote_Work_Percentage'].median(), inplace=True)
df['Gender'].fillna("Not selected", inplace=True)




#  Pie Chart: Department Distribution
df_exploded = df['Department'].str.split(',').explode()
department_counts = df_exploded.value_counts()
plt.figure(figsize=(8, 6))
plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title("Department Distribution")
plt.show()

#  Histogram: Working Hours Distribution
plt.figure(figsize=(8, 6))
plt.hist(df['Working_Hours_per_Week'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Working Hours per Week")
plt.ylabel("Number of Employees")
plt.title("Distribution of Working Hours")
plt.show()

#  Bar Chart: Gender Distribution
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(gender_counts.index, gender_counts.values, color=['blue', 'pink', 'gray'])
plt.xlabel("Gender")
plt.ylabel("Number of Employees")
plt.title("Gender Distribution")
plt.show()

# Bar Chart: Job Level Distribution
job_counts = df['Job_Level'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(job_counts.index, job_counts.values, color=['blue', 'orange', 'green'])
plt.xlabel("Job Level")
plt.ylabel("Number of Employees")
plt.title("Job Level Distribution")
plt.xticks(rotation=30)
plt.show()

#  Box Plot: Bonus Distribution
plt.figure(figsize=(8, 6))
plt.boxplot(df['Bonus'])
plt.ylabel("Bonus Amount")
plt.title("Bonus Distribution")
plt.show()

#  Scatter Plot: Remote Work % vs Bonus
plt.figure(figsize=(8, 6))
plt.scatter(df['Remote_Work_Percentage'], df['Bonus'], alpha=0.5, color='purple')
plt.xlabel("Remote Work Percentage")
plt.ylabel("Bonus Amount")
plt.title("Remote Work Percentage vs Bonus")
plt.show()


