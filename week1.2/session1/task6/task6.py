# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    "ArtistName1" : "ArtistAlbum1",
    "ArtistName2" : "ArtistAlbum2",
    "ArtistName3" : "ArtistAlbum3"
}

# Pretty-print the data structure
pprint(music,stream=None, indent=155, width=80, depth=None,compact=False, sort_dicts=False, underscore_numbers=False)

# Display details of one album recorded by a specific artist
