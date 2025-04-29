from rest_framework import serializers

from rest_framework.exceptions import ValidationError
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = ('id','title','subtitle','author','content','isbn','price')
    
    def validate(self,data):
        #print(data)
        title=data.get('title',None)
        # print(f"title {title}")
        # print(type(title))
        #check title if it contains only alphabetical chars
        if not isinstance(title, str) or not title.replace(' ', '').isalpha():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Kitobni sarlovhasi harflardan tashkil topgan bo'lishi kerak!"
                }
            )
        author=data.get('author',None)
        #check title and author from database
        if Book.objects.filter(title=title,author=author).exists():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Kitobni sarlovhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz."
                }
            )
        return data 
    def validate_price(self, price):
        #print(price)
        if price<0 or price>9999999999:
            raise ValidationError(
                {
                    "status":False,
                    "message":"Narx noto'g'ri kiritilgan."
                }
            )
        return price