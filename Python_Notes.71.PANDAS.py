Pandas!
*lesson conducted in python notebook

import statement:
import pandas as pd

read the data:
df= pd.read_csv(‘name_of_file.csv’)

data exploration:
df.shape
	* returns # of rows and columns within data frame as tuple
	*(columns, rows)

df.columns
	*returns names of columns as a list within Index()

df.dtypes
	*returns data types of entries

df.duplicated()
	*returns true or false denoting existence of duplicate rows

df.head(n)
	* shows top “n” rows of data, default is 5

df.tail(n)
	* shows bottom “n” rows of data, default is 5

df.describe()
	*returns count, mean, min, max and other stats on every column

df.sample(n)
	*returns ’n’ number of random rows

df.isna()
	* returns True where values==None, NA etc.

df.isna().values.any()
	* checks entirety of file for NaN values
	* returns False if None

.info()
	*concise summary of DataFrame
	*inclues index dtypes and columns as well as existence of NaN values!

.nunique()
	* counts number of distinct elements in specified axis
	*ex) df[column_name].nunique()

.count()
	* counts amount of entries in a table
	* returns an integer value, count of whatever comes before

.value_counts()
	* returns a series with number of unique values
	*ex) df.data_column.value_counts()


df.[‘column name’]
	*returns entire column

df.[[‘column name 1’, ‘column name 2’, ‘column name 3’,]]
	*returns multiple columns

df[‘column_name].idxmax()
	* returns index for row with largest value

df[‘column_name].idxmin()
	* returns index for row with lowest value

.min()
	*returns smallest value for indicated column

.max()
	*returns largest value for indicated column

df.loc[n]
	* returns data at a particular row
		—> would return entire row
	* df[‘column_name’].loc[n] == df[‘column_name’][n]
		—>would return a single value for ‘column_name’

**Multiple Conditional Search**

1) df.loc[] + bitwise and operator

	ex) international_releases = data.loc[(data.column1 == 0) & (data.column2 !=0)]
	*parentheses required!*

2) df.query()
	ex)international_releases = data.query(‘column1 == 0 and column2 !=0’)


actions:

df.dropna()
	* removes missing values
	* clean_df = df.dropna() —> best practice!

df.fillna()
	* replace NaN values, instead of removing them
	* like with int 0!
	ex) df.fillna(0, inplace=True)
					**inplace infers we are updating a dataframe

.to_datetime()
	* converts str to datetime object
	ex) df.DATE = pd.to_datetime(df.DATE)

.to_numeric
	*converts to numeric data type
	ex) df.Column = pd.to_numeric(df.Column)

.insert(n, ‘Column Title’, variable)
	*creates new column out of variable at position ’n’, with ‘Column title’

.sort_values(‘Column Title’)
	* sorts values by default in ascending order
	* ascending=False for descending

.groupby(‘Column_Title’)
	* creates an object that groups rows by particular category
	* must apply another function to return something; I.E. .count() or mean()


.sum()
	* counts integer values within an entry!

.subtract()
	*returns difference between two integer values

.mean()
	* returns average 

.agg()
	*aggregates using one or more operations over the specified axis
	*takes dictionary as argument
	*ex) parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
	*ex)themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})


.resample()
	* resamples time-series data
	* ex) new_df = df.resample(‘M’, on=‘Column_Name).last()
		—> this would take ‘last’ value in month
		—> .mean() would take average over the month

****TO FORMAT NUMBERS IN READABLE FORMAT****
		
		pd.options.display.float_format = '{:,.2f}'.format
