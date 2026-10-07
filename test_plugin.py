import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLUGIN = ROOT / "motion-director"
RDC_KEY = "app-6a057d268ebc81919918d37eec718425"
RDC_ID = "asdk_app_6a057d268ebc81919918d37eec718425"


def test_marketplace_points_to_plugin():
    market = json.loads((ROOT / "marketplace.json").read_text(encoding="utf-8"))
    item = market["plugins"][0]
    assert market["name"] == "motion-director-plugins"
    assert item["name"] == "motion-director"
    assert item["source"] == {"source": "local", "path": "./motion-director"}


def test_required_remote_desktop_commander_dependency():
    plugin = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
    apps = json.loads((PLUGIN / ".app.json").read_text(encoding="utf-8"))["apps"]
    assert plugin["extensions"]["com.openai"]["apps"] == "./.app.json"
    assert apps[RDC_KEY] == {"id": RDC_ID, "required": True}
