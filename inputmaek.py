# inputmarks=[50,45,66,7,89,21,39,40,89]
# inputmarks.sort()
# marks=[[x] for x in inputmarks]#Classification needs input as a 2d array
# #Use one of the following three
# results=[classifications(x) for x in inputmarks]#Calculated
# #results= [4, 4, 4, 3, 3, 2, 1, 1,1]# Input Results
# #results= [4, 4, 1, 3, 3, 2, 1, 1,1]# Input Results with error
# #results= [4, 4, 1, 1, 1, 1, 1, 1,4]# Input Results with fail pass error
# #results= [4, 4, 4, 3, 3, 2, 1, 1,4]# Input Results with labeling error. 89 = both1 and 2
# textresults=[divisions(x) for x in results]