import os

import dotenv

dotenv.load_dotenv(verbose=True, override=True)
# del dotenv.load_dotenv

class Config:

    instance = None

    def __new__(cls):

        if cls.instance is None:

            cls.instance = super(Config, cls).__new__(cls)

            cls.instance.from_env()

        return cls.instance

    def from_env(self):

        self.apikey = os.getenv('APIKEY')

