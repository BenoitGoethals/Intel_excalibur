from typing import List, Optional
from sqlalchemy.orm import Session
from model.orm.standalone_orm import (
    MasIntOrm, MedIntOrm, TechIntOrm, SigIntOrm, GeoIntOrm,
    ImIntOrm, FinancialIntOrm, CounterIntOrm, SitRepOrm,
    HumanSourceOrm, OperatorIntelOrm, GovSourceOrm, ReportDataOrm,
)
from repo.base_repo import BaseRepo


class MasIntRepo(BaseRepo[MasIntOrm]):
    def __init__(self) -> None:
        super().__init__(MasIntOrm)

    def get_filtered(
        self,
        db: Session,
        mas_int_type: Optional[str] = None,
        target_name: Optional[str] = None,
        target_location: Optional[str] = None,
    ) -> List[MasIntOrm]:
        q = db.query(MasIntOrm)
        if mas_int_type:
            q = q.filter(MasIntOrm.mas_int_type == mas_int_type)
        if target_name:
            q = q.filter(MasIntOrm.target_name.ilike(f"%{target_name}%"))
        if target_location:
            q = q.filter(MasIntOrm.target_location.ilike(f"%{target_location}%"))
        return q.all()


class MedIntRepo(BaseRepo[MedIntOrm]):
    def __init__(self) -> None:
        super().__init__(MedIntOrm)

    def get_filtered(
        self,
        db: Session,
        patient_name: Optional[str] = None,
        diagnosis: Optional[str] = None,
        facility_name: Optional[str] = None,
        facility_location: Optional[str] = None,
    ) -> List[MedIntOrm]:
        q = db.query(MedIntOrm)
        if patient_name:
            q = q.filter(MedIntOrm.patient_name.ilike(f"%{patient_name}%"))
        if diagnosis:
            q = q.filter(MedIntOrm.diagnosis.ilike(f"%{diagnosis}%"))
        if facility_name:
            q = q.filter(MedIntOrm.facility_name.ilike(f"%{facility_name}%"))
        if facility_location:
            q = q.filter(MedIntOrm.facility_location.ilike(f"%{facility_location}%"))
        return q.all()


class TechIntRepo(BaseRepo[TechIntOrm]):
    def __init__(self) -> None:
        super().__init__(TechIntOrm)

    def get_filtered(
        self,
        db: Session,
        technology_name: Optional[str] = None,
        manufacturer: Optional[str] = None,
        acquisition_source: Optional[str] = None,
    ) -> List[TechIntOrm]:
        q = db.query(TechIntOrm)
        if technology_name:
            q = q.filter(TechIntOrm.technology_name.ilike(f"%{technology_name}%"))
        if manufacturer:
            q = q.filter(TechIntOrm.manufacturer.ilike(f"%{manufacturer}%"))
        if acquisition_source:
            q = q.filter(TechIntOrm.acquisition_source.ilike(f"%{acquisition_source}%"))
        return q.all()


class SigIntRepo(BaseRepo[SigIntOrm]):
    def __init__(self) -> None:
        super().__init__(SigIntOrm)

    def get_filtered(
        self,
        db: Session,
        signal_type: Optional[str] = None,
        sender: Optional[str] = None,
        receiver: Optional[str] = None,
        sender_location: Optional[str] = None,
    ) -> List[SigIntOrm]:
        q = db.query(SigIntOrm)
        if signal_type:
            q = q.filter(SigIntOrm.signal_type.ilike(f"%{signal_type}%"))
        if sender:
            q = q.filter(SigIntOrm.sender.ilike(f"%{sender}%"))
        if receiver:
            q = q.filter(SigIntOrm.receiver.ilike(f"%{receiver}%"))
        if sender_location:
            q = q.filter(SigIntOrm.sender_location.ilike(f"%{sender_location}%"))
        return q.all()


class GeoIntRepo(BaseRepo[GeoIntOrm]):
    def __init__(self) -> None:
        super().__init__(GeoIntOrm)

    def get_filtered(
        self,
        db: Session,
        target_location: Optional[str] = None,
        weather_conditions: Optional[str] = None,
        natural_hazards: Optional[str] = None,
    ) -> List[GeoIntOrm]:
        q = db.query(GeoIntOrm)
        if target_location:
            q = q.filter(GeoIntOrm.target_location.ilike(f"%{target_location}%"))
        if weather_conditions:
            q = q.filter(GeoIntOrm.weather_conditions.ilike(f"%{weather_conditions}%"))
        if natural_hazards:
            q = q.filter(GeoIntOrm.natural_hazards.ilike(f"%{natural_hazards}%"))
        return q.all()


class ImIntRepo(BaseRepo[ImIntOrm]):
    def __init__(self) -> None:
        super().__init__(ImIntOrm)

    def get_filtered(
        self,
        db: Session,
        target_name: Optional[str] = None,
        target_location: Optional[str] = None,
        image_format: Optional[str] = None,
    ) -> List[ImIntOrm]:
        q = db.query(ImIntOrm)
        if target_name:
            q = q.filter(ImIntOrm.target_name.ilike(f"%{target_name}%"))
        if target_location:
            q = q.filter(ImIntOrm.target_location.ilike(f"%{target_location}%"))
        if image_format:
            q = q.filter(ImIntOrm.image_format.ilike(f"%{image_format}%"))
        return q.all()


class FinancialIntRepo(BaseRepo[FinancialIntOrm]):
    def __init__(self) -> None:
        super().__init__(FinancialIntOrm)

    def get_filtered(
        self,
        db: Session,
        transaction_type: Optional[str] = None,
        counterparty: Optional[str] = None,
        investigation_status: Optional[str] = None,
        investigating_agency: Optional[str] = None,
    ) -> List[FinancialIntOrm]:
        q = db.query(FinancialIntOrm)
        if transaction_type:
            q = q.filter(FinancialIntOrm.transaction_type.ilike(f"%{transaction_type}%"))
        if counterparty:
            q = q.filter(FinancialIntOrm.counterparty.ilike(f"%{counterparty}%"))
        if investigation_status:
            q = q.filter(FinancialIntOrm.investigation_status.ilike(f"%{investigation_status}%"))
        if investigating_agency:
            q = q.filter(FinancialIntOrm.investigating_agency.ilike(f"%{investigating_agency}%"))
        return q.all()


class CounterIntRepo(BaseRepo[CounterIntOrm]):
    def __init__(self) -> None:
        super().__init__(CounterIntOrm)

    def get_filtered(
        self,
        db: Session,
        operation_name: Optional[str] = None,
    ) -> List[CounterIntOrm]:
        q = db.query(CounterIntOrm)
        if operation_name:
            q = q.filter(CounterIntOrm.operation_name.ilike(f"%{operation_name}%"))
        return q.all()


class SitRepRepo(BaseRepo[SitRepOrm]):
    def __init__(self) -> None:
        super().__init__(SitRepOrm)

    def get_filtered(
        self,
        db: Session,
        reporting_unit: Optional[str] = None,
        location: Optional[str] = None,
        weather_conditions: Optional[str] = None,
    ) -> List[SitRepOrm]:
        q = db.query(SitRepOrm)
        if reporting_unit:
            q = q.filter(SitRepOrm.reporting_unit.ilike(f"%{reporting_unit}%"))
        if location:
            q = q.filter(SitRepOrm.location.ilike(f"%{location}%"))
        if weather_conditions:
            q = q.filter(SitRepOrm.weather_conditions.ilike(f"%{weather_conditions}%"))
        return q.all()


class HumanSourceRepo(BaseRepo[HumanSourceOrm]):
    def __init__(self) -> None:
        super().__init__(HumanSourceOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        for_name: Optional[str] = None,
    ) -> List[HumanSourceOrm]:
        q = db.query(HumanSourceOrm)
        if name:
            q = q.filter(HumanSourceOrm.name.ilike(f"%{name}%"))
        if for_name:
            q = q.filter(HumanSourceOrm.for_name.ilike(f"%{for_name}%"))
        return q.all()


class OperatorIntelRepo(BaseRepo[OperatorIntelOrm]):
    def __init__(self) -> None:
        super().__init__(OperatorIntelOrm)

    def get_filtered(
        self,
        db: Session,
        name: Optional[str] = None,
        serial_nbr: Optional[str] = None,
    ) -> List[OperatorIntelOrm]:
        q = db.query(OperatorIntelOrm)
        if name:
            q = q.filter(OperatorIntelOrm.name.ilike(f"%{name}%"))
        if serial_nbr:
            q = q.filter(OperatorIntelOrm.serial_nbr.ilike(f"%{serial_nbr}%"))
        return q.all()


class GovSourceRepo(BaseRepo[GovSourceOrm]):
    def __init__(self) -> None:
        super().__init__(GovSourceOrm)

    def get_filtered(
        self,
        db: Session,
        source_agency: Optional[str] = None,
        source_type: Optional[str] = None,
        clearance_level: Optional[str] = None,
        operational_status: Optional[str] = None,
    ) -> List[GovSourceOrm]:
        q = db.query(GovSourceOrm)
        if source_agency:
            q = q.filter(GovSourceOrm.source_agency.ilike(f"%{source_agency}%"))
        if source_type:
            q = q.filter(GovSourceOrm.source_type.ilike(f"%{source_type}%"))
        if clearance_level:
            q = q.filter(GovSourceOrm.clearance_level.ilike(f"%{clearance_level}%"))
        if operational_status:
            q = q.filter(GovSourceOrm.operational_status.ilike(f"%{operational_status}%"))
        return q.all()


class ReportDataRepo(BaseRepo[ReportDataOrm]):
    def __init__(self) -> None:
        super().__init__(ReportDataOrm)

    def get_filtered(
        self,
        db: Session,
        type_base_line: Optional[str] = None,
        min_count: Optional[int] = None,
    ) -> List[ReportDataOrm]:
        q = db.query(ReportDataOrm)
        if type_base_line:
            q = q.filter(ReportDataOrm.type_base_line == type_base_line)
        if min_count is not None:
            q = q.filter(ReportDataOrm.count >= min_count)
        return q.all()


# Singletons
mas_int_repo = MasIntRepo()
med_int_repo = MedIntRepo()
tech_int_repo = TechIntRepo()
sig_int_repo = SigIntRepo()
geo_int_repo = GeoIntRepo()
im_int_repo = ImIntRepo()
financial_int_repo = FinancialIntRepo()
counter_int_repo = CounterIntRepo()
sit_rep_repo = SitRepRepo()
human_source_repo = HumanSourceRepo()
operator_intel_repo = OperatorIntelRepo()
gov_source_repo = GovSourceRepo()
report_data_repo = ReportDataRepo()
