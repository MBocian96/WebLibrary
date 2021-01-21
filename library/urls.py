from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from library import views, class_based_views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('class_based/books/', class_based_views.BookList.as_view()),
    path('class_based/books/<int:pk>/', class_based_views.BookDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
