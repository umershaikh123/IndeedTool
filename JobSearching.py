from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests

class JobSearchInput(BaseModel):
    keywords: str = Field(..., description="Keywords for job search")
    location: str = Field(..., description="Location for job search")

class JobSearchingTool(BaseTool):
    name: str = "Job Searching Tool"
    args_schema: Type[BaseModel] = JobSearchInput
    description: str = "Search for job listings using Indeed API"

    def _execute(self, keywords: str = None, location: str = None):
        api_url = "https://api.indeed.com/ads/apisearch"         
        params = {
            "publisher": "YOUR_PUBLISHER_ID",
            "q": keywords,
            "l": location,
        }

        response = requests.get(api_url, params=params)
        data = response.json()

        # Process and display job listings
        for job in data['results']:
            print(f"Job Title: {job['jobtitle']}")
            print(f"Company: {job['company']}")
            print(f"Location: {job['formattedLocation']}")
            print(f"Apply URL: {job['url']}")
            print("--------")

# Create an instance of the tool and execute it
job_search_tool = JobSearchingTool()
job_search_tool.execute(keywords="software engineer", location="New York")
