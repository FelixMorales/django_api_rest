from django.urls import path
from scrumboard.views.card_views import Cards, CardsPaged
from scrumboard.views.list_views import Lists, ListsPaged

urlpatterns = [
    ## cards
    path('cards', Cards.as_view(), name='Cards CRUD'),
    path('cards/paged', CardsPaged.as_view(), name='Cards Paged'),

    ## lists
    path('lists', Lists.as_view(), name='Lists CRUD'),
    path('lists/paged', ListsPaged.as_view(), name='Lists Paged'),
]