# Flights - Data Visualization


<h2>
This project includes basic data visualization methods can be used with python libraries numpy, pandas, matplotlib and seaborn.</h2>
<h3>The data sheet used in this project is a flight detail dataframe about Indian flights and destnations.</h3>
<h5>Screenshots of output tables have included in the below table with corresponding python code.</h5>
<h1>  </h1>

<h4>1) Visualizing bar plot of 'Source' column (port of departure) with number of flights from each source in the flights datframe (lets's say df).</h4>

```python 
sb.countplot(data = flights, x= 'Source')
plt.ylabel('Number of flights',fontsize=12)
plt.xlabel('Source',fontsize=12)
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar1.png" width="350" title="hover text" >
</p> 

<h4>2) Displaying same plot (1)  with minor changes of its appearance. Colors of the bars are changed and the x lables have a rotation of 30 degrees.</h4>

```python 
base_color = sb.color_palette()[0]
sb.countplot(data = flights, x = 'Source', color = base_color)
plt.xticks(rotation = 30)
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar2.png" width="350" title="hover text" >
</p> 

<h4>3) Displaying same plot (1)  with appearance changed to orange and the indeces have been ordered to decending order.</h4>

```python 
base_color = sb.color_palette()[1]
gen_order = flights['Source'].value_counts().index
sb.countplot(data = flights, x = 'Source', color = base_color, order = gen_order)
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar3.png" width="350" title="hover text" >
</p> 

<h4>4) Visualizing the bar plot of the column 'Airlines' indicating the variety of airline. The x labels have been rotated 90 degrees.</h4>

```python 
base_color = sb.color_palette()[2]
sb.countplot(data = flights, x = 'Airline', color = base_color)
plt.xticks(rotation = 90);
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar5.png" width="350" title="hover text" >
</p> 

<h4>5) Displaying the same plot as (4) but previous indeces of x axis now lie on y axis.</h4>

```python 
base_color = sb.color_palette()[2]
sb.countplot(data = flights, y = 'Airline', color = base_color)
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar6.png" width="500" title="hover text" >
</p> 

<h4>6) The method isna() allows finding null values in a dataframe. Here it diplays the barplot of all columns and number of null values lying inside.</h4>

```python 
na_counts = flights.isna().sum()
base_color = sb.color_palette()[0]
sb.barplot(na_counts.index.values, na_counts, color = base_color)
plt.xticks(rotation = 90)
plt.ylabel('Number of missing values', fontsize = 12)
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar7.png" width="350" title="hover text" >
</p> 

<h4>7) Visualizing pie chart of the column 'Destination'. The values have been sorted and the chart start from 0 degrees and following descending order clockwise.</h4>

```python 
sorted_counts = flights['Destination'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False);
plt.axis('square')
plt.title('Flight Destination\'s')
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar8.png" width="350" title="hover text" >
</p> 

<h4>8) Visualizing doughnut-pie chart of the column 'Destination'.</h4>

```python 
sorted_counts = flights['Destination'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False, wedgeprops = {'width' : 0.4});
plt.axis('square');
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar9.png" width="350" title="hover text" >
</p> 

<h4>9) Visualizing histogram of the column 'Duration'</h4>

```python 
plt.hist(data = flights, x = 'Duration(minutes)')
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar10.png" width="350" title="hover text" >
</p> 

<h4>10) Histogram of the column 'Price' and the number of bins have been limited to 20.</h4>

```python 
plt.hist(data = flights, x = 'Price', bins = 20)
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar11.png" width="350" title="hover text" >
</p> 

<h4>11) Histogram of the column 'Price' and the number of bins has been allocated as each bin has a width of 1200 units.</h4>

```python 
bins = np.arange(0, flights['Price'].max()+1, 1200)
plt.hist(data = flights, x = 'Price', bins = bins)
plt.show()
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar12.png" width="350" title="hover text" >
</p> 

<h4>12) Histogram of the column 'Price' with kde representation.</h4>

```python 
sb.distplot(flights['Price']);
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar13.png" width="350" title="hover text" >
</p> 

<h4>11) Histogram of the column 'Price' without kde.</h4>

```python 
sb.distplot(flights['Price'], kde=False);
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar14.png" width="350" title="hover text" >
</p> 

<h4>11) Histogram of the column 'Price' and the number of bins has been allocated as each bin has a width of 1200 units and without kde.</h4>

```python 
bin_edges = np.arange(0, flights['Price'].max()+1, 1200)
sb.distplot(flights['Price'], bins = bin_edges, kde = False,
            hist_kws = {'alpha' : 1});
```
<p align="left">
 <img src="https://github.com/januka36/dataviz-flights/blob/main/Screenshots/bar15.png" width="350" title="hover text" >
</p> 



