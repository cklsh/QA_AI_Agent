import json
import re

def clean_json_text(text):
    # remove non-ASCII characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    # remove weird lines (like garbage tokens)
    text = re.sub(r',\s*}', '}', text)
    text = re.sub(r',\s*]', ']', text)

    return text


def safe_parse_json(text):
    try:
        return json.loads(text)
    except:
        cleaned = clean_json_text(text)
        try:
            return json.loads(cleaned)
        except Exception as e:
            print("⚠️ JSON parse failed after cleaning:", e)
            print("RAW OUTPUT:", text)
            return None