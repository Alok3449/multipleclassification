from sklearn import tree
import matplotlib.pyplot as plt


def divisions(n):
    if n == 2:
        return "fail"
    return "pass"


# print(divisions(5))


def classifications(n):
    # Less than 40 is fail and the numeric code is 2.
    # Pass numeric code is 1
    if n < 40:
        return 2
    return 1



trainingmarks = [50, 45,40, 66, 7, 89, 21, 39, 10, 89]
trainingmarks.sort()
marks = [[x] for x in trainingmarks]  # Classification needs input as a 2d array

# Use one of the following three
results = [classifications(x) for x in trainingmarks]  # Calculated
passorfail=[divisions(x) for  x in results]
print(f'marks = {marks}\nresults={results}\npassorfail={passorfail}')
classifier = tree.DecisionTreeClassifier()
model = classifier.fit(marks, results)
fullmarksrange=[x for x in range(39,45)]
print(model.predict([[42]])[0])
fullresultrange=[model.predict([[x]])[0] for x in fullmarksrange]
print(fullresultrange)

plt.plot(marks,results,color='red')
plt.scatter(marks,results,color='blue',marker='o')
plt.grid()
plt.xlabel('Marks')
plt.ylabel('Division')
plt.title("Marks - Division")
plt.legend(["Actual Division","Actual Division"])
plt.show()