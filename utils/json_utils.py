import json

def safe_parse_json(text):
    try:
        return json.loads(text)
    except:
        print("⚠️ JSON parsing failed. Raw output:")
        print(text)
        return None