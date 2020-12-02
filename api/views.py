from django.views import View
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import jwt
import json
from api.models import Pengunjung, Camera
from datetime import date
from api.db_manager import *

class DashboardView(View):

    def get(self, *args, **kwargs):
        total_pengunjung = get_total_pengunjung()   
        total_pelanggaran = get_total_pelanggaran()
        total_aman = get_total_aman()
        pelanggaran = get_pelanggaran()
        
        return JsonResponse({
            "total_pengunjung": total_pengunjung,
            "total_pelanggaran": total_pelanggaran,
            "total_aman": total_aman,
            "pelanggaran": pelanggaran
        }, status=200)
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            status_pelanggaran = data['pelanggaran']
        except Exception as e:
            return JsonResponse({'message': str(e)})

        response = post_pengunjung(status_pelanggaran)
        return response