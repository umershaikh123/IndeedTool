import unittest
from unittest.mock import patch, MagicMock
from jobSearching import JobSearchingTool

class TestJobSearchingTool(unittest.TestCase):
    @patch("jobSearching.requests.get")
    def test_search_jobs(self, mock_get):
        # Create a mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "jobtitle": "Software Engineer",
                    "company": "TechCo",
                    "formattedLocation": "New York, NY",
                    "url": "https://www.indeed.com/job_url_1"
                },
                # Add more mock job data
            ]
        }
        mock_get.return_value = mock_response

        # Create an instance of the tool and execute it
        job_search_tool = JobSearchingTool()
        job_search_tool.execute(keywords="software engineer", location="New York")

        # Add your assertions here to check if the output matches the mock response

if __name__ == "__main__":
    unittest.main()
