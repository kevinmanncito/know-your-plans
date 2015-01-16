from rest_framework import serializers

from apps.core import models


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Level


class CarrierSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Carrier


class PlanSerializer(serializers.ModelSerializer):
    levels = serializers.SerializerMethodField()
    carrier = serializers.SerializerMethodField()

    class Meta:
        model = models.Plan

    def get_levels(self, obj):
        levels = models.Level.objects.filter(plan=obj)
        return LevelSerializer(levels, many=True).data

    def get_carrier(self, obj):
        carrier = models.Carrier.objects.get(id=obj.carrier.id)
        return CarrierSerializer(carrier).data


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Organization
        exclude = ('sales_channel',)


class MemberSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    medical_plans = serializers.SerializerMethodField()
    dental_plans = serializers.SerializerMethodField()

    class Meta:
        model = models.Member

    def get_medical_plans(self, obj):
        plans = models.Plan.objects.filter(organization=obj.organization,
                                           plan_type__value="medical")
        return PlanSerializer(plans, many=True).data

    def get_dental_plans(self, obj):
        plans = models.Plan.objects.filter(organization=obj.organization,
                                           plan_type__value="dental")
        return PlanSerializer(plans, many=True).data

