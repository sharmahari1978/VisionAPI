#import json
import requests
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

def call_vision_api(image_filename, api_keys):
     # Replace the subscription_key string value with your valid subscription key.
    #subscription_key = api_keys['microsoft']
    subscription_key = '87b79cae46fb4ecfb53ea7bf59bcedde'
    uri_base = 'westcentralus.api.cognitive.microsoft.com'

    headers = {
        # Request headers.
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = urllib.parse.urlencode({
        # Request parameters. All of them are optional.
        'visualFeatures': 'Categories,Tags,Description,Faces,ImageType,Color,Adult',
        'language': 'en',
    })
    #post_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=Categories,Tags,Description,Faces,ImageType,Color,Adult&subscription-key=" + api_key
    image_data = open(image_filename, 'rb').read()
    #result = requests.post(post_url, data=image_data, headers={'Content-Type': 'application/octet-stream'})  # Execute the REST API call and get the response.
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, image_data, headers)
    result = conn.getresponse()
    data = result.read().decode('utf-8')


    return json.loads(data)



def get_standardized_result(api_result):
    output = {
        'tags' : [],
        'captions' : [],

    }

    for tag_data in api_result['tags']:
        output['tags'].append((tag_data['name'], tag_data['confidence']))

    for caption in api_result['description']['captions']:
        output['captions'].append((caption['text'], caption['confidence']))

    return output
