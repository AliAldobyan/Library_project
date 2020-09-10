from django.contrib import admin
from django.urls import path
from library import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('create/',views.create_book ,name='book-create'),
    path('', views.library_list, name='library-list'),
    path('<int:book_id>/',views.book_detail ,name='book-detail'),
    path('<int:book_id>/update/',views.update_book ,name='book-update'),
    path('<int:book_id>/delete/',views.delete_book ,name='book-delete'),

    path('create-membership/',views.create_membership ,name='create-membership'),
    path('signin/',views.signin ,name='signin'),
    path('signout/',views.signout ,name='signout'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
