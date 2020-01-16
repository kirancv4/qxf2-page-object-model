"""
This page contains the objects in the Home page.
Example buttons,checkbox etc(clickable items)


"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Home_page_object(Base_Page):
    "Page object for Home Page "
    
    #Getting locators from Locators_conf
    word_count=locators.word_count
    word_count_success=locators.word_count_success
    word_count_textarea=locators.word_count_textarea
    word_count_button=locators.word_count_button
    word_count_result_wordcount=locators.word_count_result_wordcount
    word_count_result_charcount=locators.word_count_result_charcount
    #word_count_result=locators.word_count_result
    
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def word_count_click(self):
        "Click word count"
        result_flag = self.click_element(self.word_count)
        self.conditional_write(result_flag,
        positive="Clicked on the word count button",
        negative="Could not click on the word count button")
        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def verify_frame(self):
        "Verify automation is on the frame"
        result_flag = self.smart_wait(5,self.word_count_success) #pylint: disable=no-member
        self.conditional_write(result_flag,
        positive="Automation is on the Frame",
        negative="Automation is not able to locate the Frame Title.")
        return result_flag

   
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def input_sample_text(self,word_count_textarea):
        "set sample text in the textarea"
        result_flag = self.set_text(self.word_count_textarea,word_count_textarea)
        self.conditional_write(result_flag,
        positive='Set the sample text to: %s'%word_count_textarea,
        negative='Failed to set sample text',
        level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def word_count_button_click(self):
        "Click 'word count' button"
        result_flag = self.click_element(self.word_count_button)
        self.conditional_write(result_flag,
        positive="Clicked on the 'word count' button",
        negative="Could not click on the 'word count' button")
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def get_result(self,sample_word_count,sample_char_count):
        "get the result of total Number of words and characters and compare with sample." 
        wordcount = self.get_text(self.word_count_result_wordcount) #Getting the wordcount
        charcount = self.get_text(self.word_count_result_charcount) #Getting the charcount
        wordcount = int(wordcount)                                  #Conversion of unicode to int    
        charcount = int(charcount)                                  #conversion of unicode to int
        if (wordcount is not None) and  (charcount is not None):
            self.write("The word count is {} and character count is {}".format(wordcount,charcount))
            if (wordcount==sample_word_count ) and (charcount==sample_char_count):
                result_flag = True
        else:
            result_flag = False
        self.conditional_write(result_flag,
        positive="Automation was able to fetch the word and character count and both are same",
        negative="Automation was not able to fetch the word and character count")
        return result_flag


    


    