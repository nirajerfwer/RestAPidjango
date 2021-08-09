from django.shortcuts import render
from django.http import HttpResponse
import json
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

from myapp.models import Data
def empty(request):
      response = json.dumps([{}])
      return HttpResponse(response,content_type="text/json")
def index(request):
##      response = "<h1>yrd</h1>"
##      datafatch = Data()
##      datafatch.first_name = "neraj"
##      datafatch.last_name = "vishwakarma"
##      datafatch.contact = "38945094534"
##      datafatch.dob = 12/4/2000
##      datafatch.email = "testinemail@gmail.com"
##      datafatch.email = "32"
      if request.method == "GET":
                try:
                      response=""
                      data = Data.objects.all()
                      #data = Data.objects.get(first_name=data_type)
                      for i in data.iterator():
                         #response = append(json.dumps([{"firstname":str(i.first_name)}]))
                         response = response+"\n"+json.dumps([{"firstname":i.first_name," last_name ":i.last_name,"contact":i.contact,"email":i.email,"age":i.age}])
                except:
                     response = json.dumps([{"error happed"}])
      return HttpResponse(response,content_type="text/json")
##@csrf_exempt
##def testinfun(request,data_type):
##      if request.method == "GET":
##            data = Data.objects.get(first_name=data_type)
##            response = json.dumps([{"error":f"can't get data{len(data)}"}])
##      return HttpResponse(response,content_type="text/json")
@csrf_exempt   
def getdata(request,data_type):
            if request.method == "GET":
                  try:
                      response=""
                      data = Data.objects.get(first_name=data_type)
                         #response = append(json.dumps([{"firstname":str(i.first_name)}]))
                      response = json.dumps([{"firstname":data.first_name," last_name ":data.last_name,"contact":data.contact,"email":data.email,"age":data.age}])
                      #response = json.dumps([{"succes":""}])
                  except Exception as e:
                     response = json.dumps([{"error":f"can't get data{e}"}])
            #return HttpResponse(response,content_type="text/json")
            if request.method == "DELETE":
                  try:
                            data = Data.objects.get(first_name=data_type).delete()
                            response = json.dumps([{"success":"deleted data"}])
                  except:
                        response = json.dumps([{"error":"can't delete data"}])
            return HttpResponse(response,content_type="text/json")
@csrf_exempt
def xlsxdata(request):
            if request.method == "POST":
                       #response = json.dumps({"sus": "yes"})
                  workbook = pd.read_excel(r"D:\Peopleinfoproject\userdata.xlsx")
                  for i in workbook.iterrows():
                        j = tuple(i[1])
                        datainfo = Data(first_name=j[0] , last_name=j[1] , contact=j[2] , dob=j[3] , email=j[4] , age=j[5])
                        try:
                          datainfo.save()
                          response = json.dumps([{"succes":"succes fully add"}])
                        except:
                             response= json.dumps([{"error":"can't add"}])
                        
            return HttpResponse(response,content_type="text/json")
