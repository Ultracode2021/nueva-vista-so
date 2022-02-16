from polls import views
from rest_framework import routers
from django.urls import re_path, include

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewset)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]