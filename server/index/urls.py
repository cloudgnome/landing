from index.views import index,FeedbackView
from django.urls import path

urlpatterns = [
    path('',index),
    path('feedback/',FeedbackView.as_view())
]