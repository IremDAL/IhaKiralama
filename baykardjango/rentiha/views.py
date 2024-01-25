from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rentiha.models import ihaalls, ihainformation, UserLogin
from rentiha.serializers import (
    IhaSerializer,
    IhainformationSerializer,
    UserLoginSerializer,
)

isLogin = 0
isAdmin = 0


@csrf_exempt
def ihaApi(request, id=0):
    if isAdmin == 1 and isLogin == 1:
        if request.method == "GET":
            ihaall = ihaalls.objects.filter(isDeleted=0)
            iha_serializer = IhaSerializer(ihaall, many=True)
            return JsonResponse(iha_serializer.data, safe=False)
        elif request.method == "POST":
            iha_data = JSONParser().parse(request)
            iha_serializer = IhaSerializer(data=iha_data)
            if iha_serializer.is_valid():
                iha_serializer.save()
                return JsonResponse("Added Successfully ", safe=False)
            return JsonResponse("Failed to Add", safe=False)
        elif request.method == "PUT":
            iha_data = JSONParser().parse(request)

            ihaall = ihaalls.objects.get(Id=id)
            iha_serializer = IhaSerializer(ihaall, data=iha_data)
            if iha_serializer.is_valid():
                iha_serializer.save()
                return JsonResponse("Update Successfully ", safe=False)
            return JsonResponse("Failed to Add", safe=False)
        elif request.method == "DELETE":
            ihaall = ihaalls.objects.get(Id=id)
            ihaall.delete()
            return JsonResponse("Delete Succesfully", safe=False)
    else:
        return JsonResponse("Giriş başarısız", safe=False)


@csrf_exempt
def ihaApi2(request, id=0):
    if isLogin == 1:
        if request.method == "GET":
            ihainformation1 = ihainformation.objects.all()
            ihainformation_serializer = IhainformationSerializer(
                ihainformation1, many=True
            )
            return JsonResponse(ihainformation_serializer.data, safe=False)
        elif request.method == "POST":
            ihainformation_data = JSONParser().parse(request)
            ihainformation_serializer = IhainformationSerializer(
                data=ihainformation_data
            )

            if ihainformation_serializer.is_valid():
                iha_number = ihaalls.objects.get(Id=ihainformation_data["rentihaid"])
                iha_number.numbers -= int(ihainformation_data["item"])
                iha_number.save()

                fee = iha_number.monthOfee
                if ihainformation_data["rentcurrency"] == "TL":
                    amount = (
                        fee
                        * float(ihainformation_data["rentmonth"])
                        * (float(ihainformation_data["item"]))
                    )
                    ihainformation_serializer.validated_data["amount"] = amount
                if ihainformation_data["rentcurrency"] == "$":
                    amount = (
                        fee
                        * float(ihainformation_data["rentmonth"])
                        * 30
                        * (float(ihainformation_data["item"]))
                    )
                    ihainformation_serializer.validated_data["amount"] = amount
                if ihainformation_data["rentcurrency"] == "TL":
                    amount = (
                        fee
                        * float(ihainformation_data["rentmonth"])
                        * 32
                        * (float(ihainformation_data["item"]))
                    )
                    ihainformation_serializer.validated_data["amount"] = amount
                ihainformation_serializer.save()
                return JsonResponse("Added Successfully ", safe=False)
            return JsonResponse("Failed to Add", safe=False)
    else:
        return JsonResponse("başarısırız to Add", safe=False)


@csrf_exempt
def userlogin(request, id=0):
    global isLogin
    global isAdmin
    if request.method == "POST":
        UserLogin_Data = JSONParser().parse(request)
        UserLogin_serializer = UserLoginSerializer(data=UserLogin_Data)

        if UserLogin_serializer.is_valid():
            username = UserLogin_Data.get("Username", None)
            password = UserLogin_Data.get("Password", None)

            try:
                user = UserLogin.objects.get(Username=username, Password=password)
                isLogin = 1
                isAdmin = user.Admin
                return JsonResponse("Login Successfully", safe=False)
            except UserLogin.DoesNotExist:
                return JsonResponse("Invalid Username or Password", safe=False)
        else:
            return JsonResponse("Failed to Add", safe=False)
