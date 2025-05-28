API scripts in the webpage are not obfuscated, allowing users to reverse engineer the API. In this instance it is not particularly damaging, but in more complex applications this may allow important data to be revealed to users.

**Recreation Steps**
* Login to the Cookie Clicker application at https://christopher-corbishley-2025-05-27.cookieclickertechtest.airelogic.com/
* Create a new user
* Open browser developer tools
* Expand the script section of the Elements tab

**Expected Results**
* Script is obfuscated.

**Actual Results**
* Script is entirely visible to users. (see api-requests.png)