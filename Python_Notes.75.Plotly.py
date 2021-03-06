Plotly
* data visualization library

import plotly.express as px

 —> creates pie chart
	ex)fig = px.pie(labels=ratings.index, values=ratings.values)

*.show() —> displays resulting figure

*.update_traces() —> to configure aspects of the chart you can’t see
	ex) fig.update_traces(textposition=‘outside’, textinfo=‘percent+label’)￼
*px.bar()—> bar chart

*choloropleth—> map composed of colored polygons. It is used to represent spatial variations of a quantity

ex) 
world_map = px.choropleth(df_countries,
                          locations='ISO',
                          color='prize',
                          hover_name='birth_country_current',
                          color_continuous_scale=px.colors.sequential.matter)

world_map.update_layout(coloraxis_showscale=True)

world_map.show()

*sunburst chart
ex)
#create sunburst chart
burst = px.sunburst(country_city_org,
                    path=['organization_country', 
                          'organization_city',
                          'organization_name'],
                    values='prize',
                    title='Where do Discoveries Take Place?'
                    )

burst.update_layout(xaxis_title='Number of Prizes',
                    yaxis_title='City',
                    coloraxis_showscale=False)

burst.show()

*box plot
ex)
box = px.box(df_monthly,
             x='washing_hands',
             y='pct_deaths',
             color='washing_hands',
             title='How Have the Stats Have Changed with Handwashing?')

box.update_layout(xaxis_title='Washing Hands?',
                  yaxis_title='Percentage of Monthly Deaths')

box.show()
