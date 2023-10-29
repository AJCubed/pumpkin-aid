from app import db
from app.models import User_Hist
from sqlalchemy import create_engine, false, true
import json

db.create_all()
engine = create_engine('sqlite:///app/userdata.sqlite3', echo=False)

a = [
    {
        "name": "Emily Johnson",
        "birthday": "04-19-1976",
        "symptoms": "chest pain, shortness of breath",
        "allergies": "latex",
        "chronic_illnesses": "no",
        "doctor_status": "no",
        "medications": "aspirin occasionally for pain",
        "past_diagnosis": "no",
        "summary": "Patient has been experiencing chest pains alongside shortness of breath, symptoms have been persistent for a couple of days. Only takes aspirin occasionally.",
        "apptDate": "11-05-2023"
    },
    {
        "name": "Michael Brown",
        "birthday": "09-06-1988",
        "symptoms": "joint pain",
        "allergies": "none",
        "chronic_illnesses": "no",
        "doctor_status": "no",
        "medications": "ibuprofen for pain",
        "past_diagnosis": "mild arthritis",
        "summary": "Patient suffers from joint pain, likely related to past diagnosis of mild arthritis. Regularly uses over-the-counter pain relief.",
        "apptDate": "11-06-2023"
    },
    {
        "name": "Laura Wilson",
        "birthday": "01-13-2002",
        "symptoms": "sore throat, swollen glands",
        "allergies": "penicillin",
        "chronic_illnesses": "no",
        "doctor_status": "no",
        "medications": "no",
        "past_diagnosis": "tonsillitis",
        "summary": "Patient presents with a sore throat and swollen glands, has a history of tonsillitis. Currently not on any medication.",
        "apptDate": "11-07-2023"
    },
    {
        "name": "Brian Miller",
        "birthday": "12-30-1995",
        "symptoms": "constant fatigue",
        "allergies": "none",
        "chronic_illnesses": "type 2 diabetes",
        "doctor_status": "Dr. Adams, endocrinologist",
        "medications": "metformin for diabetes",
        "past_diagnosis": "type 2 diabetes",
        "summary": "Patient has reported constant fatigue; has an ongoing treatment for type 2 diabetes under Dr. Adams.",
        "apptDate": "11-08-2023"
    },
    {
        "name": "Anna Garcia",
        "birthday": "08-26-1983",
        "symptoms": "back pain",
        "allergies": "NSAIDs",
        "chronic_illnesses": "no",
        "doctor_status": "no",
        "medications": "acetaminophen for pain",
        "past_diagnosis": "herniated disc",
        "summary": "Patient complains of back pain, has a history of a herniated disc. Allergic to NSAIDs and takes acetaminophen for pain management.",
        "apptDate": "11-09-2023"
    }
]

for element in a:
    GPT_res = json.loads(json.dumps(element))

    user_name = GPT_res["name"]
    user_birthday = GPT_res["birthday"]
    user_symptoms = GPT_res["symptoms"]
    user_chronic_illnesses = GPT_res["chronic_illnesses"]
    user_doctor_status = GPT_res["doctor_status"]
    user_allergies = GPT_res["allergies"]
    user_medications = GPT_res["medications"]
    user_summary = GPT_res["summary"]
    user_past_diagnosis = GPT_res["past_diagnosis"]
    user_apptDate = GPT_res["apptDate"]

    User_entry = User_Hist(user_name, user_birthday, user_symptoms, user_allergies, user_chronic_illnesses, user_doctor_status, user_medications, user_summary, user_past_diagnosis, user_apptDate)

    db.session.add(User_entry)
    db.session.commit()