import asyncio
import random

class call_service:

    def __init__(self):
        
        pass

    async def process_message(message: str) -> str:
        """
        Dummy service function that processes the incoming message
        and returns a response. Replace this with your actual service logic.
        """
        
        # Simulate some processing time
        await asyncio.sleep(0.5)
        
        # Dummy responses based on message content
        dummy_responses = [
            f"I received your message: '{message}'. Here's a thoughtful response!",
            f"Interesting point about '{message}'. Let me elaborate on that...",
            f"Thanks for saying '{message}'. Here's what I think about it:",
            f"Your message '{message}' reminds me of something important...",
            f"Processing '{message}'... Here's my analysis:"
        ]
        
        # Simple logic based on message content
        if "hello" in message.lower():
            return "Hello there! How can I help you today?"
        elif "how are you" in message.lower():
            return "I'm doing great! Thanks for asking. How are you?"
        elif "bye" in message.lower():
            return "Goodbye! It was nice chatting with you!"
        elif "weather" in message.lower():
            return "I'm sorry, I don't have access to real-time weather data, but it's always sunny in the code!"
        else:
            # Return a random dummy response
            return random.choice(dummy_responses)


        