from src.common.config import Config

from supabase import create_client


class Supabase:
    def __init__(self):
        self.SUPABASE_URL = Config.get_supabase()["url"]
        self.SUPABASE_KEY = Config.get_supabase()["key"]

    def get_client(self):
        return create_client(self.SUPABASE_URL, self.SUPABASE_KEY)


if __name__ == "__main__":
    client = Supabase().get_client()
    print(client)
