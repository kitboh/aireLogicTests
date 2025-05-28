There is no text limit for the amount of characters a new users username can take up

**Recreation Steps**
* Login to the Cookie Clicker application at https://christopher-corbishley-2025-05-27.cookieclickertechtest.airelogic.com/
* Create a new user with a > 5000 character username (You can generate one at https://www.lipsum.com)

**Expected Results**
* Text box alerts user to username character limits

**Actual Results**
* User account is created and a 502 Bad Gateway error is returned (see textlimits-1.png)

**Further Issues**
Once the user goes to the homepage, they can then click on this newly created user.
Doing so results in a 414, Request-URI Too Large error (see textlimits-2.png)