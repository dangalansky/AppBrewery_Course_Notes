
Matplotlib!

import matplotlib.pyplot as plt

* to create a chart from data accessed as obj[‘y’]:

plt.plot(x, y)
	
	*ex) plt.plot(df.index, df.java)

* to create a chart from multiple data sets:

plt.plot(x1, y1)
plt.plot(x2, y2)



* smoothing out time data

.rolling(n)
	* provides rolling window calculations
	* n = size of moving window
	*	 can be chained with .mean() to simplify charts

ex) df.rolling(window=6).mean()
	

*Bubble Charts(Seaborn!)
-form of scatterplot
import seaborn as sns

ex) basic bubblechart:
	plt.figure(figsize=(8,4), dpi=200)

	with sns.axes_style('darkgrid'):
  	ax = sns.scatterplot(data=data, 
                      	x='Release_Date', 
                      	y='USD_Production_Budget',
                      	hue='USD_Worldwide_Gross', 
                      	size='USD_Worldwide_Gross',)

  	ax.set(xlim=('1915-08-02', scrape_date),
         	ylim=(0, 450000000),
         	ylabel='Budget in $100 millions',
         	xlabel='Year')

	plt.show()

ex) bubble chart with linear regression model:
	**regplot**
	plt.figure(figsize=(8,4), dpi=200)
	with sns.axes_style('darkgrid'):
	  ax2 = sns.regplot(data=new_films,
    	          x='USD_Production_Budget',
    	          y='USD_Worldwide_Gross',
    	          color = '#2f4b7c',
    	          scatter_kws={'alpha': 0.4},
    	          line_kws={'color':'#ff7c43'})
  
      ax.set(xlim=(0, 450000000),
         ylim=(0, 3000000000),
         ylabel='Revenue in Billions',
         xlabel='Budget in $ Millions')
  
  	plt.show()


* formatting:

.figure() - allows us to resize our chart
.xticks() - configures our x-axis
.yticks() - configures our y-axis
.xlabel() - add text to the x-axis
.ylabel() - add text to the y-axis
.ylim() - allows us to set a lower and upper bound
