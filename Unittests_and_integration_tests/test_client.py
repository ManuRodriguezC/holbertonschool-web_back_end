#!/usr/bin/env python3
""" This module contein the test client"""
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from clients import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """
    This class check and review the funtions and methos is GitHubOrgClient
    """

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc")
    ])
    def test_org(self, org, expected_url):
        """
        Using 'google' and 'abc' as the 'org' argument,
        this method creates a new <gh_client = GutHubOrgClient(<org>)>
        instance, and accesses its 'org' property twice
        """
        with patch('utils.get_json') as mock_get_json:
            mock_get_json.return_value = {"payload": True}
            client = GithubOrgClient()
            result = client.org(org)
            self.assertEqual(result, {"payload": True})
            mock_get_json.assert_called_once_with(expected_url)
