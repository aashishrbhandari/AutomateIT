import requests, sys
from pathlib import Path

"""
[Key Fields]

Data Fields to be retrived from the Request making deleteUser
Open DevTools when making the User Delete Request in NetSkope
search for the URL Endpoint: deleteUserList
You will see a request grab all the below values from that request

"""
test_tenant = "[To Be Added]"; # Example abc.eu.netskope.com // Tenant URL of NetSkope
test_netskope_req_id = "[To Be Added]"; # // Found in Headers when converted to Python: Key: Netskope-req-id
test_token = "[To Be Added]"; # // Foud in json_data Key: token
test_email = "[Not Required since File as Input is used]";
ci_session_cookie = "[To Be Added]"; # // Foud in Cookies: Key `ci_session` -> value

# Data Points 
netskope_tenant = f"{test_tenant}" # Get this from the NetSkope Dashboard URL
netskope_deleteuser_endpoint = "/settings/users/deleteUserList"


## ---- Authorization Data Starts ---- Get this from Identifying the URL making the Delete User(Email) Call
cookies = {
    'ci_session': f'{ci_session_cookie}',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Netskope-req-id': f'{test_netskope_req_id}',
    'Origin': f'https://{test_tenant}',
    'Pragma': 'no-cache',
    'Referer': f'https://{test_tenant}/ns',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

## ---- Authorization Data Ends ----

## --- The JSON till the time i used NetSkope was as shows below --- 
json_data = {
    'emails': f'{test_email}',
    'token': f'{test_token}',
}

""" Function to Delete Single User/Email From NetSkope """
def delete_user(user_email):
    json_data["emails"] = user_email;
    response = requests.post(f'https://{netskope_tenant}/{netskope_deleteuser_endpoint}', cookies=cookies, headers=headers, json=json_data);
    resp_headers = response.headers
    if resp_headers["content-type"] and "json" in resp_headers["content-type"]:
        response_json = response.json()
        print(f"[+] Success: Reason: JSON Response \nActual Response: {response_json}")
    else:
        print(f"[-] Debug: Request Headers: {response.request.headers},\nRequest Body: {response.request.body}, \nResponse Headers: {resp_headers}, \nResponse Body:{response.text} \n")

if __name__ == "__main__":
    print ("[=>] Remove/Delete User Process Started.")
    if len(sys.argv) < 2:
        print(f"[-] Provide File with Email IDs in New Line")
    else:
        email_file = sys.argv[1]
        if Path(email_file).is_file():
            with open(email_file) as file_object:
                for counter, one_email in enumerate(file_object):
                    print(f"[{counter}]: Processing User/Email: {one_email}")
                    delete_user(one_email)
        else:
            print(f"[-] Given File Does not Exists... Kindly Check Path or Filename")
