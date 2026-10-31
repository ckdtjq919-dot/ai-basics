from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser

class GraduationStatus(BaseModel):

    total_ok: bool
    liberal_ok: bool
    major_required_ok: bool
    major_selective_ok: bool
    recommendation: str

parser = PydanticOutputParser(

pydantic_object=GraduationStatus

)