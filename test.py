from extfstr import extract, ExtractException

format_string = "I bought {good} for {price} to {what} at {where}."
sentence = "I bought bread for 5 dollars to eat at 711."

try:
    result = extract(format_string, sentence)
    print('result:', result)
except ExtractException as e:
    print('failed:', e)
