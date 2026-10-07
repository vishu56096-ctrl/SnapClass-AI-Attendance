import ssl

import httpx
import streamlit as st
import truststore

from supabase import create_client, Client
from supabase.lib.client_options import SyncClientOptions

httpx_client = httpx.Client(
    verify=truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
)

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"],
    options=SyncClientOptions(httpx_client=httpx_client),
)
