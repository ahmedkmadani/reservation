from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from  django.core.exceptions import ObjectDoesNotExist

from app.models.tables import Tables
from app.constants.working_hours import WorkingHours

class AvailableSlotView(APIView):
    permission_classes = [IsAuthenticated & AllowAny]
    def get(self, request):
        seats_number = request.data['seats_number']
        table = Tables.objects.filter(seats_number=seats_number+1).all()
        if not table:
            res = Response()
            res.data = {"msg": "There is no tables"}
            return res
        else:
            res = Response()
            res.data = table.table_number
            return res
