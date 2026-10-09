from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["devl"]
collection = db["students"]
print("MongoDB connected successfully!")
 
students = [
    {
        "roll_no": 102,
        "name": "Sneha",
        "department": "CSE",
        "marks": 85,
        "city": "Mumbai"
    },
    {
        "roll_no": 103,
        "name": "Rahul",
        "department": "AIML",
        "marks": 72,
        "city": "Pune"
    },
    {
        "roll_no": 104,
        "name": "Priya",
        "department": "CSE",
        "marks": 90,
        "city": "Nashik"
    },
    {
        "roll_no": 105,
        "name": "Rohan",
        "department": "AIML",
        "marks": 68,
        "city": "Pune"
    }
]
 
result = collection.insert_many(students)
 
print("Multiple documents inserted successfully")
print(result.inserted_ids)
 
print("\nAll Students:")
 
for student in collection.find():
    print(student)
 
    student = collection.find_one({"roll_no": 103})
 
print(student)
 
student = collection.find_one({"name": "Priya"})
 
print(student)
 
students = collection.find({
    "marks": {"$gt": 75}
})
 
for student in students:
    print(student)
 
 
    students = collection.find({
    "marks": {
        "$gte": 70,
        "$lte": 90
    }
})
 
for student in students:
    print(student)
 
    collection.update_one(
    {"roll_no": 101},
    {
        "$set": {
            "marks": 82
        }
    }
)
 
print("Document updated successfully")
print(collection.find_one({"roll_no": 101}))