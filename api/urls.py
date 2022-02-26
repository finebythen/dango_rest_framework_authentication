from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('routes/', views.api_routes, name="api-routes"),
    path('authors/all/', views.api_authors_all_view, name="api-author-all-view"),
    path('authors/detail/<int:pk>/', views.api_authors_detail_view, name="api-authors-detail-view"),
    path('books/all/', views.api_books_all_view, name="api-books-all-view"),

    path('api-token-auth/', obtain_auth_token),
]