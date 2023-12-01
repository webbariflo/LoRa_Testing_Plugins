# coding=utf-8
from __future__ import absolute_import

import json
import six
import time
from collections import deque
import os
import octoprint.plugin

from octoprint.events import Events
from octoprint.util import dict_minimal_mergediff


class MqttPlugin(octoprint.printer.PrinterCallback):
    ##~~ PrinterCallback

    def on_printer_add_temperature(self, data):
        for key, value in data.items():
            dataset = json.dumps({"actual": value["actual"], "target": value["target"]})
            directory_path = '/home/pi/OctoPrint/'
            file_name = 'example.txt'
            file_path = os.path.join(directory_path, file_name)
    
            with open(file_path, 'a') as file:
                file.write(str(dataset) + '\n')
    
            self._logger.info(f"Temperature data written: {dataset}")


__plugin_name__ = "LoRa_Testing_Plugins"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = MqttPlugin()
