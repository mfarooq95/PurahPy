# PurahPy
A Tears of the Kingdom API returning detailed in-game data 

# About
**PurahPy** is a REST API for *The Legend of Zelda: Tears of the Kingdom*, providing detailed data on in-game resources. **PurahPy** is robust and structured, serving data on multiple categories of in-game content at various endpoints, each categorized by their resource type enabling organized data return.

Coded in Python, **PurahPy** is built with the Flask framework and works with MongoDB as its backend database, utilizing `flask-restful` and `flask-mongoengine` to structure, control and communicate data with the API.

## Data Categories & Endpoints
The API contains and returns access to in-game data on various content in *Tears of the Kingdom*. Examaples include:
1. Weapons
2. Monsters
3. Creatures
4. Materials

A few of the categories above are broken down even further, allowing for further organization of data:
1. Weapons
   * One-Handed Weapons
   * Two-Handed Weapons
   * Spears
   * Bows
   * Shields

2. Creatures
   * Non-Consumable Creatures
   * Consumable Creatures

3. Materials
   * Non-Consumable Materials
   * Consumable Materials

Each category has its endpoint with its apprpriate resource/content tied to the route available for consumption. Each category has two routes for `GET` requests to be made to returning all the data within the database's respective collection as JSON data or returning a single document/entry.
  
### Routes
  Below are a few examples of routes available:
  ```
  /api/onehandedweapons
  /api/onehandedweapons/<name>
  /api/shields
  /api/shields</name>
  ```

Note the two routes per category, allowing end-users to consume all documents in the database's collection for that category or an individual item/entry/document in the in-game content's respective collection.
  
**PurahPy** only accepts `GET` requests.
 
Users cannot make any other standard operating CRUD requests to the API.


# Project Pipeline
- [ ] Parse and enter all source data into database
- [ ] Create and host image content
- [ ] Update database with images
- [ ] Host database
- [ ] Connect API to database
- [ ] Update and review data schemas
- [ ] Update routes and endpoints
- [ ] Auth consideration 
- [ ] GUnicorn, multithreading, etc.
- [ ] Error and exception handling of API
- [ ] API testings
- [ ] Host API live
- [ ] Documentation of API
