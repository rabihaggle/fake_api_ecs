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
    
    
def aspirin_info():
    try:
        compounds = pcp.get_compounds('Aspirin', 'name')
        if compounds:
            list_comp = []
            for comp in compounds:
                list_comp.append(comp.iupac_name)
            return f'Compound name: {list_comp}'
    except IndexError:
        return ' Ohhh Error !'
    except Exception as e:
        return f'An error occurred: {str(e)}'
    
def information_medicament(search):
    try:
        compounds = pcp.get_compounds(search, 'name')
        if compounds:
            list_comp = []
            list_synonyms = []
            for comp in compounds:
                list_comp.append(comp.iupac_name)
                list_synonyms.append(comp.synonyms)
        if len(list_synonyms) == 1:
            list_synonyms = list_synonyms[0]
            return list_comp, list_synonyms
    except IndexError:
        return f'Ohhh Error {search}'
    except Exception as e:
        return f'An error occurred: {str(e)}'
