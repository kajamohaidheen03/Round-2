# Define the collection names 
v_nameCollection = 'Hash_kaja'
v_phoneCollection = 'Hash_5893'

# Step 1: Create collections
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

# Step 2: Get employee count 
print(f"Initial Employee Count in {v_nameCollection}: {getEmpCount(v_nameCollection)}")

# Step 3: Index data excluding certain columns
indexData(v_nameCollection, 'Department')  # Index excluding 'Department' column
indexData(v_phoneCollection, 'Gender')     # Index excluding 'Gender' column

# Step 4: Delete employee by ID from 'Hash_kaja'
delEmpById(v_nameCollection, 'E02003')

# Step 5: Get employee count after deletion
print(f"Employee Count in {v_nameCollection} after deletion: {getEmpCount(v_nameCollection)}")

# Step 6: Search by columns
print(f"Search for 'IT' department in {v_nameCollection}: {searchByColumn(v_nameCollection, 'Department', 'IT')}")
print(f"Search for 'Male' gender in {v_nameCollection}: {searchByColumn(v_nameCollection, 'Gender', 'Male')}")
print(f"Search for 'IT' department in {v_phoneCollection}: {searchByColumn(v_phoneCollection, 'Department', 'IT')}")

# Step 7: Get department facet (grouped employee count by department)
print(f"Department facet in {v_nameCollection}: {getDepFacet(v_nameCollection)}")
print(f"Department facet in {v_phoneCollection}: {getDepFacet(v_phoneCollection)}")
