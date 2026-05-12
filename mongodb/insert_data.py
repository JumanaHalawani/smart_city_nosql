from pymongo import MongoClient 
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client.smart_city

db.reports.delete_many({})
db.citizens.delete_many({})
db.departments.delete_many({})
db.locations.delete_many({})

db.reports.create_index("report_id", unique=True)
db.citizens.create_index("citizen_id", unique=True)
db.departments.create_index("department_id", unique=True)
db.locations.create_index("location_id", unique=True)

db.citizens.insert_many([{"citizen_id":"CIT-001", "name":"Ahmed Ahmed", "email":"ahmed@gmail.com","phone":"0598800000", "district":"Ein Sarah","created_at":datetime.now()},
                         {"citizen_id":"CIT-002", "name":"Fatima Al-Zahra", "email":"fatima@gmail.com","phone":"0591110000", "district":"Downtown","created_at":datetime.now()},
                         {"citizen_id":"CIT-003", "name":"Omar Omar", "email":"omar@gmail.com","phone":"0528800000", "district":"Wad El Haryeh","created_at":datetime.now()}
                        ])

db.reports.insert_many([{"report_id": "REP-001", "citizen_id": "CIT-001", "location_id": "LOC-101", "issue_type": "waste", "status": "in_progress","submitted_at": datetime.now()},
                        {"report_id":"REP-002", "citizen_id": "CIT-002", "location_id": "LOC-103", "issue_type": "traffic", "status": "submitted", "submitted_at": datetime.now()},
                        {"report_id": "REP-003", "citizen_id": "CIT-003", "location_id": "LOC-102", "issue_type": "lighting", "status": "resolved", "submitted_at": datetime.now()}
                        ])

db.departments.insert_many([{"department_id": "DEPT-01", "name": "Sanitation Department", "responsibility": ["waste"], "contact_phone": "0560090000"},
                            {"department_id": "DEPT-02", "name": "Traffic Department", "responsibility": ["traffic"], "contact_phone": "0598880000"},
                            {"department_id": "DEPT-03", "name": "Electricity Department", "responsibility": ["lighting"], "contact_phone": "0563330000"}
                            ])  
   
db.locations.insert_many([{"location_id": "LOC-101", "name": "Nijmah Street", "district": "Downtown"},
                        {"location_id": "LOC-102", "name": "Ein Sarah park", "district": "Ein Sarah"},
                        {"location_id": "LOC-103", "name": "Main Intersection", "district": "Wad El Haryeh"}
                        ]) 
print("all data has been inserted to the database successfully!")