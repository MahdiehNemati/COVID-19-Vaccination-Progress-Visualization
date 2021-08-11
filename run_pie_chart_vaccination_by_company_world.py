import pandas as pd
import matplotlib.pyplot as plt

from pie_chart_by_company import vaccine_number_by_company


data1 = pd.DataFrame.from_dict(vaccine_number_by_company, orient='index')

y = data1[0]

plt.pie(y,startangle=90)
plt.legend(data1.index, loc="lower right")
plt.show()