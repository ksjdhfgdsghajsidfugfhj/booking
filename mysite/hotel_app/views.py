from .filter import HotelFilter
from .models import (UserProfile, Country, City, Services, Hotels, ImageHotel,
                     Room, ImageRoom, Review, Booking)
from .serializers import (UserProfileSerializers, CountryListSerializers, CountryDetailSerializers,
                          CityListSerializers,CityDetailSerializers,
                          ServicesSerializers, HotelListSerializers, HotelDetailSerializers,
                          ImageHotelSerializers, RoomSerializers,
                          ImageRoomSerializers, ReviewSerializers, BookingSerializers, LoginSerializer, UserSerializer)
from rest_framework import viewsets, generics, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filter import HotelFilter, RoomFilter
from .permissions import CheckStatusUser

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CityListViewSet(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CityDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CountryListViewSet(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CountryDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HotelListViewSet(generics.ListCreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['hotel_name']
    filterset_class = HotelFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckStatusUser]

class HotelDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckStatusUser]

class ImageHotelViewSet(viewsets.ModelViewSet):
    queryset = ImageHotel.objects.all()
    serializer_class = ImageHotelSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['room_name']
    ordering_fields = ['price']
    filterset_class = RoomFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ImageRoomViewSet(viewsets.ModelViewSet):
    queryset = ImageRoom.objects.all()
    serializer_class = ImageRoomSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
