import requests
import json

import response as response

url = "https://addresses.wixapps.net/_api/addresses-web/v1/addresses"

payload = "{\r\n\t\"address\": {\r\n\t\t\"fullName\": {\r\n\t\t\t\"firstName\": \"Sergey\",\r\n\t\t\t\"lastName\": " \
          "\"Efremov\"\r\n\t\t},\r\n\t\t\"company\": \"\",\r\n\t\t\"taxInfo\": {\r\n\t\t\t\"id\": null," \
          "\r\n\t\t\t\"type\": null\r\n\t\t},\r\n\t\t\"addressLine1\": \"888 Gold Dr\",\r\n\t\t\"addressLine2\": " \
          "\"Apt 777\",\r\n\t\t\"street\": {\r\n\t\t\t\"name\": null,\r\n\t\t\t\"number\": null\r\n\t\t}," \
          "\r\n\t\t\"city\": \"Bel Air\",\r\n\t\t\"country\": \"US\",\r\n\t\t\"subdivision\": \"CA\"," \
          "\r\n\t\t\"zipCode\": \"90210\",\r\n\t\t\"phoneNumber\": \"888-888-8888\"\r\n\t},\r\n\t\"setAsDefault\": " \
          "true\r\n} "
headers = {
    'Content-Type': 'application/json',
    'Authorization': '6PoPcOXszUYsiMJFuwF3G12xtH7V2mWahaWpLv5bpas'
                     'RZkmpM2LqC_77nI4YMcYvvK4AMAWxeyabQMOZl3oXBc.eyJpbnN0YW5jZUlkIjoiZjQ2Y2Q1MDItZjcyZi00NGY3LTk2MzgtNWRhMWRlYjBiNGU3IiwiYXBwRGVmSWQiOiIxNTA1Yjc3NS1lODg1LWViMWItYjY2NS0xZTQ4NWQ5YmY5MGUiLCJtZXRhU2l0ZUlkIjoiMjhiNzkzZDYtNTQyNC00MDU4LTgwNDktMDI2YTRkYjAyODJmIiwic2lnbkRhdGUiOiIyMDIzLTA4LTE4VDE5OjA2OjM5LjA2OVoiLCJ1aWQiOiJlZmRhMzYyMy0xY2JmLTRlODMtODkxYi1iZTgxNTFmNTA1NWQiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImI4MmQwZmI2LWRjMGYtNDJjYy1iMjFhLWNiNzgwYzAzYmMxNiIsImJpVG9rZW4iOiJkY2RiNDZkNC1hMzBiLTA0YWYtMTY3MS01ZmNiOTMwMDljYzgiLCJzaXRlT3duZXJJZCI6ImY5MTRmMTFjLWFhYjMtNDUyNy04ZDRlLWJhYjc2MjE0M2E2MCIsImV4cGlyYXRpb25EYXRlIjoiMjAyMy0wOC0xOFQyMzowNjozOS4wNjlaIiwiaGFzVXNlclJvbGUiOmZhbHNlfQ'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
