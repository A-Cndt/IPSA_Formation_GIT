# -*- coding utf-8 -*-
"""
===========================
Workshop Git - Code Exemple
===========================

Ceci est un code python d'exemple, développé dans le cadre de la formation Git
pour l'IPSA de Toulouse 2023

:Authors: - Alexandre Condette
:Date: 2023-04-06
:Version: 0.0.1

.. note::
    Ce code montre également un exemple de documentation en ReStructuredText (rst)
    utile pour la génération de doc automatique et l'ajout de tests avec doctest.

    Les docstrings sont les commentaires majeurs permettant d'expliquer le fonctionnement
    de chaque fonctions.
    Des commentaires supplémentaires sont ajoutables dans le code, mais n'apparaitront pas
    dans la doc générée
"""

#-------------------------------
#%% Import de modules
import numpy as np
import matplotlib.pyplot as plt
import doctest
import logging
import logging.config
from pathlib import Path

# ------------------------------
#%% Variables Hard-Codées
current_path = Path().absolute()

# ------------------------------
#%% Utils
#logging.config.fileConfig(fname = current_path / "config" / "logging.conf")
#logger = logging.getLogger()

# ------------------------------
#%% Fonction "somme"
def somme(a, b):
    """
    Fonction qui retourne la somme de deux nombres flottants

    :param float a: Nombre flottant 1 à additionner
    :param float b: Nombre flottant 2 à additionner
    
    :return S: La somme a + b
    :rtype: float

    **Exemple :**
    ::

    >>> somme(5, 10)
    15

    """

    S = a + b
    return S

#%% Main
if __name__ == "__main__":
    Test = doctest.testmod(verbose=True)
    print(Test)

    #logger.info("\n[Test du script 'Main.py']\n \
    #    {resultats}\n"
    #    .format(resultats=Test))
