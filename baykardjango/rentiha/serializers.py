from rest_framework import serializers
from rentiha.models import ihaalls,ihainformation,UserLogin

class IhaSerializer(serializers.ModelSerializer):
    class Meta:
        model=ihaalls
        fields=('Id','ihaName','serialNo','yearOfProduction','numbers','monthOfee','currency','rentalActive','isDeleted')
        
 
class IhainformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=ihainformation
        fields=('Id','rentihaid','rentmonth','rentcurrency','item','amount','currency','rentalPeriodOver') 

class UserLoginSerializer(serializers.ModelSerializer):
     class Meta:
        model = UserLogin
        fields = ('Id', 'Username', 'Password')
