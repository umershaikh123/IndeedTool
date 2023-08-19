from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List

# Import your custom tools
from jobSearching import JobSearchingTool
from jobApplying import JobApplyingTool

class IndeedToolkit(BaseToolkit):
    name: str = "Indeed Toolkit"
    description: str = "Custom toolkit for job searching and applying on indeed.com"

    def get_tools(self) -> List[BaseTool]:
        # Return instances of your custom tools
        return [JobSearchingTool(), JobApplyingTool()]

    def get_env_keys(self) -> List[str]:
        # If you need environment keys for your tools, specify them here
        return ["YOUR_ENV_KEY_1", "YOUR_ENV_KEY_2"]
