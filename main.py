import pandas
import numpy
import matplotlib.pyplot as plt
data=(pandas.read_csv("shs_platform.csv"))
macData=data[data['platform'].str.contains('mac')]
deviceData=(macData[data["category"].str.contains("OSX Hardware")])[["date",'category', 'name', 'percentage']]
laterData=deviceData[deviceData["date"].str.contains("(201[6-9])|(202[0-5])")]
lessData=laterData[laterData["date"].str.contains("(06-01)|(01-01)")]

macbookdata=lessData[lessData["name"].str.contains("MacBook$")]
macbookairdata=lessData[lessData["name"].str.contains("MacBookAir")]
macbookprodata=lessData[lessData["name"].str.contains("MacBookPro")]
imacdata=lessData[lessData["name"].str.contains("iMac$")]
macminidata=lessData[lessData["name"].str.contains("MacMini$")]
macprodata=lessData[lessData["name"].str.contains("MacMini$")]

x=macbookdata["date"]
y1=numpy.ravel(macbookdata["percentage"])
y2=numpy.ravel(macbookairdata["percentage"])
y3=numpy.ravel(macbookprodata["percentage"])
y4=numpy.ravel(imacdata["percentage"])
y5=numpy.ravel(macminidata["percentage"])
y6=numpy.ravel(macprodata["percentage"])

plt.bar(x, y1, color='#28245a', label="MacBook")
plt.bar(x, y2, bottom=y1, color='#682d68', label="MacBook Air")
plt.bar(x, y3, bottom=y1+y2, color='#a03968', label="MacBook Pro")
plt.bar(x, y4, bottom=y1+y2+y3, color='#cc535d', label="Mac Mini")
plt.bar(x, y5, bottom=y1+y2+y3+y4, color='#e77a4d', label="Mac Pro")
plt.bar(x, y6, bottom=y1+y2+y3+y4+y5, color='#eea942', label="iMac")
plt.bar("2023-06-01",1.02-0.853,bottom=0.853,color='#8f9092', label="unklassifiziert")


plt.xlabel("Devices")
plt.ylabel("Percentage")
plt.legend()
plt.show()
"""print((lessData[lessData["date"].str.contains("2023-06-01")]).tail(6))
print(y1)
print(y2)
print(y1+y2)"""

#print(laterData.tail(30))