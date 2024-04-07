

#* (2) - We need to import it first
from extra_views import ModelFormSetView 
from django.http import HttpResponseRedirect

# Create your views here.

#* (3) - Then use it
'''
 #* (4) - To create more than one form use 
 #TODO: "ModelFormSetView"
'''
class ObjectCreateView(ModelFormSetView):
    model = ObjectModel
    template_name = "create-object.html"
    form_class = ObjectForm
    success_url = "/"

    def formset_valid(self, formset):
        self.object_list = formset.save(commit=False) #* Do not save it into the database
        for object in self.object_list:
            object.user = self.request.user #* If the user is authenticated, get it 
            object.save() #* Save into the database
        
        return HttpResponseRedirect(self.get_success_url())


#*  ---- This is better just for performance, However both of them are acceptable
class ObjectCreateView(ModelFormSetView):
    model = ObjectModel
    template_name = "create-object.html"
    form_class = ObjectForm
    success_url = "/"

    def formset_valid(self, formset):

        obj = []

        self.object_list = formset.save(commit=False) #* Do not save it into the database
        for object in self.object_list:
            object.user = self.request.user #* If the user is authenticated, get it 
            obj.append(object)
            #object.save() #* Save into the database
        Flower.object.bulk_update(
            obj, ["title", "title_ar", "image", "description", "description_ar", "user"] 
        ) #* This create one number of calls to the database not n number of calls, Better for performance
        return HttpResponseRedirect(self.get_success_url())