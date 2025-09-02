import json
from typing import List
from fastapi import APIRouter,WebSocket,WebSocketDisconnect
from services.call_service import call_service

call_router=APIRouter()

# Store active connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                # Remove dead connections
                self.active_connections.remove(connection)


manager=ConnectionManager()
call_service=call_service()


@call_router.websocket("/chat")
async def chat_endpoint(websocket:WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data =await websocket.receive_text()
            message=json.loads(data)
            user_message = message.get('text','')


                # Process message through service function
            service_response = await call_service.process_message(user_message)
            
            # Send the service response back to the client
            response = {
                "type": "response",
                "original_message": user_message,
                "response": service_response
            }
            
            await manager.send_personal_message(
                json.dumps(response), 
                websocket
            )


    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A client disconnected")
