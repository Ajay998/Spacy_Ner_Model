import re

def clean_text(text):
    symbols = ["#","’","$", "?", "-", "—", "~", "“", "*", "^", ";", "'", ":", "<", ">", "[", "]", "{", "}", "!", "`", "(", ")",
               "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "|"]
    cleaned_text = ''
    segments = text.split(" ")
    for segment in segments:
        for y in segment:
            if y in symbols:
                segment = segment.replace(y, "")
        cleaned_text = cleaned_text + " " + segment
        cleaned_text = re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', cleaned_text)
    return cleaned_text