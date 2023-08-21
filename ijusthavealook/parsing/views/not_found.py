from django.http import HttpResponseNotFound


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Not found</h1><br>This page is not found")