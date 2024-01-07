def Constructable(m_Subset, m_Superset):
    # If the subset is longer than the superset, it cannot be a multiset subset.
    if len(m_Subset) > len(m_Superset):
        return "Not a multi subset"

    # Initialize an empty hashtable to store the characters in the subset.
    char_Hashtable = {}

    # For each character in the subset
    for char in m_Subset:
        # If the character is already in the hashtable, increment its count.
        if char in char_Hashtable:
            char_Hashtable[char] += 1
        # If the character is not in the hashtable, add it and set its count to 1.
        else:
            char_Hashtable[char] = 1

    # For each character in the superset
    for char in m_Superset:
        # If the character is in the hashtable, decrement its count.
        if char in char_Hashtable:
            char_Hashtable[char] -= 1
            # If the count of the character is 0 after decrementing, remove it from the hashtable.
            if char_Hashtable[char] == 0:
                del char_Hashtable[char]

    # If the hashtable is empty, the subset is a multiset subset of the superset.
    if len(char_Hashtable) == 0:
        return "Yes, it is a multi subset"
    # If the hashtable is not empty, the subset is not a multiset subset of the superset.
    else:
        return "Not a multi subset"
