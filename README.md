![GitHub contributors](https://img.shields.io/github/contributors/A-Cndt/IPSA_Formation_GIT?color=blue&label=Contributors&logo=GitHub)
![Branchs](https://badgen.net/badge/Branchs/2/blue?icon=github)

![GitHub last commit (branch)](https://img.shields.io/github/last-commit/A-Cndt/IPSA_Formation_GIT/main?label=Last%20Commit)
![GitHub issues](https://img.shields.io/github/issues/A-Cndt/IPSA_Formation_GIT?label=Issues)
![GitHub pull requests](https://img.shields.io/github/issues-pr/A-Cndt/IPSA_Formation_GIT?label=Pull%20Requests)
![GitHub milestones](https://img.shields.io/github/milestones/open/A-Cndt/IPSA_Formation_GIT?label=Open%20Milestones)

![GitHub top language](https://img.shields.io/github/languages/top/A-Cndt/IPSA_Formation_GIT?color=blueviolet&label=Language&logo=Python&logoColor=white)
![GitHub Release Date](https://img.shields.io/github/release-date/A-Cndt/IPSA_Formation_GIT?color=blueviolet&label=Release%20Date)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/A-Cndt/IPSA_Formation_GIT?color=blueviolet&label=Lastest%20Release)

# Introduction à l'usage de Git pour le contrôle de version
**IPSA 2022 - 2023**

Alexandre Condette - alexandre2.condette@ipsa.fr
---
*Introduction à Git pour les étudiants d'Aéro 3 et 4*
____

## Installer Git
Avant de lancer cette procédure, vérifiez que Git n'est pas déjà installé sur votre PC :
- Ouvrer un terminal
- Executer la commande suivante : 
```console
git --version
```

### Windows 
Télécharger l'exécutable directement depuis le site de GitHub : https://gitforwindows.org/

Pour installer l’outil, double cliquez simplement sur l’icone du fichier téléchargé. Une interface se lance alors et vous propose, page après page, de configurer l’installation de Git. Je vous conseil alors de laisser les valeurs par défaut et de simplement cliquer sur suivant.

Une fois arrivé sur la dernière page, il ne vous reste plus qu’à cliquer sur installer.

Vous venez alors d’installer les éléments suivants sur votre machine:
- L’outil Git.
- Git bash: terminal qui vous permet d’utiliser git en ligne de commande.
- Git gui: interface graphique qui permet de gérer les commits.
- Gitk: interface graphique qui permet de gérer l’historique de votre dépôt.

### Linux
#### Debian / Ubuntu 

```console
sudo apt-get update
sudo apt-get install git
```

#### Fedora

```console
sudo dnf install git
```

#### RedHat / CentOS

```console
sudo yum install git
```

### MacOs
Télécharger l'exécutable directement depuis le site de GitHub :  https://git-scm.com/download/mac (binary Installer)

#### Homebrew 
```console
brew install git
```

#### MacPorts
- Ouvrez le terminal et mettez à jour MacPorts
```console
sudo port selfupdate
```
- Recherchez les derniers ports Git disponibles et leurs variantes
```console
port search git
port variants git
```
- Installez Git
```console
sudo port install git +bash_completion +credential_osxkeychain +doc
```

