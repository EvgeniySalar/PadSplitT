from selenium.webdriver.common.by import By




class MainPageLocatorsSc2:
    GET_STARTED = (By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root jss40 jss53 MuiButton-text"]')


    POP_UP_WINDOW = (By.XPATH, "//div[@role='dialog']")

    JOIN_AS_A_MEMBER = (By.XPATH, "//span[normalize-space()='Join as a Member']")

    POP_UP_WINDOW_N = (By.XPATH, "//input[@name='email']")
    GET_STARTED_N = (By.XPATH, '//button[@type="submit"]')
    NEXT_PAGE_INDICATOR = (By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root jss43 "
                                     "jss118 jss107 jss101 MuiButton-outlined jss44 jss119 "
                                     "MuiButton-outlinedSizeSmall MuiButton-sizeSmall jss48']")
    CLOSE_POP_UP = (By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root']"
                                     "//span[@class='MuiIconButton-label']//*[local-name()='svg']")

    CLOSE_POP_UP_INDICATOR = (By.XPATH, "//input[@id='placesAutocomplete']")