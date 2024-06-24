from django.urls import path

from forum.consumers import FloodConsumer, ProductDiscussionConsumer

websocket_urlpatterns = [
    path('ws/flood/<int:category_id>/<int:universe_id>/', FloodConsumer.as_asgi()),
    path('ws/product/<int:product_id>/', ProductDiscussionConsumer.as_asgi()),
]
