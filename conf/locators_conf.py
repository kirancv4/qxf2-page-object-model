#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the footer object(footer_object.py)

word_count = "xpath,//ul[@class='common-sidebar']//a[contains(text(),'Word Counter')]"
word_count_success= "xpath,//h4[contains(.,'Word Counter | Character Counter')]"
word_count_textarea = "xpath,//textarea[@id='input-content']"
word_count_button = "xpath,//a[@id='next-input']"
word_count_result_wordcount= "xpath,//span[@id='wordCount']"
word_count_result_charcount= "xpath,//span[@id='charCount']"
#word_count_result = "xpath,//h1[contains(text(),'Accurately Counts the Number of Wor')]"