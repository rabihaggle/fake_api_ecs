import pubchempy as pcp

chemical_formula = 'K2Cr2O7'

try:
    compound = pcp.get_compounds(chemical_formula, 'formula')[0]
    # Do something with the compound information
    print(f'Compound name: {compound.iupac_name}')
except IndexError:
    print(f'No compound found for formula: {chemical_formula}')
except Exception as e:
    print(f'An error occurred: {str(e)}')
