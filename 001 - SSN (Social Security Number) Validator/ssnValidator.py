import re

def validateSsn(text: str):
    matchObj = re.search(
        "^((?!(000|666|9))\\d{3}-(?!(00))\\d{2}-(?!(0000))\\d{4})", text)
    trueValue = bool(matchObj)
    return trueValue
