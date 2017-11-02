---
{
  "title": "pandas-brandon-rhodes-part1",
  "subtitle": "Generic subtitle",
  "date": "2017-11-02",
  "slug": "pandas-brandon-rhodes-part1"
}
---
<!--more-->


```python
#Import libraries, display plot in the notebook
%matplotlib inline
import pandas as pd

# import jtplot submodule from jupyterthemes
from jupyterthemes import jtplot
# currently installed theme will be used to
# set plot style if no arguments provided
jtplot.style()

#Ignore warnings
import warnings
warnings.filterwarnings('ignore')
```

### 1. Read Data files and Explore Contents


```python
titles_path = \
"/home/isaac/Dropbox/Pandas/pycon-pandas-tutorial/data/titles.csv"

cast_path = \
"/home/isaac/Dropbox/Pandas/pycon-pandas-tutorial/data/cast.csv"

release_path = \
"/home/isaac/Dropbox/Pandas/pycon-pandas-tutorial/data/release_dates.csv"
```

```python
titles = pd.read_csv(titles_path)
cast = pd.read_csv(cast_path)
release = pd.read_csv(release_path)
```

```python
titles.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Anashim Ketumim</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ritu</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nelumbo</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Black to White</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Godsalt</td>
      <td>2014</td>
    </tr>
  </tbody>
</table>
</div>




```python
cast.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
      <th>name</th>
      <th>type</th>
      <th>character</th>
      <th>n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Suuri illusioni</td>
      <td>1985</td>
      <td>Homo $</td>
      <td>actor</td>
      <td>Guests</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gangsta Rap: The Glockumentary</td>
      <td>2007</td>
      <td>Too $hort</td>
      <td>actor</td>
      <td>Himself</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Menace II Society</td>
      <td>1993</td>
      <td>Too $hort</td>
      <td>actor</td>
      <td>Lew-Loc</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Porndogs: The Adventures of Sadie</td>
      <td>2009</td>
      <td>Too $hort</td>
      <td>actor</td>
      <td>Bosco</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Stop Pepper Palmer</td>
      <td>2014</td>
      <td>Too $hort</td>
      <td>actor</td>
      <td>Himself</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
release.head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
      <th>country</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>#73, Shaanthi Nivaasa</td>
      <td>2007</td>
      <td>India</td>
      <td>2007-06-15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>#Beings</td>
      <td>2015</td>
      <td>Romania</td>
      <td>2015-01-29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>#Ewankosau saranghaeyo</td>
      <td>2015</td>
      <td>Philippines</td>
      <td>2015-01-21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>#Horror</td>
      <td>2015</td>
      <td>USA</td>
      <td>2015-11-20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>#Horror</td>
      <td>2015</td>
      <td>UK</td>
      <td>2016-05-16</td>
    </tr>
  </tbody>
</table>
</div>



### 2. Warm-ups


```python
#Check the length of the dataframe
len(titles)
```

    234375




```python
#Get head
h = titles.head(10)
h
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Anashim Ketumim</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ritu</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nelumbo</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Black to White</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Godsalt</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Conrack</td>
      <td>1974</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Find a Way</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kamandag sa araw</td>
      <td>1987</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Chal Chalein</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A Good Day to Die Hard</td>
      <td>2013</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Get the tail
t = titles.tail(10)
t
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>234365</th>
      <td>Coma</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>234366</th>
      <td>Narendran Makan Jayakanthan Vaka</td>
      <td>2001</td>
    </tr>
    <tr>
      <th>234367</th>
      <td>Where Thunder Reigns</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>234368</th>
      <td>Vidas Estranhas</td>
      <td>1968</td>
    </tr>
    <tr>
      <th>234369</th>
      <td>Proud to Be a Sikh</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>234370</th>
      <td>Yenti Bava Mareenu</td>
      <td>1993</td>
    </tr>
    <tr>
      <th>234371</th>
      <td>Il conte Max</td>
      <td>1957</td>
    </tr>
    <tr>
      <th>234372</th>
      <td>Heimat-Fragmente: Die Frauen</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>234373</th>
      <td>The Vanquished</td>
      <td>1953</td>
    </tr>
    <tr>
      <th>234374</th>
      <td>Blood in Eden</td>
      <td>2017</td>
    </tr>
  </tbody>
</table>
</div>




```python
titles.columns
```

    Index(['title', 'year'], dtype='object')




```python
#Convert years to decades
h.year // 10 * 10
```

    0    2010
    1    2010
    2    2010
    3    2010
    4    2010
    5    1970
    6    2010
    7    1980
    8    2000
    9    2010
    Name: year, dtype: int64




```python
#Filtering
h[h.year >= 2005]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Anashim Ketumim</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ritu</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nelumbo</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Black to White</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Godsalt</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Find a Way</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Chal Chalein</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A Good Day to Die Hard</td>
      <td>2013</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Combined filter, and doesn't work here
h[(h.year >= 2005) and (h.year <=2010) ]
```

    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)

    <ipython-input-13-b2ea91a7da3c> in <module>()
          1 #Combined filter, and doesn't work here
    ----> 2 h[(h.year >= 2005) and (h.year <=2010) ]
    

    /home/isaac/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py in __nonzero__(self)
        915         raise ValueError("The truth value of a {0} is ambiguous. "
        916                          "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
    --> 917                          .format(self.__class__.__name__))
        918 
        919     __bool__ = __nonzero__


    ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().



```python
# Use & for and
h[(h.year >= 2005) & (h.year <=2010) ]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Chal Chalein</td>
      <td>2009</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Use | for or
h[(h.year <= 2005) | (h.year >=2010) ]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Anashim Ketumim</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ritu</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Nelumbo</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Black to White</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Godsalt</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Conrack</td>
      <td>1974</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Find a Way</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Kamandag sa araw</td>
      <td>1987</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A Good Day to Die Hard</td>
      <td>2013</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Select all the movies with the name Macbeth
t = titles
t[t.title == "Macbeth"]
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21652</th>
      <td>Macbeth</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>27859</th>
      <td>Macbeth</td>
      <td>2003</td>
    </tr>
    <tr>
      <th>45120</th>
      <td>Macbeth</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>53709</th>
      <td>Macbeth</td>
      <td>1916</td>
    </tr>
    <tr>
      <th>87382</th>
      <td>Macbeth</td>
      <td>2004</td>
    </tr>
    <tr>
      <th>97756</th>
      <td>Macbeth</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>105546</th>
      <td>Macbeth</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>109611</th>
      <td>Macbeth</td>
      <td>1987</td>
    </tr>
    <tr>
      <th>115457</th>
      <td>Macbeth</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>136197</th>
      <td>Macbeth</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>183168</th>
      <td>Macbeth</td>
      <td>1998</td>
    </tr>
    <tr>
      <th>190616</th>
      <td>Macbeth</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>222186</th>
      <td>Macbeth</td>
      <td>1913</td>
    </tr>
    <tr>
      <th>227155</th>
      <td>Macbeth</td>
      <td>1997</td>
    </tr>
    <tr>
      <th>227219</th>
      <td>Macbeth</td>
      <td>1948</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Sort the table by column's value
t[t.title == "Macbeth"].sort_values(by="year").head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>222186</th>
      <td>Macbeth</td>
      <td>1913</td>
    </tr>
    <tr>
      <th>53709</th>
      <td>Macbeth</td>
      <td>1916</td>
    </tr>
    <tr>
      <th>227219</th>
      <td>Macbeth</td>
      <td>1948</td>
    </tr>
    <tr>
      <th>109611</th>
      <td>Macbeth</td>
      <td>1987</td>
    </tr>
    <tr>
      <th>227155</th>
      <td>Macbeth</td>
      <td>1997</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Sort the table by column's value
t[t.title == "Macbeth"].sort_values(by="year", ascending=False)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>97756</th>
      <td>Macbeth</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>21652</th>
      <td>Macbeth</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>105546</th>
      <td>Macbeth</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>45120</th>
      <td>Macbeth</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>136197</th>
      <td>Macbeth</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>115457</th>
      <td>Macbeth</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>190616</th>
      <td>Macbeth</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>87382</th>
      <td>Macbeth</td>
      <td>2004</td>
    </tr>
    <tr>
      <th>27859</th>
      <td>Macbeth</td>
      <td>2003</td>
    </tr>
    <tr>
      <th>183168</th>
      <td>Macbeth</td>
      <td>1998</td>
    </tr>
    <tr>
      <th>227155</th>
      <td>Macbeth</td>
      <td>1997</td>
    </tr>
    <tr>
      <th>109611</th>
      <td>Macbeth</td>
      <td>1987</td>
    </tr>
    <tr>
      <th>227219</th>
      <td>Macbeth</td>
      <td>1948</td>
    </tr>
    <tr>
      <th>53709</th>
      <td>Macbeth</td>
      <td>1916</td>
    </tr>
    <tr>
      <th>222186</th>
      <td>Macbeth</td>
      <td>1913</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Drop na and filter by multiple columns
c = cast.dropna().head(100)
c.sort_values(["year", "n"], ascending=False)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
      <th>name</th>
      <th>type</th>
      <th>character</th>
      <th>n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>54</th>
      <td>Candie's Harem</td>
      <td>2015</td>
      <td>Andrew 'Shotgun' Smith</td>
      <td>actor</td>
      <td>TV narrator</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>140</th>
      <td>Spy</td>
      <td>2015</td>
      <td>50 Cent</td>
      <td>actor</td>
      <td>Himself</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>172</th>
      <td>The Vixens</td>
      <td>2015</td>
      <td>Brandon A. Wright</td>
      <td>actor</td>
      <td>Officer Chode</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Using</td>
      <td>2015</td>
      <td>Johnny 'Koolout' Starks</td>
      <td>actor</td>
      <td>Randall Dawson</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Little Angel (Angelita)</td>
      <td>2015</td>
      <td>Michael 'babeepower' Viera</td>
      <td>actor</td>
      <td>Chico</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Josephine Doe</td>
      <td>2015</td>
      <td>Michael 'Stake' Morton III</td>
      <td>actor</td>
      <td>Cashier</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>149</th>
      <td>Z</td>
      <td>2015</td>
      <td>Zapata 666</td>
      <td>actor</td>
      <td>Z</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Angry Video Game Nerd: The Movie</td>
      <td>2014</td>
      <td>Sergeant 16-bit</td>
      <td>actor</td>
      <td>AVGN Webcam Fan</td>
      <td>382.0</td>
    </tr>
    <tr>
      <th>154</th>
      <td>Angry Video Game Nerd: The Movie</td>
      <td>2014</td>
      <td>92soothsayer</td>
      <td>actor</td>
      <td>AVGN Webcam Fan</td>
      <td>381.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Step Up All In</td>
      <td>2014</td>
      <td>Jesse 'Casper' Brown</td>
      <td>actor</td>
      <td>Grim Knight Dancer</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Mahogany Sunrise</td>
      <td>2014</td>
      <td>Gilberto 'Ghetto Bird' Bahena</td>
      <td>actor</td>
      <td>Jesse</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>When the Man Went South</td>
      <td>2014</td>
      <td>Taipaleti 'Atu'ake</td>
      <td>actor</td>
      <td>Two Palms - Ua'i Paame</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>142</th>
      <td>The Prince</td>
      <td>2014</td>
      <td>50 Cent</td>
      <td>actor</td>
      <td>The Pharmacy</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ransum Games</td>
      <td>2014</td>
      <td>Johnny 'Koolout' Starks</td>
      <td>actor</td>
      <td>Henchman #3</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>95</th>
      <td>Fall Out Boy: The Young Blood Chronicles</td>
      <td>2014</td>
      <td>2 Chainz</td>
      <td>actor</td>
      <td>The Problem Solver</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Battle of the Year</td>
      <td>2013</td>
      <td>Albert 'Trix' Thompson</td>
      <td>actor</td>
      <td>MC Trix</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Battle of the Year</td>
      <td>2013</td>
      <td>Rafael 'Spax' Szulc-Vollmann</td>
      <td>actor</td>
      <td>MC Spax</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>134</th>
      <td>Last Vegas</td>
      <td>2013</td>
      <td>50 Cent</td>
      <td>actor</td>
      <td>50 Cent</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Wakolda</td>
      <td>2013</td>
      <td>Marcelo 'Hos' Bearzi</td>
      <td>actor</td>
      <td>Due?o de la hoster?a</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>141</th>
      <td>The Frozen Ground</td>
      <td>2013</td>
      <td>50 Cent</td>
      <td>actor</td>
      <td>Pimp Clate Johnson</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Escape Plan</td>
      <td>2013</td>
      <td>50 Cent</td>
      <td>actor</td>
      <td>Hush</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Battle of the Year</td>
      <td>2013</td>
      <td>Jesse 'Casper' Brown</td>
      <td>actor</td>
      <td>Rebel</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>128</th>
      <td>Fire with Fire (II)</td>
      <td>2012</td>
      <td>50 Cent</td>
      <td>actor</td>
      <td>Lamar</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>129</th>
      <td>Freelancers</td>
      <td>2012</td>
      <td>50 Cent</td>
      <td>actor</td>
      <td>Malo</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>145</th>
      <td>Hollywood Sex Wars</td>
      <td>2011</td>
      <td>Blitch 66</td>
      <td>actor</td>
      <td>Biker</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>155</th>
      <td>Amors baller</td>
      <td>2011</td>
      <td>Hauketo 95</td>
      <td>actor</td>
      <td>Brixton Town</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>156</th>
      <td>Amors baller</td>
      <td>2011</td>
      <td>Holmen 95</td>
      <td>actor</td>
      <td>Guttelaget</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Big Weekend</td>
      <td>2011</td>
      <td>Paulex -</td>
      <td>actor</td>
      <td>Alex</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>146</th>
      <td>El rumor de las piedras</td>
      <td>2011</td>
      <td>Zapata 666</td>
      <td>actor</td>
      <td>El Mota</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>124</th>
      <td>All Things Fall Apart</td>
      <td>2011</td>
      <td>50 Cent</td>
      <td>actor</td>
      <td>Deon</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Ma 6-T va crack-er</td>
      <td>1997</td>
      <td>2 Neg</td>
      <td>actor</td>
      <td>Chanteur rap</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Ma 6-T va crack-er</td>
      <td>1997</td>
      <td>2 Bal</td>
      <td>actor</td>
      <td>Chanteur rap</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Violencia urbana</td>
      <td>1996</td>
      <td>N?stor 'Kick Boxer'</td>
      <td>actor</td>
      <td>Monta?a</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>161</th>
      <td>Lady Blues</td>
      <td>1996</td>
      <td>Charles A'Lexis</td>
      <td>actor</td>
      <td>Clerk</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>162</th>
      <td>Shadow Creature</td>
      <td>1995</td>
      <td>Charles A'Lexis</td>
      <td>actor</td>
      <td>Guard</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Violencia en la sierra</td>
      <td>1995</td>
      <td>Tony 'La Chispa'</td>
      <td>actor</td>
      <td>Victoriano</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Killing Device</td>
      <td>1993</td>
      <td>Van 'Igor' Morrison</td>
      <td>actor</td>
      <td>Jeep Driver</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Menace II Society</td>
      <td>1993</td>
      <td>Too $hort</td>
      <td>actor</td>
      <td>Lew-Loc</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>169</th>
      <td>Miami Shakedown</td>
      <td>1993</td>
      <td>A-Hito</td>
      <td>actor</td>
      <td>Tennis Trainer</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Pelotazo nacional</td>
      <td>1993</td>
      <td>F?lix 'El Gato'</td>
      <td>actor</td>
      <td>Rebolledo</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Who's the Man?</td>
      <td>1993</td>
      <td>Todd 1</td>
      <td>actor</td>
      <td>Shorty</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>159</th>
      <td>Watch the Shadows Dance</td>
      <td>1987</td>
      <td>Brett A'Hearn</td>
      <td>actor</td>
      <td>Karate Contestant</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Hannah and Her Sisters</td>
      <td>1986</td>
      <td>The 39 Steps</td>
      <td>actor</td>
      <td>Rock Band</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Suuri illusioni</td>
      <td>1985</td>
      <td>Homo $</td>
      <td>actor</td>
      <td>Guests</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Moord in extase</td>
      <td>1984</td>
      <td>Dick 't Hooft</td>
      <td>actor</td>
      <td>Officier van Justitie</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>110</th>
      <td>The House on Sorority Row</td>
      <td>1983</td>
      <td>4 Out of 5 Doctors</td>
      <td>actor</td>
      <td>The Band</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Boardinghouse</td>
      <td>1982</td>
      <td>33 1/3</td>
      <td>actor</td>
      <td>The Band</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>176</th>
      <td>Cheech and Chong's Next Movie</td>
      <td>1980</td>
      <td>Bobby A.</td>
      <td>actor</td>
      <td>Doorman</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>I Wanna Hold Your Hand</td>
      <td>1978</td>
      <td>Murray the 'K'</td>
      <td>actor</td>
      <td>Himself</td>
      <td>47.0</td>
    </tr>
    <tr>
      <th>93</th>
      <td>C.B. Hustlers</td>
      <td>1976</td>
      <td>The 18 Wheelers of Interstate 5</td>
      <td>actor</td>
      <td>The 18 Wheelers of Interstate 5</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>That's the Way of the World</td>
      <td>1975</td>
      <td>Murray the 'K'</td>
      <td>actor</td>
      <td>Big John Little</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Wild Wheels</td>
      <td>1969</td>
      <td>13th Committee</td>
      <td>actor</td>
      <td>Themselves</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Los tarantos</td>
      <td>1963</td>
      <td>'El Guisa'</td>
      <td>actor</td>
      <td>Bailaor</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Los tarantos</td>
      <td>1963</td>
      <td>'El Viti'</td>
      <td>actor</td>
      <td>Cantaor</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Los tarantos</td>
      <td>1963</td>
      <td>'Morita'</td>
      <td>actor</td>
      <td>Cantaor</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Los tarantos</td>
      <td>1963</td>
      <td>'Pucherete'</td>
      <td>actor</td>
      <td>Guitarist</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>De zaak M.P.</td>
      <td>1960</td>
      <td>Frans 't Hoen</td>
      <td>actor</td>
      <td>Hollandse boer</td>
      <td>29.0</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Dorp aan de rivier</td>
      <td>1958</td>
      <td>Frans 't Hoen</td>
      <td>actor</td>
      <td>Dirk Jan</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Fire Down Below</td>
      <td>1957</td>
      <td>'Stretch' Cox Troupe</td>
      <td>actor</td>
      <td>Limbo Dance by</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>In the Land of the Head Hunters</td>
      <td>1914</td>
      <td>Paddy 'Malid</td>
      <td>actor</td>
      <td>Kenada</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 6 columns</p>
</div>




```python
#Not null
cast.n.notnull().head()
```

    0     True
    1    False
    2     True
    3     True
    4    False
    Name: n, dtype: bool




```python
#Is null
cast.n.isnull().head()
```

    0    False
    1     True
    2    False
    3    False
    4     True
    Name: n, dtype: bool




```python
# Series should use .order not sort
cast.n.dropna().order(ascending=False).head()
```

    2396208    33613.0
    2552361      999.0
    3000293      999.0
    628654       999.0
    2382559      938.0
    Name: n, dtype: float64




```python
# df should use sort_values
cast.dropna().sort_values("n",ascending=False).head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
      <th>name</th>
      <th>type</th>
      <th>character</th>
      <th>n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2396208</th>
      <td>Tribulation</td>
      <td>2000</td>
      <td>Marium Carvell</td>
      <td>actress</td>
      <td>Selma Davis</td>
      <td>33613.0</td>
    </tr>
    <tr>
      <th>628654</th>
      <td>Rift</td>
      <td>2011</td>
      <td>Leon Fazzio</td>
      <td>actor</td>
      <td>Henry</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2552361</th>
      <td>Rift</td>
      <td>2011</td>
      <td>Catherine Fitzlanders</td>
      <td>actress</td>
      <td>Matty</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>3000293</th>
      <td>Rift</td>
      <td>2011</td>
      <td>Brittany Alexis Phillips</td>
      <td>actress</td>
      <td>Erica</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2382559</th>
      <td>Lloyd</td>
      <td>2001</td>
      <td>Lisa Calvillo</td>
      <td>actress</td>
      <td>Spaghetti Spectator</td>
      <td>938.0</td>
    </tr>
  </tbody>
</table>
</div>



### 3. Drill 1


```python
### How many movies are listed in the titles dataframe?
len(titles)
```

    234375




```python
### What are the earliest two films listed in the titles dataframe?
titles.sort_values("year").head(2)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>77349</th>
      <td>Miss Jerry</td>
      <td>1894</td>
    </tr>
    <tr>
      <th>141504</th>
      <td>The Startled Lover</td>
      <td>1898</td>
    </tr>
  </tbody>
</table>
</div>




```python
### How many movies have the title "Hamlet"?
len(titles[titles.title == "Hamlet"])
```

    20




```python
### How many movies are titled "North by Northwest"?
len(titles[titles.title == "North by Northwest"])
```

    1




```python
### When was the first movie titled "Hamlet" made?
titles[titles.title == "Hamlet"].sort_values("year").head(1)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>221639</th>
      <td>Hamlet</td>
      <td>1910</td>
    </tr>
  </tbody>
</table>
</div>




```python
### List all of the "Treasure Island" movies from earliest to most recent.
titles[titles.title == "Treasure Island"].sort_values("year")
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>129482</th>
      <td>Treasure Island</td>
      <td>1918</td>
    </tr>
    <tr>
      <th>177032</th>
      <td>Treasure Island</td>
      <td>1920</td>
    </tr>
    <tr>
      <th>40168</th>
      <td>Treasure Island</td>
      <td>1934</td>
    </tr>
    <tr>
      <th>93285</th>
      <td>Treasure Island</td>
      <td>1950</td>
    </tr>
    <tr>
      <th>48753</th>
      <td>Treasure Island</td>
      <td>1972</td>
    </tr>
    <tr>
      <th>79322</th>
      <td>Treasure Island</td>
      <td>1973</td>
    </tr>
    <tr>
      <th>223825</th>
      <td>Treasure Island</td>
      <td>1985</td>
    </tr>
    <tr>
      <th>62983</th>
      <td>Treasure Island</td>
      <td>1999</td>
    </tr>
  </tbody>
</table>
</div>




```python
### How many movies were made in the year 1950?
len(titles[titles.year == 1950])
```

    1108




```python
### How many movies were made in the year 1960?
len(titles[titles.year == 1960])
```

    1522




```python
### How many movies were made from 1950 through 1959?
len(titles[(titles.year // 10 * 10) == 1950])
```

    12838




```python
### How many movies were made from 1950 through 1959?
### Alternatively
len(titles[(titles.year >= 1950) & (titles.year <= 1959)])
```

    12838




```python
### In what years has a movie titled "Batman" been released?
titles[titles.title == "Batman"].year
```

    33079     1943
    104831    1989
    Name: year, dtype: int64




```python
### How many roles were there in the movie "Inception"?
len(cast[cast.title == "Inception"].character.unique())
```

    51




```python
### How many roles in the movie "Inception" are NOT ranked by an "n" value?
len(cast[cast.title == "Inception"][cast[cast.title == "Inception"].n.isnull()])
```

    21




```python
### But how many roles in the movie "Inception" did receive an "n" value?
len(cast[cast.title == "Inception"][cast[cast.title == "Inception"].n.notnull()])
```

    51




```python
###The above example need to align the dataframe, e.g. below is wrong
cast[cast[cast.title == "Inception"].n.notnull()]
```

    ---------------------------------------------------------------------------
    IndexingError                             Traceback (most recent call last)

    <ipython-input-38-f34acc899823> in <module>()
          1 ###The above example need to align the dataframe, e.g. below is wrong
    ----> 2 cast[cast[cast.title == "Inception"].n.notnull()]
    

    /home/isaac/anaconda3/lib/python3.6/site-packages/pandas/core/frame.py in __getitem__(self, key)
       2051         if isinstance(key, (Series, np.ndarray, Index, list)):
       2052             # either boolean or fancy integer index
    -> 2053             return self._getitem_array(key)
       2054         elif isinstance(key, DataFrame):
       2055             return self._getitem_frame(key)


    /home/isaac/anaconda3/lib/python3.6/site-packages/pandas/core/frame.py in _getitem_array(self, key)
       2091             # check_bool_indexer will throw exception if Series key cannot
       2092             # be reindexed to match DataFrame rows
    -> 2093             key = check_bool_indexer(self.index, key)
       2094             indexer = key.nonzero()[0]
       2095             return self.take(indexer, axis=0, convert=False)


    /home/isaac/anaconda3/lib/python3.6/site-packages/pandas/core/indexing.py in check_bool_indexer(ax, key)
       1815         mask = isnull(result._values)
       1816         if mask.any():
    -> 1817             raise IndexingError('Unalignable boolean Series key provided')
       1818         result = result.astype(bool)._values
       1819     elif is_sparse(result):


    IndexingError: Unalignable boolean Series key provided



```python
### Display the cast of "North by Northwest" in their correct "n"-value order, ignoring roles that did not earn a numeric "n" value.
c = cast.dropna()
c[c.title == "North by Northwest"].sort_values("n")
```

```python
### Display the entire cast, in "n"-order, of the 1972 film "Sleuth".
cast[(cast.title == "Sleuth") & (cast.year == 1972)].sort_values("n")
```

```python
### Now display the entire cast, in "n"-order, of the 2007 version of "Sleuth".
cast[(cast.title == "Sleuth") & (cast.year == 2007)].sort_values("n")
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
      <th>name</th>
      <th>type</th>
      <th>character</th>
      <th>n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>288503</th>
      <td>Sleuth</td>
      <td>2007</td>
      <td>Michael Caine</td>
      <td>actor</td>
      <td>Andrew</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1147041</th>
      <td>Sleuth</td>
      <td>2007</td>
      <td>Jude Law</td>
      <td>actor</td>
      <td>Milo</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1602268</th>
      <td>Sleuth</td>
      <td>2007</td>
      <td>Harold Pinter</td>
      <td>actor</td>
      <td>Man on T.V.</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>228757</th>
      <td>Sleuth</td>
      <td>2007</td>
      <td>Kenneth Branagh</td>
      <td>actor</td>
      <td>Other Man on T.V.</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>330751</th>
      <td>Sleuth</td>
      <td>2007</td>
      <td>Alec (II) Cawthorne</td>
      <td>actor</td>
      <td>Inspector Doppler</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2406761</th>
      <td>Sleuth</td>
      <td>2007</td>
      <td>Eve (II) Channing</td>
      <td>actress</td>
      <td>Marguerite Wyke</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2958823</th>
      <td>Sleuth</td>
      <td>2007</td>
      <td>Carmel O'Sullivan</td>
      <td>actress</td>
      <td>Maggie</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
### How many roles were credited in the silent 1921 version of Hamlet?
len(cast[(cast.title == "Hamlet") & (cast.year == 1921)])
```

    9




```python
### How many roles were credited in Branagh’s 1996 Hamlet?
len(cast[(cast.title == "Hamlet") & (cast.year == 1996)])
```

    55




```python
### How many "Hamlet" roles have been listed in all film credits through history?
len(cast[(cast.character == "Hamlet")])
```

    81




```python
### How many people have played an "Ophelia"?
len(cast[(cast.character == "Ophelia")].name.unique())
```

    94




```python
### The below answer has duplicates
len(cast[(cast.character == "Ophelia")])
```

    96




```python
### How many people have played a role called "The Dude"?
len(cast[(cast.character == "The Dude")].name.unique())
```

    16




```python
### How many people have played a role called "The Stranger"?
len(cast[(cast.character == "The Stranger")].name.unique())
```

    184




```python
### How many roles has Sidney Poitier played throughout his career?
len(cast[(cast.name == "Sidney Poitier")])
```

    43




```python
### How many roles has Judi Dench played?
len(cast[(cast.name == "Judi Dench")])
```

    51




```python
### List the supporting roles (having n=2) played by Cary Grant in the 1940s, in order by year.
cast[(cast.name == "Cary Grant") & (cast.n == 2) & (cast.year // 10 * 10 == 1940)].sort_values("year")
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
      <th>name</th>
      <th>type</th>
      <th>character</th>
      <th>n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>773493</th>
      <td>My Favorite Wife</td>
      <td>1940</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Nick</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>773503</th>
      <td>Penny Serenade</td>
      <td>1941</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Roger Adams</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
### List the leading roles that Cary Grant played in the 1940s in order by year.
cast[(cast.name == "Cary Grant") & (cast.n == 1) & (cast.year // 10 * 10 == 1940)].sort_values("year")
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
      <th>name</th>
      <th>type</th>
      <th>character</th>
      <th>n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>773518</th>
      <td>The Howards of Virginia</td>
      <td>1940</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Matt Howard</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773475</th>
      <td>His Girl Friday</td>
      <td>1940</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Walter Burns</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773520</th>
      <td>The Philadelphia Story</td>
      <td>1940</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>C. K. Dexter Haven</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773508</th>
      <td>Suspicion</td>
      <td>1941</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Johnnie</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773522</th>
      <td>The Talk of the Town</td>
      <td>1942</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Leopold Dilg</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773499</th>
      <td>Once Upon a Honeymoon</td>
      <td>1942</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Patrick 'Pat' O'Toole</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773466</th>
      <td>Destination Tokyo</td>
      <td>1943</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Capt. Cassidy</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773491</th>
      <td>Mr. Lucky</td>
      <td>1943</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Joe Adams</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773492</th>
      <td>Mr. Lucky</td>
      <td>1943</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Joe Bascopolous</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773500</th>
      <td>Once Upon a Time</td>
      <td>1944</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Jerry Flynn</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773458</th>
      <td>Arsenic and Old Lace</td>
      <td>1944</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Mortimer Brewster</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773495</th>
      <td>None But the Lonely Heart</td>
      <td>1944</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Ernie Mott</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773494</th>
      <td>Night and Day</td>
      <td>1946</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Cole Porter</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773497</th>
      <td>Notorious</td>
      <td>1946</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Devlin</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773514</th>
      <td>The Bachelor and the Bobby-Soxer</td>
      <td>1947</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Dick</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773515</th>
      <td>The Bishop's Wife</td>
      <td>1947</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Dudley</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773490</th>
      <td>Mr. Blandings Builds His Dream House</td>
      <td>1948</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Jim Blandings</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773470</th>
      <td>Every Girl Should Be Married</td>
      <td>1948</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Dr. Madison Brown</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>773479</th>
      <td>I Was a Male War Bride</td>
      <td>1949</td>
      <td>Cary Grant</td>
      <td>actor</td>
      <td>Capt. Henri Rochard</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
### How many roles were available for actors in the 1950s?
len(cast[(cast.year // 10 == 195) & (cast.type == "actor")])
```

    147951




```python
### How many roles were avilable for actresses in the 1950s?
len(cast[(cast.year // 10 == 195) & (cast.type == "actress")])
```

    53969




```python
### How many leading roles (n=1) were available from the beginning of film history through 1980?
len(cast[(cast.n == 1) & (cast.year <= 1980)])
```

    61444




```python
### How many non-leading roles were available through from the beginning of film history through 1980?
len(cast[(cast.n != 1) & (cast.year <= 1980)])
```

    1047877




```python
### How many roles through 1980 were minor enough that they did not warrant a numeric "n" rank?
len(cast[(cast.year <= 1980)][cast[(cast.year <= 1980)].n.isnull()])
```

    415167



### 4.Lecture


```python
#String operation: .str.
t = titles
#Start with Hamlet
t[t.title.str.startswith("Hamlet")].head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4158</th>
      <td>Hamlet</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>13646</th>
      <td>Hamlet</td>
      <td>1990</td>
    </tr>
    <tr>
      <th>14175</th>
      <td>Hamlet</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>17566</th>
      <td>Hamlet Unbound</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>18760</th>
      <td>Hamlet (II)</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
t[t.title.str.contains("Hamlet")].head()
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>919</th>
      <td>Harry, Hamlet and I</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>1248</th>
      <td>Han, hun og Hamlet</td>
      <td>1922</td>
    </tr>
    <tr>
      <th>4158</th>
      <td>Hamlet</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>7672</th>
      <td>Dogg's Hamlet, Cahoot's Macbeth</td>
      <td>2005</td>
    </tr>
    <tr>
      <th>13646</th>
      <td>Hamlet</td>
      <td>1990</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Value counts
#Sort based on pandas index
t.year.value_counts().sort_index().plot(xlim=(1900,2025), color = "#F7C242")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb75fbe0320>




![png](output_63_1.png)



```python
c = cast
c = c[c.character == "Kermit the Frog"]
c.plot(x = "year", y = "n", kind = "scatter", color = "#D0104C")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb75fb0b908>




![png](output_64_1.png)


### 5. Drill 2


```python
### What are the ten most common movie names of all time?
t = titles
t.title.value_counts().head(10)
```

    Hamlet                  20
    Carmen                  17
    Macbeth                 15
    The Outsider            12
    Maya                    12
    Temptation              11
    The Three Musketeers    11
    Othello                 11
    Freedom                 11
    She                     10
    Name: title, dtype: int64




```python
### Which three years of the 1930s saw the most films released?
t[t.year //10 == 193].year.value_counts().head(3)
```

    1937    1200
    1936    1142
    1938    1138
    Name: year, dtype: int64




```python
### Plot the number of films that have been released each decade over the history of cinema.
t["decade"] = t.year // 10 * 10
t.decade.value_counts().sort_index().plot(kind="bar")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb75fbe0cf8>




![png](output_68_1.png)



```python
### Plot the number of "Hamlet" films made each decade.
t[t.title=="Hamlet"].decade.value_counts().sort_index().plot(kind="bar")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb74cc8aa58>




![png](output_69_1.png)



```python
### Plot the number of "Rustler" characters in each decade of the history of film.
c = cast
c = c[c.character == "Rustler"]
(c.year // 10 * 10).value_counts().sort_index().plot(kind="bar", alpha=0.75, color = "#F05E1C")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb74cc51940>




![png](output_70_1.png)



```python
### Plot the number of "Hamlet" characters each decade.
c = cast
c = c[c.character == "Hamlet"]
(c.year // 10 * 10).value_counts().sort_index().plot(kind="bar", alpha=0.75, color = "#66327C")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb74cb99550>




![png](output_71_1.png)



```python
### What are the 11 most common character names in movie history?
c = cast
c.character.value_counts().head(11)
```

    Himself        18926
    Dancer         11015
    Extra           8638
    Reporter        7593
    Doctor          6803
    Policeman       6470
    Student         6390
    Nurse           6127
    Bartender       6123
    Minor Role      5830
    Party Guest     5820
    Name: character, dtype: int64




```python
### Who are the 10 people most often credited as "Herself" in film history?
c = cast
c[c.character == "Herself"].name.value_counts().head(10)
```

    Joyce Brothers         14
    Queen Elizabeth II     11
    Margaret Thatcher       8
    Mary Jo Pehl            7
    Joan Rivers             7
    Caroline Rhea           5
    Chris Evert             5
    Lili?n Garc?a           5
    Sally Jessy Raphael     5
    Rekha                   5
    Name: name, dtype: int64




```python
### Who are the 10 people most often credited as "Himself" in film history?
c[c.character == "Himself"].name.value_counts().head(10)
```

    Adolf Hitler             93
    Richard Nixon            39
    Ronald Reagan            31
    John F. Kennedy          26
    Ron Jeremy               24
    Franklin D. Roosevelt    20
    Bill Clinton             20
    George W. Bush           20
    Winston Churchill        20
    Martin Luther King       19
    Name: name, dtype: int64




```python
### Which actors or actresses appeared in the most movies in the year 1945?
c[c.year == 1945].name.value_counts().head()
```

    Emmett Vogan       39
    Sam (II) Harris    30
    Harold Miller      28
    Bess Flowers       28
    Nolan Leary        27
    Name: name, dtype: int64




```python
### Which actors or actresses appeared in the most movies in the year 1985?
c[c.year == 1985].name.value_counts().head()
```

    Shakti Kapoor    19
    Mammootty        17
    Sukumari         16
    Lou Scheimer     15
    Aruna Irani      14
    Name: name, dtype: int64




```python
### Plot how many roles Mammootty has played in each year of his career.
c[c.name == "Mammootty"].year.value_counts().sort_index().plot(color = "#66327C")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb74cb1f048>




![png](output_77_1.png)



```python
### What are the 10 most frequent roles that start with the phrase "Patron in"?
c[c.character.str.startswith("Patron in")].character.value_counts().head(10)
```

    Patron in Frisky Rabbit         16
    Patron in the Coffee House       9
    Patron in Chinese Restaurant     9
    Patron in Billiard Parlor        5
    Patron in Bar                    4
    Patron in cabaret                3
    Patron in Club                   3
    Patron in Restaurant             3
    Patron in restaurant             3
    Patron in Quiet Bar              2
    Name: character, dtype: int64




```python
### What are the 10 most frequent roles that start with the word "Science"?
c[c.character.str.contains("Science")].character.value_counts().head(10)
```

    Science Teacher                            53
    The Science Fair Contestants & Families     9
    Science Student                             8
    Science Fair Student                        8
    Science Fair Judge                          6
    Science Club Member                         5
    Science Reporter                            5
    Science Promo Cadet                         4
    Science Kid                                 4
    Member of 'Science Fucktion'                3
    Name: character, dtype: int64




```python
### Plot the n-values of the roles that Judi Dench has played over her career.
c = cast
c = c[c.name == "Judi Dench"].sort_values("year")
c = c[c.n.notnull()]
c.plot(x="year", y="n", color="#E03C8A", kind="scatter")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb74c9b5198>




![png](output_80_1.png)



```python
### Plot the n-values of Cary Grant's roles through his career.
c = cast
c = c[c.name == "Cary Grant"].sort_values("year")
c = c[c.n.notnull()]
c.plot(x="year", y="n", color = "#005CAF", kind = "scatter")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb74c8b9e80>




![png](output_81_1.png)



```python
### Plot the n-value of the roles that Sidney Poitier has acted over the years.
c = cast
c = c[c.name == "Sidney Poitier"].sort_values("year")
c = c[c.n.notnull()]
c.plot(x="year", y="n", color="#EFBB24", kind="scatter")
```

    <matplotlib.axes._subplots.AxesSubplot at 0x7fb74c884cc0>




![png](output_82_1.png)



```python
### How many leading (n=1) roles were available to actors, and how many to actresses, in the 1950s?
c = cast
c = c[c.n == 1]
c_actor = c[c.type == "actor"]
len(c_actor[c_actor.year // 10 == 195])
```

    6375




```python
c_actress = c[c.type == "actress"]
len(c_actress[c_actress.year // 10 == 195])
```

    2813




```python
### I like the answer here better
c = cast
c = c[c.n == 1]
c = c[c.year // 10 == 195]
c.type.value_counts()
```

    actor      6375
    actress    2813
    Name: type, dtype: int64




```python
### How many supporting (n=2) roles were available to actors, and how many to actresses, in the 1950s?
c = cast
c = c[c.n == 2]
c = c[c.year // 10 == 195]
c.type.value_counts()
```

    actress    4399
    actor      4377
    Name: type, dtype: int64


