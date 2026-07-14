from pathlib import Path
import tarfile
import zipfile

import build_backend
from macro_policy_thesis_map import __version__


ROOT = Path(__file__).resolve().parents[1]


def test_build_backend_version_matches_package():
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")

    assert f'version = "{__version__}"' in pyproject
    assert build_backend.VERSION == __version__


def test_build_backend_outputs_reproducible(tmp_path):
    first = tmp_path / "first"
    second = tmp_path / "second"
    first.mkdir()
    second.mkdir()

    wheel = build_backend.build_wheel(first)
    sdist = build_backend.build_sdist(first)

    assert build_backend.build_wheel(second) == wheel
    assert build_backend.build_sdist(second) == sdist
    assert (first / wheel).read_bytes() == (second / wheel).read_bytes()
    assert (first / sdist).read_bytes() == (second / sdist).read_bytes()

    with zipfile.ZipFile(first / wheel) as archive:
        names = set(archive.namelist())
    assert "macro_policy_thesis_map/examples/macro_events.csv" in names
    assert "macro_policy_thesis_map/examples/prior_macro_events.csv" in names
    assert "macro_policy_thesis_map/examples/public_macro_cases.csv" in names

    with tarfile.open(first / sdist) as archive:
        names = set(archive.getnames())
    assert f"{build_backend.DIST}/src/macro_policy_thesis_map/examples/macro_events.csv" in names
    assert f"{build_backend.DIST}/src/macro_policy_thesis_map/examples/prior_macro_events.csv" in names
    assert f"{build_backend.DIST}/src/macro_policy_thesis_map/examples/public_macro_cases.csv" in names
