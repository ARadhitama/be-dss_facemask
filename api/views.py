from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import jwt
import json
from api.models import Pengunjung, Camera
from datetime import date

@csrf_exempt
def post_pengunjung(request):

    try:
        data = json.loads(request.body)
        status_pelanggaran = data['pelanggaran']
    except Exception as e:
        return JsonResponse({'message': str(e)})

    kamera = Camera.objects.get(id=1)
    try:
        Pengunjung.objects.create(melanggar=status_pelanggaran, kamera=kamera)
    except Exception as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse({"message": "success"}, status=200)

@csrf_exempt
def get_total_pengunjung(request):

    try:
        count = Pengunjung.objects.filter(waktu__date=date.today()).count()
    except Exception as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse({"total pengunjung": count}, status=200)

@csrf_exempt
def get_total_pelanggaran(request):

    try:
        count = Pengunjung.objects.filter(melanggar=True, waktu__date=date.today()).count()
    except Exception as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse({"total pelanggaran": count}, status=200)

@csrf_exempt
def get_total_aman(request):

    try:
        count = Pengunjung.objects.filter(melanggar=False, waktu__date=date.today()).count()
    except Exception as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse({"total aman": count}, status=200)

@csrf_exempt
def get_pelanggaran(request):

    try :
        pelanggaran = Pengunjung.objects.filter(melanggar=True, waktu__date=date.today()).order_by('-waktu')
    except Exception as e:
        return JsonResponse({'message': str(e)})

    response = []

    for data in pelanggaran:
        response.append({
            'kamera': data.kamera_id,
            'lokasi': data.kamera.lokasi,
            'waktu': data.waktu.time().replace(microsecond=0).isoformat()
        })

    return JsonResponse({"data": response}, status=200)
