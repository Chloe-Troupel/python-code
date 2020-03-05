# file: dataMining.py
# author: Chloé TROUPEL
# purpose: to have a bar histogram and a pie chart of the colors of a picture

from PIL import Image
import numpy
import math
import matplotlib.pyplot as plot
import matplotlib
from sklearn.cluster import KMeans

imgfile = Image.open("flower.jpg")
numarray = numpy.array(imgfile.getdata(), numpy.uint8)
n_input = input("Enter a number of categories of colors: ")
while (type(n_input) != int) :
  try:
    n = int(n_input)
    break
  except:
    print(n_input, " is not an int")
    n_input = input("Enter an int: ")
    pass

clusters = KMeans(n_clusters = n)
clusters.fit(numarray)

npbins = numpy.arange(0, n+1)
histogram = numpy.histogram(clusters.labels_, bins=npbins)
labels = numpy.unique(clusters.labels_)

dico = {}
for i in range(n):
  dico[histogram[1][i]]=histogram[0][i]

barlist = plot.bar(labels, sorted(histogram[0], reverse=True))

color=[]
for i in range(n):
  for k,val in dico.items():
    if barlist[i].get_height() == val:
      barlist[i].set_color('#%02x%02x%02x' % (math.ceil(clusters.cluster_centers_[k][0]),
        math.ceil(clusters.cluster_centers_[k][1]), math.ceil(clusters.cluster_centers_[k][2])))
      color.append('#%02x%02x%02x' % (math.ceil(clusters.cluster_centers_[k][0]),
        math.ceil(clusters.cluster_centers_[k][1]), math.ceil(clusters.cluster_centers_[k][2]))) #storing colors in a list to reuse them

plot.show()

#Pie chart
plotlist = plot.pie( sorted(histogram[0], reverse=True), labels=labels, colors = color)
plot.show()
