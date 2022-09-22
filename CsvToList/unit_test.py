import unittest
from datetime import datetime

from main import read_csv_to_list, sort_by_current_rent, get_first_5items, filter_by_lease_year, get_rent_sum, \
    gen_dict_of_tenant, get_list_in_range


class TestStringMethods(unittest.TestCase):
    # Runs before every test cases
    def setUp(self):
        print('In setUp()')
        self.raw_data = read_csv_to_list("./Python Developer Dataset.csv")
    # Runs after every test cases
    def tearDown(self):
        print('In tearDown()')
        del self.raw_data

    # Test for sort_by_current_rent
    def test_sort_by_current_rent(self):
        sorted_list = sort_by_current_rent(self.raw_data)
        self.assertEqual(sorted_list[0], ['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7', 'Potternewton Est Playing Field', 'Arqiva Ltd', '24-Jun-99', '23-Jun-19', '20', '6600'])
        self.assertEqual(sorted_list[1], ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds', 'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '8-Nov-04', '7-Nov-29', '25', '9500'])
        self.assertEqual(sorted_list[-1], ['Queens View', 'Seacroft', '', '', 'LS14', 'Queens View LDS232   LS0098', 'Everything Everywhere Ltd&Hutchison 3G UK Ltd', '1-Aug-09', '31-Jul-19', '10', '28327.09'])

    # Test for get_first_5items
    def test_get_first_5items(self):
        list = get_first_5items(self.raw_data)
        self.assertEqual(len(list), 5)
        self.assertEqual(list[0], ['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7', 'Potternewton Est Playing Field', 'Arqiva Ltd', '24-Jun-99', '23-Jun-19', '20', '6600'])
        self.assertEqual(list[1], ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds', 'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '8-Nov-04', '7-Nov-29', '25', '9500'])
        self.assertEqual(list[4], ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14', 'Seacroft Gate (Chase) - Block 2, WYK 0414', 'Hutchinson3G Uk Ltd&Everything Everywhere Ltd', '21-Aug-07', '20-Aug-32', '25', '12750'])

    # Test for filter_by_lease_year
    def test_filter_by_lease_year(self):
        list_25 = filter_by_lease_year(self.raw_data,25)
        self.assertEqual(len(list_25), 4)
        self.assertEqual(int(list_25[0][9]), 25)
        self.assertEqual(int(list_25[-1][9]), 25)

        list_64=filter_by_lease_year(self.raw_data,64)
        self.assertEqual(len(list_64), 1)
        self.assertEqual(int(list_64[0][9]), 64)
        self.assertEqual(int(list_64[-1][9]), 64)

    # Test for get_rent_sum
    def test_get_rent_sum(self):
        list_25 = filter_by_lease_year(self.raw_data,25)
        sum_25=get_rent_sum(list_25)
        self.assertEqual(sum_25, 46500.0)

        list_64=filter_by_lease_year(self.raw_data,64)
        sum_64=get_rent_sum(list_64)
        self.assertEqual(sum_64, 23950.0)

    # Test for gen_dict_of_tenant
    def test_gen_dict_of_tenant(self):
        tenant_dict = gen_dict_of_tenant(self.raw_data)
        self.assertEqual(tenant_dict['Cornerstone Telecommunications Infrastructure'], 16)
        self.assertEqual(tenant_dict['Everything Everywhere Ltd&Hutchison 3G UK LTd'], 1)
        self.assertEqual(tenant_dict['Everything Everywhere Ltd&Hutchsion 3G UK Ltd'], 1)


    # Test for get_list_in_range
    def test_get_list_in_range(self):
        list = get_list_in_range(self.raw_data, "1991-06-01", "2007-08-31")
        self.assertEqual(len(list), 6)
        self.assertGreater(datetime.strptime(list[0][7], '%d/%m/%Y'), datetime.strptime("1991-06-01", '%Y-%m-%d'))
        self.assertLess(datetime.strptime(list[0][7], '%d/%m/%Y'), datetime.strptime("2007-08-31", '%Y-%m-%d'))



if __name__ == '__main__':
    unittest.main()
