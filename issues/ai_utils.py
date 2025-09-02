import re

KEYWORDS = {
    'road': ['pothole','speed breaker','road','street','crossing','asphalt','lane'],
    'garbage': ['garbage','trash','waste','dump','litter','unclean','dustbin','sanitation'],
    'water': ['leak','water','sewage','drain','pipeline','tap','flood'],
    'electricity': ['light','streetlight','power','electric','transformer','wire','voltage','bulb'],
}

def categorize(text: str) -> str:
    if not text:
        return 'other'
    t = text.lower()
    for cat, words in KEYWORDS.items():
        for w in words:
            if re.search(r'\b' + re.escape(w) + r'\b', t):
                return cat
    return 'other'
