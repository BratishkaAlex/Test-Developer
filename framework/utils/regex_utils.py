import re


def fetch_by_regex_group(pattern: str, string: str, group_number: int) -> str:
    return re.search(pattern, string).group(group_number)
