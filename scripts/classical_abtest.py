import scipy.stats as stats
import statsmodels.stats.api as sms
import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder
from math import ceil
from statsmodels.stats.proportion import proportions_ztest,proportion_confint

path = '../data'
df = pd.read_csv(path+'/AdSmartABdata.csv')
df.loc[(df['yes']==1)|(df['no']==1),'response']=1
df['response']=df['response'].fillna(0)

# Sample size calculation
effect_size=sms.proportion_effectsize(0.20,0.25)
required_n=sms.NormalIndPower().solve_power(
    effect_size,
    power=0.8,
    alpha=0.05,
    ratio=1)
required_n=ceil(required_n)

#random sampling from the dataset to abtain a sample size of 1092
control_sample=df[df['experiment']=='control'].sample(n=required_n, random_state=22)
exposed_sample=df[df['experiment']=='exposed'].sample(n=required_n, random_state=22)

ab_test=pd.concat([control_sample,exposed_sample],axis=0)
ab_test.reset_index(drop=True, inplace=True)

ord_enc = OrdinalEncoder()
ab_test['device_make'] = ord_enc.fit_transform(ab_test[['device_make']])
ab_test['browser'] = ord_enc.fit_transform(ab_test[['browser']])

conversion_rates=ab_test.groupby('experiment')['response']
#standard deviation of the proportion
std_p=lambda x: np.std(x,ddof=0)
#standard error of the proportion
se_p=lambda x:stats.sem(x,ddof=0)

conversion_rates=conversion_rates.agg([np.mean,std_p,se_p])
conversion_rates.columns=['conversion_rate','std_deviation','std_error']
conversion_rates.style.format('{:.3f}')

control_results=ab_test[ab_test['experiment']=='control']['response']
exposed_results=ab_test[ab_test['experiment']=='exposed']['response']

n_con=control_results.count()
n_exp=exposed_results.count()
successes=[control_results.sum(),exposed_results.sum()]
nobs=[n_con, n_exp]

z_stat,pval=proportions_ztest(successes,nobs=nobs)
print("Z state: " + str(z_stat))
print("p-value: " + str(pval))
      



