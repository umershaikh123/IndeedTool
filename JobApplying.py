from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MyToolInput(BaseModel):
message: str = Field(..., description="Message to be processed by the tool")


class MyTool(BaseTool):
name: str = "My Tool"
args_schema: Type[BaseModel] = MyToolInput
description: str = "Description of my tool"

def _execute(self, message: str = None):
# Tool logic goes here