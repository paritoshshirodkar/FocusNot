import json
image_url = []
with open('db.json') as f:
    data = json.loads(f.read())
    for i in range(1,3226):
        data2 = data["_default"][str(i)]
        image_url.append(data2["media"])

with open('image_urls.txt', 'w') as f2:
    for item in image_url:
        f2.write("%s\n" % item)