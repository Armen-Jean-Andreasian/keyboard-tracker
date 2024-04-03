from src import KeyboardTrackerApp

app = KeyboardTrackerApp(log_file_name='keyboard_logs')
app.track(time_active=3)
print(app.result)
