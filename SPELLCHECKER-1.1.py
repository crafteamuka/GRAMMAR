import Levenshtein
from collections import Counter

# Use the provided words_list
words_list = [
    "aback", "abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding",
    "abject", "ablaze", "able", "abnormal", "aboard", "aboriginal", "abortive",
    "abounding", "abrasive", "abrupt", "absent", "absorbed", "absorbing", "abstracted",
    "absurd", "abundant", "abusive", "acceptable", "accessible", "accidental",
    "accurate", "acid", "acidic", "acoustic", "acrid", "actually", "ad hoc",
    "adamant", "adaptable", "addicted", "adhesive", "adjoining", "adorable",
    "adventurous", "afraid", "aggressive", "agonizing", "agreeable", "ahead", "ajar",
    "alcoholic", "alert", "alike", "alive", "alleged", "alluring", "aloof", "amazing",
    "ambiguous", "ambitious", "amuck", "amused", "amusing", "ancient", "angry",
    "animated", "annoyed", "annoying", "anxious", "apathetic", "aquatic", "aromatic",
    "arrogant", "ashamed", "aspiring", "assorted", "astonishing", "attractive",
    "auspicious", "automatic", "available", "average", "awake", "aware", "awesome",
    "awful", "axiomatic", "bad", "barbarous", "bashful", "bawdy", "beautiful",
    "befitting", "belligerent", "beneficial", "bent", "berserk", "best", "better",
    "bewildered", "big", "billowy", "bite-sized", "bitter", "bizarre", "black",
    "black-and-white", "bloody", "blue", "blue-eyed", "blushing", "boiling", "boorish",
    "bored", "boring", "bouncy", "boundless", "brainy", "brash", "brave", "brawny",
    "breakable", "breezy", "brief", "bright", "broad", "broken", "brown", "bumpy",
    "burly", "bustling", "busy", "cagey", "calculating", "callous", "calm", "capable",
    "capricious", "careful", "careless", "caring", "cautious", "ceaseless", "certain",
    "changeable", "charming", "cheap", "cheerful", "chemical", "chief", "childlike",
    "chilly", "chivalrous", "chubby", "chunky", "clammy", "classy", "clean", "clear",
    "clever", "cloistered", "cloudy", "closed", "clumsy", "cluttered", "coherent",
    "cold", "colorful", "colossal", "combative", "comfortable", "common", "complete",
    "complex", "concerned", "condemned", "confused", "conscious", "cooing", "cool",
    "cooperative", "coordinated", "courageous", "cowardly", "crabby", "craven",
    "crazy", "creepy", "crooked", "crowded", "cruel", "cuddly", "cultured",
    "cumbersome", "curious", "curly", "curved", "curvy", "cut", "cute", "cynical",
    "daffy", "daily", "damaged", "damaging", "damp", "dangerous", "dapper", "dark",
    "dashing", "dazzling", "dead", "deadpan", "deafening", "dear", "debonair",
    "decisive", "decorous", "deep", "deeply", "defeated", "defective", "defiant",
    "delicate", "delicious", "delightful", "demonic", "delirious", "dependent",
    "depressed", "deranged", "descriptive", "deserted", "detailed", "determined",
    "devilish", "didactic", "different", "difficult", "diligent", "direful", "dirty",
    "disagreeable", "disastrous", "discreet", "disgusted", "disgusting",
    "disillusioned", "dispensable", "distinct", "disturbed", "divergent", "dizzy",
    "domineering", "doubtful", "drab", "draconian", "dramatic", "dreary", "drunk",
    "dry", "dull", "dusty", "dynamic", "dysfunctional", "eager", "early",
    "earsplitting", "earthy", "easy", "eatable", "economic", "educated", "efficacious",
    "efficient", "eight", "elastic", "elated", "elderly", "electric", "elegant",
    "elfin", "elite", "embarrassed", "eminent", "empty", "enchanted", "enchanting",
    "encouraging", "endurable", "energetic", "enormous", "entertaining",
    "enthusiastic", "envious", "equable", "equal", "erect", "erratic", "ethereal",
    "evanescent", "evasive", "even", "excellent", "excited", "exciting", "exclusive",
    "exotic", "expensive", "extra-large", "extra-small", "exuberant", "exultant",
    "fabulous", "faded", "faint", "fair", "faithful", "fallacious", "false", "familiar",
    "famous", "fanatical", "fancy", "fantastic", "far", "far-flung", "fascinated",
    "fast", "fat", "faulty", "fearful", "fearless", "feeble", "feigned", "female",
    "fertile", "festive", "few", "fierce", "filthy", "fine", "finicky", "first",
    "five", "fixed", "flagrant", "flaky", "flashy", "flat", "flawless", "flimsy",
    "flippant", "flowery", "fluffy", "fluttering", "foamy", "foolish", "foregoing",
    "forgetful", "fortunate", "four", "frail", "fragile", "frantic", "free",
    "freezing", "frequent", "fresh", "fretful", "friendly", "frightened", "frightening",
    "full", "fumbling", "functional", "funny", "furry", "furtive", "future",
    "futuristic", "fuzzy", "gabby", "gainful", "gamy", "gaping", "garrulous", "gaudy",
    "general", "gentle", "giant", "giddy", "gifted", "gigantic", "glamorous", "gleaming",
    "glib", "glistening", "glorious", "glossy", "godly", "good", "goofy", "gorgeous",
    "graceful", "grandiose", "grateful", "gratis", "gray", "greasy", "great", "greedy",
    "green", "grey", "grieving", "groovy", "grotesque", "grouchy", "grubby", "gruesome",
    "grumpy", "guarded", "guiltless", "gullible", "gusty", "guttural", "habitual",
    "half", "hallowed", "halting", "handsome", "handsomely", "handy", "hanging",
    "hapless", "happy", "hard", "hard-to-find", "harmonious", "harsh", "hateful",
    "heady", "healthy", "heartbreaking", "heavenly", "heavy", "hellish", "helpful",
    "helpless", "hesitant", "hideous", "high", "highfalutin", "high-pitched", "hilarious",
    "hissing", "historical", "holistic", "hollow", "homeless", "homely", "honorable",
    "horrible", "hospitable", "hot", "huge", "hulking",
]

# Create a Counter from the words_list
WORDS = Counter(words_list)

def distance(word1, word2):
    return Levenshtein.distance(word1, word2)

def correction(word):
    # Suggest the closest match from the words_list
    closest_word = min(WORDS, key=lambda w: distance(word, w))
    return closest_word

# Get user input
input_word = input("Enter a word: ").strip()

# Predict the word the user wants
predicted_word = correction(input_word)
print(f"Did you mean: {predicted_word}?")
