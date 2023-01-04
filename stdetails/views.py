from django.views.generic import TemplateView,FormView
from .models import Post
from .forms import Form
from .variables import data
class Homepageview(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Postq = Post.objects.all()
        
        for i in Postq:
            print(i.Pinno)
            print(data.user)
            if i.Pinno == data.user:
                context['post'] = i
        return context

class Loginpageview(FormView):   
    template_name = "login.html"
    form_class = Form
    success_url = "home/"

    def form_valid(self, form):
        Postq = Post.objects.all()
        for i in Postq:
            if i.Pinno == form.cleaned_data['Ipinno']:
                data.user = i.Pinno
        if data.user == "":
            return super().form_invalid(form)
        else:
            return super().form_valid(form)



    

# Create your views here.

