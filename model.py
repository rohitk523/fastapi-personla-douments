from pydantic import BaseModel
from sqlalchemy import  Column, Integer, String

from database import Base


class Documentinfo(Base):
    __tablename__ = "documentinfo"
    
    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String)
    aadhar = Column(String)
    pan = Column(String)
    phone = Column(Integer)
    
class Docs(BaseModel):
	id: int
	user: str
	aadhar: str
	pan: str
	phone: int

# allDocuments = [{
#   "User": "Rohit",
#   "Aadhar": "R873",
#   "Pan": "P789",
#   "Phone": 8037
# },
# {
#   "User": "Renuka",
#   "Aadhar": "R348",
#   "Pan": "P748",
#   "Phone": 4948
# },
# {
#   "User": "Sunita",
#   "Aadhar": "S3940",
#   "Pan": "P348",
#   "Phone": 9233
# }]
