from src import KeyboardTrackerApp

app = KeyboardTrackerApp(time_active=3)
app.track()
result = app.result
print(len(result))
