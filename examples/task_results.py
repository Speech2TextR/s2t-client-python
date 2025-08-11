from speech2text_client.client import Speech2Text
from speech2text_client.enums import Formats

api = Speech2Text('YOUR_API_KEY')
task_id = 'TASK_ID'
task = api.recognitions().task(task_id)
print(task.result(Formats.TXT))  # txt
print("=" * 50)
print(task.result(Formats.RAW))  # raw
print("=" * 50)
print(task.result(Formats.SRT))  # srt
print("=" * 50)
print(task.result(Formats.VTT))  # vtt
print("=" * 50)
print(task.result(Formats.JSON))  # json
print("=" * 50)
print(task.result(Formats.XML))  # xml