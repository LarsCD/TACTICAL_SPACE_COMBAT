"""
by: LarsCD2002
started: 6/1/2024

SOURCES
    - Nebulous: Fleet Command (inspiration for ship/system stats)
    - https://www.youtube.com/watch?v=bImISkF76T8 (inspiration for ship/system stats)


"""

"""
FileIO testing
Testing if importing data works right 
"""
from src.engine.utilities.file_IO.dataloader import Dataloader

STATIC_DATA = Dataloader().load_all_data()
print(STATIC_DATA)

print("""-------------------------------- [VESSEL INFO] --------------------------------


""")

"""
Creating classes
Testing if creation of all classes works
"""
input('\n[ENTER]: EXIT')
