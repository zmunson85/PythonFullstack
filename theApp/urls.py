from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('registration', views.new_user),
    path('login', views.login),
    path('wall', views.wall),
    path('wall/logout', views.logout),
    path('post_message', views.message),
    path('comment/<int:message_id>', views.comment),
    path('comment_delete/<int:comment_id>', views.delete_comment),
    path('message_delete/<int:message_id>', views.delete_message),
]
