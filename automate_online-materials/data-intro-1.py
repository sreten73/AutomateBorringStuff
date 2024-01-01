import numpy as np
import pandas as pd

print(pd.notnull(3))
print(pd.isna(np.nan))

print(pd.isnull(pd.Series([1, np.nan, 7])))
print(pd.notnull(pd.Series([1, np.nan, 7])))

# Dataframe
print('\nDataframe')
print(pd.isnull(pd.DataFrame({ 'Column A': [1, np.nan, 7],
    'Column B': [np.nan, 2, 4],
    'Column C': [np.nan, 2, np.nan]
})))

# Operations
print('\nOperations')
print(pd.Series([1, 2, np.nan]).count())
print('Suma Panda Series')
print(pd.Series([1,2,np.nan]).sum())
print('Srednja vrednost')
print(pd.Series([1,2,np.nan]).mean())

print('\nFilter missing data')
s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
print(pd.notnull(s))
print(pd.isnull(s))
print(pd.notnull(s).sum())
print(pd.isnull(s).sum())
print(s[pd.notnull(s)])
print(s.isnull())
print(s.notnull())
print(s[s.notnull()])

print('\nDropping null values')
print(s)
print(s.dropna())

s = pd.Series([np.nan, 1, 2, np.nan, 3])
s = s.fillna(method='ffill')

print(s)

print('\nDropping null values on Dataframes')
df = pd.DataFrame({'Column A': [1, np.nan, 30, np.nan],
                  'Column B': [2, 8, 31, np.nan],
                   'Column C': [np.nan, 9, 32, 100],
                   'Column D': [5, 8, 34, 110],
})
print(df)
print(df.shape)
print(df.info())
print(df.isnull())
print(df.isnull().sum())
print(df.dropna())
print(df.dropna(axis=1))

df2 = pd.DataFrame({
    'Column A': [1,np.nan,30],
    'Column B': [2, np.nan, 31],
    'Column C': [np.nan,np.nan,100]
})
print(df2)
print(df2.dropna(how='all'))
print(df2.dropna(how='any'))
print(df2.dropna(thresh=3))
print(df2.dropna(thresh=2,axis='columns'))

print('\nFilling null values')
s = pd.Series([1,2,3,np.nan,np.nan,4])
print(s)
print(s.fillna(0))
print(s.fillna(s.mean()))
print(s.fillna(method='ffill'))
print(s.fillna(method='bfill'))
print(pd.Series([np.nan,3,np.nan,9]).fillna(method='ffill'))
print(pd.Series([1, np.nan, 3, np.nan, np.nan]).fillna(method='bfill'))

print('\nFilling null values on DataFrame')
print(df)
print(df.fillna({'Column A': 0, 'Column B': 99, 'Column C': df['Column C'].mean()}))
print(df.fillna(method='ffill', axis=0))
print(df.fillna(method='ffill', axis=1))

print('\nChecking if there are NAs')
print(s.dropna().count())
missing_values = len(s.dropna()) != len(s)
print(len(s))
print(len(s.dropna()))
print(missing_values)

missing_values = s.count() != len(s)
print(missing_values)