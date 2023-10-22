#!/usr/bin/env python3
""" This module contein the test client"""
from unittest import TestCase
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from clients import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
            client = GithubOrgClient(org)
            self.assertEqual(client, {"payload": True})
            mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """
        This method tests the _public_repos_url property
        of the GithubOrgClient class.
        It patches the org method to return a known payload,
        and then asserts that the
        _public_repos_url property returns the expected result
        based on the mocked payload.
        """
        URL: str = "https://api.github.com/orgs/google/repos"
        with patch.object(GithubOrgClient, 'org',
                          return_value={"repos_url": URL}):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, URL)

    @patch('utils.get_json')
    @patch.object(GithubOrgClient,
                  '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self,
                          mock_public_repos_url,
                          mock_get_json):
        """
        This method tests the public_repos method of
        the GithubOrgClient class.
        It patches the get_json function and the _public_repos_url
        property to return known payloads,
        and then asserts that the public_repos method returns the
        expected list of repositories.
        """
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl-3.0"}}
        ]
        url = "https://api.github.com/orgs/google/repos"
        mock_public_repos_url.return_value = url

        client = GithubOrgClient("google")
        repos = client.public_repos()

        self.assertEqual(repos, ["repo1", "repo2", "repo3"])
        mock_get_json.assert_called_once_with(
            mock_public_repos_url.return_value)
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        This method tests the has_license method of the GithubOrgClient class.
        It patches the access_nested_map function to return known results,
        and then asserts that the has_license method
        returns the expected result.
        """
        with patch('utils.access_nested_map',
                   return_value=MagicMock(
                       return_value=repo["license"]["key"])):
            result = GithubOrgClient.has_license(repo, license_key)
            self.assertEqual(result, expected_result)


@parameterized_class([
    "org_payload", "repos_payload", "expected_repos", "apache2_repos"])
class TestIntegrationGithubOrgClient(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            MagicMock(json=lambda: org_payload),
            MagicMock(json=lambda: repos_payload),
            MagicMock(json=lambda: apache2_repos)
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
        self.mock_get.assert_any_call(self.org_payload["repos_url"])
        self.mock_get.assert_any_call(self.repos_payload["repos_url"])
