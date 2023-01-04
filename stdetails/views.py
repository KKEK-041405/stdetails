from django.views.generic import TemplateView,FormView
from .models import Post
from .forms import Form

class Homepageview(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Post"] = Post.objects.all()
        return context

class Loginpageview(FormView):   
    template_name = "login.html"
    form_class = Form
    success_url = "home/"

    def form_valid(self, form):
        Post.objects.get()
        return super().form_valid(form)

    

# Create your views here.

