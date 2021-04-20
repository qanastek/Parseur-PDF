# Parseur-PDF

### Fonctionnement:

Vous trouverez ci-dessous le fonctionnement du programme implémenté pendant les sprints :

### Informations:

Ce logiciel a été develloppé durant le cours de Génie Logiciel de l'année universitaire 2019/2020 au CERI, Avignon University (France), par les étudiants suivants:

* Mohamed BEN YAMNA
* Quentin Capdepon
* Yanis Labrak
* Valentin Vougeot
* Zihao Zheng

### Extraction des nom des fichiers, titres et résumés:

Aller à la racine du repertoire où ce trouve les différents fichiers .PDF et lancer le programme à l'aide de:

TXT Output:

```console
user@user: python ../src/main/Extraction_Informations.py -t
> 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
```

XML Output:

```console
user@user: python ../src/main/Extraction_Informations.py -x
> 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
```

Vous trouverez par la suite un fichier **resultat.txt** ou **xml** à l'endroit où vous avez exécuté le programme.

### Dépendences

__Linux__:

```bash
xargs sudo apt-get install -y <packages.txt
```

ou

```bash
sudo apt install -y python3-pdfminer
```

__Python__:

```bash
pip install -r requirements.txt
```

* Python 2.7+ [Télécharger](https://www.python.org/download/releases/2.7/)
* Beautiful Soup 4 [Télécharger](https://pypi.org/project/beautifulsoup4/)
* Numpy [Télécharger](https://pypi.org/project/numpy/)