import re

def destination_mapper():
    text = input()
    pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"
    matches = re.findall(pattern, text)
    
    destinations = [match[1] for match in matches]
    travel_points = sum(len(dest) for dest in destinations)
    
    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {travel_points}")

destination_mapper()
