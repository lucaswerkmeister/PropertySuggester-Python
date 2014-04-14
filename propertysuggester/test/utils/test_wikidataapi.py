import requests
from testtools import TestCase, skipIf
from testtools.matchers import *

from propertysuggester.utils.WikidataApi import WikidataApi


<<<<<<< HEAD:propertysuggester/test/test_wikidataapi.py
#@skip("the test instance is currently not working")
=======
api_url = "http://suggester.wmflabs.org/w/api.php"


@skipIf(requests.get(api_url).status_code != 200, "the test instance is currently not working")
>>>>>>> bf9504b72051f4a5654f8e76cc3490330c503cc3:propertysuggester/test/utils/test_wikidataapi.py
class WikiDataApiTest(TestCase):

    def setUp(self):
        TestCase.setUp(self)

        self.api = WikidataApi(api_url)

    def test_wbsgetsuggestions(self):
        result = self.api.wbs_getsuggestions(entity="Q4", limit=3, cont=2)

        self.assertThat(result["success"], Equals(1))
        self.assertThat(result["search-continue"], Equals(5))
        self.assertThat(result["search"], HasLength(3))

    def test_wbsgetsuggestions_by_properties(self):
        result = self.api.wbs_getsuggestions(properties=[31, 373], limit=2, cont=5)

        self.assertThat(result["success"], Equals(1))
        self.assertThat(result["search-continue"], Equals(7))
        self.assertThat(result["search"], HasLength(2))

