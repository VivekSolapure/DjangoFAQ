from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faqs.views import FAQViewSet

router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line
    path('api/', include(router.urls)),
]