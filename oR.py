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

# Khamelia [Login]
khamelia_login__XPATH = "//ul[@class='nav-menu sf-js-enabled sf-arrows']//a[normalize-space()='Login']"
khamelia_email_address_inbox__ID = "txtEmailAddress"
khamelia_password_inbox__ID = "txtPassword"
khamelia_signIn_btn__ID = "DivSignIn"
khamelia_cancel_btn__ID = "lnkCancel"
khamelia_keepMeSignIn_checkbox__XPATH = "//label[normalize-space()='Keep me signed in']"
Khamelia_login_hide__ID = "login-hideMe"

# User Options
BACK_CANCEL__ID = "alinkProjectBack"
NEXT__ID = "alinkprojectnext"
FINISH__ID = "alinkprojectfinish"

# Project
new_Project__ID = "DivRibbonBarButton-105"
idasdf__ID = "txtBudgetHourlyRate"
idasdfg__ID = "txtProjectFixedCost"

kha_overlay__ID = "CustomeMessage"
New_Project_Creation_Div__ID = "DivProjectcreateNew"
Project_Name_inbox__ID = "txtProjectName_Create"
Project_Type_Dropdown__XPATH = "//select[@name='drpCreateProjectType']"
Company_Dropdown__XPATH = "//select[@ng-change='GetTeamByCompany(CreateProjectCompanyID);']"
Team_Dropdown__XPATH = "//select[@ng-class=\"{'used': CreateProjectDepartmentTeam != null}\"]"
Team_Dropdown_1__XPATH = "//select[@class='custom-field moving-txt ng-pristine ng-valid used ng-touched']"
Project_Workflow_Dropdown__XPATH = "//select[@ng-model='CreateProjectWorkflowID']"
Portfolio_Dropdown__XPATH = "//select[@ng-model='CreateProjectPortfolioID']"
Project_Rating_Dropdown__XPATH = "//div[@id='DivIPORRatingID_Create']//select"
Project_Sponsor__XPATH = "(//button[@type='button'])[2]"
Project_Approver__XPATH = "(//button[@type='button'])[3]"
Project_Contact__XPATH = "(//button[@type='button'])[4]"
Project_Default_Task_Assignee__XPATH = "(//button[@type='button'])[5]"
Project_Contact_Default_Task_Assignee__XPATH = "//div[@id='divCreateProjectSection2']//div[6]//button[1]"
TimeZone_Dropdown__XPATH = "//select[@ng-model='CreateProjectTimezoneID']"
Working_Days_Dropdown__XPATH = "//select[@ng-model='CreateProjectWorkingDaysID']"
Language_Dropdown__XPATH = "//select[@ng-model='CreateProjectlanguageID']"
Project_Percentage__XPATH = "//input[@title='Project Percentage']"
Project_Budget_Billing_Dropdown__XPATH = "//select[@ng-model='CreateProjectBudgetBilling']"
Project_Planned_Hours__XPATH = "//input[@title='Project Budget Hours']"
Project_Planned_Cost__XPATH = "//div[@id='DivBudgetCost_Create']//input"
Project_Actual_Hours__XPATH = "//input[@title='Total Project Hours']"
Project_Hourly_Rate__XPATH = "//input[@id='txtProjectHourlyRate']"
Project_Planned_Material_Cost__ID = "txtProjectMaterialCost"
Project_Actual_Material_Cost__ID = "txtProjectActualMaterialCost"
Project_Estimated_Start_Date__ID = "txtEstimatedStartDate_Create"
Project_Estimated_End_Date__ID = "txtEstimatedEndDate_Create"
Project_Sponsor_User__XPATH = "//div[@id='DivProjectSponsorUser-80946942-1809-42f7-9d71-5f28c09cf29e']"
Project_Approver_User__XPATH = "//div[@id='DivProjectApproverUser-80946942-1809-42f7-9d71-5f28c09cf29e']"
Project_Contact_User__XPATH = "//div[@id='DivProjectContactUser-80946942-1809-42f7-9d71-5f28c09cf29e']"
Project_Assignee_User__XPATH = "//div[@id='DivProjectAssigneeUser-80946942-1809-42f7-9d71-5f28c09cf29e']"
Project_Manager__XPATH = "//div[@id='divCreateProjectSection1']//button[@type='button']"
Task_Billable_Rate_Radio_btn__XPATH = "//label[normalize-space()='Task Billable Rate']"
User_Hour_Rate_Radio_btn__XPATH = "//label[normalize-space()='User Hour Rate']"
Project_Status_Dropdown__XPATH = "//select[@name='drpEditProjectStatus']"
Description__ID = "txtProjectDescription_Create"
Task_Prefix_Key__ID = "txtCreateProjectKey_Create"  # pre-filled
New_Task_Number__ID = "txtNextTaskNumber_Create" # pre-filled

Waterfall__ID = "DivProjectCategoryType-2"
Basic_Agile__ID = "DivProjectCategoryType-7"
Agile_Scrum__ID = "DivProjectCategoryType-8"
new_Project_Option_Business__ID = "li-1-Project"
new_Project_Option_Software__ID = "li-2-Project"
new_Project_Option_Private__ID = "li-4-Project"


# Date Picker
date_picker_next__XPATH = "//a[@title='Next']"
date_picker_previous__XPATH = "//a[@title='Prev']"

information_pop_up__XPATH = "//a[@class='message-popup-btn ng-scope']"

bible_frame__XPATH = "//body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/iframe[1]"
bible_Menu_1_dropdown__XPATH = "//select[@name='select1']"
bible_Menu_2_dropdown__XPATH = "//select[@name='select2']"
bible_Hebrew__XPATH = "//a[@title='Hebrew Text Analysis']"
bible_text_verse__XPATH = "//div[@id='combox']//div[@class='padcom']/span[@class='word']"
