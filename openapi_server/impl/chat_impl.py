# coding: utf-8
from fastapi import HTTPException
from openapi_server.apis.chat_api_base import BaseChatApi
from openapi_server.models.chat import Chat


class ChatImpl(BaseChatApi):
    team = None  # This will be assigned the autogen team in the app setup

    async def chat(self) -> Chat:
        """
        Handle chat requests using the autogen team to generate id, title, and content.

        Returns:
            Chat: The response object defined by the OpenAPI schema.
        """
        if not self.team:
            raise HTTPException(status_code=500, detail="Team is not initialized.")

        try:
            # Extract JSON values from the primary agent's content in the messages
            def extract_json_content(task_result):
                # Find the first message from the primary agent
                for message in task_result.messages:
                    if message.source == "primary" and message.content:
                        return message.content.strip()
                raise ValueError("No valid primary agent message found in the result.")

            # Generate unique ID
            id_result = await self.team.run(
                task="Simply generate a unique ID for the chat that will be used as a value for a JSON key with no other output."
            )
            id_content = extract_json_content(id_result)
            print(f"Generated ID: {id_content}")

            # Generate title
            title_result = await self.team.run(
                task="Simply generate a title based on construction work for the chat that will be used as a value for a JSON key with no other output."
            )
            title_content = extract_json_content(title_result)
            print(f"Generated Title: {title_content}")

            # Generate content
            content_result = await self.team.run(
                task="Generate the main content based on construction work for the chat in 25 words or less."
            )
            content_content = extract_json_content(content_result)
            print(f"Generated Content: {content_content}")

            # Parse JSON-like strings into actual values (assuming the format is predictable)
            import json

            chat_id = json.loads(id_content)["chat_id"]
            chat_title = json.loads(title_content)["chat_title"]
            chat_content = json.loads(content_content)["chat_content"]

            # Build and return the Chat model
            return Chat(
                id=chat_id,
                title=chat_title,
                content=chat_content
            )
        except Exception as e:
            # Handle and log errors gracefully
            print(f"Error: {e}")
            raise HTTPException(status_code=500, detail=str(e))
