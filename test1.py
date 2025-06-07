import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


def bestfitModel(x, y):
    bestcoeff = 0
    bestmodel = None
    bestpower = 0
    for r in range(1, 6):
        model = numpy.poly1d(numpy.polyfit(x, y, r))
        coeff = r2_score(y, model(x))
        if coeff > bestcoeff:
            bestcoeff = coeff
            bestmodel = model
            bestpower = r
    return bestcoeff, bestmodel, bestpower
def result(marks):
    if marks<40:
        return 0
    if marks<50:
        return 1
    if marks<60:
        return 2
    return 3
r=range(0,101)
x=[x for x in r]
y=[result(i) for i in x ]

failedlist=[i for i in range(40) ]
failedlistresult=[result(i) for i in failedlist]
# listy = [[1,1,1,1,],[1, 2, 3, 4], [1, 4, 9, 16], [1, 8, 27, 64], [1, 16, 81, 256]]
# y = listy[0]  # Change Here 0,1,2,3
#y=[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4]
# y=[2.5,6.0,4.5,5.0,4.5,2.0,5.5,3.0,4.5,3.0]


deg = 6
npp = numpy.polyfit(x, y, deg)
model = numpy.poly1d(npp)
coeff = r2_score(y, model(x))

print(f'\ndeg={deg}\nx={x}\ny={y}\nEquation={model}\nCorrelation={coeff}')
predictx = 1
result = model(predictx)
print(f'\nresult={result}\tfor x={predictx}')
outputy = [model(i) for i in x]
# plt.scatter(x, y,)
# plt.plot(x, y,label="Line Equation")
plt.scatter(x, outputy,label="Dots Coordinates")
# plt.plot(x, outputy,"X ka label","Y ka label")
plt.plot(failedlist, failedlistresult,label="Failed student")
plt.title(f'Lines Digram = {deg}')
plt.legend()
plt.show()