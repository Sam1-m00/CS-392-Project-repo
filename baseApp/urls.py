from django.urls import path, include
from . import views
from .views import discussionpageView, discussionDetailsView, AddPostView

urlpatterns = [
    path('', views.home, name='home'),
    path('FQA/', views.FQA, name='FQA'),
    path('CoursesList/', views.CoursesList, name='CoursesList'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('discussionpage', discussionpageView.as_view(), name="discussionpageView"),
    path('discussion_Detail/<int:pk>', discussionDetailsView.as_view(), name="discussion_Detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
]
