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

* A Series is used to model one dimensional data, similar to a list in Python
* It's formed of `index` and a `name`
* Many of the operations performed on a Series operate directly on the index or by index lookup

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
  
