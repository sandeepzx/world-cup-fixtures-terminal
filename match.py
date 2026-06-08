import os
import requests
from dotenv import load_dotenv
from difflib import get_close_matches
from datetime import datetime, timezone, timedelta


load_dotenv()
API_KEY = os.getenv("FOOTBALL_API_KEY")

IST = timezone(timedelta(hours=5, minutes=30))

teams_list = [
    "Uruguay",
    "Germany",
    "Spain",
    "Paraguay",
    "Argentina",
    "Ghana",
    "Brazil",
    "Portugal",
    "Japan",
    "Mexico",
    "England",
    "United States",
    "South Korea",
    "France",
    "South Africa",
    "Algeria",
    "Australia",
    "New Zealand",
    "Switzerland",
    "Ecuador",
    "Sweden",
    "Czechia",
    "Croatia",
    "Saudi Arabia",
    "Tunisia",
    "Turkey",
    "Senegal",
    "Belgium",
    "Morocco",
    "Austria",
    "Colombia",
    "Egypt",
    "Canada",
    "Haiti",
    "Iran",
    "Bosnia-Herzegovina",
    "Panama",
    "Cape Verde Islands",
    "Congo DR",
    "Ivory Coast",
    "Qatar",
    "Jordan",
    "Iraq",
    "Uzbekistan",
    "Netherlands",
    "Norway",
    "Scotland",
    "Curaçao"
]

headers = {
    "X-Auth-Token": API_KEY
}

r = requests.get(
    "https://api.football-data.org/v4/competitions/WC/matches",
    headers=headers
)
data = r.json()

user_input = input("Team: ")

teamn_name = get_close_matches(user_input, teams_list, n=1, cutoff=0.6)
team = teamn_name[0]  
if "matches" not in data:
    print("API Error Response:")
    print(data)
    exit()
    
print(f"{team}'s Fixtures are")
for match in data["matches"]:
    home = match["homeTeam"]["name"]
    away = match["awayTeam"]["name"]

    if team in (home, away):
        utc_dt = datetime.strptime(match["utcDate"], "%Y-%m-%dT%H:%M:%SZ")
        utc_dt = utc_dt.replace(tzinfo=timezone.utc)
        ist_dt = utc_dt.astimezone(IST)

        print(
            ist_dt.strftime("%Y-%m-%d %I:%M %p"), " - ",
            home,
            "vs",
            away
        )



