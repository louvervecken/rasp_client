import requests
import datetime
import time

while True
    alarm_config = requests.get('https://rasp-lou-server.appspot.com/alarm-config/get')
    if alarm_config.status_code == 200:
        if alarm_config.text == u'alarm_enabled = True'
            enable_alarm = True
        elif alarm_config.text == u'alarm_enabled = False'
            enable_alarm = False
        else:
            raise ValueError("Unrecognized reply when getting alarm_config: {}".format(alarm_config.text))
    else:
        raise IOError("Error getting alarm config, error code: {}".format(alarm_config.status_code))