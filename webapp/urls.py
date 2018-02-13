from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'email/', views.createEmailPage, name='createEmailPage'),
    url(r'^$', views.createEmailPage, name='createEmailPage'),
]