"""cursotelmex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include


admin.autodiscover()

urlpatterns = [
    url( r'^login/$',auth_views.LoginView.as_view(template_name="movies/index.html"), name="login"),
    url( r'^login1/$',auth_views.LoginView.as_view(template_name="movies/index1.html"), name="login"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('movies.urls',namespace='movies')),
	url(r'api/v1/',include('movies.urls',namespace='apis') ),
	url('accounts/', include('allauth.urls')),
    path('', include('pwa.urls')),
]

urlpatterns += [
	url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework'))
]