#import a .csv file to a DataFrame
##df starts with 2010 but will contain all FYs
#To avoid problems with cells without UTF-8 format, we use encoding = 'ISO-8859-1'
import pandas as pd

df_all_years = pd.read_csv('RePORTER_PRJ_C_FY2010.csv')
df_FY2011 = pd.read_csv('RePORTER_PRJ_C_FY2011.csv',encoding='ISO-8859-1')
df_FY2012 = pd.read_csv('RePORTER_PRJ_C_FY2012.csv',encoding='ISO-8859-1')
df_FY2013 = pd.read_csv('RePORTER_PRJ_C_FY2013.csv',encoding='ISO-8859-1')
df_FY2014 = pd.read_csv('RePORTER_PRJ_C_FY2014.csv',encoding='ISO-8859-1')
df_FY2015 = pd.read_csv('RePORTER_PRJ_C_FY2015.csv',encoding='ISO-8859-1')
df_FY2016 = pd.read_csv('RePORTER_PRJ_C_FY2016.csv',encoding='ISO-8859-1')
df_FY2017 = pd.read_csv('RePORTER_PRJ_C_FY2017.csv',encoding='ISO-8859-1')

#set appl ID as index
df_all_years.set_index('APPLICATION_ID', inplace=True)
df_FY2011.set_index('APPLICATION_ID', inplace=True)
df_FY2012.set_index('APPLICATION_ID', inplace=True)
df_FY2013.set_index('APPLICATION_ID', inplace=True)
df_FY2014.set_index('APPLICATION_ID', inplace=True)
df_FY2015.set_index('APPLICATION_ID', inplace=True)
df_FY2016.set_index('APPLICATION_ID', inplace=True)
df_FY2017.set_index('APPLICATION_ID', inplace=True)


#clean headers
df_all_years.columns = df_all_years.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2011.columns = df_FY2011.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2012.columns = df_FY2012.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2013.columns = df_FY2013.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2014.columns = df_FY2014.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2015.columns = df_FY2015.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2016.columns = df_FY2016.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')
df_FY2017.columns = df_FY2017.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-','_')

#Creating a list with column headers
col_names_10 = list(df_all_years.columns)
col_names_10
col_names_11 = list(df_FY2011.columns)
col_names_11
col_names_12 = list(df_FY2012.columns)
col_names_12
col_names_13 = list(df_FY2013.columns)
col_names_13
col_names_14 = list(df_FY2014.columns)
col_names_14
col_names_15 = list(df_FY2015.columns)
col_names_15
col_names_16 = list(df_FY2016.columns)
col_names_16
col_names_17 = list(df_FY2017.columns)
col_names_17

# looking for the intersection
intersection = set(col_names_10) & set(col_names_11) & set(col_names_12) & set(col_names_13) & set(col_names_14) & set(col_names_15) & set(col_names_16) & set(col_names_17)
intersection

# change set intersection for a list named test
columns_in_common = list(intersection)
columns_in_common

# Get info from columns in common
df_all_years[columns_in_common].info()

# locate extra columns
difference = set(col_names_13) - set(col_names_10)
difference

# drop columns from df 12-17
df_FY2012_43 = df_FY2012.drop(columns=['direct_cost_amt'])
df_FY2012_42 = df_FY2012_43.drop(columns=['indirect_cost_amt'])
df_FY2012_42

df_FY2013_43 = df_FY2013.drop(columns=['direct_cost_amt'])
df_FY2013_42 = df_FY2013_43.drop(columns=['indirect_cost_amt'])
df_FY2013_42

df_FY2014_44 = df_FY2014.drop(columns=['direct_cost_amt'])
df_FY2014_43 = df_FY2014_44.drop(columns=['indirect_cost_amt'])
df_FY2014_42 = df_FY2014_43.drop(columns=['org_ipf_code'])
df_FY2014_42

df_FY2015_44 = df_FY2015.drop(columns=['direct_cost_amt'])
df_FY2015_43 = df_FY2015_44.drop(columns=['indirect_cost_amt'])
df_FY2015_42 = df_FY2015_43.drop(columns=['org_ipf_code'])
df_FY2015_42

df_FY2016_44 = df_FY2016.drop(columns=['direct_cost_amt'])
df_FY2016_43 = df_FY2016_44.drop(columns=['indirect_cost_amt'])
df_FY2016_42 = df_FY2016_43.drop(columns=['org_ipf_code'])
df_FY2016_42

df_FY2017_44 = df_FY2017.drop(columns=['direct_cost_amt'])
df_FY2017_43 = df_FY2017_44.drop(columns=['indirect_cost_amt'])
df_FY2017_42 = df_FY2017_43.drop(columns=['org_ipf_code'])
df_FY2017_42.shape


# combine DataFrames (final is df_10to17)
df_10and11_joined = df_all_years.append(df_FY2011)
df_10and11_joined
df_10to12 = df_10and11_joined.append(df_FY2012_42)
df_10to12
df_10to13 = df_10to12.append(df_FY2013_42)
df_10to13
df_10to14 = df_10to13.append(df_FY2014_42)
df_10to14
df_10to15 = df_10to14.append(df_FY2015_42)
df_10to15
df_10to16 = df_10to15.append(df_FY2016_42)
df_10to16
df_10to17 = df_10to16.append(df_FY2017_42)
df_10to17

#check data
df_10to17.columns
df_10to17.shape
df_10to17.info()

#check admin IC
df_10to17.iloc[:,1]

# null values (NaN and null are the same)
df_10to17.isnull().sum()
df_10to17.isna().sum()

#number of PIIDs
df_10to17_PIsNumber = df_10to17.pi_ids.unique()
len(df_10to17_PIsNumber)

df_PI_per_year = df_10to17.groupby('fy')['pi_ids'].nunique()

# new DataFrame for individual PIs 11/30/18
df_PIs = df_10to17.filter(["application_id", "pi_names"])

# remove semicolon from end of pi_names
df_PIs['pi_names'] = df_PIs['pi_names'].astype(str).str[:-1]
df_PIs

#Put each PI, separated by a semicolon, in a different row and repeat the PMID (index)
df_PIs_out = (pd.DataFrame(df_PIs.pi_names.str.split(';').tolist(), index=df_PIs.application_id)
      .stack()
      .reset_index()
      .drop('level_1',axis=1)
      .rename(columns={0:'pis_unwound'}))
df_PIs_out.shape
df_PIs_out.head

#Merge inital dataframes 'df_authors' with unwound one 'df_authors_out' using PMID as key
df_merged = pd.merge(df_PIs_out,df_PIs[['application_id','pi_names']],on='application_id')
df_merged.shape
df_merged.columns
df_merged_check.to_csv('df_merged_check.csv', sep = ',')

#CHANGE ORDER OF COLUMNS IN MERGED DATAFRAME
df_merged = df_merged [['application_id','pi_names','pis_unwound']]
df_merged.head()

#Add unwound PI data to original dataset

df_merged = df_merged.pis_unwound.unique()
len(df_merged)


#bar chart # of PIs per year
import matplotlib.pyplot as plt
df_PI_per_year.plot(kind='bar')
plt.show()

# of mechanisms and bar chart
df_10to17_mechs = df_10to17.activity.unique()
len(df_10to17_mechs)

df_10to17_mechs_per_year = df_10to17.groupby('fy')['activity'].nunique()

df_10to17_mechs_per_year.plot(kind = 'bar')

# pivot chart

