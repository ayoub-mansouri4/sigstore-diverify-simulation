# Sigstore + DiVerify Simulation

Ce projet simule et analyse les performances de la signature de code avec Sigstore et Sigstore + DiVerify. L'objectif est de mesurer l'impact de DiVerify sur le temps de signature, le temps système, et le temps total des processus de signature.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- Python 3.x
- pip (le gestionnaire de paquets Python)
- `Matplotlib` pour les visualisations graphiques (sera installé automatiquement via pip)

## Installation

   ```bash
   git clone https://github.com/ayoub-mansouri4/sigstore-diverify-simulation.git
   cd sigstore-diverify-simulation
   pip install matplotlib
   python3 src/benchmark.py

