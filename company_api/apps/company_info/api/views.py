from company_api.apps.company_info.models import Company, Team
from company_api.apps.company_info.api.serializers import CompanySerializer, TeamDetailSerializer, TeamSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser

# Create your views here.


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class CompanyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]

    def post(self, request):
        try:
            company = CompanySerializer(data=request.data)
            if company.is_valid():
                company.save()
                return Response({"data": company.data, "success": "True"}, status=status.HTTP_201_CREATED)
            return Response({"data": company.errors, "success": "False"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e), "success": "False"}, status=status.HTTP_400_BAD_REQUEST)


class TeamView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]

    def post(self, request):
        try:

            id = self.request.query_params.get("id")
            data = request.data
            data["company"] = id
            team = TeamSerializer(data=data)
            if team.is_valid():
                team.save()
                return Response({"data": team.data, "success": "True"}, status=status.HTTP_201_CREATED)

            return Response({"data": team.errors, "success": "False"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": e, "success": "False"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:

            data = Company.objects.all()
            teams = TeamDetailSerializer(data, many=True)
            return Response({"data": teams.data, "success": "True"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": e, "success": "False"}, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]

    def get(self, request):
        try:
            id = request.query_params.get("company_id")
            data = Company.objects.get(uuid=id)
            company = CompanySerializer(data)
            return Response({"data": company.data, "success": "True"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": e, "success": "False"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            company_name = data["company_name"]
            data = Company.objects.filter(company_name=company_name)
            company = CompanySerializer(data, many=True)

            return Response({"data": company.data, "success": "True"}, status=status.HTTP_302_FOUND)
        except Exception as e:
            return Response({"data": e, "success": "False"}, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import generics


# class TeamByCompanyView(generics.ListAPIView):
#     serializer_class = TeamDetailSerializer
#     queryset = Company.objects.all()

#     def get_queryset(self):

#         return Company.objects.all()
