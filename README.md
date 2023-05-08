# Matplotlib horizontal bar chart with country flags

This code generates a horizontal bar chart using Matplotlib library in Python. The chart shows the values and their corresponding imagens.

## Dependencies
* numpy
* requests
* io
* matplotlib
* PIL
## How to use
1. Install the dependencies
2. Import the required libraries
3. Customize the styles using plt.style.use()
4. Define the function h_bar() with the following parameters:
* labels: a list of names
* values: a list of values corresponding to each name
* height: the thickness of the bars
* colors: a list of colors for the bars
* ax: the Axes object of the plot
* save_fig: boolean to save the chart as an image file.
5. Define the URLs for the country flags in a list list_https
6. Define the labels for the countries in a list labels
7. Define the values for the countries in a list values
8. Define the thickness of the bars in height
9. Define the colors of the bars in a list colors
10. Call the function h_bar() with the parameters and the ax object
11. Show the plot using plt.show()
Note: The imagens are downloaded from the URLs and added to the chart using OffsetImage() and AnnotationBbox() functions.
