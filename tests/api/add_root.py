import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

subprocess.run(
    [
        "datamodel-codegen",
        "--input", "api/swagger.json",
        "--input-file-type", "openapi",
        "--output-model-type", "pydantic_v2.BaseModel",
        "--preset", "standard-py312-20260619",
        "--formatters", "BUILTIN",
        "--output", "api/models.py",
    ],
    check=True,
)