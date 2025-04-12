import base64
from pathlib import Path


# Function to load NHL logos
def load_team_logos():
    logos = {}
    logos_path = Path("assets/images") / "NHL Logos"
    for img_path in sorted(logos_path.glob("*.png")):
        team_name = img_path.stem
        with open(img_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            logos[team_name] = f"data:image/png;base64,{encoded}"
    return logos


# We get the NHL logos
TEAM_LOGOS = load_team_logos()
