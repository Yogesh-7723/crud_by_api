from rest_framework import serializers
from .models import Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id','book','title','price']
        
    def validate_book(self,value):
        if value[0].islower():
            raise serializers.ValidationError('Keep First Charector Capital !')
        return value
    
    