from sklearn import tree


def divisions(n):
    if n == 2:
        return "fail"
    return "pass"


print(divisions(5))


def classifications(n):
    # Less than 40 is fail and the numeric code is 2.
    # Pass numeric code is 1
    if n < 40:
        return 2
    return 1


print(classifications(7))

inputmarks = [50, 45, 66, 7, 89, 21, 39, 10, 89]
inputmarks.sort()
marks = [[x] for x in inputmarks]  # Classification needs input as a 2d array
print(marks)
# Use one of the following three
results = [classifications(x) for x in inputmarks]  # Calculated
print(results)
# results= [4, 4, 4, 3, 3, 2, 1, 1,1]# Input Results
# results= [4, 4, 1, 3, 3, 2, 1, 1,1]# Input Results with error
# results= [4, 4, 1, 1, 1, 1, 1, 1,4]# Input Results with fail pass error
# results= [4, 4, 4, 3, 3, 2, 1, 1,4]# Input Results with labeling error. 89 = both1 and 2
textresults = [divisions(x) for x in results]
print(textresults)

classifier = tree.DecisionTreeClassifier()
model = classifier.fit(marks, results)
print(model)
results=[classifications(x) for x in inputmarks]#Calculated
print(results)

textresults=[divisions(x) for x in results]# Print results in words

print(textresults)