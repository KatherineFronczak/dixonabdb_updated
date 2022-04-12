#url paths from app templates folder 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.database, name='database'),
    path('antibody/<str:pk>',views.antibody, name='antibody'),
    path('antibody_Ind/<str:pk>',views.antibodyInd, name='antibodyInd'),
    path('add_entry/', views.addEntry, name="add"),
    path('add_entry2/', views.addEntry2, name="add2"),
    path('add_entry3/<str:pk>', views.addEntry3, name="add3"),
    path('update_entry/<str:pk>',views.updateEntry, name='update'),
    path('update_entry2/<str:pk>',views.updateEntry2, name='update2'),
    path('update_entry3/<str:pk>',views.updateEntry3, name='update3'),
    path('update_entry_arc/<str:pk>',views.updateEntryArc, name='updateArc'),
    path('remove_entry/<str:pk>',views.removeEntry, name='remove'),
    path('remove_entryInd/<str:pk>',views.removeEntryInd, name='removeInd'),
    path('search/',views.search, name='search'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('archive_entry/<str:pk>',views.archive, name='archive'),
    path('archives/',views.archives, name='archives'),
    path('antibody_archive/<str:pk>',views.antibodyArc, name='antibody_archive'),
    path('restore/<str:pk>',views.restore, name='restore'),
]
