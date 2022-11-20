"""
Modify SMILES String

Contents:
    DChemPy.Chem.NormalizeSmiles: Change SMILES into RDKit's standard format.
"""


from rdkit import Chem


def NormalizeSmiles(smi):
    """
    :param smi: SMILES String
    :return: SMILES String with RDKit's standard format
    """
    n_smi = Chem.MolToSmiles(Chem.MolFromSmiles(smi))
    print(n_smi)
    return n_smi

