import requests
import datetime
import time

from subprocess import Popen
from rasp_client.system_status import *

alarm_enabled = False



def enable_motion():
    return subprocess.Popen(['motion'])

    
while True
    # get alarm enabled config from server
    alarm_config = requests.get('https://rasp-lou-server.appspot.com/alarm-config/get')
    if alarm_config.status_code == 200:
        if alarm_config.text == u'alarm_enabled = True':
            if alarm_enabled is False:
                motion_process = enable_motion()
                alarm_enabled = True
        elif alarm_config.text == u'alarm_enabled = False':
            if alarm_enabled is True:
                motion_process.terminate()
                alarm_enabled = False
        else:
            raise ValueError("Unrecognized reply when getting alarm_config: {}".format(alarm_config.text))
    else:
        raise IOError("Error getting alarm config, error code: {}".format(alarm_config.status_code))
    
    cpu_temp = get_cpu_temperature()
    r = requests.post('https://rasp-lou-server.appspot.com/data-posting',
                      data={'cpu_temp': 44.3})
    time.sleep(10)
    
    
    