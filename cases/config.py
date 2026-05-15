# controlling the order of levels , which level must be completed before the next
LEVEL_ORDER = ["Junior", "Senior", "Head", "Chief", "CEO"]

LEVEL_REQUIREMENTS = {
    "Junior": None,
    "Senior": "Junior",
    "Head": "Senior",
    "Chief": "Head",
    "CEO": "Chief",
}