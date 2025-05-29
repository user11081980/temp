__author__ = 'jliu'

import pandas as pd
import numpy as np

def variable_type(df, nominal_level = 5):
    categorical, numeric, nominal = [],[],[]
    for variable in df.columns.values:
        if np.issubdtype(np.array(df[variable]).dtype, int) or np.issubdtype(np.array(df[variable]).dtype, float):
            if len(np.unique(np.array(df[variable]))) <= nominal_level:
                nominal.append(variable)
            else:
                numeric.append(variable)
        else:
            categorical.append(variable)
    return numeric,categorical,nominal

def variable_with_missing(df):
    var_with_missing = []
    col_names = df.columns.tolist()
    for variable in col_names:
        percent = float(sum(df[variable].isnull()))/len(df.index)
        print variable+":", percent
        if percent != 0:
            var_with_missing.append(variable)
    return var_with_missing