from django.http import HttpResponse, HttpResponseNotFound


def test(request, *args, **kwargs):
    return HttpResponse('OK')
