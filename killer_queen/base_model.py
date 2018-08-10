from sqlalchemy.ext.declarative import declarative_base
from killer_queen.db import metadata

BaseModel = declarative_base(metadata=metadata)
