import numpy as np
import os
import sys
import pandas as pd
import random

'''
random.seed(9001)
x = [random.randint(1,200) for i in range(1,200)]
print(x)
exit(1)
'''

p_students = '../records/CCS514 - Introduction (Responses) - Form Responses 1.csv'
df_students = pd.read_csv( p_students )
df_students.rename( columns={'Student Full Name (as it appears in  University of Juba records)':'NAME'}, inplace=True )
df_students.rename( columns={'Student Index Number  (as it appears in  University of Juba records)':'INDEX'}, inplace=True )
df_students.rename( columns={'Email Address':'EMAIL'}, inplace=True )
df_students.rename( columns={'WhatsApp':'WHATSAPP'}, inplace=True )
df_students.rename( columns={'Gender':'GENDER'}, inplace=True )

df_students = df_students[ ['NAME', 'EMAIL', 'INDEX', 'GENDER' ]  ]

df_students[ 'NAME' ] = df_students[ 'NAME' ].str.strip()
df_students[ 'EMAIL' ] = df_students[ 'EMAIL' ].str.strip()
df_students[ 'INDEX' ] = df_students[ 'INDEX' ].str.strip()
df_students[ 'GENDER' ] = df_students[ 'GENDER' ].str.strip()
df_students[ 'INDEX' ] = df_students[ 'INDEX' ].str.upper()
df_students[ 'GENDER' ] = df_students[ 'GENDER' ].str.upper()
df_students[ 'GROUP' ] = [ 'A' if i%2==0 else 'B' for i in range( len(df_students) ) ]

department = []
for index, row in df_students.iterrows():
	d = 'CS' if ( 'CS' in row['INDEX'] ) else 'IT'
	department.append( d  )

df_students[ 'DEPARTMENT' ] = department

num_coursework = 5
for i in range(num_coursework):
	df_students[ f'A{i+1}' ] = [ 0 for i in range( len(df_students) ) ]
	df_students[ f'Q{i+1}' ] = [ 0 for i in range( len(df_students) ) ]

df_students['FINAL'] = [0 for i in range( len(df_students) ) ]

p_out = '../records/students.csv'
df_students.to_csv( p_out, index=False )
