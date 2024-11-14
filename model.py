from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Consulta(Base):
    __tablename__ = 'tbl_consulta'
    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey('tbl_paciente.id'), nullable= False)
    doctor_id = Column(Integer, ForeignKey('tbl_doctor.id'), nullable= False)
    descripcion = Column(String, nullable= False)

    paciente = relationship("Paciente", back_populates="consulta")
    doctor = relationship("Doctor", back_populates="consulta")

class Doctor(Base):
    __tablename__ = 'tbl_doctor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable= False)
    apellido = Column(String, nullable= False)
    especialidad = Column(String, nullable= False)

    consultas = relationship("Consulta", back_populates="doctor")

class Paciente(Base):
    __tablename__ = 'tbl_paciente'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable= False)
    apellido = Column(String, nullable= False)
    edad = Column(Integer, nullable= False)

    consulta = relationship("Consulta", back_populates="paciente")

engine = create_engine('sqlite:///clinica.db', echo=True)

Base.metadata.create_all(engine)
