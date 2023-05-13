from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import  Car
from .forms import  CarForm, RegisterForm, LoginForm

from django.views.generic import ListView,   View, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.views import LoginView

# Create your views here.




class IndexView(ListView):
    model = Car
    template_name = 'avto/index.html'
    context_object_name = 'avto'

    

class MyAvtoView(ListView):
    model = Car
    template_name = 'avto/index.html'
    context_object_name = 'avto'

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)


class AvtoDetailView(DetailView):
    model = Car
    template_name  = 'avto/avto.html'
    context_object_name  = 'avto' 
    pk_url_kwarg = 'avto_id' 

    



class DeleteAvtoView(DeleteView):
    model = Car
    template_name = 'avto/delete.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'avto_id'
    login_url = reverse_lazy('login')

    


class AvtoCreateView(LoginRequiredMixin,CreateView):
    form_class = CarForm
    template_name = 'avto/create.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    

    
    
class AvtoUpdateViews(UpdateView):
    model = Car
    template_name = 'avto/update.html'  
    success_url = reverse_lazy('index')
    fields = ['make', 'model', 'year', 'engine_volume', 'color', 'image', 'body_type', 'mileage', 'price']
    pk_url_kwarg = 'avto_id'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    

class RegisterView(View):
    form_class = RegisterForm
    template_name = 'avto/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    
    
class AuthLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'avto/login.html'

    def get_success_url(self):
        return reverse_lazy('index')
    

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')