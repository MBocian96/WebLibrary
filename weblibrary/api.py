from rest_framework import routers

from library import api_views

router = routers.DefaultRouter()
router.register(r'books', api_views.BookViewset)
router.register(r'opinions', api_views.OpinionViewset)
