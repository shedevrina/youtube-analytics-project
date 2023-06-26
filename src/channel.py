import os
import requests
import json
import pprint

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')
    print(os.getenv('YT_API_KEY'))
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        pp = pprint.PrettyPrinter(width=10)
        pp.pprint(channel)

