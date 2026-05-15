# influxdb/connect.py
from influxdb_client import InfluxDBClient

print("=" * 40)
print("InfluxDB Connection Test")
print("=" * 40)

# InfluxDB connection details
URL = "http://localhost:8086"
TOKEN = "h25ii5peBP4ESZkeKu03iMhr2ZdmZ2GuDAb8Z4eAR7Q91A_n3FPOAAxq1GAzqy1SZwvE_nShAyUZZo0TJGbciA=="
ORG = "smart_city"
BUCKET = "Smart_City_Bucket"

try:
    client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
    
    health = client.health()
    
    print("SUCCESS! Connected to InfluxDB")
    print(f" URL: {URL}")
    print(f"Status: {health.status}")
    print(f" Bucket: {BUCKET}")
    
    client.close()
    
except Exception as e:
    print("FAILED! Could not connect to InfluxDB")
    print("Error: {e}")
    print("\n Make sure you started influxdb on docker!")
    print("\ndocker start influxdb")
