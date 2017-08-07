import http.client, urllib.request, urllib.parse, urllib.error, base64, json

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
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

# Replace the three dots below with the URL of a JPEG image of a celebrity.
#with open("C:\Temp\Project\VisionAPI\input_images\IMG-20170801-WA0006.jpg", "rb") as image_file:
 #   encoded_image = base64.b64encode(image_file.read())
image_data = open("C:\Temp\Project\VisionAPI\input_images\IMG-20170801-WA0006.jpg", 'rb').read()
body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/1/12/Broadway_and_Times_Square_by_night.jpg'}"


# Execute the REST API call and get the response.
conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
conn.request("POST", "/vision/v1.0/analyze?%s" % params, image_data, headers)
response = conn.getresponse()
data = response.read().decode('utf-8')

# 'data' contains the JSON data. The following formats the JSON data for display.
parsed = json.loads(data)
print ("Response:")
print (json.dumps(parsed, sort_keys=True, indent=2))
conn.close()

