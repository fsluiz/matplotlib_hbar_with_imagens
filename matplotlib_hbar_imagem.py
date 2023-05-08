import requests
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
# Customaze styles see https://matplotlib.org/stable/tutorials/introductory/customizing.html
plt.style.use("seaborn-darkgrid")

def h_bar(labels, values,height,colors, ax, save_fig=False):
    #matplot lib horizontal bar
    plt.barh(y=labels, width=values, height=height, color=colors, align='center', alpha=0.8)
   
    for i, (label, value) in enumerate(zip(labels, values)):
        response = requests.get(list_https[i])#take html code where image is
        imga = BytesIO(response.content)# take html code to binary
        img = Image.open(imga)#take the binary to image
        im = OffsetImage(img, zoom=0.05)#change the size of the image
        im.image.axes = ax
        ab = AnnotationBbox(im, (0, i), xybox=(-25, 0), frameon=False,
                        xycoords='data', boxcoords="offset points", pad=0)
        ax.add_artist(ab)
        #offset_image(value, i, label, bar_is_too_short=value < max_value / 10, ax=plt.gca())
    plt.subplots_adjust(left=0.15)
    #remove the labels of y-axis
    plt.yticks([]) 
    plt.xlabel('Values')
    if save_fig:
        plt.savefig('hbar_chart.png')
    plt.show()
