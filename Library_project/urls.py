from django.contrib import admin
from django.urls import path
from library import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/list/', views.library_list, name='library-list'),
    path('library/detail/<int:book_id>/',views.book_detail ,name='book-detail'),


    path('library/book/create/',views.create_book ,name='book-create'),
    path('library/book/update/<int:book_id>/',views.update_book ,name='book-update'),
    path('library/book/delete/<int:book_id>/',views.delete_book ,name='book-delete'),


    path('create-membership/',views.create_membership ,name='create-membership'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
