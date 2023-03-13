# Basic Configs
browser = ["chrome", "firefox"]
test_site_url = "https://www.way2automation.com/"
implicit_wait = 10
explicit_wait = 10
fluent_wait = 0.01
headless = False  # True

# [SEO_MARKETING] Locators
email__ID = "txtEmailid"
password__ID = "txtPassword"
sign_in_button__XPATH = "//button[normalize-space()='Sign in']"
dashboard_heading__XPATH = "//h1[normalize-space()='WELCOME TO DASHBOARD']"
Seo_Marketing__XPATH = "//li[@id='Li_ModuleID_2021']//a[@href='#']"
Team_Master__XPATH = "//a[@href='/Team_Master']"
Add_Team__XPATH = "//div[@title='Add Team']"
Team_Name_input__ID = "txtTeamName"
Select_user__ID = "ddlUser_input"
Multiple_Options__XPATH = "//div[@id='ddlUser_itemList']//span[@class='multiselect-text']"
Help_Information__XPATH = "//h2[@class='form-right-title']//span[@id='user_edit_uname']"
iframe_Description__ID = "txtCustomNote_ifr"
inside_Description__XPATH = "//body//p"
submit_Btn__ID = "btnsubmit"
alert__XPATH = "//a[@class='login-alert']"
Team_Name_Search_InputField__XPATH = "//td[2]//input[1]"
Teams_list__XPATH = "//tbody[@aria-relevant='all']//td"
Delete_team__XPATH = "(//tbody[@aria-relevant='all']//td//a//i[@title='Delete'])[6]"
View_team__XPATH = "(//tbody[@aria-relevant='all']//td//a//i[@title='View'])[6]"
Delete_the_record__XPATH = "//span[normalize-space()='Delete']"
Project_Details_view__XPATH = "//div[@class='uk-sticky-placeholder']//span[@id='user_edit_uname']"
Team_Name__ID = "lblTeamName"
Close__XPATH = "//button[normalize-space()='Close']"

# Way2Automation_Locators
# DUMMY REGISTRATION page
name__XPATH = "//input[@name='name']"
phone__CSS = "input[name='phone']"
email__NAME = "email"
country__XPATH = "//select[@name='country']"
city__XPATH = "//input[@name='city']"
username__XPATH = "//div[@id='load_box']//input[@name='username']"
password__XPATH = "//div[@id='load_box']//input[@name='password']"
Name_label__XPATH = "//label[normalize-space()='Name:']"
Phone_label__XPATH = "//label[normalize-space()='Phone:']"
Email_label__XPATH = "//label[normalize-space()='Email:']"
Country_label__XPATH = "//label[normalize-space()='Country:']"
City_label__XPATH = "//label[normalize-space()='City:']"
Username_label__XPATH = "//div[@id='load_box']//label[contains(text(),'Username:')]"
Password_label__XPATH = "//div[@id='load_box']//label[contains(text(),'Password:')]"
ENTER_TO_THE_TESTING_WEBSITE__XPATH = "//div[@id='load_box']//a[@class='fancybox'][normalize-space()='ENTER TO THE TESTING WEBSITE']"
EXPLORE_LIFETIME_MEMBERSHIP__XPATH = "//div[@id='load_box']//a[@class='fancybox'][normalize-space()='EXPLORE LIFETIME MEMBERSHIP']"
Submit_btn__XPATH = "//div[@id='load_box']//input[@value='Submit']"
# Automation_Practice_Site_Page
resources__XPATH = "//li[@id='menu-item-27617']//span[@class='menu-text'][normalize-space()='Resources']"
resources_practice_site_1__XPATH = "//li[@id='menu-item-27618']//span[@class='menu-text'][normalize-space()='Practice Site 1']"
