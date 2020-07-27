class HatAuth:
    appId: str

    def __init__( self, appId: str) -> None:
        self.appId = appId
         

    def enable_hat_auth(self):
        print(self.appId) 


 
