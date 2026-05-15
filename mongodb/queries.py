from pymongo import MongoClient 

client = MongoClient("mongodb://localhost:27017")
db = client.smart_city

# CRUD queries 
# already did the create thing in insert_data.py 
# now Read queries :
print("\n" + "=" * 30)
print("   ALL REPORTS")
print("=" * 30)

all_reports = db.reports.find()
for report in all_reports:
    print(f"Report ID: {report['report_id']}")
    print(f"   Issue Type: {report['type']}")
    print(f"   Status: {report['status']}")
    print(f"   Citizen ID: {report['user_id']}")
    print("-" * 30)

print("\n" + "=" * 30)
print("   WASTE REPORTS ONLY")
print("=" * 30)

waste_reports = db.reports.find({"type": "waste"})
for report in waste_reports:
    print(f"Report ID: {report['report_id']}")
    print(f"   Status: {report['status']}")
    print(f"   Citizen ID: {report['user_id']}")
    print("-" * 30)

print("\n" + "=" * 30)
print("   TRAFFIC REPORTS ONLY")
print("=" * 30)
traffic_reports = db.reports.find({"type": "traffic"})
for report in traffic_reports:
    print(f"Report ID: {report['report_id']}")
    print(f"   Status: {report['status']}")
    print(f"   Citizen ID: {report['user_id']}")
    print("-" * 30)

print("\n" + "=" * 30)
print("   ELECTRICITY REPORTS ONLY")
print("=" * 30)
electricity_reports = db.reports.find({"type": "electricity"})
for report in electricity_reports:
    print(f"Report ID: {report['report_id']}")
    print(f"   Status: {report['status']}")
    print(f"   Citizen ID: {report['user_id']}")
    print("-" * 30)

# now an Update query :
print("\n" + "=" * 30)
print("   UPDATE REPORT STATUS")
print("=" * 30)
print("BEFORE UPDATE:")
report_before = db.reports.find_one({"report_id": "R001"})
print(f"Report ID: {report_before['report_id']} - Status: {report_before['status']}")
db.reports.update_one(
    {"report_id": "R001"},
    {"$set": {"status": "resolved"}}
)
print("\nAFTER UPDATE:")
report_after = db.reports.find_one({"report_id": "R001"})
print(f"Report ID: {report_after['report_id']} - Status: {report_after['status']}")

# now a Delete query :
db.reports.delete_many({"status": "resolved"})
print("\n" + "=" * 30)
print("   ALL REPORTS AFTER REMOVING RESOLVED ONES")
print("=" * 30)

all_reports = db.reports.find()
for report in all_reports:
    print(f"Report ID: {report['report_id']}")
    print(f"   Issue Type: {report['type']}")
    print(f"   Status: {report['status']}")
    print(f"   Citizen ID: {report['user_id']}")
    print("-" * 30)

# A Complex query :
# # count by issue type 
print("\n" + "=" * 30)
print("   COUNT BY ISSUE TYPE")
print("=" * 30)
pipeline = [{"$group": {"_id": "$type", "count": {"$sum": 1}}}]
results = db.reports.aggregate(pipeline)
for item in results:
    print(f"   {item['_id']}: {item['count']} report(s)")

 