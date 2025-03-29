import re

def find_mirror_words():
    text = input()
    pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'
    matches = re.findall(pattern, text)
    
    if not matches:
        print("No word pairs found!")
        print("No mirror words!")
        return
    
    valid_pairs = [match[1:] for match in matches]
    print(f"{len(valid_pairs)} word pairs found!")
    
    mirror_words = [f"{w1} <=> {w2}" for w1, w2 in valid_pairs if w1 == w2[::-1]]
    
    if mirror_words:
        print("The mirror words are:")
        print(", ".join(mirror_words))
    else:
        print("No mirror words!")

find_mirror_words()
