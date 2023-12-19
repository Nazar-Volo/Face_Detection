#Python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-5ac4c-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "459635":
        {
            "name": "Nazar Voloshanivskyi",
            "major": "Data Science",
            "starting_year": 2022,
            "standing": "Master",
            "total_attendance": 0,
            "year": 2,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "203948":
        {
            "name": "Dmytro Filipov",
            "major": "Devops",
            "starting_year": 2019,
            "standing": "Bachelor",
            "total_attendance": 1,
            "year": 4,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "203949":
        {
            "name": "Nazar Petriv",
            "major": "Devops",
            "starting_year": 2019,
            "standing": "Master",
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "655432":
        {
            "name": "Serhii Voloshyn",
            "major": "Data Science",
            "starting_year": 2022,
            "standing": "M",
            "total_attendance": 0,
            "year": 2,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "857377":
        {
            "name": "Andrii Vasyliuk",
            "major": "Candidate of Sciences",
            "starting_year": 2010,
            "standing": "Docent",
            "total_attendance": 0,
            "year": 13,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "143245":
        {
            "name": "Taras Basuik",
            "major": "Candidate of Sciences",
            "starting_year": 2010,
            "standing": "Docent",
            "total_attendance": 0,
            "year": 13,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "564932":
        {
            "name": "Vasyl Lytvyn",
            "major": "Candidate of Sciences",
            "starting_year": 2010,
            "standing": "Docent",
            "total_attendance": 0,
            "year": 13,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "489087":
        {
            "name": "Jennifer Lawrence",
            "major": "Actor",
            "starting_year": 2007,
            "standing": "A",
            "total_attendance": 0,
            "year": 13,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "586032":
        {
            "name": "Yaroslav Kis'",
            "major": "Candidate of Sciences",
            "starting_year": 2010,
            "standing": "Docent",
            "total_attendance": 0,
            "year": 13,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "564932":
        {
            "name": "Vasyl Lytvyn",
            "major": "Candidate of Sciences",
            "starting_year": 2010,
            "standing": "Docent",
            "total_attendance": 0,
            "year": 13,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "786942":
        {
            "name": "Ryan Reynolds",
            "major": "Actor",
            "starting_year": 2010,
            "standing": "A",
            "total_attendance": 0,
            "year": 13,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "764327":
        {
            "name": "Iruna Zavushchak",
            "major": "Candidate of Sciences",
            "starting_year": 2010,
            "standing": "Docent",
            "total_attendance": 0,
            "year": 13,
            "last_attendance_time": "2023-05-29 13:31:34"
        },
    "886546":
        {
            "name": "Veres Oleh",
            "major": "Candidate of Sciences",
            "starting_year": 2010,
            "standing": "Docent",
            "total_attendance": 0,
            "year": 13,
            "last_attendance_time": "2023-05-29 13:31:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)