from online.helpers.base_component import BaseComponent


class SearchBar(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'input': '.searchBar__form .searchBar__textfield._refbook .suggest__input',
        'submit': '.searchBar__submit._refbook',
        'name_search': 'div.searchBar__tab:nth-child(1)',
        'way_search': 'div.searchBar__tab:nth-child(2)',
        'departure_input': '#module-1-1-2 > div:nth-child(1) > input:nth-child(1)',
        'arrival_input': '#module-1-1-3 > div:nth-child(1) > input:nth-child(1)',
        'submit_way': 'button.searchBar__submit:nth-child(6)'
    }

    def open_name_search(self):
        self.driver.find_element_by_css_selector(self.selectors['name_search']).click()

    def open_way_search(self):
        self.driver.find_element_by_css_selector(self.selectors['way_search']).click()

    def search_by_name(self, query):
        self.open_name_search()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def search_by_way(self, departure, arrival):
        self.open_way_search()
        self.driver.find_element_by_css_selector(self.selectors['departure_input']).send_keys(departure)
        self.driver.find_element_by_css_selector(self.selectors['arrival_input']).send_keys(arrival)
        self.driver.find_element_by_css_selector(self.selectors['submit_way']).submit()

    def clear_input(self):
        self.driver.find_element_by_css_selector(self.selectors['input']).clear()

    @property
    def request(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute('value')