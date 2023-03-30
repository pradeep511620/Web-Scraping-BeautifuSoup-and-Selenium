import requests
from typing import TextIO
api_key = '2526b018-e6cb-488c-b074-0c764f168b29'
url = 'https://www.webpagetest.org/runtest.php'

# Set the parameters for the test
params = {
    'url': 'https://www.raptorsupplies.com',
    'f': 'json',
    'k': api_key,
    'runs': 1,
    'video': 0,
    'location': 'ec2-eu-west-1:Chrome',  # Update the location parameter
    'fvonly': 1,
    'noopt': 1,
    'noimages': 1
}

# Make the API request
response = requests.get(url, params=params)

# Parse the JSON response
try:
    test_id = response.json()['data']['testId']
except KeyError:
    print('Error: Failed to retrieve test ID.')
    # print(response.json())
    exit()

# Check the test status
status_url = f'https://www.webpagetest.org/testStatus.php?f=json&test={test_id}&k={api_key}'
# print(status_url)
while True:
    status_response = requests.get(status_url)
    status_data = status_response.json()
    if status_data['statusCode'] == 200:
        break

# Get the TTFB value
results_url = f'https://www.webpagetest.org/jsonResult.php?test={test_id}&k={api_key}'
results_response = requests.get(results_url)
results_data = results_response.json()

try:
    ttfb = results_data['data']['median']['response']['TTFB']
    print(f'Time to First Byte: {ttfb} ms')
except KeyError:
    print('Error: Failed to retrieve TTFB data.')
    # print(results_data)
    save_details: TextIO = open("web_page_test_result.txt", "a+", encoding="utf-8")
    save_details.write(str(results_data))
    save_details.close()
    print("\n**Record stored into txt file1.**")
    exit()
