# ToneMark
A computational linguistics demo exploring tonal ambiguity in Twi NLP
ToneMark
A computational linguistics demonstration tool exploring how the absence of tonal diacritics causes ambiguity and mistranslation in Twi NLP systems.
What is ToneMark?
Twi is a tonal language spoken in Ghana. In Twi, the same sequence of letters can carry completely different meanings depending on tone — yet most NLP tools, including Google Translate, process Twi text without tone marks. ToneMark demonstrates exactly what goes wrong when that happens.
The application has three tabs:

1. Tonal Minimal Pairs
Side-by-side comparisons of Twi words where tone alone distinguishes meaning. For example, papa can mean father (pàpá), good (pápá), or fan (pàpà) depending on tone pattern — yet without diacritics, an NLP model sees only "papa" and must guess.
2. Google Translate Failures
Real, live-tested examples where stripping tone marks causes Google Translate to produce wrong or nonsensical output. For example:

"kooko" → Google returns coconut, which is not a meaning of the word at all
"Kofi begyina ha" → Google returns coffee will stand here, mistranslating both a proper Ghanaian name and a grammatical tonal distinction

3. NLP Model Comparison
A side-by-side view of how NLP model predictions and confidence scores shift depending on whether tone marks are present or absent. Note: confidence scores are illustrative estimates based on documented NLP behaviour on low-resource tonal languages, not live model outputs.
Why this matters
Twi is a low-resource language. Most NLP benchmarks and tools are built for high-resource languages where tone is not phonemic. ToneMark makes the cost of that gap visible and concrete — word by word, translation by translation.
Built with

Python 3
Tkinter

Running the app
bashpython main.py
Data
All linguistic data — tonal minimal pairs, correct translations, and failure examples — was sourced from native speaker knowledge of Twi (Akan dialect).
