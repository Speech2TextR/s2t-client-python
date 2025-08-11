from speech2text_client.client import Speech2Text
from speech2text_client.enums import ListStages

api = Speech2Text("YOUR_API_KEY")

print(f"Count (complete/all): {api.recognitions().count(stage=ListStages.COMPLETE.value)}/{api.recognitions().count()}")
print(f"Errors count: {api.recognitions().count(stage=ListStages.ERRORS.value)}")
print(f"Last tasks:")
for task in api.recognitions().list(limit=10):
    print(task.recognize_options())
    print(f"Id: {task.id()}")
    print(f"    Status: {task.status().code} ({task.status().description})")
    print(f"    Type: {task.source_type()}")
    print(f"    Options:")
    print(f"        Language: {task.recognize_options().lang}")
    print(f"        Stereo: {task.recognize_options().stereo}")
    print(f"        Speakers: {task.recognize_options().speakers if isinstance(task.recognize_options().speakers, int) or task.recognize_options().speakers is None else f'from {task.recognize_options().speakers[0]} to {task.recognize_options().speakers[1]}'}")
    print(f"    Mime: {task.meta().mime}")
    print(f"    File format: {task.meta().format}")
    print(f"    Audio format: {task.meta().audio_format}")
    print("=" * 50)

get_last_complete_tasks = api.recognitions().list(stage=ListStages.COMPLETE.value, page=1, limit=1)
if get_last_complete_tasks:
    print(f"Result fot task {get_last_complete_tasks[0].id()}")
    print(get_last_complete_tasks[0].result())
