import unittest
from project import parser_vk


class test_parser_vk(unittest.TestCase):



    def test_check_page_status_code(self):
        url = "https://vk.com/id185394982/"
        self.assertRaises(ValueError, parser_vk.check_page_status_code(url))

    def test_profile_name_only_af(self):
        url = "https://vk.com/id185394982/"
        self.assertEqual(parser_vk.get_profile_name(url), "Александр Филипповский")

    def test_profile_name(self):
        url = "https://vk.com/id185394982/"
        raised = False
        try:
            parser_vk.get_profile_name(url)
        except ValueError:
            raised = True
        self.assertFalse(raised, "can't get profile name: html class has been changed")

    def test_profile_pic(self):
        url = "https://vk.com/id185394982/"
        raised = False
        try:
            parser_vk.get_profile_pic(url)
        except ValueError:
            raised = True
        self.assertFalse(raised, "can't get pic url: html class has been changed")

    def test_get_profile_online_status(self):
        url = "https://vk.com/id185394982/"
        raised = False
        try:
            parser_vk.get_profile_online_status(url)
        except IndentationError:
            raised = True
        self.assertFalse(raised, "can't get online status: html class has been changed")


if __name__ == '__main__':
    unittest.main()
