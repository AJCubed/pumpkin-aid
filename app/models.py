from app import db

class User_Hist(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    birthday = db.Column(db.String(50)) 
    symptoms = db.Column(db.String(200))
    allergies = db.Column(db.String(50))
    chronic_illnesses = db.Column(db.String(200))
    doctor_status = db.Column(db.String(200))
    medications = db.Column(db.String(200))
    past_diagnosis = db.Column(db.String(200))
    summary = db.Column(db.String(1000))
    apptDate = db.Column(db.String(50))
    

    def __init__(self, name, birthday, symptoms,allergies, chronic_illnesses, doctor_status, medications, summary, past_diagnosis, apptDate):
        self.name = name
        self.birthday = birthday
        self.symptoms = symptoms
        self.allergies = allergies
        self.chronic_illnesses = chronic_illnesses
        self.doctor_status = doctor_status
        self.allergies = allergies
        self.medications = medications
        self.summary = summary
        self.past_diagnosis = medications
        self.apptDate = apptDate