import aiohttp, asyncio, json, base64
from urllib.parse import unquote

class GDPS:
	def __init__(self, gdpsid: str):
		self.fruitspacedb = f"https://rugd.gofruit.space/{gdpsid}/db"
	def __makeRequest(self, page, params={}, rtype='get'):
		global response
		response = ''
		async def main():
			async with aiohttp.ClientSession() as session:
				global response
				if rtype == 'get':
					async with session.get(self.fruitspacedb+page) as resp:
						response = await resp.text()
				elif rtype == 'post':
					async with session.post(self.fruitspacedb+page, data=params, headers={"Content-Type": "application/json"}) as resp:
						response = await resp.text()

		asyncio.run(main())
		return response
	def __parse_level(self, raw_response):
		args = raw_response.split(':')
		try:
			password = base64.b64decode(args[5]).decode('utf-8')
		except:
			password = ''
		return {'id': int(args[1]),
				'name': args[3],
				'description': password,
				'version': int(args[10]),
				'uid': int(args[12]),
				'downloads': int(args[17]),
				'track_id': int(args[19]),
				'versionGame': int(args[21]),
				'likes': int(args[23]),
				'length': int(args[25]),
				'demonDifficulty': int(args[27]),
				'stars': int(args[29]),
				'isFeatured': int(args[31]),
				'auto': int(args[33]),
				'password': args[35],
				'uploadedAgo': args[37],
				'updatedAgo': args[39],
				'originalID': int(args[41]),
				'songID': int(args[45]),
				'userCoins': int(args[49]),
				'requestedStars': int(args[53]),
				'isLDM': int(args[55]),
				'isEpic': int(args[57]),
				'objects': int(args[61])
				}
	def __parse_song(self, songraw: str):
		args = songraw.split('|')
		argsn = []
		for arg in args:
			argsn.append(arg.replace('~', ''))
		return {'id': int(argsn[1]),
				'name': argsn[3],
				'artist': argsn[7],
				'size': argsn[9],
				'url': unquote(argsn[13])}
	def __parse_user(self, userraw: str):
		args = userraw.split(':')
		return {'username': args[1],
				"id": int(args[3]),
				'stars': int(args[5]),
				'demons': int(args[7]),
				'leaderBoardRank': int(args[9]),
				'creatorPoints': int(args[13]),
				'icon': int(args[15]),
				'color': int(args[17]),
				'secondColor': int(args[19]),
				'coins': int(args[21]),
				'iconType': int(args[23]),
				'special': int(args[25]),
				'userCoins': int(args[29]),
				'youtube': f'https://youtube.com/channel/{args[35]}',
				'cube': int(args[37]),
				'ship': int(args[39]),
				'ball': int(args[41]),
				'ufo': int(args[43]),
				'wave': int(args[45]),
				'robot': int(args[47]),
				'trace': int(args[49]),
				'spider': int(args[57]),
				'twitter': f'https://twitter.com/{args[59]}',
				'twitch': f'https://twitch.tv/{args[61]}',
				'diamonds': int(args[63]),
				'death': int(args[65])
				}
	def __parse_score(self, scoreraw: str):
		args = scoreraw.split(':')
		return {'username': args[1],
				'id': int(args[3]),
				'stars': int(args[5]),
				'demons': int(args[7]),
				'creatorPoints': int(args[13]),
				'icon': int(args[15]),
				'color': int(args[17]),
				'secondColor': int(args[19]),
				'coins': int(args[21]),
				'iconType': int(args[23]),
				'special': int(args[25]),
				'userCoins': int(args[29]),
				'diamonds': int(args[31])}
	def __parse_scores(self, rawscores: str):
		args = rawscores.split('|')
		scores = []
		for score in args:
			scores.append(self.__parse_score(score))
		return scores
	def __parse_comment(self, commraw: str):
		args=commraw.split('~')
		return {'comment': base64.b64decode(args[1]).decode('utf-8'),
				'uid': int(args[3]),
				'likes': int(args[5]),
				'isSpam': int(args[9]),
				'age': args[13]}
	def __parse_lvl_comment(self, commraw:str):
		args=commraw.split('~')
		return {'comment': base64.b64decode(args[1]).decode('utf-8'),
				'uid': int(args[3]),
				'likes': int(args[5]),
				'isSpam': int(args[9]),
				'age': args[11],
				'percent': int(args[13]),
				'id': int(args[19]),
				'username': args[22],
				'icon': int(args[24]),
				'color': int(args[26]),
				'secondColor': int(args[28]),
				'iconType': int(args[30]),
				'special': args[32]
				}
	def getDaily(self):
		raw_response = self.__makeRequest('/getGJDailyLevel.php')
		return {'id': int(raw_response.split('|')[0]), 'remaining_time': int(raw_response.split('|')[1])}
	def getLevel(self, levelID: int):
		raw_response = self.__makeRequest('/downloadGJLevel21.php', params={'levelID': levelID, 'secret': "Wmdf2893gb7"}, rtype='post')
		parsed_response = self.__parse_level(raw_response)
		return parsed_response
	def getLevels(self):
		return self.__makeRequest('/getGJLevels21.php')
	def getSong(self, songID: int):
		raw_response = self.__makeRequest('/getGJSongInfo.php', params={'songID': songID, 'secret': 'Wmfd2893gb7'}, rtype='post')
		return self.__parse_song(raw_response)
	def getUser(self, userID: int):
		raw_response = self.__makeRequest('/getGJUserInfo20.php', params={'secret': 'Wmfd2893gb7', 'targetAccountID': userID}, rtype='post')
		return self.__parse_user(raw_response)
	def getScores(self):
		raw_response = self.__makeRequest('/getGJScores.php', params={'secret': 'Wmfd2893gb7'}, rtype='post')
		return self.__parse_scores(raw_response)
	def getAccComments(self, accid: int, page:int):
		raw_response = self.__makeRequest('/getGJAccountComments20.php', params={"secret": 'Wmfd2893gb7', 'page': page, 'accountID': accid}, rtype='post')
		comments = []
		if '|' in raw_response:
			for comm in raw_response.split('|'):
				comments.append(self.__parse_comment(comm))
			comments[-1]['age'] = comments[-1]['age'].removesuffix('#'+comments[-1]['age'].split('#')[1])
		else:
			comments.append(self.__parse_comment(comm))
		print(raw_response)
		return comments
	def getComments(self, levelID: int, page: int):
		raw = self.__makeRequest('/getGJComments21.php', params={"secret": 'Wmfd2893gb7', 'page': page, 'levelID': levelID}, rtype='post')
		comments = []
		try:
			for comm in raw.split('|'):
				comments.append(self.__parse_lvl_comment(comm))
			comments[-1]['special'] = comments[-1]['special'].removesuffix('#'+comments[-1]['special'].split('#')[1])
		except IndexError:
			pass
		return comments
