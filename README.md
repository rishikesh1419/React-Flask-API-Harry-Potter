<h1> Harry Potter<br/>
Web App (React) and Custom API (Flask, MongoDB) </h1>

<em><h2>Index</h2></em>
1. [Web app screenshots](#ss)
2. [How to run this repository](#repo)
3. [API documentation](#docs)

<hr/>

<h2 id="ss">1. Web App Screenshots </h2>

<h2 id="repo">2. How To Run This Repository </h2>

<h2 id="docs">3. API Documentation (Built using Flask, MongoDB: </h2>

(All routes are GET, response format is json.)
### Get sorted into a random house
```
/sortinghat
```
<em>Returns a random house with its id, name, mascot, head of house, house ghost, founder, school, list of members (id), list of values, list of colors.</em>

### Get all characters / search 
```
/characters
/characters?name=<search_term>
```
<em>Returns basic details (id, name, house and species) of all characters.</em>

### Get details of a character
```
/characters/<id>
```
<em>Returns id, name, role, wand, boggart, patronus, house, school, alias, animagus, blood status, species, if member of ministry of magic, order of phoenix, Dumbledore's army, death eaters (4 booleans).
</em>

### Get houses
```
/houses
```
<em>Returns house names with their id and founders.</em>

### Get house details
```
/houses/<name>
```
<em>Get house details using name (Gryffindor, Slytherin, Ravenclaw, Hufflepuff).  
Returns id, name, mascot, head of house, house ghost, founder, school, list of members (id), list of values, list of colors.
</em>

### Get all spells
```
/spells
```
<em>Returns all spells with details: id, spell, type, effect.</em>