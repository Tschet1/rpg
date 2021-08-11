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
                name = m_json["increase"]
                if name in self.charakter.sheet.attributes:
                    self.charakter.sheet.attributes[name].increase_value()
                    val = self.charakter.sheet.attributes[name]
                elif name in self.charakter.sheet.abilities:
                    self.charakter.sheet.abilities[name].increase_value()
                    val = self.charakter.sheet.abilities[name]
                else:
                    return

                print("Increase " + name)
                self.charakter.store_to_file()

                self.send(text_data=json.dumps({
                    'att': name,
                    'value': val.value
                }))
            elif "decrease" in m_json:
                name = m_json["decrease"]
                if name in self.charakter.sheet.attributes:
                    self.charakter.sheet.attributes[name].decrease_value()
                    val = self.charakter.sheet.attributes[name]
                elif name in self.charakter.sheet.abilities:
                    self.charakter.sheet.abilities[name].decrease_value()
                    val = self.charakter.sheet.abilities[name]
                else:
                    return

                print("Decrease" + name)
                self.charakter.store_to_file()

                self.send(text_data=json.dumps({
                    'att': name,
                    'value': val.value
                }))
            else:

                self.send(text_data=json.dumps({
                    'message': self.charakter.name
                }))
        except Exception as e:
            self.send(text_data=json.dumps({
                'error': str(e)
            }))
