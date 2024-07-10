# Define the event details
event_title = "Summer Party"
event_date = "2024-07-24"
event_start_time = "19:00"
event_end_time = "23:00"

# Format the date and time
event_date_formatted = event_date.split("-")[1] + " " + event_date.split("-")[2] + ", " + event_date.split("-")[0]
event_start_time_formatted = event_start_time[:2] + ":" + event_start_time[3:] + "pm" if int(event_start_time[:2]) > 12 else event_start_time[:2] + ":" + event_start_time[3:] + "am"
event_end_time_formatted = event_end_time[:2] + ":" + event_end_time[3:] + "pm" if int(event_end_time[:2]) > 12 else event_end_time[:2] + ":" + event_end_time[3:] + "am"

# Create the HTML template
html_template = """
         <div class="demo-card-event mdl-card mdl-shadow--2dp">
              <div class="mdl-card__title mdl-card--expand">
                <h4>
                  {event_title}:<br>
                  {event_date_formatted}<br>
                  {event_start_time_formatted}-{event_end_time_formatted}
                </h4>
              </div>
              <div class="mdl-card__actions mdl-card--border">
                <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                  Add to Calendar
                </a>
                <div class="mdl-layout-spacer"></div>
                <i class="material-icons">event</i>
              </div>
         </div>
"""

# Fill in the values and print the HTML
print(html_template.format(
    event_title=event_title,
    event_date_formatted=event_date_formatted,
    event_start_time_formatted=event_start_time_formatted,
    event_end_time_formatted=event_end_time_formatted
))