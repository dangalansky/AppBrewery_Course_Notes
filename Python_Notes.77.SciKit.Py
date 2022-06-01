Scikit-Learn
* library of machine learning tools

from sklearn.linear_model import LinearRegression


*features —> machine learning term for variables in a chart
	ex) Movie Budget 
	** often named capital X

*target —> response variable
	ex) Movie Revenue

*intercept —> where the slope lies at 0

*coefficient —> the slope

*r-squared —> how much of the variance will be explained by chart
		   —> expressed as a percentage 


𝑅𝐸𝑉𝐸𝑁𝑈𝐸 = 𝜃0 + 𝜃1𝐵𝑈𝐷𝐺𝐸𝑇

X = pd.DataFrame(old_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])
regression.fit(X,y)
#Theta zero(intercept)
regression.intercept_
	—>array([22821538.63508039])
#Theta one (slope)
regression.coef_
	->array([[1.64771314]])
#R-squared
regression.score(X,y)
	->0.02937258620576877

so…calculating how much revenue we would make on a budget of $350,000,000

—>22821538 + 1.64771314 * 350000000 = $599,521,137.00





