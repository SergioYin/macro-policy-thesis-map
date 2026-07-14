"""Tiny offline PEP 517 backend for this zero-dependency project."""

from __future__ import annotations

import base64
import csv
import gzip
import hashlib
import io
import tarfile
import zipfile
from pathlib import Path


NAME = "macro-policy-thesis-map"
MODULE = "macro_policy_thesis_map"
ROOT = Path(__file__).resolve().parent


def _read_version() -> str:
    init_text = (ROOT / "src" / MODULE / "__init__.py").read_text(encoding="utf-8")
    for line in init_text.splitlines():
        if line.startswith("__version__"):
            return line.split("=", 1)[1].strip().strip('"')
    raise RuntimeError("could not read package version")


VERSION = _read_version()
DIST = f"{NAME}-{VERSION}"
DIST_INFO = f"{NAME.replace('-', '_')}-{VERSION}.dist-info"


def get_requires_for_build_wheel(config_settings=None):  # noqa: ANN001
    return []


def get_requires_for_build_sdist(config_settings=None):  # noqa: ANN001
    return []


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):  # noqa: ANN001
    dist_info = Path(metadata_directory) / DIST_INFO
    dist_info.mkdir(parents=True, exist_ok=True)
    (dist_info / "METADATA").write_text(_metadata(), encoding="utf-8")
    (dist_info / "WHEEL").write_text(_wheel_metadata(), encoding="utf-8")
    (dist_info / "entry_points.txt").write_text(_entry_points(), encoding="utf-8")
    return DIST_INFO


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):  # noqa: ANN001
    wheel_name = f"{NAME.replace('-', '_')}-{VERSION}-py3-none-any.whl"
    wheel_path = Path(wheel_directory) / wheel_name
    records: list[tuple[str, bytes]] = []
    with zipfile.ZipFile(wheel_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted((ROOT / "src" / MODULE).rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                rel = str(path.relative_to(ROOT / "src")).replace("\\", "/")
                data = path.read_bytes()
                _write_zip(archive, rel, data)
                records.append((rel, data))
        for rel, data in {
            f"{DIST_INFO}/METADATA": _metadata().encode("utf-8"),
            f"{DIST_INFO}/WHEEL": _wheel_metadata().encode("utf-8"),
            f"{DIST_INFO}/entry_points.txt": _entry_points().encode("utf-8"),
        }.items():
            _write_zip(archive, rel, data)
            records.append((rel, data))
        record_rel = f"{DIST_INFO}/RECORD"
        _write_zip(archive, record_rel, _record(records, record_rel).encode("utf-8"))
    return wheel_name


def build_sdist(sdist_directory, config_settings=None):  # noqa: ANN001
    sdist_name = f"{DIST}.tar.gz"
    sdist_path = Path(sdist_directory) / sdist_name
    with sdist_path.open("wb") as raw_file:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw_file, mtime=0) as gzip_file:
            with tarfile.open(fileobj=gzip_file, mode="w") as archive:
                for root_name in ["src", "tests", "examples", "demo", "skills"]:
                    for path in sorted((ROOT / root_name).rglob("*")):
                        if path.is_file() and "__pycache__" not in path.parts:
                            _add_tar_file(archive, path, f"{DIST}/{path.relative_to(ROOT)}")
                for rel in ["README.md", "LICENSE", "pyproject.toml", "build_backend.py", ".gitignore"]:
                    _add_tar_file(archive, ROOT / rel, f"{DIST}/{rel}")
                metadata = _metadata().encode("utf-8")
                archive.addfile(_tar_info(f"{DIST}/PKG-INFO", len(metadata)), io.BytesIO(metadata))
    return sdist_name


def _metadata() -> str:
    return (
        "Metadata-Version: 2.3\n"
        f"Name: {NAME}\n"
        f"Version: {VERSION}\n"
        "Summary: Zero-dependency static macro policy thesis mapping CLI.\n"
        "License-Expression: MIT\n"
        "Requires-Python: >=3.11\n"
        "Description-Content-Type: text/markdown\n\n"
        f"{(ROOT / 'README.md').read_text(encoding='utf-8')}\n"
    )


def _wheel_metadata() -> str:
    return "Wheel-Version: 1.0\nGenerator: macro-policy-thesis-map-build-backend\nRoot-Is-Purelib: true\nTag: py3-none-any\n"


def _entry_points() -> str:
    return "[console_scripts]\nmacro-policy-thesis-map = macro_policy_thesis_map.cli:main\n"


def _add_tar_file(archive: tarfile.TarFile, path: Path, arcname: str) -> None:
    data = path.read_bytes()
    archive.addfile(_tar_info(arcname, len(data)), io.BytesIO(data))


def _tar_info(arcname: str, size: int) -> tarfile.TarInfo:
    info = tarfile.TarInfo(arcname)
    info.size = size
    info.mtime = 0
    info.mode = 0o644
    info.uid = 0
    info.gid = 0
    info.uname = ""
    info.gname = ""
    return info


def _write_zip(archive: zipfile.ZipFile, rel: str, data: bytes) -> None:
    info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, data)


def _record(records: list[tuple[str, bytes]], record_rel: str) -> str:
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")
    for rel, data in records:
        digest = base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode("ascii")
        writer.writerow([rel, f"sha256={digest}", str(len(data))])
    writer.writerow([record_rel, "", ""])
    return output.getvalue()
