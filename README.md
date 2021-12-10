Projet Python (framework Django) réalisé par Marchand Thibaud, Colliaux Tom-Olivier, Karembé Moussa, Ollivier Dimitri

Cette aplication permet à un utilisateur de consulter les 151 premiers pokemons de l'API "Pokéapi" (https://pokeapi.co/) et des les ajouter dans une équipe.

Les routes accessibles sont les suivantes :
  - http://127.0.0.1:8000/pokedex/ (consulter le pokedex)
  - http://127.0.0.1:8000/pokedex/pokemon/x (consulter le pokemon ayant pour id : x)
  - http://127.0.0.1:8000/pokedex/team/ (consulter notre equipe)
  
Nous avons créé plusieurs filtres qui permettent de modifier l'affichage de certaines valeurs sans modifier leur contenue. 
Par exmple les ids des pokémons sont uniquement lors de l'affichage composés de 3 caractères (ex: id = 1 → 001). 
Ces filtres sont chagés au début de nos templates.
On les appelle avec un "| nomFilte" sur la variable souhaité.
Par exemple, le filtre pour modifier l'affichage de l'id est appeller comme cela : "pokemon.id | format_id"

Nous avons utilisé du scss pour l'affichage de notre site. Le scss est un language compilé qui permet de générer un fichier css.
