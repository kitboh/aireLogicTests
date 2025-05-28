class Config:
    """
    A class to store configuration variables accessible by test steps.
    """
    base_url = "https://christopher-corbishley-2025-05-27.cookieclickertechtest.airelogic.com/"
    driver_type = "firefox"
    user_name = "Test_User"
    password = "Unused"

    def __init__(self):
        # If needed you could add code in here to pull usernames/password from a secure store, or from a config file/env vars
        return None
