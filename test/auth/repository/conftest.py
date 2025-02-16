import pytest
from src.common.db.supabase.client import Supabase

@pytest.fixture
def client():
    return Supabase().get_client()
