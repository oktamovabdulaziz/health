from rest_framework import serializers
from .models import *


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class DoctorAboutOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAboutOpinion
        fields = "__all__"


class HospitalAboutOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalAboutOpinion
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"


class HealthyFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyFood
        fields = "__all__"


class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = "__all__"


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"


class ResultDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultDonation
        fields = "__all__"


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = "__all__"

