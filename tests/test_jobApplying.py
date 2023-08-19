import unittest
from unittest.mock import patch
from jobApplying import JobApplyingTool

class TestJobApplyingTool(unittest.TestCase):
    @patch("jobApplying.webdriver.Chrome")
    def test_apply_for_job(self, mock_chrome):
        mock_driver = mock_chrome.return_value
        mock_driver.get.return_value = None  # Mock the get method

        # Create an instance of the tool and execute it
        job_apply_tool = JobApplyingTool()
        job_apply_tool.execute(job_url="https://www.indeed.com/job_url", resume_path="path/to/resume.pdf")

        # Add your assertions here to check if the Selenium interactions are as expected

if __name__ == "__main__":
    unittest.main()
