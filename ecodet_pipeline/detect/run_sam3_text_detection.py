#!/usr/bin/env python3
"""Run local SAM3 text-prompt detection for the EcoDet pipeline.

Thin CLI wrapper around ``ecodet_pipeline.detect.sam3_text.inference.main``. Run either
as a module (``python -m ecodet_pipeline.detect.run_sam3_text_detection ...``) or as a
script; in script mode it puts the repo root on ``sys.path`` so the package resolves.
"""
from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    # invoked as a bare script: ensure the repo root (which contains ecodet_pipeline/)
    # is importable.
    REPO_ROOT = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(REPO_ROOT))

from ecodet_pipeline.detect.sam3_text.inference import main


if __name__ == "__main__":
    raise SystemExit(main())
