import requests

class SetlistFmClient:
    apiKey = 'ZKHx6tWfpAPqP2vRjdeA9dL5DKi4HO_Dl7w5'
    headers = {
            "Accept": "application/json",
            "x-api-key": apiKey
        }
    
    def searchArtists(self, artistName):
        url = 'https://api.setlist.fm/rest/1.0/search/artists'
        params = {"artistName": artistName, "sort": "relevance"}

        response = requests.get(url, params=params, headers=self.headers)

        if response.status_code in range(200, 299):
            return self.returnFirstArtist(response.json())
        else:
            return response.status_code

    def returnFirstArtist(self, responseJson):
        responseResults = responseJson.get('artist', [])
        if len(responseResults) > 0:
            artistInfo = responseResults[0]
            return {"artist": artistInfo['name'], "mbid": artistInfo['mbid']}
        else:
            return {"artist": "", "mbid": "Error"}
    
    def getSetlistForArtist(self, artistName):
        artistObject = self.searchArtists(artistName)
        mbid = artistObject["mbid"]
        if mbid != "Error":
            url = f'https://api.setlist.fm/rest/1.0/artist/{mbid}/setlists'
            response = requests.get(url, headers=self.headers)
            if response.status_code in range(200, 299):
                return self.returnFirstSetlist(response.json())
            else:
                return response.status_code
        return {"Error":"No mbid"}
            
    def returnFirstSetlist(self, responseJson):
        responseResults = responseJson.get('setlist', [])
        if len(responseResults) > 0:
            setlistInfo = responseResults[0]
            return {
                "setlist": {
                    "eventDate": setlistInfo['eventDate'],
                    "venue": setlistInfo.get("venue", {"name":None}).get("name"),
                    
                }
            }

Client =  SetlistFmClient()
print(Client.getSetlistForArtist("Zhu"))
