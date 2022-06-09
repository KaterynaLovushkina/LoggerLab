import re
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(name)s:  %(message)s)")

file_handler = logging.FileHandler('regex.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class LoggerManager:
    @staticmethod
    def print_count_of_data_contains_regex(filename: str):
        regex = r'(21).+.+(php).+(HTTP).+'
        count = 0
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                find_regex = re.search(regex, line)
                if find_regex :
                    logger.info(find_regex.group())
                    count += 1
        print(f"Count of matches: {count}")
