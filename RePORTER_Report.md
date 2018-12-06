**RePORTER Report (BIOF309 Final Project)**
============================================
_Using Python to analyze NIH-funded data over time (FY2010 to FY2017)_

**NIH RePORTER:** RePORTER is an electronic tool that provides public access
to repositories of both intramural and extramural NIH-funded research
projects from the past 25 years

**NIH RePORTER information is drawn from several extended databases**
- eRA databases
- Medline
- PubMed Central
- The NIH Intramural Database
- iEdison

**How do you analyze this data over time?**
- Data is available by month or fiscal year
- Multiple years cannot be analyzed at once in Excel as combined datasets are too large

Using Python to analyze RePORTER Data (FY2010 to FY2017)
==============================================================
##Access RePORTER data using  [ExPORTER](https://exporter.nih.gov/ExPORTER_Catalog.aspx) 
1. Download CSV files for years of interest
    * FY2010 example: download 'FY2010 RePORTER Project Data' for all months
    * Download csv files for all years of interest (for this project FY2010 to FY2017 data)
2. Save csv files to 'RePORTER Data' folder
    * Example of file names: FY2010 data is saved as 'RePORTER_PRJ_C_FY2010.csv'

Use Python 3.6.5 (via PyCharm) to analyze code:

##Python RePORTER Pipeline:

RePORTER pipeline steps:

|  Pipeline Step | Function  |  
|---|---|
|  Import Data | Imports documents, sets documents to DataFrame, and converts all characters to unicode  |   
| Index  | Set DataFrame index to application ID (APPLICATION_ID)  |   
|  Clean Headers | Standardizes format of column headers   |   
|  Difference | Determine if columns differ between datasets |   
|  Drop Columns | Drop columns that do not match and create new DataFrames |
|  Combine DataFrames | Now that columns match, merge the DataFrames | 
|  Analyze Data | Use pandas to analyze NIH-funded research |

##Import Data  
This step of the pipeline ensures the csv files from ExPORTER
can be read using pandas, and converts latin characters within the
datasets to a single eight-bit code.

    Import Data example (FY2010 to FY2012):
    #FY2010 has no UTF-8 conversion issues, so 'ISO-8859-1' is used
    #FY2010 DataFrame will be used in the future to append all data, so it is titled 'df_all_years'
    
    First import pandas as pd

    df_all_years = pd.read_csv('RePORTER_PRJ_C_FY2010.csv')
    df_FY2011 = pd.read_csv('RePORTER_PRJ_C_FY2011.csv',encoding='ISO-8859-1')
    df_FY2012 = pd.read_csv('RePORTER_PRJ_C_FY2012.csv',encoding='ISO-8859-1')
    
## Index
Set Grant Application IDs as the index for all of the DataFrames

![Application ID Index](C:\Users\Zuehlkes\PycharmProjects\RePORTER Data\Indexing picture.PNG)

## Clean Headers
Before combining DataFrames, column headers must be formatted in a consistent manner.
For this, we need to use the following methods:
1. Strip characters using str.strip()
2. Convert characters to lowercase strings using str.lower()
3. Replace blank space and hyphens (-) with an underscore (_) using str.replace()

![Clean Headers](C:\Users\Zuehlkes\PycharmProjects\RePORTER Data\Formatted columns.PNG)

## Difference
Determine if columns differ between DataSets after cleaning the headers

1. Convert columns to lists and save to a col_names_year:
    * FY2011 DataFrame example: col_names_11 = list(df_FY2011.columns)
2. Determine intersection of all columns using & and set() function
    * intersection = set(col_names_10) & set(col_names_11) & set(col_names_12) & set(col_names_13) & set(col_names_14) & set(col_names_15) & set(col_names_16) & set(col_names_17)
intersection
    * If column names appear to be duplicated, go back and look for formatting errors
3. Convert intersection into a list using list() function and save it to columns_in_common
4. Determine if there are differences between columns
    * FY2012 and FY2010 difference example:   difference = set(col_names_12) - set(col_names_10)
    * FY2012 had two additional columns ['direct_cost_amt'] and ['indirect_cost_amt']
    
## Drop Columns
Additional columns identified in the Difference section are dropped from the
DataFrames using df.drop(columns=[]). Now all columns will match for all years.

## Combine DataFrames 
Data for all years are now ready to combine. Here df.append() was used to append 
all fiscal years to the first DataFrame 
* Example of appending FY2011 data to FY2010: df_10and11_joined = df_all_years.append(df_FY2011)

## Analyze Data
Now is the fun part, use the combined data to analyze NIH-funded research from FY2010 to FY2017

