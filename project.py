# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.

# Done after the submission Data, hence answers already known and looked at. 

import pandas as pd
import numpy as np
import tensorflow as tf

# fixing the random seed for reproducibility
np.random.seed(50)
tf.random.set_seed(50)

# Saving the filepath of 'Phishing.csv' saved in the GitHub repository
filepath = "https://raw.githubusercontent.com/sayakpaul/Manning-Phishing-Websites-Detection/master/Phishing.csv"

# Loading the .csv into a DataFrame
myData = pd.read_csv(filepath)
