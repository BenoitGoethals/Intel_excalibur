from model.general_intel import GeneralIntel
from model.type_intel import TypeIntel


class InSum(GeneralIntel):
    intel_type: TypeIntel = TypeIntel.INSUM
    short_description: str = ""
    long_description: str = ""
