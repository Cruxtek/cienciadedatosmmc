import pandas
data = pandas.read_excel('GSM151667.xls')
dv = data.values
print( dv[1650,:9])
#array([1, 1, 1, 1, 1,'phosphodiesterase I/nucleotide pyrophosphatase 2 (autotaxin)',3170, 4730, 3077.651611], dtype=object)
ch1 = dv[1650:1650+1600,8]- dv[1650:1650+1600,9]
ch1[:4]
#array([1993.9797359999998, 2072.756592, 1511.40625, 2540.880615],dtype=object)
ch2 = dv[1650:1650+1600,20]- dv[1650:1650+1600,21]

import matplotlib.pyplot as plt
plt.scatter(ch1,ch2)
rgratio = ch1/ch2
intensity = (ch1 + ch2)/2

import matplotlib.pyplot as plt
plt.scatter(intensity,rgratio)
plt.xlim(-10,8000)
plt.ylim(-5,30)
plt.show()

M = np.log2(rgratio.astype(float))
A = np.log2(intensity.astype(float))
plt.scatter(A,M)

from statsmodels.nonparametric.smoothers_lowess import lowess
ag = A.argsort()
A2 = A[ag]
M2 = M[ag]

filtered= lowess(M2,A2,is_sorted=True,frac=0.03125,it=0)

plt.scatter(A,M)
plt.scatter(filtered[:,0],filtered[:,1])
plt.show()
genex = M2[12:-10]- filtered[:,1]
plt.scatter(filtered[:,0], genex)
