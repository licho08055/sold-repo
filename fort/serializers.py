from rest_framework import serializers
from .models import User,Sell,Buyer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','phone_number',]
        

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sell
        fields=['user','price',]
        
        
class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Buyer
        fields=['sell','Buyer_id',]