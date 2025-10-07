import spacy

MODEL_PATH = "mental_health_ner" 
nlp = spacy.load(MODEL_PATH)

MENTAL_HEALTH_CATEGORIES = {
    "Anxiety": {
        "keywords": [
            "anxious", "panic", "worried", "overthinking", "nervous", "uneasy", "tense", 
            "restless", "calm", "relaxed", "dread", "apprehensive", "jittery", "paranoid", 
            "on edge", "fearful", "hesitant"
        ],
        "intensity": {
            "suicide": 10, "panic": 9, "anxious": 8, "nervous": 7, "worried": 6, "overthinking": 7, 
            "uneasy": 5, "tense": 5, "restless": 5, "dread": 8, "apprehensive": 6, "jittery": 7, 
            "paranoid": 9, "on edge": 8, "fearful": 7, "hesitant": 4, "calm": 2, "relaxed": 1
        }
    },
    "Depression": {
        "keywords": [
            "sad", "hopeless", "worthless", "unmotivated", "empty", "down", "gloomy", 
            "lonely", "content", "hopeful", "miserable", "melancholy", "drained", 
            "isolated", "despair", "numb", "apathetic"
        ],
        "intensity": {
            "hopeless": 10, "depressed": 9, "worthless": 9, "sad": 7, "unmotivated": 6, 
            "empty": 8, "down": 5, "gloomy": 4, "lonely": 5, "miserable": 8, "melancholy": 7, 
            "drained": 7, "isolated": 9, "despair": 10, "numb": 9, "apathetic": 6, 
            "content": 2, "hopeful": 1, "happy": 1
        }
    },
    "Stress": {
        "keywords": [
            "stressed", "pressure", "overwhelmed", "burnout", "tension", "frustrated", 
            "exhausted", "agitated", "focused", "motivated", "irritable", "snappy", 
            "drained", "worked up", "short-tempered"
        ],
        "intensity": {
            "burnout": 10, "overwhelmed": 9, "stressed": 8, "pressure": 7, "tension": 6, 
            "frustrated": 5, "exhausted": 4, "agitated": 3, "irritable": 6, "snappy": 6, 
            "drained": 7, "worked up": 6, "short-tempered": 5, "focused": 2, "motivated": 1, 
            "sleepy": 2
        }
    },
    "Insomnia": {
        "keywords": [
            "can't sleep", "insomnia", "restless", "sleep-deprived", "awake", "nightmare", 
            "tossing", "turning", "well-rested", "refreshed", "wide awake", "sleepless", 
            "lethargic", "overtired", "exhausted", "night terrors"
        ],
        "intensity": {
            "insomnia": 10, "sleep-deprived": 9, "restless": 8, "can't sleep": 7, "awake": 6, 
            "nightmare": 5, "night terrors": 9, "tossing": 4, "turning": 3, "wide awake": 6, 
            "sleepless": 8, "lethargic": 5, "overtired": 6, "exhausted": 7, 
            "well-rested": 2, "refreshed": 1
        }
    },
    "Eating Disorder": {
        "keywords": [
            "not eating", "overeating", "binge eating", "starving", "food issue", 
            "skipping meals", "losing appetite", "craving food", "healthy eating", 
            "balanced diet", "purging", "underweight", "overweight", "dieting", "body image"
        ],
        "intensity": {
            "binge eating": 10, "starving": 9, "overeating": 8, "food issue": 7, 
            "not eating": 6, "skipping meals": 5, "losing appetite": 4, "purging": 9, 
            "underweight": 7, "overweight": 7, "dieting": 5, "body image": 6, 
            "craving food": 3, "healthy eating": 2, "balanced diet": 1
        }
    },
    "PTSD": {
        "keywords": [
            "flashback", "trauma", "nightmare", "panic attack", "startled", "hypervigilant", 
            "numb", "intrusive thoughts", "detached", "triggers", "shaking", "paranoia", 
            "dissociation", "fear", "jumpy"
        ],
        "intensity": {
            "flashback": 10, "trauma": 9, "nightmare": 8, "panic attack": 9, "startled": 7, 
            "hypervigilant": 8, "numb": 6, "intrusive thoughts": 9, "detached": 7, 
            "triggers": 9, "shaking": 7, "paranoia": 9, "dissociation": 10, "fear": 7, 
            "jumpy": 6
        }
    },
    "OCD": {
        "keywords": [
            "compulsive", "obsessive", "intrusive thoughts", "rituals", "checking", 
            "repeating", "cleaning", "contamination fear", "perfectionism", "fixation", 
            "uncontrollable urges"
        ],
        "intensity": {
            "compulsive": 9, "obsessive": 9, "intrusive thoughts": 10, "rituals": 8, 
            "checking": 6, "repeating": 7, "cleaning": 6, "contamination fear": 8, 
            "perfectionism": 5, "fixation": 7, "uncontrollable urges": 9
        }
    },
    "Social Anxiety": {
        "keywords": [
            "fear of judgment", "self-conscious", "social withdrawal", "nervous in crowds", 
            "avoidant", "blushing", "shaky voice", "afraid of talking", "overanalyzing", 
            "avoiding eye contact"
        ],
        "intensity": {
            "fear of judgment": 9, "self-conscious": 8, "social withdrawal": 9, 
            "nervous in crowds": 7, "avoidant": 8, "blushing": 6, "shaky voice": 5, 
            "afraid of talking": 7, "overanalyzing": 6, "avoiding eye contact": 5
        }
    },
    "Bipolar Disorder": {
        "keywords": [
            "manic", "elevated mood", "impulsive", "racing thoughts", "energetic", 
            "mood swings", "grandiose", "depressed", "low mood"
        ],
        "intensity": {
            "manic": 10, "elevated mood": 8, "impulsive": 7, "racing thoughts": 8, 
            "energetic": 6, "mood swings": 7, "grandiose": 9, "depressed": 9, "low mood": 7
        }
    },
    "Cyclothymia": {
        "keywords": [
            "mood fluctuations", "hypomania", "mild depression", "emotional instability", 
            "up and down", "unstable mood"
        ],
        "intensity": {
            "mood fluctuations": 7, "hypomania": 8, "mild depression": 6, 
            "emotional instability": 7, "up and down": 6, "unstable mood": 7
        }
    },
    "Seasonal Affective Disorder": {
        "keywords": [
            "winter blues", "seasonal depression", "low energy in winter", "sunlight deficit", 
            "darkness sadness", "seasonal mood"
        ],
        "intensity": {
            "winter blues": 6, "seasonal depression": 8, "low energy in winter": 7, 
            "sunlight deficit": 8, "darkness sadness": 7, "seasonal mood": 5
        }
    },
    "Phobia": {
        "keywords": [
            "fear of heights", "fear of spiders", "claustrophobic", "fear of flying", 
            "irrational fear", "avoidance", "phobia"
        ],
        "intensity": {
            "fear of heights": 8, "fear of spiders": 7, "claustrophobic": 9, 
            "fear of flying": 8, "irrational fear": 7, "avoidance": 6, "phobia": 9
        }
    },
    "Panic Disorder": {
        "keywords": [
            "panic attacks", "suffocating", "chest pain", "dizziness", "shaking", 
            "fear of dying", "loss of control"
        ],
        "intensity": {
            "panic attacks": 10, "suffocating": 9, "chest pain": 8, "dizziness": 7, 
            "shaking": 8, "fear of dying": 10, "loss of control": 9
        }
    },
    "Generalized Anxiety Disorder": {
        "keywords": [
            "constant worry", "overthinking", "uneasy", "tense all day", "excessive fear", 
            "can't relax"
        ],
        "intensity": {
            "constant worry": 8, "overthinking": 7, "uneasy": 6, "tense all day": 7, 
            "excessive fear": 8, "can't relax": 8
        }
    },
    "Borderline Personality Disorder": {
        "keywords": [
            "unstable", "fear of abandonment", "impulsive", "self-harm", "emotional swings", 
            "emptiness", "anger outbursts"
        ],
        "intensity": {
            "unstable": 8, "fear of abandonment": 9, "impulsive": 7, "self-harm": 10, 
            "emotional swings": 8, "emptiness": 9, "anger outbursts": 7
        }
    },
    "Narcissistic Personality Disorder": {
        "keywords": [
            "grandiosity", "ego", "lack of empathy", "self-centered", "superiority", 
            "attention seeking", "arrogant"
        ],
        "intensity": {
            "grandiosity": 9, "ego": 7, "lack of empathy": 8, "self-centered": 7, 
            "superiority": 8, "attention seeking": 6, "arrogant": 7
        }
    },
    "Antisocial Personality Disorder": {
        "keywords": [
            "manipulative", "reckless", "aggressive", "lack of remorse", 
            "impulsive violence", "law-breaking", "hostile"
        ],
        "intensity": {
            "manipulative": 8, "reckless": 7, "aggressive": 8, "lack of remorse": 9, 
            "impulsive violence": 10, "law-breaking": 9, "hostile": 7
        }
    },
    "Avoidant Personality Disorder": {
        "keywords": [
            "avoidant", "social inhibition", "fear of rejection", "low self-esteem", 
            "withdrawn", "shy", "sensitive"
        ],
        "intensity": {
            "avoidant": 8, "social inhibition": 9, "fear of rejection": 9, "low self-esteem": 7, 
            "withdrawn": 8, "shy": 6, "sensitive": 7
        }
    },
    "ADHD": {
        "keywords": [
            "distracted", "hyperactive", "impulsive", "restless", "inattentive", 
            "fidgeting", "can't focus", "forgetful"
        ],
        "intensity": {
            "distracted": 6, "hyperactive": 8, "impulsive": 7, "restless": 6, 
            "inattentive": 7, "fidgeting": 6, "can't focus": 7, "forgetful": 5
        }
    },
    "Autism Spectrum Disorder": {
        "keywords": [
            "social difficulties", "restricted interests", "repetitive behaviors", 
            "sensory overload", "nonverbal", "difficulty with eye contact"
        ],
        "intensity": {
            "social difficulties": 7, "restricted interests": 6, "repetitive behaviors": 7, 
            "sensory overload": 8, "nonverbal": 9, "difficulty with eye contact": 6
        }
    },
    "Learning Disorder": {
        "keywords": [
            "dyslexia", "difficulty reading", "difficulty writing", "slow learner", 
            "struggle in school", "academic issues"
        ],
        "intensity": {
            "dyslexia": 8, "difficulty reading": 7, "difficulty writing": 7, 
            "slow learner": 6, "struggle in school": 6, "academic issues": 6
        }
    },
    "Schizophrenia": {
        "keywords": [
            "hallucinations", "delusions", "paranoia", "disorganized speech", 
            "psychosis", "voices", "withdrawal"
        ],
        "intensity": {
            "hallucinations": 10, "delusions": 9, "paranoia": 8, "disorganized speech": 8, 
            "psychosis": 10, "voices": 9, "withdrawal": 7
        }
    },
    "Schizoaffective Disorder": {
        "keywords": [
            "hallucinations", "delusions", "depression with psychosis", 
            "mood swings with psychosis", "paranoia", "voices"
        ],
        "intensity": {
            "hallucinations": 10, "delusions": 9, "depression with psychosis": 9, 
            "mood swings with psychosis": 8, "paranoia": 8, "voices": 9
        }
    },
    "Delusional Disorder": {
        "keywords": [
            "paranoia", "jealousy", "delusional thinking", "false beliefs", 
            "suspicion", "grandiosity", "fixed ideas"
        ],
        "intensity": {
            "paranoia": 9, "jealousy": 7, "delusional thinking": 9, "false beliefs": 8, 
            "suspicion": 7, "grandiosity": 8, "fixed ideas": 7
        }
    },
    "Brief Psychotic Disorder": {
        "keywords": [
            "sudden psychosis", "hallucinations", "paranoia", "disorganized behavior", 
            "delusions", "confused speech"
        ],
        "intensity": {
            "sudden psychosis": 10, "hallucinations": 9, "paranoia": 8, 
            "disorganized behavior": 7, "delusions": 9, "confused speech": 7
        }
    },
    "Substance Use Disorder": {
        "keywords": [
            "alcohol", "drugs", "withdrawal", "cravings", "intoxicated", 
            "dependency", "relapse"
        ],
        "intensity": {
            "alcohol": 7, "drugs": 8, "withdrawal": 9, "cravings": 8, 
            "intoxicated": 7, "dependency": 9, "relapse": 9
        }
    },
    "Alcohol Use Disorder": {
        "keywords": [
            "alcoholic", "drunk", "hangover", "dependency", "withdrawal", 
            "binge drinking", "relapse"
        ],
        "intensity": {
            "alcoholic": 9, "drunk": 7, "hangover": 5, "dependency": 9, 
            "withdrawal": 8, "binge drinking": 9, "relapse": 8
        }
    },
    "Drug Addiction": {
        "keywords": [
            "drug use", "craving drugs", "high", "overdose", "withdrawal", 
            "dependency", "relapse"
        ],
        "intensity": {
            "drug use": 8, "craving drugs": 9, "high": 7, "overdose": 10, 
            "withdrawal": 9, "dependency": 9, "relapse": 9
        }
    },
    "Gambling Disorder": {
        "keywords": [
            "gambling", "betting", "compulsive gambling", "loss chasing", 
            "money problems", "casino addiction"
        ],
        "intensity": {
            "gambling": 8, "betting": 7, "compulsive gambling": 9, "loss chasing": 8, 
            "money problems": 7, "casino addiction": 9
        }
    },
    "Internet Addiction": {
        "keywords": [
            "screen addiction", "can't stop scrolling", "gaming addiction", 
            "social media obsession", "online all night", "digital overload"
        ],
        "intensity": {
            "screen addiction": 7, "can't stop scrolling": 8, "gaming addiction": 9, 
            "social media obsession": 7, "online all night": 8, "digital overload": 7
        }
    },
    "Workaholism": {
        "keywords": [
            "work addiction", "can't stop working", "overworking", "burnout", 
            "job stress", "always busy"
        ],
        "intensity": {
            "work addiction": 8, "can't stop working": 9, "overworking": 8, 
            "burnout": 9, "job stress": 7, "always busy": 6
        }
    },
    "Hoarding Disorder": {
        "keywords": [
            "can't throw things", "cluttered", "messy house", "excess possessions", 
            "hoarding", "compulsive saving"
        ],
        "intensity": {
            "can't throw things": 8, "cluttered": 6, "messy house": 7, 
            "excess possessions": 8, "hoarding": 9, "compulsive saving": 9
        }
    },
    "Body Dysmorphic Disorder": {
        "keywords": [
            "hate my body", "flaws", "ugly", "appearance anxiety", "body image", 
            "checking mirror", "self-conscious about looks"
        ],
        "intensity": {
            "hate my body": 9, "flaws": 7, "ugly": 8, "appearance anxiety": 8, 
            "body image": 7, "checking mirror": 6, "self-conscious about looks": 7
        }
    },
    "Trichotillomania": {
        "keywords": [
            "hair pulling", "can't stop pulling hair", "bald spots", "compulsive hair pulling"
        ],
        "intensity": {
            "hair pulling": 9, "can't stop pulling hair": 9, "bald spots": 8, 
            "compulsive hair pulling": 9
        }
    },
    "Excoriation Disorder": {
        "keywords": [
            "skin picking", "can't stop picking", "scabs", "bleeding skin", 
            "compulsive picking", "dermatillomania"
        ],
        "intensity": {
            "skin picking": 9, "can't stop picking": 9, "scabs": 7, "bleeding skin": 8, 
            "compulsive picking": 9, "dermatillomania": 9
        }
    },
    "Dissociative Identity Disorder": {
        "keywords": [
            "multiple personalities", "split identity", "alters", "memory gaps", 
            "dissociation", "different selves"
        ],
        "intensity": {
            "multiple personalities": 10, "split identity": 9, "alters": 9, 
            "memory gaps": 8, "dissociation": 9, "different selves": 8
        }
    },
    "Dissociative Amnesia": {
        "keywords": [
            "memory loss", "can't recall events", "forget trauma", "lost identity", 
            "gaps in memory"
        ],
        "intensity": {
            "memory loss": 8, "can't recall events": 9, "forget trauma": 9, 
            "lost identity": 10, "gaps in memory": 8
        }
    },
    "Depersonalization Disorder": {
        "keywords": [
            "out of body", "detached", "unreal feeling", "not myself", "dreamlike state"
        ],
        "intensity": {
            "out of body": 9, "detached": 8, "unreal feeling": 8, 
            "not myself": 9, "dreamlike state": 7
        }
    },
    "Somatic Symptom Disorder": {
        "keywords": [
            "physical symptoms", "pain", "fatigue", "nausea", "dizziness", 
            "aches", "unexplained symptoms"
        ],
        "intensity": {
            "physical symptoms": 7, "pain": 8, "fatigue": 7, "nausea": 6, 
            "dizziness": 6, "aches": 5, "unexplained symptoms": 7
        }
    },
}




def extract_mental_health_concerns(text):
    doc = nlp(text)
    concerns = [ent.text for ent in doc.ents if ent.label_ == "MENTAL_HEALTH_CONCERN"]
    return concerns

def classify_concern(concern_text):
    for category, data in MENTAL_HEALTH_CATEGORIES.items():
        if any(keyword in concern_text.lower() for keyword in data["keywords"]):
            return category
    return "Other"  

def score_intensity(concern_text):
    intensity_score = 0
    for category, data in MENTAL_HEALTH_CATEGORIES.items():
        for keyword, score in data["intensity"].items():
            if keyword in concern_text.lower():
                intensity_score = max(intensity_score, score)
    return intensity_score if intensity_score > 0 else 1  
