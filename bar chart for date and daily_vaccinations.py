import inline as inline
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from graph import country_vaccinations_data
%matplotlib inline

country_vaccinations_data.set_index('date',inplace=True)

#set ggplot style
plt.style.use('ggplot')

#plot data
fig, ax = plt.subplots(figsize=(15,7))
ax.bar(country_vaccinations_data.index, country_vaccinations_data['daily_vaccinations'])

#set ticks every week
ax.xaxis.set_major_locator(mdates.MonthLocator())
#format date
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

ax.set_title('Daily Vaccinations Progress of the World in 2021')
ax.set_ylabel('Daily Vaccinations')
ax.set_xlabel('Date')

plt.show()