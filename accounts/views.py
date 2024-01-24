from accounts.models import Account
from accounts.serializers import AccountSerializer
from rest_framework.generics import ListCreateAPIView


class CreateAccountView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
