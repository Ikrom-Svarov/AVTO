from django.urls import path, include

from .views import IndexView, AvtoDetailView, DeleteAvtoView, AvtoUpdateViews


urlpatterns = [ 
    path('',IndexView.as_view(), name='index'), 
    path('<int:avto_id>/', AvtoDetailView.as_view(), name='avto'),
    path('<int:avto_id>/delete', DeleteAvtoView.as_view(), name='delete'),
    path('<int:avto_id>/update/', AvtoUpdateViews.as_view(), name='update'),

    
    
    

]