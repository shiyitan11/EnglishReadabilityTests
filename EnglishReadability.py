import textstat

# copy paste the text here
test_data = """

"""
smog = textstat.smog_index(test_data)
flesch_reading = textstat.flesch_reading_ease(test_data)
fk_grade = textstat.flesch_kincaid_grade(test_data)
gunning_fog = textstat.gunning_fog(test_data)

print("SMOG Index:", smog) 
print("Flesch Reading Ease:", flesch_reading)  
print("Flesch-Kincaid Grade Level:", fk_grade) 
print("Gunning Fog Index:", gunning_fog) 
