from rest_framework import serializers
from . import CoinsFromXML


class CoinSerializer(serializers.Serializer):

    _id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    website = serializers.CharField(max_length=20)
    exchange_id = serializers.CharField(max_length=30)

    # def create(self, validated_data):
        
    #     return CoinsFromXML(id=None, **validated_data)

    # def update(self, instance, validated_data):
    #     # for field, value in validated_data.items():
    #     #     setattr(instance, field, value)
    #     # return instance
        
    #     instance._id = validated_data.get('_id', instance._id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.website = validated_data.get('website', instance.website)
    #     instance.exchange_id = validated_data.get('exchange_id', instance.exchange_id)
    #     return instance