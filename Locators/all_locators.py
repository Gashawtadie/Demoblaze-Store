class LocatoresBlaze:
    HOME_PAGE = "https://www.demoblaze.com/index.html"
    LOGIN_PATH = "//a[@id='login2']"
    USERNAME_FIELD = "loginusername"
    PASSWORD_FIELD = "loginpassword"
    LOGIN_BTN = "//button[contains(text(),'Log in')]"
    ASSERTION_NAME = "//a[@id='nameofuser']"

    #signup
    SIGNUP = "//a[@id='signin2']"
    SIGNUP_USERNAME = "//input[@id='sign-username']"
    SIGNUP_PASSWORD = "//input[@id='sign-password']"
    SIGNUP_BTN = "//button[contains(text(),'Sign up')]"

    # home
    MAIN_HOME = "//body/nav[1]/div[1]/div[1]/ul[1]/li[1]/a[1]"
    CATEGORY = "//a[@id='cat']"
    LAPTOPS_PATH = "//a[contains(text(),'Laptops')]"
    MACBOOK_PATH = "/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[6]/div[1]/a[1]/img[1]"
    product_title = "//h2[contains(text(),'MacBook Pro')]"
    ADD_CART = "//a[contains(text(),'Add to cart')]"
    MACBOOK_NAME = "//h2[contains(text(),'MacBook air')]"
    PRICE_MAC = "//body/div[5]/div[1]/div[2]/h3[1]"

    PHONE_PATH = "//a[contains(text(),'Phones')]"
    IPHONE_PATH = "//a[contains(text(),'Iphone 6 32gb')]"
    IPHONE_PRICE = "//body/div[5]/div[1]/div[2]/h3[1]"

    HTC_PHONE_PATH = "//a[contains(text(),'HTC One M9')]"
    HTC_NAME_PATH = "//h2[contains(text(),'HTC One M9')]"
    HTC_PRICE = "//body/div[5]/div[1]/div[2]/h3[1]"

    MACBOOK_PRO = "//a[contains(text(),'MacBook Pro')]"
    MAC_NAME = "//h2[contains(text(),'MacBook Pro')]"
    MAC_PRICE = "//body/div[5]/div[1]/div[2]/h3[1]"

    MONITOR = "//a[contains(text(),'Monitors')]"
    APPLE_MONITOR = "//a[contains(text(),'Apple monitor 24')]"
    APPLE_NAME_PATH = "//h2[contains(text(),'Apple monitor 24')]"
    APPLE_PRICE_PATH = "//body/div[5]/div[1]/div[2]/h3[1]"

    TOTAL_pro = "//h2[contains(text(),'Total')]"
    TOTAL_PRICES = "//h3[@id='totalp']"
    MAIN_TOTAL = "//body/div[@id='page-wrapper']/div[1]/div[2]"
    TITLE = "//body/div[@id='page-wrapper']/div[1]/div[1]/div[1]/table[1]"

    SONY_XPERIA_PATH = "//a[contains(text(),'Sony xperia z5')]"
    SONY_VAIO = "//a[contains(text(),'Sony vaio i7')]"


    # cart
    CART_PATH = "//a[contains(text(),'Cart')]"
    PLACE_OREDR = "//button[contains(text(),'Place Order')]"
    NAME = "//input[@id='name']"
    COUNTRY = "//input[@id='country']"
    CITY = "//input[@id='city']"
    CREDIT_CARD = "//input[@id='card']"
    MONTH = "//input[@id='card']"
    YEAR = "//input[@id='year']"
    PURCHASE = "//button[contains(text(),'Purchase')]"
    FINAL_PURCHASE = "//h2[contains(text(),'Thank you for your purchase!')]"
    OK = "//button[contains(text(),'OK')]"
    DELETE_PRODUCT = "//a[contains(text(),'Delete')]"
    TAX_PATH ="//small[contains(text(),'*includes tax')]"
    THANKYOU_PATH = "//h2[contains(text(),'Thank you for your purchase!')]"
    CLOSE = "//body/div[@id='orderModal']/div[1]/div[1]/div[3]/button[1]"
    X_PLACE_ORDER = "//body/div[@id='orderModal']/div[1]/div[1]/div[1]/button[1]/span[1]"


    # contact
    CONTACT_US = "//a[contains(text(),'Contact')]"
    CONTACT_EMAIL = "recipient-email"
    CONTACT_NAME = "recipient-name"
    MESSAGE = "message-text"
    SEND_MESSAGE = "//button[contains(text(),'Send message')]"

    # about us
    ABOUT = "//a[contains(text(),'About us')]"
    PLAY_BTN = "//body/div[@id='videoModal']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/button[1]"
    CLOSE_BTN = "//body/div[@id='videoModal']/div[1]/div[1]/div[3]/button[1]"
    X_CLOSE = "//body/div[@id='videoModal']/div[1]/div[1]/div[1]/button[1]/span[1]"

    # logout
    LOGOUT = "//a[@id='logout2']"

    # API server
    SIGNIN_URL = "https://api.demoblaze.com/entries"
    SIGNIN_DATA = {"token":"Z2FzaHUxNjc1NTE4"}
    SIGNUP_URL = "https://api.demoblaze.com/signup"
    DATA_SIGNUP = {"username":"gashu","password":"MTIzNDU2"}

    LOGOUT_URL = "https://www.demoblaze.com/config.json"
    LOGOUT_DATA = "{API_URL: 'https://api.demoblaze.com', HLS_URL: 'https://hls.demoblaze.com'}"
    HOME_API_URL = "https://api.demoblaze.com/entries"
    SIGNUP_API_URL = "https://www.demoblaze.com/config.json"
    SIGNUP_BTN = "https://api.demoblaze.com/entries"
    ABOUT_API_URL = "https://www.demoblaze.com/config.json"
    CART_API_URL = " https://api.demoblaze.com/viewcart"
    PAYLOAD = "{username: 'beast', password: 'MTIzNDU2'}"
    CHECK_CART = "https://api.demoblaze.com/check"
    CHECK_API = "{token: 'Z2FzaHUxNjc2MjI4'}"


    #others
    NEX_PICTURES = "//body/nav[@id='narvbarx']/div[@id='contcar']/div[@id='carouselExampleIndicators']/a[2]/span[1]"
    BACK_PICTURES = "//body/nav[@id='narvbarx']/div[@id='contcar']/div[@id='carouselExampleIndicators']/a[1]/span[1]"
    CONTACT_CLOSE = "//body/div[@id='exampleModal']/div[1]/div[1]/div[3]/button[1]"
    CONTACT_X_close = "//body/div[@id='exampleModal']/div[1]/div[1]/div[1]/button[1]/span[1]"
    PLACEORDER_CLOSE = "//body/div[@id='orderModal']/div[1]/div[1]/div[3]/button[1]"
    PLACE_ORDER_X_CLOSE = "//body/div[@id='orderModal']/div[1]/div[1]/div[1]/button[1]/span[1]"
    LOGIN_CLOSE = "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[1]"
    LOGIN_X_CLOSE = "//body/div[@id='logInModal']/div[1]/div[1]/div[1]/button[1]/span[1]"
    SIGNUP_CLOSE_BTN = "//body/div[@id='signInModal']/div[1]/div[1]/div[3]/button[1]"
    SIGNUP_X_CLOSE_BTN= "//body/div[@id='signInModal']/div[1]/div[1]/div[1]/button[1]/span[1]"
    #scroll
    NEXT_SCROLL = "//button[@id='next2']"
    PREVIOUS_SCROLL = "//button[@id='prev2']"
    # NEXT = "//body/nav[@id='narvbarx']/div[@id='contcar']/div[@id='carouselExampleIndicators']/ol[1]/li[1]"
    # BACK = "//body/nav[@id='narvbarx']/div[@id='contcar']/div[@id='carouselExampleIndicators']/ol[1]/li[2]"

    EDGE_SIGN_UP = "signin2"
    EDGE_USERNAME_FIELD = "sign-username"
    EDGE_PASSWORD_FIELD = "sign-password"
    EDGE_SIGN_UP_BUTTON = "//*[@id='signInModal']/div/div/div[3]/button[2]"

    BACKGROUND_COLOR = "//nav[@id='narvbarx']"

