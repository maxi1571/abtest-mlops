import dvc.api
import pandas as pd
import numpy as np

path = 'data/AdSmartABdata1.csv'
repo = '/home/michael/abtest-mlops'
version = 'v2'
data_url = dvc.api.get_url(
  path = path,
  repo = repo,
  rev=version
  )

if name == "main":
    warnings.filterwarnings("ignore")
    np.random.seed(60)

    data=pd.read_csv(data_url,sep=",")
