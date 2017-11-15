from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
  "year": strftime("%Y", gmtime()),
  "newTime": strftime("%B %d,%Y %H:%M %p", gmtime()),
  "timeZoneName": strftime("%Z", gmtime()),
  "12hourClock": strftime("%I", gmtime())
  }
  return render(request,'timeApp/index.html', context)
