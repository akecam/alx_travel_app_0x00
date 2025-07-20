from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ["title", "description", "price_per_night", "host"]

    def validate_price_per_night(self, value):
        if value <= 0:
            serializers.ValidationError("price must be greater than 0")
        return value


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"
