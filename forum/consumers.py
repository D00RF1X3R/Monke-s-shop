import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404

from catalog.models import Product
from core.models import User, Category, Universe
from forum.models import FloodMessage, ProductMessage
from users.models import BuyHistory


class FloodConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.category_id = self.scope['url_route']['kwargs']['category_id']
        self.universe_id = self.scope['url_route']['kwargs']['universe_id']
        self.room_name = f'flood_{self.category_id}_{self.universe_id}'

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        if message == '':
            return

        username = data['username']
        category_id = data['category_id']
        universe_id = data['universe_id']

        await self.save_message(username, message, category_id, universe_id)

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'time': self.time
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        time = event['time']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'time': time
        }))

    @sync_to_async
    def save_message(self, username, message, category_id, universe_id):
        user = get_object_or_404(User, username=username)
        category = get_object_or_404(Category, id=category_id)
        universe = get_object_or_404(Universe, id=universe_id)

        flood_message = FloodMessage.objects.create(
            user=user,
            category=category,
            universe=universe,
            message=message
        )
        self.time = flood_message.time.strftime('%H:%M')


class ProductDiscussionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.product_id = self.scope['url_route']['kwargs']['product_id']
        self.room_name = f'product_{self.product_id}'

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        if message == '':
            return

        username = data['username']
        product_id = data['product_id']

        await self.save_message(username, message, product_id)
        await self.check_is_buyed(username, product_id)

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'is_buyed': self.is_buyed,
                'message_id': self.message_id,
                'time': self.time
            }
        )

    async def chat_message(self, event):

        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
            'is_buyed': event['is_buyed'],
            'message_id': event['message_id'],
            'time': event['time'],
        }))

    @sync_to_async
    def save_message(self, username, message, product_id):
        user = get_object_or_404(User, username=username)
        product = get_object_or_404(Product, id=product_id)

        msg = ProductMessage.objects.create(
            user=user,
            product=product,
            message=message
        )
        self.message_id = msg.id
        self.time = msg.time.strftime('%H:%M')

    @sync_to_async
    def check_is_buyed(self, username, product_id):
        user = get_object_or_404(User, username=username)
        product = get_object_or_404(Product, id=product_id)
        self.is_buyed = BuyHistory.objects.filter(customer=user, product=product).exists()
        self.is_buyed |= product.seller.id == user.id
