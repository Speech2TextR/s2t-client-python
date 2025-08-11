from speech2text_client.client import Speech2Text

api = Speech2Text("YOUR_API_KEY")

print(f"Balance: {api.user().amounts().balance()}")
print(f"Available Minutes: {api.user().amounts().available_minutes()}")
print(f"Used Minutes: {api.user().amounts().used_minutes()}")

print(f"Rate: {api.user().rate().title} ({api.user().rate().minutes} minutes for {api.user().rate().period} day(s))")

print(f"Threads: {api.user().settings().threads()}")
print(f"Auto payment status: {'Да' if api.user().settings().auto_payments_status() else 'Нет'}")
print(f"Auto payment ON: {'✅' if api.user().settings().auto_payments_on() else '❌'}")
print(f"Auto payment OFF: {'✅' if api.user().settings().auto_payments_off() else '❌'}")
