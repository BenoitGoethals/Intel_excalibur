from enum import Enum


class TypeIntel(Enum):
    HUMINT = "Humint"           # Human Intelligence
    CYBER_INT = "CyberInt"      # Cyber Intelligence
    GEO_INT = "GeoInt"          # Geospatial Intelligence
    IMINT = "Imint"             # Imagery Intelligence
    SIGINT = "Sigint"           # Signals Intelligence
    MASINT = "Masint"           # Measurement and Signature Intelligence
    MEDINT = "Medint"           # Medical Intelligence
    TECH_INT = "TechInt"        # Technical Intelligence
    COUNTER_INTEL = "CounterIntel"  # Counterintelligence
    OPEN_SOURCE = "OpenSource"  # Open Source Intelligence
    INSUM = "Insum"             # Intelligence Summary
    OTHER = "Other"             # Other or unclassified
    INFORMANT = "Informant"
    SOCIAL_MEDIA = "SocialMedia"
    NEWS_ARTICLE = "NewsArticle"
