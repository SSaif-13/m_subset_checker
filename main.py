# Import the Constructable function from the checker module.
from checker import Constructable

# Define the superset and subset as strings
# In this case, both the superset and subset are 'I was one'
m_Superset = 'I was one'
m_Subset = 'I was one'

# Call the Constructable function with the subset and superset
# The Constructable function checks if the subset is a multiset subset of the superset
# It returns "Yes, it is a multi subset" if the subset is a multiset subset of the superset,
# and "Not a multi subset" otherwise.
# The result is printed to the console.
print(Constructable(m_Subset, m_Superset))
