import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

# Day 1,2
st.header('Day 1&2')
st.header('Hello **World!**')
st.markdown('### This is an introduction to _streamlit_.')
st.caption('Building apps made easy.')

# Day 3
st.header('Day 3: st.button')

if st.button('Greet', key='hello1', help='Click to say hi.'):
    st.write('Bonjour, ca va?')
else:
    st.write('Goodbye')

if st.button('Bonjour', key='hello2', disabled=True):
    st.write('Bye')

# Day 4 - To do
st.header('Day 4: To do')

# Day 5

st.header('Day 5: st.write')

st.write('Hello! :flag-fr:')

st.write(1729)

data = {'colors': ['blue', 'orange', 'green', 'red'],
        'happiness': [78, 64, 59, 33]}

st.write('Here is the data:', data)
df = pd.DataFrame(data)

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

np.random.seed(seed=1729)

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
st.write(df2)

st.subheader('Plot a graph')
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.subheader('Write an SQL code')
code = '''SELECT e.id, 
e.name, 
e.age, 
m.experience as manager_experience
FROM employees e
WHERE department = 'Product'
INNER JOIN managers m
ON e.manager_id = m.id
'''
st.code(code, language='sql')

st.subheader('Write in LateX')
# st.latex(r'''
#      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#      \sum_{k=0}^{n-1} ar^k =
#      a \left(\frac{1-r^{n}}{1-r}\right)
#      ''')
st.text('Fourier expansion:')
st.latex(r'''
1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots =
 \sum_{k=0}^{\infty} \frac{x^k}{k!} =
 e^x
''')

# Day 6


