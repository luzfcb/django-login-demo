from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .forms import LoginForm

class Home(generic.TemplateView):
    template_name = 'home.html'

home = Home.as_view()

class Login(generic.FormView):
    template_name = "login.html"
    form_class    = LoginForm
    success_url   = reverse_lazy("index")

    def form_valid(self, form):
        login(self.request, form.login(self.request))
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.success_url 

login = Login.as_view()        
