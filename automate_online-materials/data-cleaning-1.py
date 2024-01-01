import numpy as np
import pandas as pd
import re

df = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'D', '?'],
    'Age': [29,30,24,290,25]
})
print(df)
print(df['Sex'].unique())
print(df['Sex'].value_counts())
print(df['Sex'].replace('D', 'F'))
print(df['Sex'].replace({'D': 'F', 'N': 'M'}))

print(df.replace({
    'Sex': {
        'D': 'F',
        'N': 'M'
    },
    'Age': {
        290: 29
    }
}))

print(df[df['Age'] > 100])

df.loc[df['Age']>100, 'Age'] = df.loc[df['Age']>100, 'Age'] / 10
print(df)

print('\n Duplicates')
ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany',
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Peter Ammon',
    'Klaus Scharioth '
])
print(ambassadors)
print(ambassadors.duplicated())
print(ambassadors.duplicated(keep='last'))
print(ambassadors.duplicated(keep=False))
print(ambassadors.drop_duplicates())
print(ambassadors.drop_duplicates(keep='last'))
print(ambassadors.drop_duplicates(keep=False))

players = pd.DataFrame({
    'Name': [
        'Kobe Bryant',
        'LeBron James',
        'Kobe Bryant',
        'Carmelo Anthony',
        'Kobe Bryant',
    ],
    'Pos': [
        'SG',
        'SF',
        'SG',
        'SF',
        'SF'
    ]
})
print(players)
print(players.duplicated())
print(players.duplicated(subset=['Name']))
print(players.duplicated(subset=['Name'], keep='last'))
print(players.drop_duplicates())
print(players.drop_duplicates(subset=['Name']))
print(players.drop_duplicates(subset=['Name'], keep='last'))

df = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I  T_2'
]})

print(df)
print(df['Data'].str.split('_'))
print(df['Data'].str.split('_', expand=True))

df = df['Data'].str.split('_', expand=True)
df.columns = ['Year', 'Sex', 'Country', 'No Children']
print(df['Year'].str.contains('\?'))
print(df['Country'].str.contains('U'))
print(df['Country'].str.strip())
print(df['Country'].str.replace(' ', ''))
print(df['Year'].str.replace(r'(?P<year>\d{4})\?', lambda m: m.group('year')))