import psycopg2
import psycopg2.extras
import os

# Create database connection
connection = psycopg2.connect(host="localhost", dbname="postgres", user=os.environ['PY_ROLE'], password=os.environ['PY_PASS'])

def get_cursor():
    """Get a client side cursor. This cursor can be used to execute queries and read results."""
    # Note: Current implementation is using a DictCursor to create
    # cursors which can be accessed 'like' a dict but also like a list.
    # These cannot be consumed as responses by Flask, so the map_list function
    # is used to map lists, or for single values .copy() is used to convert
    # them to native Python dicts that Flask understands.
    # Alternatively, we could probably use psycopg2.extras.RealDictCursor,
    # though I expect that this will still have issues with it not being
    # organized in a native list of dicts.
    return connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

def commit():
    """Used to commit an ongoing operation. Necessary for any mutative database operations."""
    return connection.commit()

def map_list(l):
    """Convenience method for mapping lists results from the data layer to a standard Python dict."""
    return list(map(lambda i: i.copy(), l))