import requests, json
def emotion_detector(text_to_analyze):
    WATSON_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(WATSON_URL, headers=HEADERS, json=input_json)
    total_value = json.loads(response.text)
    emotion_dict = total_value["emotionPredictions"][0]["emotion"]
    HighValue = 0
    for i in emotion_dict:
        if emotion_dict[i] > HighValue:
            HighValue = emotion_dict[i]
            dominant_emotion = i
    emotion_dict['dominant_emotion'] = dominant_emotion
    if response.status_code == 200:
        return emotion_dict
    elif response.status_code == 400:
        return {
            "anger":None,
            "disgust":None,
            "fear":None,
            "joy":None,
            "sadness":None,

        }
    else:
        return {"error": "Failed to get response from Watson API"}
