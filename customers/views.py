from django.shortcuts import render
from rest_framework.response import Response

from customers.models import Client, Domain
from rest_framework import viewsets, response, status
from .serializers import ClientSerializer, DomainSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new client
        :Parameter: name, paid_until, on_trial
        :Authentication: nill
        """

        try:
            # Domain.objects.get(id=5)
            # serializer = self.serializer_class(data=request.data)
            # serializer.is_valid(raise_exception=True)
            # serializer.save()
            tenant = Client(schema_name=request.data.get("name"),

                            # schema_name=serializer.data.get("username"),
                            name=request.data.get("name"),
                            paid_until=request.data.get("paid_until"),
                            on_trial=True)
            tenant.save()

            domain = Domain()
            domain.domain = request.data.get("name")+".localhost.com"             # don't add your port or www here! on a local server you'll want to use localhost here
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
            response = {"statusCode": 200, "error": False, "message": "Client created successfully!"}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            error = {"statusCode": 400, "error": True, "data": "", "message": "Bad Request, Please check request",
                     "errors": e.args[0]}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


