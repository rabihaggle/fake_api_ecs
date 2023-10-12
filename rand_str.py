import random
import string
import pubchempy as pcp

def information(str_aa):
    length = 100
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def chemical_formula_information(chemical_formula):
    try:
        compound = pcp.get_compounds('CC', 'smiles', searchtype='superstructure', listkey_count=3)
        # Do something with the compound information
        return f'Compound name: {compound}'
    except IndexError:
        return  f'No compound found for formula: {chemical_formula}'
    except Exception as e:
        return f'An error occurred: {str(e)}'