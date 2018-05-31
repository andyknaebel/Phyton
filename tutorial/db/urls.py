from django.urls import path, include
from django.conf.urls import url
from .import views

# note you do not need a '/' in front of urls in 
# the main path, i.e 'data' will resolve to 
# '/db/data' in this particular programming 
# example. I also know / expects the "dataview"
# to be in the db/templates/db folder.

urlpatterns = [
    path('data', views.dataview),
    path('add', views.add_data),
    path('', views.dbview),
   
]
