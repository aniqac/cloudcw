from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from cassandra.concurrent import execute_concurrent, execute_concurrent_with_args
from cassandra import ConsistencyLevel
import csv

try:
    cluster = Cluster()
    session = cluster.connect()
    status = "Cassandra Success"
except Exception as e:
    status = "Cassandra fail"
    print (e.message, e.args)


KEYSPACE = "country"
TABLENAME = "countryTable"
NAMELIST = ['Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Holy See', 'Italy', 'San Marino', 'Switzerland', 'Fiji', 'India']
LANGLIST = ['Spanish', 'Spanish', 'Spanish', 'Spanish', 'Italian', 'Italian', 'Italian', 'Italian', 'Hindi', 'Hindi']


def table_exist():
    # create keyspace if it doesn't exist
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %session
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': "1"} AND durable writes = True
        """ % KEYSPACE)
    print ("{} has been created".format(KEYSPACE))
    return ("its working")
    # create table if not exist
