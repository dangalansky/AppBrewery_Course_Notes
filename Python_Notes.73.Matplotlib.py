
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

ex) scatter chart with line chart superimposed, second y-axis!
	* line chart shows a preconfigured rolling average!

#create scatter plot with rolling average superimposed over it
plt.figure(figsize=(16,8), dpi=200)

plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)

plt.yticks(fontsize=14)

#👇 create x-axis that only shows every 5 years!
plt.xticks(ticks=np.arange(1900, 2021, step=5),
           fontsize=14,
           rotation=45)

ax1 = plt.gca() #get current axis
ax2 = ax1.twinx() #creates second y-axis
ax1.set_xlim(1900, 2020)
#invert y-axis!
ax2.invert_yaxis()

#scatter plot
ax1.scatter(x=yearly_total.index,
            y=yearly_total.values,
            c='dodgerblue',
            alpha=0.7,#alpha=how opaque or transparent the dots will be; scale 0-1
            s=100)


#line chart, superimposed with moving_average instead of actual totals
ax1.plot(yearly_total.index,
         moving_average.values,
         c='crimson',
         linewidth=3)

#add prize share to second axis
ax2.plot(av_share.index,
         fiveyr_av.values,
         c='green',
         linewidth=3)

plt.show()





* formatting:

.figure() - allows us to resize our chart
.xticks() - configures our x-axis
.yticks() - configures our y-axis
.xlabel() - add text to the x-axis
.ylabel() - add text to the y-axis
.ylim() - allows us to set a lower and upper bound
