
def calculate_bmi(weight,height):

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Under Weight"

    elif bmi < 25:
        category = "Normal"

    elif bmi < 30:
        category = "Over Weight"

    else:
        category = "Obese"

    return round(bmi,2), category
