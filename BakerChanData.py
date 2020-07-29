from os import path
class __Messages__():
    __Language__ = None
    __LanguageEnabled__ = ["Poland", "English"]

    __PolandMessages__ = {
        "OpenExtension":"Poprawnie załadowano rozszerzenie.",
        "CloseExtension":"Poprawnie rozłączono rozszerzenie.",
        "RestartExtension":"Poprawnie przeładowano rozszerzenie.",
        "CheckFailure":"Nie masz uprawnień do tej funckji.",
        "on_ready":"Baker chan jest gotowa upiec trochę chleba.",
        "activity":"na śmierć i życie.",
        "ping":"Baker chan mówi, że ping na serwerze wynosi",
        "clear":"Baker chan mówi, że nie może usunąć tylu wiadomości.",
        "play":"Baker chan mówi, że takiej piosenki nie ma w jej bazie danych :c",
        "download1":"Piosenka o takiej nazwie już jest w bazie danych.",
        "download2":"Baker chan nie ma jeszcze takiej funkcjonalności."
    }

    __EnglishMessages__ = {
        "OpenExtension":"Module was loaded corectly.",
        "CloseExtension":"Module was disloaded corectly.",
        "RestartExtension":"Module was reloaded corectly.",
        "CheckFailure":"You don't have permission to use this function.",
        "on_ready":"Baker chan is ready to bake some bread.",
        "activity":"to dead or alive.",
        "ping":"Baker chan says, that ping on this server is ",
        "clear":"Baker chan says, that she can't delete that amount of messages.",
        "play":"Baker chan says, that this song doesn't exist in her database :c",
        "download1":"That song is in Baker chan database.",
        "download2":"Baker chan can't do that yet."
    }

    def __init__(self, Language:str = "Poland"):
        try:
            self.__LanguageEnabled__.index(Language)
        except ValueError:
            print(f"{Language} is not available.")
        else:
            self.__Language__ = Language

    def ChangeLanguage(self, Language:str):
        try:
            self.__LanguageEnabled__.index(Language)
        except ValueError:
            print(f"{Language} is not available.")
        else:
            self.__Language__ = Language

    def Get(self, Index:str):
        if self.__Language__ == "Poland":
            return self.__PolandMessages__.get(Index)
        if self.__Language__ == "English":
            return self.__EnglishMessages__.get(Index)

class __Settings__():

    Prefix = None
    Token = None
    
    MainPath = None
    BodyName = None
    BodyPath = None
    SongsFolder = None

    def __init__(self, MainPath:str):
        self.Prefix = "."
        self.Token = 'Not Public'

        self.MainPath = MainPath
        self.BodyName = "BakerChanBody"
        self.BodyPath = path.join(self.MainPath, self.BodyName)

        self.SongsFolder = "SongsDatabase"

if __name__ != "__main__":
    def init(MainPath:str):
        global Messages
        global Settings
        Messages = __Messages__()
        Settings = __Settings__(MainPath)