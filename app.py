from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

exercises = ["Push-ups", "Squats", "Plank"]

def calories_needed(bmi):
    if bmi < 18.5:
        return "You may need to gain weight. Aim for light exercise."
    elif 18.5 <= bmi < 25:
        return "Maintain your weight with ~200-300 calories burned per day."
    elif 25 <= bmi < 30:
        return "Aim to burn ~400-500 calories daily."
    else:
        return "Aim to burn ~500-700 calories daily."

@app.route("/", methods=["GET", "POST"])
def home():
    bmi_result = None
    calorie_advice = None
    today = datetime.now().strftime("%Y-%m-%d")

    if request.method == "POST":
        if "add" in request.form:
            new_exercise = request.form.get("exercise")
            if new_exercise:
                exercises.append(new_exercise)
        elif "remove" in request.form:
            to_remove = request.form.get("remove")
            if to_remove in exercises:
                exercises.remove(to_remove)
        elif "calculate_bmi" in request.form:
            try:
                weight = float(request.form.get("weight"))
                height = float(request.form.get("height")) / 100
                bmi_result = round(weight / (height ** 2), 2)
                calorie_advice = calories_needed(bmi_result)
            except:
                bmi_result = "Invalid input"

    return render_template(
        "home.html",
        exercises=exercises,
        today=today,
        bmi_result=bmi_result,
        calorie_advice=calorie_advice
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
