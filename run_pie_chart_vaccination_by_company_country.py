import matplotlib.pyplot as plt
import pandas as pd

from pie_chart_by_company import vaccine_number_by_company_in_country

data2 = pd.DataFrame.from_dict(vaccine_number_by_company_in_country, orient='index')

y = data2[0]

plt.pie(y,startangle=90)
plt.legend(data2.index, loc="lower right")
plt.show()









