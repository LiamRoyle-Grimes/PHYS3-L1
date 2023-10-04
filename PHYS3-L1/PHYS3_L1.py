from math import sin, cos, radians
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv('Lab 1 - Sheet2.csv')
RefA=170.1
RefB=350+(8/60)
A=60

def calcn(d):
    t1=sin(radians((0.5)*(A+d)))
    t2=sin(radians(A/2))
    return(t1/t2)

df.columns=['angle','wavelength']
df['angle1']=df['angle'].map(lambda x: RefA-x)
df['n']= df['angle1'].map(lambda x: calcn(x))
df['wave2']= df['wavelength'].map(lambda x: 1/(x**(2)))


model1 = smf.ols(formula='n~wave2', data=df).fit()
print(model1.summary())
print(model1.params)


plt.figure()
plt.plot(df['wave2'],df['n'],'rx')
plt.plot([1/(i**2) for i in range(400,700)],[model1.params[0]+model1.params[1]*(1/i**2) for i in range(400,700)])
plt.xlabel('$\lambda^{-2}$')
plt.ylabel('Index of Refraction')
plt.legend(['He','Best Fit'])


plt.figure()
plt.plot(df['wavelength'],df['n'],'rx')
plt.plot([i for i in range(400,700)],[model1.params[0]+model1.params[1]*(1/i**2) for i in range(400,700)])
plt.xlabel('$\lambda$')
plt.ylabel('Index of Refraction')
plt.legend(['He','Best Fit'])

plt.show()
