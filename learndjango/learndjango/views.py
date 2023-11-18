from django.http import HttpResponse

def aboutus(request):
  return HttpResponse("Welcome to our siva tranings")

def course(request):
  return HttpResponse("welcome to the course page")