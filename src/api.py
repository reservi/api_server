from rest_framework import routers
from src.user.user_viewset import UserRegisterViewset

router = routers.DefaultRouter()
router.register(r'register', UserRegisterViewset)