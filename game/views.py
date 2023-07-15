from django.http import HttpResponse

def index(request):
    return HttpResponse("12345")

# Create your views here.
