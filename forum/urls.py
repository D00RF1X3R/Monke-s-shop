from django.urls import path
from forum.views import ForumsView, SubForumsView, FloodView, ProductDiscussionView, ChatsView

app_name = 'forum'
urlpatterns = [
    path('', ForumsView.as_view(), name='forums'),
    path('<int:category_id>/', SubForumsView.as_view(), name='sub_forums'),
    path('<int:category_id>/<int:universe_id>/', ChatsView.as_view(), name='chats'),
    path('flood/<int:category_id>/<int:universe_id>/', FloodView.as_view(), name='flood'),
    path('discussion/<int:product_id>/', ProductDiscussionView.as_view(), name='product_discussion'),
]
