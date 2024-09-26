"""
URL configuration for dora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('new_req',views.new_req,name="new_req"),
    path('approve_request/<int:rid>',views.approve_request,name="approve_request"),
     path('reject_request/<int:rid>',views.reject_request,name="reject_request"),
     path('search',views.search,name="search"),
    path('category',views.category,name="category"),
    path('save_cat',views.save_cat,name="save_cat"),
    path('new_password',views.new_password,name="new_password"),
    path('update_password',views.update_password,name="update_password"),
    path('cat_edit<int:cat_id>',views.cat_edit,name="cat_edit"),
    path('update_cat',views.update_cat,name="update_cat"),
    path('cat_delete<int:cat_id>',views.cat_delete,name="cat_delete"),    
    path('pack_view',views.pack_view,name="pack_view"),
    path('p_edit<int:package_id>',views.p_edit,name="p_edit"),
     path('p_delete<int:package_id>',views.p_delete,name="p_delete"),
    path('save_pack',views.save_pack,name="save_pack"),    
    path('update_pack',views.update_pack,name="update_pack"),
    path('paid',views.paid,name="paid"),
    path('free',views.free,name="free"),
    path('portfolio',views.portfolio,name="portfolio"),
    path('search_port',views.search_port,name="search_port"),
    path('p_reject_request<int:portfolio_id>',views.p_reject_request,name="p_reject_request"),
    path('p_approve_request<int:portfolio_id>',views.p_approve_request,name="p_approve_request"),
    path('details/<int:portfolio_id>',views.details,name="details"),
    path('dashboard',views.dashboard,name="dashboard"),    
    path('cl/',views.cl,name="cl"),
    path('gallery_port<int:pi>',views.gallery_port,name="gallery_port"),
    path('reject_image',views.reject_image,name="reject_image"),
    path('approve_image<int:gid>',views.approve_image,name="approve_image"),
     path('logout/',views.logout,name="logout"),
    path('reason<int:gid>',views.reason,name="reason")

]   
