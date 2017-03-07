import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

class _corpus:
	def __init__(self):
		self.m_parentList = []

class _parentDoc:
	def __init__(self):
		self.m_topic = []
		self.m_name = ""
		self.m_childList = []

class _childDoc:
	def __init__(self):
		self.m_topic = []
		self.m_name = ""
		self.m_time = None

def readFile(inputFileName, corpusObj):
	f = open(inputFileName)

	rawLine = f.readline()
	line = rawLine.strip().split("\t")
	topicProportion = []
	topicNum = len(line)-2

	parentObj.m_name = line[0]

	for i in range(2, topicNum+2):
		parentObj.m_topic.append(float(line[i]))

	# print topicProportion
	# parentObj.m_topic = topicProportion

	# print parentObj.m_topic

	for rawLine in f:
		line = rawLine.strip().split("\t")
		dateTimeStr = line[2]
		# print dateTimeStr
		cdateTime = datetime.strptime(dateTimeStr, "%Y-%m-%d_%H:%M:%S")

		childObj = _childDoc()
		childObj.m_name = line[0]
		childObj.m_time = cdateTime
		# print cdateTime

		# print line
		for i in range(4, topicNum+4):
			childObj.m_topic.append(float(line[i]))

		parentObj.m_childList.append(childObj)

def visualizeDynamicTopic(parentObj, timeDelta):
	xTrickList = []
	yTrickList = []

	topicProportionDict = {} ##topicIndex:[]

	initialCommentTime = None
	firstFlag = True

	# print "paren topic\t", parentObj.m_topic
	topicNum = len(parentObj.m_topic)
	xList = []

	fig = plt.figure()
	ax = fig.add_subplot(111)

	for topicIndex in range(topicNum):
		topicProportionDict.setdefault(topicIndex, [])

	print "commentNum\t", len(parentObj.m_childList)
	for childObj in parentObj.m_childList:
		commentTime = None
		if firstFlag:
			initialCommentTime = childObj.m_time
			firstFlag = False
		
		commentTime = childObj.m_time

		xList.append(commentTime)

		for topicIndex in range(topicNum):
			topicProportionDict[topicIndex].append(childObj.m_topic[topicIndex])

		# print "topic proportion\t", childObj.m_topic

	# print xList
	topicProportionList = []
	print xList, "\t before convert \t"
	xList = matplotlib.dates.date2num(xList)

	print xList 

	markerList = ["s", "*", "d", ">", "x", "p", "<"]
	linestyleList = ["--", "--", ":", "-", "-.", "-", ":"]
	colorList = ['b', 'r', 'g', 'm', "k", "#8b4513", "#800000"]


	# for topicIndex in range(topicNum):
	# 	topicProportionList = topicProportionDict[topicIndex]
	# 	# print topicProportionList
	# 	plt.plot_date(xList, topicProportionList, linewidth=2, label=str(topicIndex), color=colorList[topicIndex], marker=markerList[topicIndex], linestyle=linestyleList[topicIndex])

	# 	print topicProportionList

	topicIndexList = [0, 3, 5]
	for topicIndex in topicIndexList:
	# for topicIndex in range(topicNum):
		topicProportionList = topicProportionDict[topicIndex]
			# print topicProportionList
		plt.plot_date(xList, topicProportionList, linewidth=2, label=str(topicIndex), color=colorList[topicIndex], marker=markerList[topicIndex])

	legendProp = {"weight":"semibold", "size":18}
	plt.legend(prop=legendProp)
	plt.xlabel("timeline", fontsize=20)
	plt.ylabel("topic proportion", fontsize=20)

	for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
	    item.set_fontsize(20)
	    item.set_fontweight('semibold')
	plt.show()

inputFile = "2.txt"
parentObj = _parentDoc()

timeDelta = 60 ###seconds

fileDir = ""

for fileName in os.listdir(fileDir):
	inputFile = os.path.join(fileDir, fileName)
	readFile(inputFile, parentObj)

visualizeDynamicTopic(parentObj, timeDelta)



