# Nesting
capitals = {"France": "Paris", "Germany": "Berlin",
            }

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a Dictionary in a Dictionary
travel_log_V2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12, },
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting a Dictionary in a List
travel_log_V3 = [
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12, },
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
]
