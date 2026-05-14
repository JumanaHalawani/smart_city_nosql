from neo4j import GraphDatabase

# Connection info
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"

# Create driver
driver = GraphDatabase.driver(
    URI,
    auth=(USER, PASSWORD)
)

# Function that inserts graph data
def create_data(tx):

    tx.run("""

        CREATE (u1:User {
            name: 'Ahmad'
        })

        CREATE (u2:User {
            name: 'Sara'
        })

        CREATE (r1:Report {
            type: 'waste',
            area: 'Ramallah',
            status: 'pending'
        })

        CREATE (r2:Report {
            type: 'traffic',
            area: 'Nablus',
            status: 'resolved'
        })

        CREATE (d1:Department {
            name: 'Waste Department',
            type: 'waste',
            area: 'Ramallah'
        })

        CREATE (d2:Department {
            name: 'Traffic Department',
            type: 'traffic',
            area: 'Nablus'
        })

        CREATE (u1)-[:REPORTS]->(r1)
        CREATE (u2)-[:REPORTS]->(r2)

        CREATE (d1)-[:HANDLES]->(r1)
        CREATE (d2)-[:HANDLES]->(r2)

    """)

# Open session
with driver.session() as session:

    # Execute function
    session.execute_write(create_data)

print("Data inserted successfully!")

# Close connection
driver.close()