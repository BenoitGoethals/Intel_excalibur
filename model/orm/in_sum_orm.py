from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.general_intel_orm import GeneralIntelOrm


class InSumOrm(GeneralIntelOrm):
    __tablename__ = "in_sum"

    id: Mapped[str] = mapped_column(ForeignKey("general_intel.id"), primary_key=True)
    short_description: Mapped[str] = mapped_column(String, default="")
    long_description: Mapped[str] = mapped_column(String, default="")

    __mapper_args__ = {
        "polymorphic_identity": "in_sum",
    }
