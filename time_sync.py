import ntplib                                                     # 타임 서버...(pip install ntplib)

from dateutil import tz                                           # UTC → GMT 변경...
from datetime import datetime
from numpy import double
from numpy.lib.function_base import gradient
import win32api

import time
from time import ctime, localtime

countnum = 0        # 몇번만에 동기화가 되었는지 카운터 해주는 변수, 또한 하단부 while문을 정지 시켜주는 역할도 함.

def time_sync(setTime=0.01):    # setTime : 시간 동기화의 오차를 정하는 변수. 설정 이상이면 다시 동기화 함.

    global countnum, localtime

    # timeserver = 'kr.pool.ntp.org'
    timeserver = 'time.windows.com'               # NTP Server Domain Or IP 

    client = ntplib.NTPClient()
    response = client.request(timeserver, version=3)
    # time.sleep(0.01)                              # NTP 서버 응답 대기시간... time.windows.com에서는 대기시간 없이 빠르게 동기화 되길래. 주석처리 함.
    ctime_ = ctime(response.tx_time)

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    utcTime = datetime.strptime(ctime_, '%a %b %d %H:%M:%S %Y')
    utcTime_ = utcTime.replace(tzinfo=to_zone)
    localTime = utcTime_.astimezone(from_zone)

    # if countnum == 0:
    #     print(response.offset)

    if abs(response.offset) >= setTime:     # 위 client.request(timeserver, version=3) 코드에서 표준시간을 받은 후 오차가 설정한 오차보다 큰지 비교. 크면 아래 코드 실행.
        win32api.SetSystemTime(localTime.year, localTime.month, localTime.weekday(), localTime.day, localTime.hour, localTime.minute, localTime.second, localTime.microsecond)
        countnum = countnum + 1
        # time_sync()                   # 처음엔 이 if문에서 다시 동기화 함수를 불렀는데, 그렇게되면, 함수 안에 함수, 또 함수 안에 함수 이렇게 계속 들어가게 된다고 생각되어, 주석처리함.
        return countnum                 # 함수안에 함수로 가지 않게 하기 위해서 함수를 탈출하고, 리턴값이 양수이므로 다시 while문을 통해 다시 동기화를 시도하게 됨.
    else:
        print("(시간 : ", localTime.hour,":", localTime.minute, ":", localTime.second, ")", "동기화 완료 : ", response.offset, "카운팅 : ", countnum)
        return 0    # 동기화가 되었으니, while문을 빠져나오기 위해서 0을 리턴시킴.

if __name__ == '__main__':  # 테스트 모드
    while True:             # 테스트를 위한 반복문
        countnum = 1
        while countnum:
            countnum = time_sync()
        time.sleep(0.5)     # 0.5초마다 동기화 상태를 체크할 수 있음.
else:                       # 모듈 실행부
    countnum = 1
    while countnum:
        countnum = time_sync()

