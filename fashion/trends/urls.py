from django.urls import path, re_path

from trends.views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<int:post_id>/', showpost, name='post'),

]


