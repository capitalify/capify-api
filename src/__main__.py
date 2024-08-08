import os
import sys
from pathlib import Path

import uvicorn

# change dir to project root
os.chdir(Path(__file__).parents[1])

# get arguments from command
args = sys.argv[1:]

uvicorn.main.main(
    [
        "src.app:app",
        "--reload",
        "--use-colors",
        "--proxy-headers",
        "--forwarded-allow-ips=*",
        "--port=8000",
        *args,
    ]
)
