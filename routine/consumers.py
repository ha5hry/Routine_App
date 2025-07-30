from channels.generic.websocket import AsyncWebsocketConsumer
import json
class RoutineConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.routine = self.scope['url_route']['kwargs']['routine_slug']
        await self.channel_layer.group_add(
            self.routine, 
            self.channel_name
        )
        await self.accept()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.routine, self.channel_name)
    async def receive(self, text_data):
        # user = self.scope['user']
        data = "This user routine has started"
        message = data['message']
        await self.channel_layer.group_send(
            self.routine,
            {
                'type': 'routine_notification',
                'message': message
            }
        )
    async def routine_notification(self, event):
        await self.send(text_data=json.dumps({'message': event['message']}))

