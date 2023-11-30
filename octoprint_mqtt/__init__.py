# coding=utf-8
from __future__ import absolute_import

import json
import six
import time
from collections import deque

import octoprint.plugin

from octoprint.events import Events
from octoprint.util import dict_minimal_mergediff


class MqttPlugin(octoprint.plugin.SettingsPlugin,
                 octoprint.plugin.StartupPlugin,
                 octoprint.plugin.ShutdownPlugin,
                 octoprint.plugin.EventHandlerPlugin,
                 octoprint.plugin.ProgressPlugin,
                 octoprint.plugin.TemplatePlugin,
                 octoprint.plugin.AssetPlugin,
                 octoprint.printer.PrinterCallback):

    def __init__(self):
        self._mqtt = None
        self._mqtt_connected = False
        self._mqtt_reset_state = True

        self._mqtt_subscriptions = []

        self._mqtt_publish_queue = deque()
        self._mqtt_subscribe_queue = deque()

        self.lastTemp = {}

    def initialize(self):
        self._printer.register_callback(self)

        if self._settings.get(["broker", "url"]) is None:
            self._logger.error("No broker URL defined, MQTT plugin won't be able to work")
            return False

    ##~~ TemplatePlugin API

    def get_template_configs(self):
        return [
            dict(type="settings", name="MQTT")
        ]


    ##~~ PrinterCallback

    def on_printer_add_temperature(self, data):
        for key, value in data.items():
                
            dataset = dict(actual=value["actual"],
                            target=value["target"])
            directory_path = '/home/pi/OctoPrint/'
            file_name = 'example.txt'
            file_path = os.path.join(directory_path, file_name)
        
            with open(file_path, 'w') as file:
                file.write(str(dataset))


__plugin_name__ = "MQTT"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    plugin = MqttPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
