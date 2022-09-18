from rest_framework import serializers
from company_api.apps.company_info.models import Company, Team


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamDetailSerializer(serializers.ModelSerializer):
    teams = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ["company_name", "company_ceo", "company_address", "inception_date", "teams"]

    def get_teams(self, obj):
        team = Team.objects.filter(company=obj)  # Or do some other filtering here
        return TeamSerializer(instance=team, many=True).data
