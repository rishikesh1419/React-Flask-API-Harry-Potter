"""
This module parses the URL query parameters
"""
from urllib.parse import parse_qs

def parse_query(query_str):
    parameters = dict(parse_qs(query_str))
    q_params = {k.decode(): v[0].decode() for k, v in parameters.items()}
    return q_params