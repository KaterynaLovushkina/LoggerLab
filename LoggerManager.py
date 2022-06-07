import re

class LoggerManager:
    @staticmethod
    def print_data_contains_regex(filename: str):
        regex = r'(21).+.+(php).+(HTTP).+'
        count = 0
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                find_regex = re.search(regex, line)
                if find_regex is not None:
                    print(find_regex.group())
                    count += 1
        print(f"Count of matches: {count}")
