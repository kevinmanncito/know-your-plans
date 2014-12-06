from rest_framework import serializers

from apps.core import models


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Plan


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Organization
        exclude = ('sales_channel',)


class MemberSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    plans = serializers.SerializerMethodField()

    class Meta:
        model = models.Member

    def get_plans(self, obj):
        plans = models.Plan.objects.filter(organization=obj.organization)
        return PlanSerializer(plans, many=True).data
