from django.views.generic import ListView
from .models import Car
# Create your views here.

class Home(ListView):
    template_name = "home.html"
    model = Car
    context_object_name = "cars"
    paginate_by = 5

    #* For all objects
    queryset = Car.objects.all()

    #? For just the Cars with images
    queryset = Car.with_images.all()
