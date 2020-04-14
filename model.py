from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql+psycopg2://postgres:pass@localhost/sqlachemy')
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Computers(Base):
    __tablename__ = 'computers'
    id = Column(Integer, primary_key=True)
    hard_drve_type = Column(String)
    processor = Column(Integer)
    amount_of_ram = Column(Integer)
    maximum_ram = Column(Integer)
    hard_drve_space = Column(Integer)
    form_factor= Column(String)
     
    def __init__(self, hard_drve_type, processor, amount_of_ram, maximum_ram, hard_drve_space, form_factor):
        self.hard_drve_type = hard_drve_type
        self.processor = processor
        self.amount_of_ram = maximum_ram
        self.hard_drve_space =hard_drve_space
        self.form_factor =form_factor

    def save_umuzi_computers(self):
        session.add(self)
        session.commit()
    
    def __repr__(self):
        return f'Computer: {self.id}'

Base.metadata.create_all(engine)



