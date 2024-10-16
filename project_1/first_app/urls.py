from django.urls import path
# from views import contact
from . import views

urlpatterns = [
    # path('contact/', contact),
    # path("", views.course),
    path("course/", views.courses),
    path("about/", views.about),
    path("", views.home),

]