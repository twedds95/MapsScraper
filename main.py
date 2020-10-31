from selenium import webdriver


class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.ca/maps')

    def find_locations(self, location):
        input = self.driver.find_element_by_xpath('//*[@id="searchboxinput"]')
        input.send_keys(location + '\n')
        location_divs = s.driver.find_elements_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div')
        locations = [loc for loc in location_divs if len(loc.text) != 0]
        for l in locations:
            btns = l.find_elements_by_tag_name('button')
            dir_button = [b for b in btns if b.text == 'Directions'][0]

    def find_distance(self):





s = Scraper()
