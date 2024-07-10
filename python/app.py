from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    event_title = "Summer Party"
    event_date = "2024-07-24"
    event_start_time = "19:00"
    event_end_time = "23:00"

    event_date_formatted = event_date.split("-")[1] + " " + event_date.split("-")[2] + ", " + event_date.split("-")[0]
    event_start_time_formatted = event_start_time[:2] + ":" + event_start_time[3:] + "pm" if int(event_start_time[:2]) > 12 else event_start_time[:2] + ":" + event_start_time[3:] + "am"
    event_end_time_formatted = event_end_time[:2] + ":" + event_end_time[3:] + "pm" if int(event_end_time[:2]) > 12 else event_end_time[:2] + ":" + event_end_time[3:] + "am"

    return render_template("index.html", event_title=event_title, event_date_formatted=event_date_formatted, event_start_time_formatted=event_start_time_formatted, event_end_time_formatted=event_end_time_formatted)

if __name__ == "__main__":
    app.run(debug=True)