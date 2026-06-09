# PST Liège Data

## Projet

Analyse du Programme Stratégique Transversal (PST) de la Ville de Liège.

## Objectif

Évaluer certaines politiques publiques à l'aide de données ouvertes et produire des indicateurs reproductibles.

## Axes d'analyse

### Population

- Évolution de la population
- Structure par âge
- Répartition par sexe
- Répartition par nationalité
- Migrations résidentielles

### Environnement

- Arbres urbains
- Espaces verts
- Îlots de chaleur
- Qualité de l'air

### Attractivité et économie

- Entreprises
- Emploi
- Activité économique
- Mobilité domicile-travail

## Sources :

### PST Liège 2030

https://www.liege.be/fr/vie-communale/projet-de-ville/liege-2030

### Population Statbel

Population commune :  par lieu de résidence, nationalité, état civil, âge et sexe.
https://statbel.fgov.be/fr/open-data/population-par-lieu-de-residence-nationalite-etat-civil-age-et-sexe-14

Population secteur :
https://statbel.fgov.be/fr/open-data/population-par-secteur-statistique-12

Sectors déodata :
https://statbel.fgov.be/en/open-data/statistical-sectors-2025

Densité de la population ar secteurs statistiques 
https://walstat.iweps.be/walstat-catalogue.php?niveau_agre=Q&theme_id=1&indicateur_id=9201000&sel_niveau_catalogue=T&ordre=1#

Migrations entrantes et sortantes avec les communs limitrophes ou pas
!!! + delimitations geographiques de la province, l'arrondissement et la commune de Liège !!!
https://spi-digitalwallonia.opendatasoft.com/explore/dataset/migrations/information/?disjunctive.arrondissement&disjunctive.province&location=10,50.60427,5.58411&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkNPVU5UIiwieUF4aXMiOiJub21icmVfZF9lbnRyZWVzX2RlcHVpc191bmVfZGVzX2NvbW11bmVzX2RlX2xfYXJyb25kaXNzZW1lbnQiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjNjZjMmE1IiwicG9zaXRpb24iOiJjZW50ZXIifV0sInhBeGlzIjoidHlwZV9ldF9lbnRpdGUiLCJtYXhwb2ludHMiOm51bGwsInNvcnQiOiJzZXJpZTEtMSIsImNvbmZpZyI6eyJkYXRhc2V0IjoibWlncmF0aW9ucyIsIm9wdGlvbnMiOnsiZGlzanVuY3RpdmUuYXJyb25kaXNzZW1lbnQiOnRydWUsImRpc2p1bmN0aXZlLnByb3ZpbmNlIjp0cnVlLCJyZWZpbmUuYXJyb25kaXNzZW1lbnQiOiJBcnJvbmRpc3NlbWVudCBkZSBMaVx1MDBFOGdlIn19LCJzZXJpZXNCcmVha2Rvd24iOiIiLCJzZXJpZXNCcmVha2Rvd25UaW1lc2NhbGUiOiIifV0sInRpbWVzY2FsZSI6IiIsImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9

Deplacements travail 
https://mobilit.belgium.be/fr/documents-et-statistiques/open-data/mobilite-durable/enquete-des-deplacements-domicile-travail
    https://mobilit.belgium.be/fr/mobilite-durable/enquetes-et-resultats/enquete-sur-les-deplacements-domicile-travail/lenquete-sur


# Inspitations 
https://mobilit.belgium.be/fr/publications/analyse-des-deplacements-sur-base-de-donnees-issues-de-la-telephonie-mobile
file:///C:/Users/ST1803-04/Downloads/Mobilit%C3%A9%20et%20donn%C3%A9es%20t%C3%A9l%C3%A9com%20FR.pdf

## Structure du projet

data/
- Données brutes et préparées

notebooks/
- Exploration des données

src/
- Scripts Python réutilisables

docs/
- Documentation des sources

personal_docs/
- Documents de travail non publiés

powerbi/
- Rapports Power BI