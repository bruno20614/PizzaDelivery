from databse import engine,Base
from models import User,Order

Base.metadata.Create_all(bind=engine)