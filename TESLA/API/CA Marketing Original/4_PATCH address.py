import requests

url = "https://addresses.wixapps.net/_api/addresses-web/v1/addresses/?id=dce5aada-cc7f-4ad2-b272-bc8c68fd9875"

payload = "{\r\n\t\"address\": {\r\n\t\t\"id\": \"dce5aada-cc7f-4ad2-b272-bc8c68fd9875\",\r\n\t\t\"fullName\": {" \
          "\r\n\t\t\t\"firstName\": \"Sergey\",\r\n\t\t\t\"lastName\": \"Efremov\"\r\n\t\t},\r\n\t\t\"company\": \"{{" \
          "company}}\",\r\n\t\t\"taxInfo\": {\r\n\t\t\t\"id\": null,\r\n\t\t\t\"type\": null\r\n\t\t}," \
          "\r\n\t\t\"addressLine1\": \"888 Gold Dr\",\r\n\t\t\"addressLine2\": \"Apt 777\",\r\n\t\t\"street\": {" \
          "\r\n\t\t\t\"name\": null,\r\n\t\t\t\"number\": null\r\n\t\t},\r\n\t\t\"city\": \"Bel Air\"," \
          "\r\n\t\t\"country\": \"US\",\r\n\t\t\"subdivision\": \"CA\",\r\n\t\t\"zipCode\": \"90210\"," \
          "\r\n\t\t\"phoneNumber\": \"888-888-8888\"\r\n\t},\r\n\t\"setAsDefault\": false,\r\n\t\"fieldMask\": {" \
          "\r\n\t\t\"paths\": [\"fullName.firstName\", \"fullName.lastName\", \"company\", \"addressLine1\", " \
          "\"addressLine2\", \"city\", \"country\", \"subdivision\", \"zipCode\", \"phoneNumber\", " \
          "\"setAsDefault\"]\r\n\t}\r\n} "
headers = {
    'Authorization': '6PoPcOXszUYsiMJFuwF3G12xtH7V2mWahaWpLv5bpas.eyJpbnN0YW5jZUlkIjoiZjQ2Y2Q1MDItZjcyZi00NGY3LTk2MzgtNWRhMWRlYjBiNGU3IiwiYXBwRGVmSWQiOiIxNTA1Yjc3NS1lODg1LWViMWItYjY2NS0xZTQ4NWQ5YmY5MGUiLCJtZXRhU2l0ZUlkIjoiMjhiNzkzZDYtNTQyNC00MDU4LTgwNDktMDI2YTRkYjAyODJmIiwic2lnbkRhdGUiOiIyMDIwLTEwLTMxVDAzOjE4OjQxLjk1M1oiLCJ1aWQiOiJhY2M4ZmM5ZS05MTBiLTRhMGQtOGEzZS00M2I5MDUyNDE3YTkiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjJhNGE5Y2YzLTExNmUtNDIyNS1hZmZhLWIzNTBlMGUyN2Y5NCIsImJpVG9rZW4iOiJkY2RiNDZkNC1hMzBiLTA0YWYtMTY3MS01ZmNiOTMwMDljYzgiLCJzaXRlT3duZXJJZCI6ImY5MTRmMTFjLWFhYjMtNDUyNy04ZDRlLWJhYjc2MjE0M2E2MCIsImV4cGlyYXRpb25EYXRlIjoiMjAyMC0xMC0zMVQwNzoxODo0MS45NTNaIiwiaGFzVXNlclJvbGUiOmZhbHNlfQ',
    'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
