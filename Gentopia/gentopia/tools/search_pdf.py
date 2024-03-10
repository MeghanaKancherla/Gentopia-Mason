from PyPDF2 import PdfReader
from io import BytesIO
from pathlib import Path
from typing import AnyStr, Optional, Type
from gentopia.tools.basetool import *
from pydantic import Field
import requests

class SearchPDFArgs(BaseModel):
    url: str = Field(..., description="PDF URL to be read")

class SearchPDFTool(BaseTool):
    name = "SearchPDF"
    description = "Reads and searches the contents of a PDF file from thr URL"
    args_schema: Optional[Type[BaseModel]] = SearchPDFArgs

    def _run(self, file_path: str = None, url: str = None) -> AnyStr:
        try:
            file = self._load_pdf(file_path, url)
            text = self._extract_text(file)
            file.close()
            return text

        except requests.RequestException as e:
            return f"Request error: {e}"
        except Exception as e:
            return f"Error: {e}"

    def _load_pdf(self, file_path: str = None, url: str = None):
        if url:
            response = requests.get(url)
            response.raise_for_status()
            return BytesIO(response.content)
        else:
            return open(Path(file_path), 'rb')

    def _extract_text(self, file, char_limit=9250): # setting the limit since the access to read file is only for 10000 characters
        reader = PdfReader(file)
        text = ""
        for page_num in reader.pages:
            page_text = page_num.extract_text() or ""
            if len(text) + len(page_text) > char_limit:
                text = text + page_text[:char_limit - len(text)]
                break
            else:
                text = text + page_text
        return text

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    pdf_url = "abc.pdf" 
    res = SearchPDFTool()._run(url=pdf_url)
    print(res)
