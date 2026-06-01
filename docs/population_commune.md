# Population Statbel

## Source

Population par lieu de résidence, nationalité, état civil, âge et sexe.

## Description

Chaque ligne représente un groupe d'individus défini par :

* une commune
* un sexe
* une nationalité
* un état civil
* un âge

La colonne `MS_POPULATION` contient le nombre d'individus correspondant à cette combinaison.

## Colonnes

| Nom                  | Description                  |
| -------------------- | ---------------------------- |
| CD_REFNIS            | Code INS de la commune       |
| TX_DESCR_FR          | Nom de la commune            |
| CD_DSTR_REFNIS       | Code INS de l'arrondissement |
| TX_ADM_DSTR_DESCR_FR | Nom de l'arrondissement      |
| CD_PROV_REFNIS       | Code INS de la province      |
| TX_PROV_DESCR_FR     | Nom de la province           |
| CD_RGN_REFNIS        | Code INS de la région        |
| TX_RGN_DESCR_FR      | Nom de la région             |
| CD_SEX               | Sexe                         |
| CD_NATLTY            | Code nationalité             |
| TX_NATLTY_FR         | Nationalité                  |
| CD_CIV_STS           | Code état civil              |
| TX_CIV_STS_FR        | État civil                   |
| CD_AGE               | Âge                          |
| MS_POPULATION        | Nombre d'individus           |
| CD_YEAR              | Année de référence           |

## Questions métier possibles

* Population totale de Liège
* Répartition par âge
* Répartition par sexe
* Répartition par nationalité
* Répartition par état civil
* Évolution de la population dans le temps

## Limites

Le dataset ne contient qu'une année de référence (2025).
Il permet l'analyse de la structure de la population mais pas son évolution dans le temps.