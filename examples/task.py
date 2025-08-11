from speech2text_client.client import Speech2Text

api = Speech2Text('YOUR_API_KEY')
task_id = 'TASK_ID'
task = api.recognitions().task(task_id)
print(f"Id: {task.id()}")
print(f"    Status: {task.status().code} ({task.status().description})")
print(f"    Type: {task.source_type()}")
print(f"    Options:")
print(f"        Language: {task.recognize_options().lang}")
print(f"        Stereo: {task.recognize_options().stereo}")
print(
    f"        Speakers: {task.recognize_options().speakers if isinstance(task.recognize_options().speakers, int) or task.recognize_options().speakers is None else f'from {task.recognize_options().speakers[0]} to {task.recognize_options().speakers[1]}'}")
print(f"    Mime: {task.meta().mime}")
print(f"    File format: {task.meta().format}")
print(f"    Audio format: {task.meta().audio_format}")