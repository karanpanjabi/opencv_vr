# import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import scipy.stats as ss
import scipy.spatial.distance as ssd
import random

#template
x = [0.0, 0.14285714285714285, 0.2857142857142857, 0.42857142857142855, 0.5714285714285714, 0.7142857142857143, 0.8571428571428571]
y = [0.47251887927832953, 0.6810175786242851, 0.8970394779234148, 1.0, 0.7647218447684332, 0.9441395458321341, 0.6121627518846883]

templateArr = np.divide(x,y) #combining x and y
print(templateArr)

#door
x2 = [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334]
y2 = [0.5391977899726808, 0.7144540848914289, 1.0, 0.788270649047515, 0.9334667418822455, 0.6299332455984632]

#not a door
x3 = [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]
y3 = [0.7071067811865475, 0.7071067811865475, 0.8944271909999159, 1.0, 1.0, 1.0, 0.9486832980505138, 0.7071067811865475]
# x3 = [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334]
# y3 = [0.5, 0.5, 0.7071067811865476, 1.0, 0.7071067811865476, 0.5]
# x3 = [0.0, 0.16666666666666666, 0.3333333333333333, 0.5, 0.6666666666666666, 0.8333333333333334]
# y3 = [0.5472166715955232, 0.6764666215737458, 1.0, 0.8520112619833901, 0.91606779595982, 0.7507750795602012]
# x3 = [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]
# y3 = [0.1865801030443587, 0.6034621742832079, 1.0, 0.9782922141343521, 0.496126613768977, 0.7715631861005089, 0.5825554757910253, 0.2420142085502091]

def getNewXAndY(x,y, points):
	# f = interp1d(x,y, kind='linear')

	# xnew = np.linspace ( min(x), max(x), num = points)
	# ynew = f(xnew)

	xnew = []
	ynew = []
	#if we have the same number of points as points then just return
	if(len(x) == points):
		xnew.extend(x)
		ynew.extend(y)
	#else if this happens, then add some point in the middle
	elif(len(x) < points):
		f = interp1d(x,y)
		idx = random.randint(0,len(x)-1)
		pass


	return (xnew, ynew)

# points = 50
# xnew, ynew = getNewXAndY(x, y, points)
# xnew2, ynew2 = getNewXAndY(x2, y2, points)
# xnew3, ynew3 = getNewXAndY(x3, y3, points)

# plt.plot(xnew, ynew, 'r', xnew2, ynew2, 'g', xnew3, ynew3, 'r--')
#
# print("Template + door",ss.spearmanr(ynew, ynew2))
# print("Template + door",ssd.correlation(ynew, ynew))
# print("Template + not a door",ss.spearmanr(ynew, ynew3))
# print("Template + not a door",ssd.correlation(ynew, ynew3))

def isADoor(contX, contY):
	contXNew, contYNew = getNewXAndY(contX, contY, len(x))
	contArr = np.divide(contXNew, contYNew)
	# print(contArr)
	# corr = ssd.correlation(ynew, contYNew)
	# spear = ss.spearmanr(ynew, contYNew)
	# pearson = np.correlate(ynew, contYNew, mode='valid')

	corr = ssd.correlation(templateArr, contArr)
	spear = ss.spearmanr(templateArr, contArr)
	pearson = np.correlate(templateArr, contArr)

	# print(corr, spear, pearson),
	# plt.plot(x, y, 'r', contXNew, contYNew, 'g')
	# plt.show()
	# plt.clf()
	return corr < 0.018

# print(isADoor(ynew, ynew3))

# plt.show()
