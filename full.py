import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta


load_dotenv()
API_KEY = os.getenv("FOOTBALL_API_KEY")

IST = timezone(timedelta(hours=5, minutes=30))

headers = {
    "X-Auth-Token": API_KEY
}

r = requests.get(
    "https://api.football-data.org/v4/competitions/WC/matches",
    headers=headers
)
data = r.json()

if "matches" not in data:
    print("API Error Response:")
    print(data)
    exit()
    
print(f"Fixtures are")
for match in data["matches"]:
    home = match["homeTeam"]["name"]
    away = match["awayTeam"]["name"]

    utc_dt = datetime.strptime(match["utcDate"], "%Y-%m-%dT%H:%M:%SZ")
    utc_dt = utc_dt.replace(tzinfo=timezone.utc)
    ist_dt = utc_dt.astimezone(IST)

    print(
        ist_dt.strftime("%Y-%m-%d %I:%M %p"), " - ",
        home,
        "vs",
        away
    )



