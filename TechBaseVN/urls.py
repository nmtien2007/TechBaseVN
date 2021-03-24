"""TechBaseVN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from TechBaseVN.views import login_api, admin_api

urlpatterns = [
    url(r'^login$', login_api.login),

    url(r'^admin/create_user$', admin_api.create_user),
    url(r'^admin/create_group$', admin_api.create_group),
    url(r'^admin/create_team$', admin_api.create_team),
    url(r'^admin/get_user_ids$', admin_api.get_user_ids),
    url(r'^admin/get_user_infos$', admin_api.get_user_infos),
    url(r'^admin/set_user_mapping_group$', admin_api.set_user_mapping_group),
    url(r'^admin/set_group_mapping_team$', admin_api.set_group_mapping_team),
    url(r'^admin/set_user_mapping_team$', admin_api.set_user_mapping_team),
    url(r'^admin/set_user_role$', admin_api.set_user_role),
]
