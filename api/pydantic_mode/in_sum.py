from api.pydantic_mode.general_intel import GeneralIntel
from api.pydantic_mode.type_intel import TypeIntel


class InSum(GeneralIntel):
    intel_type: TypeIntel = TypeIntel.INSUM
    short_description: str = ""
    long_description: str = ""
