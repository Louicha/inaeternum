"""inaeternum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from polls import views
from django.contrib.auth import views as auth_views
from polls.views import settings, settings2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('polls.urls')),
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^accounts/profile/$', settings.as_view(), name='settings'),
    url(r'^accounts/profile2/$', settings2.as_view(), name='settings2'),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
