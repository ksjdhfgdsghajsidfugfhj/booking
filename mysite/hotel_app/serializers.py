from .models import (UserProfile, Country, City, Services, Hotels, ImageHotel,
                     Room, ImageRoom, Review, Booking)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username']


class CountryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name']


class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name']


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'service_name', 'service_image']


class HotelListSerializers(serializers.ModelSerializer):
    country = CountryListSerializers()
    city = CityListSerializers()
    services = ServicesSerializers(many=True)

    class Meta:
        model = Hotels
        fields = ['id', 'hotel_image', 'hotel_name', 'country', 'city']


class ImageHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageHotel
        fields = ['id', 'image']


class CityDetailSerializers(serializers.ModelSerializer):
    city_hotel = HotelListSerializers(read_only=True, many=True)

    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_hotel']



class CountryDetailSerializers(serializers.ModelSerializer):
    country_hotel = HotelListSerializers(read_only=True, many=True)

    class Meta:
        model = Country
        fields = ['id', 'country_name', 'country_hotel']


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ImageRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageRoom
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()

    class Meta:
        model = Review
        fields = ['id', 'user', 'comment', 'stars']


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class HotelDetailSerializers(serializers.ModelSerializer):
    country = CountryListSerializers()
    city = CityListSerializers()
    services = ServicesSerializers(many=True)
    images_hotel = ImageHotelSerializers(read_only=True, many=True)
    reviews = ReviewSerializers(read_only=True, many=True)

    class Meta:
        model = Hotels
        fields = ['id', 'hotel_image', 'images_hotel', 'hotel_name', 'country', 'city',
                  'address', 'services', 'description', 'reviews']
