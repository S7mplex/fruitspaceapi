<div align='center'><img src="imgs/fpapi.png" alt="alt text" width="150"/></div>

# FruitSpace API

**Модуль для взаимодействие с приватными серверами сделанными на FruitSpace**

----

Этот модуль предназначен для получения информации и взаимодействия с базой данных приватного сервера, созданного на хостинге FruitSpace.

Установить модуль

```plain
pip install fruitspaceapi
```

----

## Примеры

**Получить уровень по ID.**
```python
import FruitSpaceAPI
gdps = FruitSpaceAPI('01KG') # Тут нужно указать ID вашего GDPS

print(gdps.getLevel(30)) # Тут нужно ввести ID уровня
```
Пример ответа
```plain
{'id': 30, 'name': 'but fifn', 'description': '', 'version': 6, 'uid': 8, 'downloads': 25, 'track_id': 0, 'versionGame': 21, 'likes': 1, 'length': 1, 'demonDifficulty': 0, 'stars': 2, 'isFeatured': 0, 'auto': 0, 'password': '0', 'uploadedAgo': '3 weeks', 'updatedAgo': '3 weeks', 'originalID': 0, 'songID': 0, 'userCoins': 0, 'requestedStars': 2, 'isLDM': 0, 'isEpic': 0, 'objects': 102}
```
<br>
**Получить пользователя по ID.**
```python
import FruitSpaceAPI
gdps = FruitSpaceAPI('01KG')

print(gdps.getUser(1)) # Тут нужно ввести ID пользователя
```
Пример ответа
```plain
{'username': 'mrlogon', 'id': 1, 'stars': 4, 'demons': 0, 'leaderBoardRank': 5, 'creatorPoints': 1, 'icon': 1, 'color': 0, 'secondColor': 3, 'coins': 0, 'iconType': 0, 'special': 0, 'userCoins': 0, 'youtube': 'https://youtube.com/channel/UCDdT65wYaVTqpsI6TES_Mqw', 'cube': 1, 'ship': 1, 'ball': 1, 'ufo': 1, 'wave': 1, 'robot': 1, 'trace': 0, 'spider': 1, 'twitter': 'https://twitter.com/', 'twitch': 'https://twitch.tv/', 'diamonds': 227, 'death': 1}
```
