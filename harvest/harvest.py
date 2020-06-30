import time, requests, json, random

while True:
    # Generate a random number and assign it to "random"
    telemetry = random.randint(0,255)

    # Set the HTTP request header and payload content
    headers = {"Content-Type": "application/json"}
    payload = {"random": telemetry}

    # Send the HTTP request to Harvest via Unified Endpoint
    print("Sending data %s to Harvest via Unified Endpoint..." % (json.dumps(payload)))
    try:
        response = requests.post("http://unified.soracom.io", data=json.dumps(payload), headers=headers, timeout=5)
    except requests.exceptions.ConnectTimeout:
        print("Error: Connection timeout. Is the modem connected?")

    # Display HTTP request response
    if response.status_code == 201:
        print("Response 201: Success!")
    elif response.status_code == 400:
        print("Error 400: Harvest did not accept the data. Is Harvest enabled?")

    # Sleep for X seconds before looping again
    time.sleep(10)