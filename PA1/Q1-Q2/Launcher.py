__author__ = 'Dmitry Spikhalskiy'

from Utils import *
from Sort import *

list = read("jobs.txt")               # Get all the arguments

#Q1
sortedQ1List = minusSort(list)
print "Sorted Q1 list: %s" % "".join(map(str, sortedQ1List))            # Print out the sorted list
metricQ1 = computeWeightEndTimeMetric(sortedQ1List)
print "Q1 Metric: %s" % metricQ1

#Q2
sortedQ2List = divisionSort(list)
print "Sorted Q2 list: %s" % "".join(map(str, sortedQ2List))            # Print out the sorted list
metricQ2 = computeWeightEndTimeMetric(sortedQ2List)
print "Q2 Metric: %s" % metricQ2