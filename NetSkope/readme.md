# NetSkope User Removal Automation

The Script helps in automating the user removal from NetSkope, I had a previous experience where the client wanted to remove alot of users and what they has was just a sheet containing users to remove, they were till now just doing 1 by 1, as they had to search confirm and then click delete/remove, it was a very tedious process and they reached out to me to help automate this, currently at the movement when this problem was addressed by me, there was no Bulk delete/remove or automation around this.
I created the above script to automate it


| Usage |
| --- |

The Script identifies the request make to delete 1 user and then it creates the similar and runs it in iteration, getting 1 user from the file and mking the same request

<br>

| Prerequisites |
| --- |

> Get the Auth Token and required fields to make the delete request
  1. Login to NetSkope
  2. Navigate to Users Section where you can delete user.
  3. While doing this open devtools - network tab, search for `deleteUserList`
  4. Delete 1 User and you will see the request in Network Tab
  5. Right Click the Request
  6. Copy(5th Option) - Copy as cURL (bash)
  7. Paste it in Notepad
  8. the Script requires major of the fields key from here

<br>

| Execution |
| --- |

> Follow the below steps to install the script and run it over email id for deletion

0. Go into a working dir
```
cd /usr/local/src/
mkdir netskope
cd netskope
```

1. Download the script from here: 
```
curl 'https://raw.githubusercontent.com/aashishrbhandari/AutomateIT/master/NetSkope/remove_users_template.py' -O
```

2. Paste all the Email ID to a file (using name netskope_users.txt
```
vim netskope_users.txt
```

> **Note** Commands <br> <br>
(copy the email from excel) <br>
i -> Get into Insert Mode <br>
SHIFT+INSERT -> Paste the content <br>
ESC -> Get out of Insert Mode and move to Command Mode <br>
:wq -> Write and Quit the file <br>


3. Run the script
(make sure python3 is available and greater than 3.6)
```
python3 remove_users_template.py
```


