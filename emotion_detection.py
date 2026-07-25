import requests


def emotion_detector(text):

    url = "https://sn-watson-emotion.labs.coursera.org/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    response = requests.post(
        url,
        json={
            "raw_document":{
                "text":text
            }
        }
    )

    result=response.json()

    return result
