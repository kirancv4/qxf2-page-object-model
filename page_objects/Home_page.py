"""
Redirects to the home page of the rewritertools.com
URL: https://www.rewritertools.com/
"""
from .Base_Page import Base_Page
from page_objects.Home_page_object import Home_page_object
class Home_page(Home_page_object,Base_Page):
    "Page Object for the Home Page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        
        url=" "
        self.open(url)