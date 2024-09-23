from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library_view'),
    path('books/', views.book_list, name='book_list'),
    path('books/new/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('issue/', views.issue_book, name='issue_book'),
    path('return/<int:transaction_id>/', views.return_book, name='return_book'),
    path('search/', views.search_books, name='search_books'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('members/', views.member_list, name='member_list'),
    path('members/new/', views.member_create, name='member_create'),
    path('members/<int:pk>/edit/', views.member_update, name='member_update'),
    path('members/<int:pk>/delete/', views.member_delete, name='member_delete'),

]
