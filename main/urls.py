from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_event/', views.add_event, name='add_event'),
    url(r'^add_achievement/',views.add_achievement,name='add_achievement'),
    url(r'^add_news/',views.add_news,name='add_news'),
    url(r'^change_director_desk/',views.cddesk,name='cddesk'),
    url(r'^add_initiative/', views.add_initiative, name='add_initiative'),
]
