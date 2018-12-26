# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from mailbox import Message

from bothub_client.bot import BaseBot
from bothub_client.decorators import channel

from bothub.movie import BoxOffice


class Bot(BaseBot):
    def handle_message(self, event, context):
        message = event.get('content')
        if message == '영화순위':
            self.send_box_office(event)

    def send_box_office(self, event):
        data = self.get_project_data()
        api_key = data.get('box_office_api_key')
        box_office = BoxOffice(api_key)
        movies = box_office.simplify(box_office.get_movies())
        rank_message = ', '.join(['{}. {}'.format(m['rank'], m['name']) for m in movies])
        response = '요즘 볼만한 영화들의 순위입니다\n{}'.format(rank_message)

        message = Message(event).set_text(response) \
            .add_quick_reply('영화순위') \
            .add_quick_reply('근처 상영관 찾기')
        self.send_message(message)


