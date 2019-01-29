from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fun(request):
	# read the template html code, create HttpResponse
	return render(request,"index.html")
'''
def fun(request):
	resp = """
	<html>
		<body>
		<h1>Weather is ok today in hyd</h1>
		</body>
	</html>
	"""
	return HttpResponse(resp)
'''
