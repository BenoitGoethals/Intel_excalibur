"""
SQLAlchemy ORM for standalone intel types (no BaseIntel inheritance):
MasInt, MedInt, TechInt, SigInt, GeoInt, ImInt, FinancialInt, CounterInt, SitRep.
Also helper tables: ListItem, ListItemDate, ListItemPhoto,
HumanSource, OperatorIntel, GovSource, ReportData.
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional
from sqlalchemy import String, Integer, Float, Boolean, DateTime, JSON, LargeBinary, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from model.orm.base import Base


class ListItemOrm(Base):
    __tablename__ = "list_item"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    text: Mapped[Optional[str]] = mapped_column(String, nullable=True)


class ListItemDateOrm(Base):
    __tablename__ = "list_item_date"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    dtg: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class ListItemPhotoOrm(Base):
    __tablename__ = "list_item_photo"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    file_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    text: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    picture: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)


class HumanSourceOrm(Base):
    __tablename__ = "human_source"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    name: Mapped[str] = mapped_column(String, default="")
    for_name: Mapped[str] = mapped_column(String, default="")
    additional_info: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    dtg_injected: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class OperatorIntelOrm(Base):
    __tablename__ = "operator_intel"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    for_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    serial_nbr: Mapped[Optional[str]] = mapped_column(String, nullable=True)


class GovSourceOrm(Base):
    __tablename__ = "gov_source"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    source_name: Mapped[str] = mapped_column(String, default="")
    source_type: Mapped[str] = mapped_column(String, default="")
    source_agency: Mapped[str] = mapped_column(String, default="")
    reliability_rating: Mapped[int] = mapped_column(Integer, default=0)
    clearance_level: Mapped[str] = mapped_column(String, default="")
    contact_name: Mapped[str] = mapped_column(String, default="")
    contact_title: Mapped[str] = mapped_column(String, default="")
    contact_phone_number: Mapped[str] = mapped_column(String, default="")
    contact_email: Mapped[str] = mapped_column(String, default="")
    intelligence_contributions: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    operational_status: Mapped[str] = mapped_column(String, default="")
    last_contact_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class ReportDataOrm(Base):
    __tablename__ = "report_data"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    type_base_line: Mapped[str] = mapped_column(String(50), default="Other")
    count: Mapped[int] = mapped_column(Integer, default=0)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)


class MasIntOrm(Base):
    __tablename__ = "mas_int"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    mas_int_type: Mapped[str] = mapped_column(String(30), default="ACINT")
    measurement_type: Mapped[str] = mapped_column(String, default="")
    measurement_value: Mapped[float] = mapped_column(Float, default=0.0)
    measurement_unit: Mapped[str] = mapped_column(String, default="")
    signature_analysis: Mapped[str] = mapped_column(String, default="")
    target_name: Mapped[str] = mapped_column(String, default="")
    target_location: Mapped[str] = mapped_column(String, default="")
    latitude: Mapped[float] = mapped_column(Float, default=0.0)
    longitude: Mapped[float] = mapped_column(Float, default=0.0)
    weather_conditions: Mapped[str] = mapped_column(String, default="")
    atmospheric_conditions: Mapped[str] = mapped_column(String, default="")
    analysis: Mapped[str] = mapped_column(String, default="")
    findings: Mapped[str] = mapped_column(String, default="")
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)


class MedIntOrm(Base):
    __tablename__ = "med_int"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    patient_name: Mapped[str] = mapped_column(String, default="")
    age: Mapped[int] = mapped_column(Integer, default=0)
    gender: Mapped[str] = mapped_column(String(10), default="")
    diagnosis: Mapped[str] = mapped_column(String, default="")
    symptoms: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    treatments: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    facility_name: Mapped[str] = mapped_column(String, default="")
    facility_location: Mapped[str] = mapped_column(String, default="")
    provider_name: Mapped[str] = mapped_column(String, default="")
    provider_contact: Mapped[str] = mapped_column(String, default="")
    analysis: Mapped[str] = mapped_column(String, default="")
    findings: Mapped[str] = mapped_column(String, default="")
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)


class TechIntOrm(Base):
    __tablename__ = "tech_int"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    technology_name: Mapped[str] = mapped_column(String, default="")
    manufacturer: Mapped[str] = mapped_column(String, default="")
    model: Mapped[str] = mapped_column(String, default="")
    technical_specifications: Mapped[str] = mapped_column(String, default="")
    acquisition_source: Mapped[str] = mapped_column(String, default="")
    acquisition_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    cost: Mapped[Decimal] = mapped_column(Numeric(precision=18, scale=4), default=0)
    usage_history: Mapped[str] = mapped_column(String, default="")
    performance_analysis: Mapped[str] = mapped_column(String, default="")
    compatible_technologies: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    integration_details: Mapped[str] = mapped_column(String, default="")
    analysis: Mapped[str] = mapped_column(String, default="")
    findings: Mapped[str] = mapped_column(String, default="")
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)


class SigIntOrm(Base):
    __tablename__ = "sig_int"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    signal_type: Mapped[str] = mapped_column(String, default="")
    signal_frequency: Mapped[str] = mapped_column(String, default="")
    signal_source: Mapped[str] = mapped_column(String, default="")
    intercept_date_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    sender: Mapped[str] = mapped_column(String, default="")
    receiver: Mapped[str] = mapped_column(String, default="")
    message_content: Mapped[str] = mapped_column(String, default="")
    analysis: Mapped[str] = mapped_column(String, default="")
    interpretation: Mapped[str] = mapped_column(String, default="")
    sender_location: Mapped[str] = mapped_column(String, default="")
    receiver_location: Mapped[str] = mapped_column(String, default="")
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)


class GeoIntOrm(Base):
    __tablename__ = "geo_int"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    target_location: Mapped[str] = mapped_column(String, default="")
    latitude: Mapped[float] = mapped_column(Float, default=0.0)
    longitude: Mapped[float] = mapped_column(Float, default=0.0)
    imagery_sources: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    maps: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    terrain_description: Mapped[str] = mapped_column(String, default="")
    infrastructure_details: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    weather_conditions: Mapped[str] = mapped_column(String, default="")
    natural_hazards: Mapped[str] = mapped_column(String, default="")
    analysis: Mapped[str] = mapped_column(String, default="")
    interpretation: Mapped[str] = mapped_column(String, default="")
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)


class ImIntOrm(Base):
    __tablename__ = "im_int"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    image_name: Mapped[str] = mapped_column(String, default="")
    image_source: Mapped[str] = mapped_column(String, default="")
    capture_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    image_format: Mapped[str] = mapped_column(String, default="")
    target_name: Mapped[str] = mapped_column(String, default="")
    target_location: Mapped[str] = mapped_column(String, default="")
    latitude: Mapped[float] = mapped_column(Float, default=0.0)
    longitude: Mapped[float] = mapped_column(Float, default=0.0)
    image_analysis: Mapped[str] = mapped_column(String, default="")
    key_features: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    interpretation: Mapped[str] = mapped_column(String, default="")
    findings: Mapped[str] = mapped_column(String, default="")
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)


class FinancialIntOrm(Base):
    __tablename__ = "financial_int"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    transaction_type: Mapped[str] = mapped_column(String, default="")
    amount: Mapped[Decimal] = mapped_column(Numeric(precision=18, scale=4), default=0)
    transaction_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    counterparty: Mapped[str] = mapped_column(String, default="")
    involved_parties: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    suspicious_activity_description: Mapped[str] = mapped_column(String, default="")
    regulatory_compliance_status: Mapped[str] = mapped_column(String, default="")
    investigating_agency: Mapped[str] = mapped_column(String, default="")
    investigation_start_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    investigation_status: Mapped[str] = mapped_column(String, default="")
    investigation_findings: Mapped[str] = mapped_column(String, default="")
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)


class CounterIntOrm(Base):
    __tablename__ = "counter_int"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    operation_name: Mapped[str] = mapped_column(String, default="")
    operation_start_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    operation_end_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    targets: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    suspects: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    tactics_used: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    techniques_used: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    intelligence_sources: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    analysis: Mapped[str] = mapped_column(String, default="")
    findings: Mapped[str] = mapped_column(String, default="")
    countermeasures: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    recommendations: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)


class SitRepOrm(Base):
    __tablename__ = "sit_rep"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    case_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True, index=True)
    report_date_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    reporting_unit: Mapped[str] = mapped_column(String, default="")
    location: Mapped[str] = mapped_column(String, default="")
    enemy_disposition: Mapped[str] = mapped_column(String, default="")
    enemy_capabilities: Mapped[str] = mapped_column(String, default="")
    friendly_disposition: Mapped[str] = mapped_column(String, default="")
    friendly_capabilities: Mapped[str] = mapped_column(String, default="")
    civilian_considerations: Mapped[str] = mapped_column(String, default="")
    weather_conditions: Mapped[str] = mapped_column(String, default="")
    terrain_analysis: Mapped[str] = mapped_column(String, default="")
    other_information: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    recommendations: Mapped[str] = mapped_column(String, default="")
    future_plans: Mapped[str] = mapped_column(String, default="")
