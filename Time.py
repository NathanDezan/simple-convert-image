from datetime import datetime

class Time:
    def getDateTime(self):
        data = datetime.now()
        return data.strftime("[%d/%m/%Y %H:%M:%S]")