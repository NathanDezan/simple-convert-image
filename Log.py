from simple_chalk import chalk
from Time import Time

class Log:
    def info(self, message, name_method):
        time = Time()
        str_time = time.getDateTime()

        print(chalk.green(f"{str_time} - INFO: {message} ({name_method})"))
    
    def error(self, message, name_method):
        time = Time()
        str_time = time.getDateTime()

        print(chalk.red(f"{str_time} - INFO: {message} ({name_method})"))