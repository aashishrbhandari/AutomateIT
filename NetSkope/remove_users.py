import requests, sys
from pathlib import Path

# test_data
# /* cSpell:disable */

test_tenant = "91streets.eu.goskope.com";
test_netskope_req_id = "69f1spo1w9jl8hdnqil";
test_token = "M2UxOTViZmVkMzUzMTM0YjNjNGE0ZjU1OGY0NmQzZWU5MXN0cmVldHMuZXUuZ29za29wZS5jb20=";
test_email = "ash.raj.rawal+test4@gmail.com";

# Data Points 
netskope_tenant = f"{test_tenant}" # Get this from the NetSkope Dashboard URL
netskope_deleteuser_endpoint = "/settings/users/deleteUserList"


## ---- Authorization Data Starts ---- Get this from Identifying the URL making the Delete User(Email) Call
cookies = {
    'ci_session': 'bnNtZW1jYWNoZWQHzfHJaAqtcL5H9ojHUcwsFtOT7HXqPIp',
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

json_data = {
    'emails': f'{test_email}',
    'token': f'{test_token}',
}

## ---- Authorization Data Ends ----


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