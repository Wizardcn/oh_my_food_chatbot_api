def botnoi_payload(line_payloads: list):
    return {
        "response_type": "object",
        "line_payload": line_payloads
    }
    
    
def flex_message(flexdata):
    return {
        "type": "flex",
        "altText": "this is a flex message",
        "contents": flexdata
    }
    
def text_message(textList):
    textPayloads = []
    for text in textList:
      textPayloads.append({"type": "text","text": text})

    out = {
      "response_type": "object",
      "line_payload": textPayloads
    }

    return out