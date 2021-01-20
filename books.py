class BaseConfig:
    DEBUG=False
    TESTING=False
    HOST="127.0.0.1"
    PORT=5000

class DevConfig(BaseConfig):
    DEBUG=True
    PORT=5001
    
    @property
    def HOST(self):
        return "0.0.0.0"
    

class TestConfig(BaseConfig):
    TESTING=True


class ProdConfig(BaseConfig):
    PORT=8081