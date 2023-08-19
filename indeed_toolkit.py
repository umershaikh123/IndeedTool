from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List


class MyToolkit(BaseToolkit):
name: str = "My Toolkit"
description: str = "Description of my toolkit"

def get_tools(self) -> List[BaseTool]:
return [MyTool()]

def get_env_keys(self) -> List[str]:
return []