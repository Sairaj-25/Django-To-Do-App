from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("add_task/", views.add_task, name="add_task"),
    path("edit/<int:pk>/", views.edit_task, name="edit_task"),
    path("remove/<int:pk>/", views.remove_task, name="remove_task"),
    path("search/", views.search_task, name="search_task"),
]
