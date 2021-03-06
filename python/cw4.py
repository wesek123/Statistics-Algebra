import scipy.stats as scs
import pandas as pd
import pylab


##1
rozklad_normalny = scs.norm.rvs(size=200, loc=2, scale=30)

srednia_rozkladu = rozklad_normalny.mean()
print(srednia_rozkladu)
tset, pval = scs.ttest_1samp(rozklad_normalny, 2.5)
print('p-values: ', pval)
if pval < 0.05:
    print('Odrzucamy hipotezę H0')
else:
    print('Przyjmujemy hipotezę H0')


##2
napoje = pd.read_csv('napoje.csv',  delimiter=';')
df_napoje = pd.DataFrame(napoje)
print(df_napoje)
srednia = df_napoje[['lech', 'cola', 'regionalne']].mean()
print(srednia)
ttest, pval = scs.ttest_rel(df_napoje['lech'], df_napoje['cola'])
print(pval)

##4
okocim = df_napoje['okocim']
lech = df_napoje['lech']
fanta = df_napoje['fanta']
regionalne = df_napoje['regionalne']
cola = df_napoje['cola']
pepsi = df_napoje['pepsi']
print('okocim-lech: ', scs.ttest_ind(okocim,lech))
print('fanta–regionalne: ', scs.ttest_ind(fanta,regionalne))
print('cola–pepsi: ', scs.ttest_ind(cola,pepsi))

zywiec = df_napoje['zywiec']
##5
stat, p = scs.levene(okocim, lech)
print('okocim-lech: stat=%.3f, p=%.3f' % (stat, p))
stat, p = scs.levene(zywiec, fanta)
print('zywiec-fanta: stat=%.3f, p=%.3f' % (stat, p))
stat, p = scs.levene(regionalne, cola)
print('regionalne-cola: stat=%.3f, p=%.3f' % (stat, p))


##6
print(df_napoje)
napoje_2001 = df_napoje[df_napoje['rok'] == 2001]
regionalne_2001 = napoje_2001['regionalne']
print(regionalne_2001)
napoje_2001 = df_napoje[df_napoje['rok'] == 2015]
regionalne_2015 = napoje_2001['regionalne']
print(regionalne_2015)
print('2001, 2015 dla piw regionalnych: ', scs.ttest_ind(regionalne_2001,regionalne_2015))