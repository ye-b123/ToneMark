# -*- coding: utf-8 -*-
# Dictionary of Twi tonal minimal pairs
# Each entry contains the plain form and its tonal variants with meanings

tonePairs = {
    "papa": {
        "description": "A word where tone distinguishes noun and adjective meanings",
        "category": "noun/adjective",
        "variants": [
            {"form": "pàpá", "tone_pattern": "low-high", "meaning": "father"},
            {"form": "pápá", "tone_pattern": "high-high", "meaning": "good"},
            {"form": "pàpà", "tone_pattern": "low-low", "meaning": "fan (object used for fanning)"},
        ]
    },
    "kooko": {
        "description": "A noun where tone distinguishes two different meanings",
        "category": "noun",
        "variants": [
            {"form": "kóókó", "tone_pattern": "high-high", "meaning": "porridge"},
            {"form": "kòòkó", "tone_pattern": "low-high", "meaning": "haemorrhoid"},
        ]
    },
    "ha": {
        "description": "A verb where tone distinguishes two different meanings",
        "category": "verb",
        "variants": [
            {"form": "há", "tone_pattern": "high", "meaning": "to disturb/here"},
            {"form": "hà", "tone_pattern": "low", "meaning": "to be light in weight"},
        ]
    },
    "da": {
        "description": "A word where tone distinguishes a noun from an adverb",
        "category": "noun/adverb",
        "variants": [
            {"form": "dá", "tone_pattern": "high", "meaning": "day"},
            {"form": "dà", "tone_pattern": "low", "meaning": "never"},
        ]
    },
    "dada": {
        "description": "A word where tone distinguishes an adjective from an adverb",
        "category": "adjective/adverb",
        "variants": [
            {"form": "dádá", "tone_pattern": "high-high", "meaning": "old"},
            {"form": "dàdà", "tone_pattern": "low-low", "meaning": "already"},
        ]
    },
    "koto": {
        "description": "A verb where tone distinguishes habitual from stative action",
        "category": "verb",
        "variants": [
            {"form": "kótó", "tone_pattern": "high-high", "meaning": "to squat (habitual — one who regularly squats)"},
            {"form": "kòtò", "tone_pattern": "low-low", "meaning": "to squat (stative — one who is currently squatting)"},
        ]
    },
    "be": {
        "description": "A prefix where tone distinguishes future tense from ingressive aspect",
        "category": "verbal prefix",
        "variants": [
            {"form": "bɛ́gyìná", "tone_pattern": "high", "meaning": "future marker — will (e.g. Kofi bɛ́gyìná há — Kofi will stand here)"},
            {"form": "bɛ̀gyìná", "tone_pattern": "low", "meaning": "ingressive prefix — come and (e.g. Kofi bɛ̀gyìná há — Kofi come and stand here)"},
        ]
    },
}

# Google Translate failure examples
googleTranslate = [
    {   
        "input": "papa",
        "googleTranslateOutput": "good",
        "correctTranslations": ["father (pàpá)", "good (pápá)", "fan (pàpà)"],
        "explanation": "Google Translate picks only one meaning — 'good' — ignoring that 'papa' has three distinct meanings depending on tone. A native speaker would need tone marks to know which meaning is intended."
    },
    {
        "input": "kooko",
        "googleTranslateOutput": "coconut",
        "correctTranslations": ["porridge (kóókó)", "haemorrhoid (kòòkó)"],
        "explanation": "Google Translate returns 'coconut' — which is not a meaning of 'kooko' in Twi at all. Without tone marks the model is completely lost, producing a meaning that does not exist in the language."
    },
    {
        "input": "Kofi begyina ha",
        "googleTranslateOutput": "coffee will stand here",
        "correctTranslations": [
            "Kofi will stand here (Kofi bɛ́gyìná há — future marker)",
            "Kofi come and stand here (Kofi bɛ̀gyìná há — ingressive prefix)"
        ],
        "explanation": "Two errors in one sentence. First, 'Kofi' (a common Ghanaian name) is mistranslated as 'coffee'. Second, the tonal distinction between the future marker bɛ́ and the ingressive prefix bɛ̀ is completely lost — the model cannot tell whether this is a statement about the future or a directive."
    },
    
    {
        "input": "ha",
        "googleTranslateOutput": "here",
        "correctTranslations": ["to disturb (há — high tone)", "here (há — high tone)", "to be light in weight (hà — low tone)"],
        "explanation": "Google Translate returns only 'here' — one of the high tone meanings. It completely misses 'to disturb' and 'to be light in weight'. Without tone marks the model cannot distinguish between these meanings at all."
    },
]

# NLP Model Comparison data
nlpComparison = [
    {
        "word": "papa",
        "with_tone": {
            "input": "pàpá",
            "prediction": "father",
            "confidence": 91,
            "explanation": "With tone marks the model correctly identifies 'pàpá' as 'father' with high confidence."
        },
        "without_tone": {
            "input": "papa",
            "prediction": "good",
            "confidence": 38,
            "explanation": "Without tone marks the model guesses 'good' — one of three possible meanings — with low confidence."
        }
    },
    {
        "word": "kooko",
        "with_tone": {
            "input": "kóókó",
            "prediction": "porridge",
            "confidence": 88,
            "explanation": "With tone marks the model correctly identifies 'kóókó' as 'porridge'."
        },
        "without_tone": {
            "input": "kooko",
            "prediction": "coconut",
            "confidence": 29,
            "explanation": "Without tone marks the model produces 'coconut' — a meaning that does not exist in Twi at all."
        }
    },
    {
        "word": "ha",
        "with_tone": {
            "input": "há",
            "prediction": "here / to disturb",
            "confidence": 85,
            "explanation": "With tone marks the model correctly identifies the high tone meaning."
        },
        "without_tone": {
            "input": "ha",
            "prediction": "here",
            "confidence": 42,
            "explanation": "Without tone marks the model picks only 'here', completely missing 'to disturb' and 'to be light in weight'."
        }
    },
]



