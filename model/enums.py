from enum import Enum


class DocumentType(Enum):
    PDF = "PDF"
    DOCX = "Docx"
    JPEG = "JPEG"
    JPG = "JPG"
    EXCEL = "EXECL"
    NOTHING = "Nothing"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class HumIntType(Enum):
    ADVISORS = "Advisors"
    DIPLOMATIC_REPORTING = "DiplomaticReporting"
    ESPIONAGE = "Espionage"
    MILITARY_ATTACHES = "MilitaryAttaches"
    NON_GOVERNMENTAL_ORGANIZATIONS = "NonGovernmentalOrganizations"
    POW = "POW"
    REFUGEES = "Refugees"
    ROUTINE_PATROLLING = "RoutinePatrolling"
    SPECIAL_RECONNAISSANCE = "SpecialReconnaissance"
    TRAVELER_DEBRIEFING = "TravelerDebriefing"


class MasIntType(Enum):
    ACINT = "ACINT"
    OPINT = "OPINT"
    ELECTRO_OPTICAL_INT = "ELECTRO_OPTICAL_INT"
    IRINT = "IRINT"
    LASINT = "LASINT"
    NUCINT = "NUCINT"
    RINT = "RINT"


class SigIntType(Enum):
    COMINT = "COMINT"
    ELINT = "ELINT"


class InvestigationStatus(Enum):
    INIT = "Init"
    APPROVED = "Approved"
    STARTED = "Started"
    CLOSED = "Closed"
    ONHOLD = "Onhold"


class TypeOfCybInt(Enum):
    MALWARE_ATTACKS = "MalwareAttacks"
    EMAIL_PHISHING = "EmailPhishing"
    DOS = "DoS"
    MALICIOUS_SOFTWARE_THAT_ENCRYPTS = "MaliciousSoftwareThatEncrypts"
    MAN_IN_THE_MIDDLE = "ManInTheMiddle"
    SQL_INJECTION = "SqlInjection"
    CROSS_SITE_SCRIPTING = "CrossSiteScripting"
    INSIDER_THREATS = "InsiderThreats"
    ZERO_DAY_EXPLOITS = "ZeroDayExploits"
    DATA_BREACHES = "DataBreaches"
    IOT = "IoT"
    SOCIAL_ENGINEERING_ATTACKS = "SocialEngineeringAttacks"
