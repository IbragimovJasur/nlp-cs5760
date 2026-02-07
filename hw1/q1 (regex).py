import re

# Task 1: Matches U.S. ZIP codes (12345 or 12345-6789 or 12345 6789)
pattern = r"\b\d{5}(?:[-\s]\d{4})?\b"
string="Zip code 1: 12345-6789. Zip code 2: 12345. Zip code 3: 12345 6789 Zip code 4: 123456789"
matches = re.findall(pattern, string)
print(matches)


# Task 2: Find all words that do not start with a capital letter. Words may include internal apostrophes/hyphens 
pattern = r"\b[a-z](?:[\w'-]*\w)?\b"
string = "Hello wOrld don't state-of-the-art"
matches = re.findall(pattern, string)
print(matches)


# Task 3: Match all numbers including numbers that may have: 
    #   a.	optional sign (+/-), 
    #   b.	optional thousands separators (commas),
    #   c.	optional decimal part
    #   d.	optional scientific notation (e.g., 1.23e-4).
pattern = r"[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:e[-+]\d+)?"
string="hello 1e-4 or 100e+1 or -5 43.54 3.40e-10 100,000 100.34e+1 hi 353,054.65 554.654e-4"
print(re.findall(pattern, string))


# Task 4: Match any spelling of “email”: email, e-mail, or e mail
string = "This is email, e-mail or e mail emailasdf"
matches = re.findall(r"\be[-\s]?mail\b", string)
print(matches)


# Task 5: Match the interjection go, goo, gooo, (one or more o) as a word, 
        # and allow an optional trailing punctuation mark ! . , ? (e.g., gooo!)
string = "gooooo and go? and goo, and gooo!, and finally goooo. go?lang"
matches = re.findall(r"\bgo+[\.!,\?]?", string)
print(matches)


# Task 6: Match lines that end with a question mark possibly followed only by closing quotes/brackets like ")”’] and spaces
matches = re.findall(r"^.*\?[\")'\]]*\s*$", "Hi There?)]  ")
print(matches)
