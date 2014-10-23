class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._way_result = None
        self._share_panel = None

    @property
    def search_bar(self):
        from online.helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver,
                                         self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from online.helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver,
                                               self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    @property
    def way_result(self):
        from online.helpers.way_results import WayResult

        if self._way_result is None:
            self._way_result = WayResult(self.driver,
                                         self.driver.find_element_by_css_selector(WayResult.selectors['self']))
        return self._way_result

    @property
    def share_panel(self):
        from online.helpers.share import SharePanel

        if self._share_panel is None:
            self._share_panel = SharePanel(self.driver,
                                           self.driver.find_element_by_css_selector(SharePanel.selectors['self']))
        return self._share_panel

    def open(self, url):
        self.driver.get(url)

