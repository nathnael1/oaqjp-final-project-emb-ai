import requests
def emotion_detector(text_to_analyze):
    WATSON_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(WATSON_URL, headers=HEADERS, json=input_json)
    if response.status_code == 200:
        return response.json() 
    else:
        return {"error": "Failed to get response from Watson API"}
