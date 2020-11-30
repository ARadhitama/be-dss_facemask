import json
from api.models import Pengunjung, Camera
from datetime import date
from django.http import HttpResponse,JsonResponse

def get_total_pengunjung():

    try:
        count = Pengunjung.objects.filter(waktu__date=date.today()).count()
    except Exception as e:
        return JsonResponse({'message': str(e)})

    return count

def get_total_pelanggaran():

    try:
        count = Pengunjung.objects.filter(melanggar=True, waktu__date=date.today()).count()
    except Exception as e:
        return JsonResponse({'message': str(e)})

    return count

def get_total_aman():

    try:
        count = Pengunjung.objects.filter(melanggar=False, waktu__date=date.today()).count()
    except Exception as e:
        return JsonResponse({'message': str(e)})

    return count

def get_pelanggaran():

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

    return response

def post_pengunjung(data):

    kamera = Camera.objects.get(id=1)
    try:
        Pengunjung.objects.create(melanggar=data, kamera=kamera)
    except Exception as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse({"message": "success"}, status=200)