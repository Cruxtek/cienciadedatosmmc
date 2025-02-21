import pandas
data = pandas.read_excel('GSM151667.xls')
dv = data.values
print( dv[1650,9])
#array([1, 1, 1, 1, 1,'phosphodiesterase Inucleotide pyrophosphatase 2(autotaxin)',3170, 4730, 3077.651611], dtype=object)
ch1 = dv[1650:1650+1600,8]- dv[1650:1650+1600,9]
#ch1[ :4]
#Out[]:array([1993.9797359999998, 2072.756592, 1511.40625, 2540.880615], dtype=object)
ch2 = dv[1650:1650+1600,20]- dv[1650:1650+1600,21]

import matplotlib.pyplot as plt

plt.scatter(ch1,ch2)
