import streamlit as st
import streamlit_theme as stt

stt.set_theme({'primary': '#f63366'})


import random 
import math 
import statistics 
from scipy.stats import norm
import numpy as np
import re
from testcode import *
import pandas as pd

PAGES = [
    "Runs Test Calculator",
    "Test for Random Number Generator",
    "Ranji Trophy Data",
    "Gold Prices",
    "Air Quality Index Data",
    "Runs Test Exception"
]

#runs test for binary sequence
 

#text templates
html_temp = """
		<div style="background-color:black;padding:10px">
		<i><b><u><h1 style="color:{};text-align:center;">{}</h1></u></b></i>
		</div>
		"""
html_temp1 = """
		<div style="background-color:black;padding:10px">
		<h2 style="color:{};text-align:center;">{}</h2>
		</div>
		"""
html_temp3 = """
		<div style="padding:10px">
		<i><b><u><h3 style="color:{};text-align:justify;">{}</h3></u></b></i>
		</div>
		"""

#sidebar code
st.sidebar.markdown(html_temp1.format("Red","Navigation"),unsafe_allow_html=True)
selection = st.sidebar.radio("", options=PAGES)


#code for random number generator testing
if(selection=="Test for Random Number Generator"):
	st.markdown(html_temp.format("white","Test for Random Number Generator"),unsafe_allow_html=True)

	st.write('\n')
	st.write('\n')
	alpha=st.number_input('Type-1 Error', min_value=0.0, max_value=1.0, value=0.01, step=0.01, format=None, key=None)
	st.write('\n')
	st.write('\n')

	p_cap=1-alpha

	samples=st.number_input('Number of binary sequence samples', min_value=0, max_value=5000, value=1000, step=10, format=None, key=None)
	st.write('\n')
	st.write('\n')
	diff = (p_cap*(1-p_cap))/samples

	diff=3*math.sqrt(diff)

	upper_limit=p_cap+diff

	lower_limit=p_cap-diff

	size_of_sequence=st.number_input('Size of binary sequence', min_value=0, max_value=500, value=100, step=10, format=None, key=None)

	#function for generating the binary sequence
	def getTest(samples,size_of_sequence):
	    count=0
	    for i in range(samples):
	        l=np.random.randint(2,size=size_of_sequence)
	        runs,mean,std=runsTest(l)
	        #continuity factor for standard normal
	        pvalue=2*min(1 - norm.cdf((runs-0.5-mean)/std),norm.cdf((runs+0.5-mean)/std))

	        if(pvalue>alpha):
	            count+=1
	    return count/samples

	def getTestPsuedo(samples,size_of_sequence):
	    count=0
	    for i in range(samples):
	       	l=np.zeros(size_of_sequence)
	       	l[0]=1
	       	for j in range(1,size_of_sequence,1):
	       		l[j]=(5*l[j-1] + 3)%2

	        runs,mean,std=runsTest(l)
	        #continuity factor for standard normal
	        pvalue=2*min(1 - norm.cdf((runs-0.5-mean)/std),norm.cdf((runs+0.5-mean)/std))

	        if(pvalue>alpha):
	            count+=1
	    return count/samples

	import matplotlib.pyplot as plt


	test_values=[]

	opt = st.radio("Select your random generator option",('Python library Random Number Generator', 'Linear Congruential Generator'))

	if(opt=='Python library Random Number Generator'):
		for i in range(20):
		    test_values.append(getTest(samples,size_of_sequence))
	elif(opt=='Linear Congruential Generator'):
		for i in range(20):
		    test_values.append(getTestPsuedo(samples,size_of_sequence))


	st.write('\n')
	st.write('\n')
	st.markdown(html_temp1.format("blue","Plot for Proportion of Sequences Passing the Test"),unsafe_allow_html=True)
	st.set_option('deprecation.showPyplotGlobalUse', False)
	plt.axhline(y=upper_limit,color='r',linestyle='-')
	plt.axhline(y=lower_limit,color='r',linestyle='-')
	plt.plot(test_values,'g^')
	plt.ylabel("Proportion Values")
	st.pyplot()



#code for run test calculator
if(selection=="Runs Test Calculator"):
	st.markdown(html_temp.format("white","Runs Test Calculator"),unsafe_allow_html=True)

	st.write('\n')
	st.write('\n')

	collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
	numbers = st.text_input("PLease enter numbers")
	l=collect_numbers(numbers)
	st.write(l)

	st.write('\n')
	st.write('\n')
	alpha=st.number_input('Type-1 Error', min_value=0.0, max_value=1.0, value=0.01, step=0.01, format=None, key=None)
	st.write('\n')
	st.write('\n')
	runs,mean,std=runsTest_notBinary(l)
	pvalue=2*min(1 - norm.cdf((runs-mean)/std),norm.cdf((runs-mean)/std))

	st.markdown(html_temp1.format("white","Results"),unsafe_allow_html=True)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","P-value"),unsafe_allow_html=True)
	st.write(pvalue)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","Decision"),unsafe_allow_html=True)
	if(pvalue>alpha):
		st.write("We cannot reject the hypothesis that the given data values are random")
	else:
		st.write("Data indicates that the hypothesis that the dataset is random should be rejected")


#code for Ranji Trophy data
if(selection=="Ranji Trophy Data"):
	st.markdown(html_temp.format("white","Ranji Trophy Data"),unsafe_allow_html=True)

	st.write('\n')
	st.write('\n')

	st.write("H0: Winning pattern for the Bombay Team is random")
	st.write("H1: Winning pattern for the Bombay Team is not random")

	st.write('\n')
	st.write('\n')
	st.markdown(html_temp3.format("blue","Data format"),unsafe_allow_html=True)
	data=pd.read_csv("./data/RanjiTrophy.csv")
	st.write(data.head())

	data=data["Bombay win"]
	data=np.array(data)

	st.write('\n')
	st.write('\n')
	alpha=st.number_input('Type-1 Error', min_value=0.0, max_value=1.0, value=0.05, step=0.01, format=None, key=None)
	st.write('\n')
	st.write('\n')
	runs,mean,std=runsTest_notBinary(data)
	pvalue=2*min(1 - norm.cdf((runs-mean)/std),norm.cdf((runs-mean)/std))

	st.markdown(html_temp1.format("white","Results"),unsafe_allow_html=True)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","P-value"),unsafe_allow_html=True)
	st.write(pvalue)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","Decision"),unsafe_allow_html=True)
	if(pvalue>alpha):
		st.write("We cannot reject the hypothesis that winning pattern of Bombay is Random")
	else:
		st.write("Data calls for rejecting the null hypothesis")



#code for Gold Prices
if(selection=="Gold Prices"):
	st.markdown(html_temp.format("white","Gold Prices"),unsafe_allow_html=True)

	st.write('\n')
	st.write('\n')

	st.write("H0: Average Gold Prices over years are random in nature")
	st.write("H1: Average Gold Prices over years are not random")

	st.write('\n')
	st.write('\n')
	st.markdown(html_temp3.format("blue","Data format"),unsafe_allow_html=True)
	data=pd.read_csv("./data/Gold_Prices.csv")
	data=data[["Year","Price (24 karat per 10 grams)"]]
	st.write(data.head())

	data=data["Price (24 karat per 10 grams)"]
	#st.write(data.head())
	data=np.array(data).astype('float32')

	st.write('\n')
	st.write('\n')
	alpha=st.number_input('Alpha', min_value=0.0, max_value=1.0, value=0.05, step=0.01, format=None, key=None)
	st.write('\n')
	st.write('\n')
	runs,mean,std=runsTest_notBinary(data)
	pvalue=2*min(1 - norm.cdf((runs-mean)/std),norm.cdf((runs-mean)/std))

	st.markdown(html_temp1.format("white","Results"),unsafe_allow_html=True)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","P-value"),unsafe_allow_html=True)
	st.write(pvalue)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","Decision"),unsafe_allow_html=True)
	if(pvalue>alpha):
		st.write("We cannot reject the hypothesis that average Gold Prices are Random")
	else:
		st.write("Data calls for rejecting the null hypothesis")


#code for runs test exception
if(selection=="Runs Test Exception"):
	st.markdown(html_temp.format("white","Runs Test Exception"),unsafe_allow_html=True)


	st.write('\n')
	st.write('\n')

	st.write("This test checks the performance of runtest on periodic data")

	st.write('\n')
	st.write('\n')
	st.write("H0: Given binary data is random in nature")
	st.write("H1: Given binary data is not random")

	st.write('\n')
	st.write('\n')

	st.write('\n')
	st.write('\n')


	opt = st.radio("Select your data option",('Binary Sequence of Period 2', 'Binary Sequence of Period 4','Binary Sequence of Period 6'))
	st.markdown(html_temp3.format("blue","Data format"),unsafe_allow_html=True)
	data=pd.read_csv("./data/Exception_runtest.csv")

	if(opt=="Binary Sequence of Period 2"):
		data=data["Period1"]
		st.write(data.head(6))

	if(opt=="Binary Sequence of Period 4"):
		data=data["Period2"]
		st.write(data.head(6))

	if(opt=="Binary Sequence of Period 6"):
		data=data["Period3"]
		st.write(data.head(6))

	data=np.array(data)

	st.write('\n')
	st.write('\n')
	alpha=st.number_input('Alpha', min_value=0.0, max_value=1.0, value=0.05, step=0.01, format=None, key=None)
	st.write('\n')
	st.write('\n')
	runs,mean,std=runsTest(data)
	pvalue=2*min(1 - norm.cdf((runs-mean)/std),norm.cdf((runs-mean)/std))

	st.markdown(html_temp1.format("white","Results"),unsafe_allow_html=True)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","P-value"),unsafe_allow_html=True)
	st.write(pvalue)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","Decision"),unsafe_allow_html=True)
	if(pvalue>alpha):
		st.write("We cannot reject the hypothesis that data is Random")
	else:
		st.write("Data calls for rejecting the null hypothesis")



#code for Air Quality index data
if(selection=="Air Quality Index Data"):
	st.markdown(html_temp.format("white","Air Quality Index Data"),unsafe_allow_html=True)

	st.write('\n')
	st.write('\n')

	st.write("H0: Average monthly Air Quality index over several months is random in nature")
	st.write("H1: Average monthly Air Quality Index is not random")

	st.write('\n')
	st.write('\n')
	st.markdown(html_temp3.format("blue","Data format"),unsafe_allow_html=True)
	data=pd.read_csv("./data/AQI_data.csv")
	
	st.write(data.head())

	data=data["AQI"]

	data=np.array(data)

	st.write('\n')
	st.write('\n')
	alpha=st.number_input('Alpha', min_value=0.0, max_value=1.0, value=0.05, step=0.01, format=None, key=None)
	st.write('\n')
	st.write('\n')
	runs,mean,std=runsTest_notBinary(data)
	pvalue=2*min(1 - norm.cdf((runs-mean)/std),norm.cdf((runs-mean)/std))

	st.markdown(html_temp1.format("white","Results"),unsafe_allow_html=True)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","P-value"),unsafe_allow_html=True)
	st.write(pvalue)
	st.write('\n')
	st.write('\n')

	st.markdown(html_temp3.format("blue","Decision"),unsafe_allow_html=True)
	if(pvalue>alpha):
		st.write("We cannot reject the hypothesis that monthly average Air Quality Index is Random")
	else:
		st.write("Data calls for rejecting the null hypothesis")