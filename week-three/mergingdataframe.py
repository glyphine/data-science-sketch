# -*- coding: utf-8 -*-
"""MergingDataFrame.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11OT1pw7o4GUUrhpH6eeWIZvi-oFf-hB7
"""

import pandas as pd

# First we create two DataFrames, staff and students.
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
# And lets index these staff by name
staff_df = staff_df.set_index('Name')
# Now we'll create a student dataframe
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
# And we'll index this by name too
student_df = student_df.set_index('Name')

# And lets just print out the dataframes
print(staff_df.head())
print(student_df.head())

pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)

pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)

pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)

pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)

# First, lets remove our index from both of our dataframes
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

# Now lets merge using the on parameter
pd.merge(staff_df, student_df, how='right', on='Name')

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR',
                          'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion',
                          'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader',
                          'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business',
                            'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law',
                            'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering',
                            'Location': '512 Wilson Crescent'}])


pd.merge(staff_df, student_df, how='left', on='Name')

# Here's an example with some new student and staff data
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins',
                          'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks',
                          'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde',
                          'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond',
                            'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith',
                            'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks',
                            'School': 'Engineering'}])

# As you see here, James Wilde and James Hammond don't match on both keys since they have different last
# names. So we would expect that an inner join doesn't include these individuals in the output, and only Sally
# Brooks will be retained.
pd.merge(staff_df, student_df, how='inner', on=['First Name','Last Name'])

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# df_2012 = pd.read_csv("/content/MERGED2012_13_PP.csv", on_bad_lines='skip')
# df_2013 = pd.read_csv("/content/MERGED2012_13_PP.csv", on_bad_lines='skip')
#

print(len(df_2012))
print(len(df_2013))

frames = [ df_2012, df_2013]
pd.concat(frames)

len(df_2012)+len(df_2013)

pd.concat(frames, keys=['2012','2013'])