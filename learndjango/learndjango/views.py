from django.http import HttpResponse

def aboutus(request):
  return HttpResponse("Welcome to our siva tranings")

def course(request):
  return HttpResponse("<b>welcome to the course page</b>")
def courseDetails(request,courseid):
  return HttpResponse(courseid)