from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

from .views import CreateUserView,NickName

"""
ENDPOINT  user/
"""
urlpatterns = [
    path('register/', CreateUserView.as_view()), # 회원가입
    path('login/',obtain_jwt_token), #jwt 토큰 획득
    path('nickname/',NickName.as_view())
    # path('',)
]