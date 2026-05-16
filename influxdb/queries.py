from influxdb_client import InfluxDBClient

URL = "http://localhost:8086"
TOKEN = "token"
ORG = "smart_city"
BUCKET = "Smart_City_Bucket"

client = InfluxDBClient(url=URL, token=TOKEN, org=ORG)
query_api = client.query_api()

query = f'''
from(bucket: "{BUCKET}")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] == "report_events")
  |> filter(fn: (r) => r["_field"] == "response_time")
'''

tables = query_api.query(query)

for table in tables:
    for record in table.records:
        print(record.values)

client.close()
