PIPELINE_REPO: str = os.getenv("PIPELINE_REPO", "")
REPORTS_DIR: str = os.getenv("REPORTS_DIR", os.path.join(os.path.dirname(__file__), "..", "..", "sample_reports"))

import os
from pydantic import BaseModel

class Settings(BaseModel):
    PIPELINE_REPO: str = os.getenv("PIPELINE_REPO", "../nordstrom_m5_end2end")
    REPORTS_DIR: str = os.getenv("REPORTS_DIR", os.path.join(PIPELINE_REPO, "reports"))

settings = Settings()