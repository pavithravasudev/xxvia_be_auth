"""xxvia_be_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path
from django.contrib import admin
from xxvia_be_auth_app import views

#URL Patterns to route List/Detail User based on endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.user_list),
    re_path('^user/(?P<id>[0-9]+)$', views.user_detail),
    re_path('^user/(?P<username>[0-9,a-z,A-Z]+)$', views.user_validation),
]
