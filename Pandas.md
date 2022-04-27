---
title:
- Pandas
  author:
- Dario Necco
  theme:
- Nalug
  date:
- Apr 23, 2022
---

---#
![](Pandas/logo.svg)

---#
# About me

![](common/me.jpg)

* Principal Technical Consultant Engineer @ Perforce
* [https://www.linkedin.com/in/dartie/](https://www.linkedin.com/in/dartie/)
* Member of Nalug ([https://www.nalug.tech/](https://www.nalug.tech/))
* Python and Go(lang) developer

---#
# Introduction

* Data analysis is the process of inspecting, cleansing, transforming, and modelling data with the goal of discovering useful information

!!! example

    Whenever we take any decision in our day-to-day life is by thinking about what happened last time or what will happen by choosing that particular decision. 


---##

```plain
“pandas is an open source, BSD-licensed library providing high 
performance, easy-to-use data structures and data analysis tools 
for the Python programming language.”

-pandas.pydata.org
```

```plain
“In memory nosql database, that has sql-like constructs, basic 
statistical and analytic support, as well as graphing capability.”

-Matt Harrison
```

* it is built on top of Cython, therefore it has less memory overhead and runs quicker.

* Pandas allow users to avoid using a Python-like dialect and gets close to the C in terms of performance.


---#
# Installation

```bash
pip3 install pandas
```

# Import convetions

```python
import pandas as pd
import numpy as np
```

---##
# IDE

* Local environments
    * [Pycharm CE](https://www.jetbrains.com/pycharm)
    * [Spyder](https://www.spyder-ide.org/)

* Online environments
    * [Jupyter Lab / Jupyter Notebook](https://jupyter.org/install)
    * [Colab](https://colab.research.google.com/)

---#
# Data Structures

| Data structure | Dimensionality | Spreadsheet Analog | Data deals with |
| -------------- | -------------- | ------------------ | --------------- |
| **Series**     | 1D             | Column             | Array           |
| **Dataframe**  | 2D             | Single Sheet       | Tabular         |
| **Panel**      | 3D             | Multiple Sheets    |                 |

---##

![](Pandas/data_structures.png)

* Dataframe : collection of series objects
* Panel : collection of dataframes objects

---#

# Series

* One dimensional data structure.
* It can hold numerical data, time data, strings, or arbitrary Python objects.
* It is used to model one dimensional data, similar to a list in Python
* It's formed of `index` and a `name`
* Many of the operations performed on a Series operate directly on the index or by index lookup
* It is faster, consumes less memory, and comes with built-in methods that are very useful to manipulate the data.

---##

| Artist | Data |
|--------|------|
| 0      | 145  |
| 1      | 142  |
| 2      | 38   |
| 3      | 13   |


```python
ser = {
    'index':[0, 1, 2, 3],
    'data':[145, 142, 38, 13],
    'name':'songs'
}
```

---##

## Native python implementation

```python
songs = {
    'index':['Paul', 'John', 'George', 'Ringo'],
    'data':[145, 142, 38, 13],
    'name':'counts'
}


def get(ser, idx):
    value_idx = ser['index'].index(idx)
    return ser['data'][value_idx]


get(songs, 'John')
```

```
142
```

---##
# Series Types

* **Index**: Series' indexes can be integers or strings
* **Data**: a Series can hold strings, floats, booleans, or arbitrary Python objects

!!! Note

    To get the best speed (such as vectorized operations), the values should be of the same type

---##
## Types

* Object:
    * Used for heterogeneous types
    * Used for strings

* Number:
    * Mixed int and float make float (int are converted to float64)

---##

* NaN (**N**ot **a** **N**umber):
    * Used when a series holds numeric values, but it cannot find a number to represent an entry, it will use NaN.
    * It's not counted
    * When NaN is present, other integer data become float: NaN is only supported by float, not by int.

    ```python
    nan_ser = pd.Series([2, None], index=['Ono', 'Clapton'])

    print(nan_ser)
    ```

    ```plain
    Ono      2.0
    Clapton  NaN
    dtype: float64
    ```

    ```python
    nan_ser.count()
    ```
  
    ```plain
    1
    ```
  
---##

# Create Series

```python
import pandas as pd

songs2 = pd.Series([145, 142, 38, 13], name='counts')

print(songs2)
```

```plain
0 145
1 142
2 38
3 13
Name: counts, dtype: int64
```

![](Pandas/series.png)

---##

* Name for `Index` -> `Axis`
* Name for `Values of the index` -> `Axis labels`

* Inspect index

    ```python
    songs2.index
    ```
    
    ```plain
    RangeIndex(start=0, stop=4, step=1)
    ```
  
---##

# Series Indexing

### In case index label is a string (object)
```python
george = pd.Series([10, 7], index=['1968', '1969'], name='George Songs')
print(george)
```

```plain
1968    10
1969     7
Name: George Songs, dtype: int64
```

* Indexing the object by position

    ```python
    print(george[0])
    ```
    
    ```plain
    10
    ```

* Indexing the object by key

    ```python
    print(george['1968'])
    ```
    
    ```plain
    10
    ```

---##

## In case index label is an integer

* Indexing the object by position

    ```python
    print(george[0])
    ```
    
    ```plain
    10
    ```

---##

## Optimized data access methods  

### Position-based indexing (`.iloc`)

```python
george.iloc[0]
```

```plain
10
```

```python
george.iloc[-1]
```

```plain
7
```

```python
george.iloc[4]
```

```plain
Traceback (most recent call last):
IndexError: single positional indexer is out-of-bounds
```

```python
george.iloc['1968']
```

```plain
Traceback (most recent call last):
TypeError: cannot do positional indexing on <class
'pandas.indexes.base.Index'> with these indexers [1968]
of <class 'str'>
```

---##
#### Slice

```python
george.iloc[0:3] # slice
```

```plain
1968    10
1969     7
Name: George Songs, dtype: int64
```

#### Indexing with list

```python
george.iloc[[0,1]] # list
```

```plain
1968  10
1969   7
Name: George Songs, dtype: int64
```

---##

### label-based indexing (`.loc`)

* Based on the index labels and not the positions (analogous to Python dictionary-based indexing)

```python
george.loc['1968']
```

```plain
10
```

```python
george.loc[['1968', '1970']] # list
```

```plain
1968  10.0
1970   NaN
Name: George Songs, dtype: float64
```

```python
george.loc['1968':] # slice
```

```plain
1968  10
1969   7
Name: George Songs, dtype: int64
```

---##

## Summary

![](Pandas/indexing.png)

---##

## `.at()` (vs `.loc()`)

* Get/set numpy array results by index label.
* Return a **numpy.ndarray** whereas `.loc()` returns a **Series** 

```python
george_dupe = pd.Series([10, 7, 1, 22], index=['1968', '1969', '1970', '1970'], name='George Songs')
```

```python
george_dupe.at['1970']
```

```plain
array([ 1, 22])
```

```python
george_dupe.loc['1970']
```

```plain
1970     1
1970    22
Name: George Songs, dtype: int64
```

---##

## `.iat()`

* Getting/setting numpy array results by index position.
* Supports both positional and label based indexing, although is suggested to be avoided

```python
george_dupe.ix[0]
```

```plain
3310
```

```python
george_dupe.ix['1970']
```

```plain
1970   1
1970  22
Name: George Songs, dtype: int64
```

---##

# Series methods

## `mean()`

---##

## `median()`
* Only keeps values greater than average

```python
import pandas as pd
import numpy as np

# Numpy array
numpy_ser = np.array([145, 142, 38, 13])

# Series
songs3 = pd.Series([145, 142, 38, 13], name='counts', index=['Paul', 'John', 'George', 'Ringo'])

print(numpy_ser[1])
print(songs3[1])
```

```plain
142
142
```

---#

# Series CRUD (`C`reate,`R`ead,`U`pdate,`D`elete)

## Create

### List
```python
george_dupe = pd.Series([10, 7, 1, 22], index=['1968', '1969', '1970', '1970'], name='George Songs')
print(george_dupe)
```

```plain
1968  10
1969   7
1970   1
1970  22
Name: George Songs, dtype: int64
```

### Dictionary

```python
g2 = pd.Series({'1969': 7, '1970': [1, 22]}, index=['1969', '1970', '1970']) 
print(g2)
```

```plain
1969        7
1970  [1, 22]
1970  [1, 22]
dtype: object
```

---##


## Reading

```python
print(george_dupe['1968'])
```

```plain
10
```

!!! warning

    When the index is duplicate, the result is not scalar as the first case

    ```python
    print(george_dupe['1970'])
    ```
    
    ```plain
    1970   1
    1970  22
    Name: George Songs, dtype: int64
    ```

---##

### Iteration

```python
for item in george_dupe:
    print(item)
```

```plain
10
7
1
22
```

* Iteration over index and value

    ```python
    for item in george_dupe.iteritems():
        print(item)
    ```
  
    ```plain
    ('1968', 10)
    ('1969', 7)
    ('1970', 1)
    ('1970', 22)
    ```

---##

### Check if value exists

!!! error
    
    It doesn't work as python list and dictionary    

    ```python
    22 in george_dupe
    ```

    ```plain
    False
    ```

!!! success
    
    ```python
    22 in set(george_dupe)
    ```
    
    ```plain
    True
    ```
    
    OR
    
    ```python
    22 in george_dupe.values
    ```
    
    ```plain
    True
    ```

---##

## Updating

### Update based on index

```python
george_dupe['1969'] = 6
print(george_dupe['1969'])
```

```plain
6
```

!!! warning
    
    In case of duplicate index, both will be updated
    ```python
    george_dupe['1970'] = 2
    print(george_dupe)
    ```
    
    ```plain
    1968    10
    1969     6
    1970     2
    1970     2
    1973    11
    Name: George Songs, dtype: int64
    ```

---##

### Update value based on position (`iloc()`)

```python
george_dupe.iloc[3] = 22
print(george_dupe)
```

```plain
1968  10
1969   6
1970   2
1970  22
1973  11
Name: George Songs, dtype: int64
```

---##

### Append

* Unlike `append()` in python list, it requires another series

```python
new_george_dupe = george_dupe.append(pd.Series({'1974':9}))
print(new_george_dupe)
```

```plain
1968  10
1969   6
1970   2
1970  22
1973  11
1974   9
dtype: int64
```

---##

### Add new item (`.set_value()`)

```python
new_george_dupe = george_dupe.set_value('1974', 9)
print(new_george_dupe)
```

```plain
1968    10
1969     6
1970     2
1970    22
1973    11
1974     9
Name: George Songs, dtype: int64
```

---##

## Deletion

### Based on index entries

```python
s = pd.Series([2, 3, 4], index=[1, 2, 1])
del s[1]
print(s)
```

```plain
1   4
dtype: int64
```

!!! warning

    In case of duplicate index values, only the first occurrence is deleted.

### Filter (creates a new series)

```python
new_george_dupe = george_dupe[george_dupe <= 2]
print(new_george_dupe)
```

```plain
1970    2
Name: George Songs, dtype: int64
```

---#

# Dataframe

```python
import pandas as pd
df = pd.DataFrame({
    'growth':[.5, .7, 1.2],
    'Name':['Paul', 'George', 'Ringo'] })

print(df)
```

```
    Name     growth    
0   Paul        0.5
1   George      0.7
2   Ringo       1.2
```

![](Pandas/dataframe.png)

---##

* Access row:
    ```python
    df.iloc[2]
    ```

    ```plain
    Name    Ringo
    growth    1.2
    Name: 2, dtype: object
    ```

* Access column:
    ```python
    df['Name']
    ```

    ```plain
    0      Paul
    1    George
    2     Ringo
    Name: Name, dtype: object
    ```

---##

# Dataframe axis

![](Pandas/dataframe-axis.png)

---##

* To sum up each of the columns, we sum along the index axis (axis=0), or along the row axis:

```python
df.apply(np.sum, axis=0)
```

```plain
Score1    NaN
Score2  175.0
dtype: float64
```

* To sum along every row, we sum down the columns axis (axis=1):

```python
df.apply(np.sum, axis=1)
```

```plain
0   85
1   90
dtype: int64
```

---#

# Dataframe methods


- `shape` : displays the dataframe structure
    
    ```python
    >>> df.shape
    (3, 3)
    ```
    
- `index` : displays the dataframe's index
    
    ```python
    >>> df.index
    (['a', 'b', 'c'], dtype='object')
    ```
    
- `index.values` : displays the dataframe's index values
    
    ```python
    >>> df.index.values
    (['a', 'b', 'c'], dtype=object)
    ```
    
- `index.size` : displays the dataframe's index values in a list
    
    ```python
    >>> df.index.size
    3
    ```

---##
    
- `index.is_integer()` : queries if the index is integer
    
    ```python
    >>> df.index.is_integer()
    False
    ```
    
- `index.is_object()` : queries if the index is object
    
    ```python
    >>> df.index.is_object()
    True
    ```
    
- `index.is_unique()` : queries if the index are all different
    
    ```python
    >>> df.index.is_unique()
    True
    ```
    
- `index.sort_values(ascending=True)` : displays the dataframe's index values sorted
    
    ```python
    >>> df.index.sort_values(ascending=True)
    Index(['c', 'b', 'a'], dtype='object')
    ```
    
---##

- `reset_index(inplace=True)` : indexes become a column (index), and the new indexes are a progressive from 0. `inplace=True` saves the changes.
    
    ```python
    >>> df.reset_index(inplace=True)
      index  c1  c2  c3
    0     a   1   2   3
    1     b   4   5   6
    2     c   7   8   9
    ```


- `set_index("index", inplace=True)` : sets a column as dataframe index. `inplace=True` saves the changes.
    
    ```python
    >>> df.reset_index(inplace=True)
             c1  c2  c3
    index
      a       1   2   3
      b       4   5   6
      c       7   8   9
    ```

---##
    
- `index.rename("indici", inplace=True)` : sets index name
    
    ```python
    >>> df.index.rename("indici", inplace=True)
             c1  c2  c3
    indici
      a       1   2   3
      b       4   5   6
      c       7   8   9
    ```
    
- `index.reset_index(drop=True, inplace=True)` : remove index permanently
    
    ```python
    >>> df.index.reset_index(drop=True, inplace=True)
             c1  c2  c3
    
      0       1   2   3
      1       4   5   6
      2       7   8   9
    ```

---##
    
- `set_index(pd.Series(["a", "b", "c"]), inplace=True)` : reset index with a Series
    
    ```python
    >>> df.index.reset_index(drop=True, inplace=True)
             c1  c2  c3
      0       1   2   3
      1       4   5   6
      2       7   8   9
    ```
    
- `head(n)`: prints the first *n* lines of the dataframe
    
    ```python
    >>> df.head()  # by default first 5 lines
       c1  c2  c3
    a   1   2   3
    b   4   5   6
    c   7   8   9
    
    >>> df.head(2)
       c1  c2  c3
    a   1   2   3
    b   4   5   6
    ```

---##
    
- `tail(n)`: prints the first *n* lines of the dataframe
    
    ```python
    >>> df.tail()  # by default first 5 lines
       c1  c2  c3
    a   1   2   3
    b   4   5   6
    c   7   8   9
    
    >>> df.tail(2)
       c1  c2  c3
    a   1   2   3
    b   4   5   6
    ```
    
- `sample(n)`: prints the a casual line from the dataframe. If `n` is not specified, only one sample is returned.
    
    ```python
    >>> df.sample()
    c1  c2  c3
    b   4   5   6
    ```

---##
    
- `max()`: returns the max value for each column
    
    ```python
    >>> df.max()
    c1    7
    c2    8
    c3    9
    dtype: int64
    
    >>> df.max(1)  # max value for each row
    a    3
    b    6
    c    9
    dtype: int64
    ```
    
- `max(1)`: returns the max value for each row
    
    ```python
    >>> df.max(1) 
    a    3
    b    6
    c    9
    dtype: int64
    ```

---##
    
- `min()`: returns the min value for each column
    
    ```python
    >>> df.min()
    c1    1
    c2    2
    c3    3
    dtype: int64
    ```
    
- `min(1)`: returns the min value for each row
    
    ```python
    >>> df.min(1)
    a    1
    b    4
    c    7
    dtype: int64
    ```

---##
    
- `describe()`: returns dataframe info
    
    ```python
    >>> df.describe()
           c1   c2   c3
    count  3.0  3.0  3.0
    mean   4.0  5.0  6.0
    std    3.0  3.0  3.0
    min    1.0  2.0  3.0
    25%    2.5  3.5  4.5
    50%    4.0  5.0  6.0
    75%    5.5  6.5  7.5
    max    7.0  8.0  9.0
    ```
    
- `count()`:
    
    ```python
    >>> df.sum()
    c1    12
    c2    15
    c3    18
    dtype: int64
    ```
    
---##

- `mean()`:
    
    ```python
    >>> df.mean()
    c1    4.0
    c2    5.0
    c3    6.0
    dtype: float64
    ```
    
- `std()`:
    
    ```python
    >>> df.std()
    c1    3.0
    c2    3.0
    c3    3.0
    dtype: float64
    ```

---##
    
- `sum()`:
    
    ```python
    >>> df.sum()
    c1    12
    c2    15
    c3    18
    dtype: int64
    ```

    
- `df.sum() / df.count() == df.mean()`
    
    ```python
    >>> df.sum() / df.count() == df.mean()
    c1    True
    c2    True
    c3    True
    dtype: bool
    ```
    
---#

# Rows/Columnns operations

## Count

```python
# Count rows
count_row = df.shape[0]  # returns number of row count

# Count columns
count_col = df.shape[1]  # returns number of col count
```

or

```python
len(df.index)
df.shape[0]
df[df.columns[0]].count() (== number of non-NaN values in first column)
```

## Move column

```python
# shift column 'Name' to first position
first_column = df.pop('Name')
  
# insert column using insert(position,column_name,
# first_column) function
df.insert(0, 'Name', first_column)
```

## Drop columns by index

```python
df.drop(df.columns[[2,3,5]], axis=1)
```

## Drop columns by column name

```python
df1 = df1.drop(['B', 'C'], axis=1)
```

---#

-----
# TODO
* Series Methods
* Dataframe
  * remove inplace from examples
  * query
* Visualize data
* Test Sharing with Giovanni