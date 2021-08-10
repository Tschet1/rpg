#!/usr/bin/env python3

import json
from channels.generic.websocket import WebsocketConsumer
from objects.person import load_person_with_name

class CharaktersheetConsumer(WebsocketConsumer):
    def connect(self):
        self.charakter = load_person_with_name(self.scope["url_route"]["kwargs"]["id"])
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        m_json = json.loads(text_data)

        try:
            if "increase" in m_json:
                att = m_json["increase"]
                print("Increase " + att)

                self.charakter.sheet.attributes[att].increase_value()
                self.charakter.store_to_file()

                self.send(text_data=json.dumps({
                    'att': att,
                    'value': self.charakter.sheet.attributes[att].value
                }))
            elif "decrease" in m_json:
                att = m_json["decrease"]
                print("Decrease" + att)

                self.charakter.sheet.attributes[att].decrease_value()
                self.charakter.store_to_file()

                self.send(text_data=json.dumps({
                    'att': att,
                    'value': self.charakter.sheet.attributes[att].value
                }))
            else:

                self.send(text_data=json.dumps({
                    'message': self.charakter.name
                }))
        except Exception as e:
            self.send(text_data=json.dumps({
                'error': str(e)
            }))
