import requests
import datetime
import time

from subprocess import Popen
from system_status import *
from temperature import TempSensorController

def enable_motion():
    return Popen(['motion'])

    
def run():
    sleep_between_uploads = 10
    sleep_between_temp_readouts = 7
    alarm_enabled = False
    temp_room = TempSensorController("28-000004cddb4f", sleep_between_temp_readouts)
    temp_heating = TempSensorController("28-28-000004cdfb9f", sleep_between_temp_readouts)
    temp_room.start()
    temp_heating.start()
    while True:
        # get alarm enabled config from server
        alarm_config = requests.get('https://rasp-lou-server.appspot.com/alarm-config/get', verify=False)
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
        ram_perc = get_ram_usage()[3]
        free_storage = round(get_storage_usage()[2], 3)
        r = requests.post('https://rasp-lou-server.appspot.com/data-posting',
                          data={'cpu_temp': cpu_temp,
                                'room_temp': temp_room.temperature.C,
                                'heating_temp': temp_heating.temperature.C,
                                'ram_perc': ram_perc,
                                'free_storage': free_storage},
                          verify=False)
        print('{}-{}'.format(cpu_temp, r))
        time.sleep(sleep_between_uploads)
    
    
    
