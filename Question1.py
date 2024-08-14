# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

def format_itineraries(itinerary_list):

    "Format a list of flight itineraries into a string.
    
    Args:
    itinerary_list (list of tuples): Each tuple contains (traveler_name, origin, destination).
    
    Returns:
    str: Formatted string listing each itinerary."
    formatted_itineraries = []
    
    for index, (traveler_name, origin, destination) in enumerate(itinerary_list, start=1):
        itinerary = f"Itinerary {index}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(itinerary)
    
    return "\n".join(formatted_itineraries)

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_string = format_itineraries(itineraries)
print(formatted_string)


