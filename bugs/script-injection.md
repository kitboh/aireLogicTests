Users can inject scripts and embeds into the name field and page will run them.

**Recreation Steps**
* Login to the Cookie Clicker application at https://christopher-corbishley-2025-05-27.cookieclickertechtest.airelogic.com/
* Create a new user with the name ```<script>alert(0)</script>```


**Expected Results**
* Username will be cleaned, and page will continue to load
* **OR** an error message will be displayed saying the name contains invalid characters

**Actual Results**
* User will be taken to the next page which will fail to load (see script-injection-1.png)
* Returning to the home page will always show an alert with the message 0 (see script-injection-2.png)

**Note**
* Users can add a lot of damaging things in here.
If a user, for example enters:
```<font size="128">Kit</font>```
All text on the page will display in a very large size.

* This could potentially lead to more damaging vulnerabilities, and I stopped testing to prevent damaging anything