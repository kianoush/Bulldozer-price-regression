

import numpy as np
import pandas as pd


def yearMade_missing(df):
    c= 0
    c_o = 0
    for i, year in enumerate (df['YearMade']):

        if c % 40000 == 0 :
            print(f'{c_o*10}% complited')
            c_o +=1
        d = []
        k = []
        if year == 1000:
            d = [np.where(df['ModelID'] == df['ModelID'][i])][0]
            #df['YearMade'][i] = np.mean[np.where(d[0] > 1000)]
            for j in d[0]:
                if df.YearMade[j]!=1000:
                    k.append(df.YearMade[j])
            if k==[]:
                continue
            df['YearMade'][i] = round(int(np.mean(k)))
            # if c <=100:
            #     print(d[0], '-->', df['YearMade'][i], k)
        c+=1
    return df