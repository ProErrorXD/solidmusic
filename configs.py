from dotenv import load_dotenv
from os import path, getenv, mkdir


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

if not path.exists("search"):
    mkdir("search")


class Configs:
    API_ID = int(getenv("API_ID", "1430775"))
    API_HASH = getenv("API_HASH", "b32cc3929f80e2a4f2ab1887ace693be")
    BOT_TOKEN = getenv("BOT_TOKEN", "1503940549:AAE0SQsXKkHTsV5ZUTGobTXYn5QzXIdX2ZY")
    OWNER_ID = int(getenv("OWNER_ID", "2007701745"))
    SESSION = getenv("SESSION", "BQCSoJsxcgqN9ze_Zw6UUa3eonlWRZC-MR8IBRsPRnXhs7YvZyE8fU04Qern9gl0Vko2Cay0IFw2bKPNsXcSOPEsHydwz3E1aJ4Romy2irAjPoiUKP8PwhD2pX28iAlm87xm9aMd1OKAePEvfRotOVdZAkhQ_ZnxuZW-FAPEoMmqBhJGnr7HyNMGBME1TmagJtJdEAcurkZYI50U-RrOVG6bxadcAI0kQh-p63NEpL2Jo2qKxNq6_oT0GATe5RLit5Qqz6x9ik7jrzBU_sEWyRf_ooq9V_XKCOYNkvcSLUZseskZLFReS6qA45xcIxwxPdf2sKdQly5bZsc2_RbtesBGVnZOIQA")
    CHANNEL_LINK = getenv("CHANNEL_LINK", "https://t.me/solidprojects")
    GROUP_LINK = getenv("GROUP_LINK", "https://t.me/solidprojects_chat")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/DoellBarr/solidmusic")


config = Configs()
