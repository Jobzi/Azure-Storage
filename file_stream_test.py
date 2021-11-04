import json

from file_stream import FileStream

def test_read_file_stream_return_file_when_enter_file_name():
    fs = FileStream()
    result = fs.get_file_stream("activity.json")
  
    assert len(json.load(result)) == 15

def test_read_file_stream_return_None_when_not_enter_file_name_or_incorrect_name():
    fs = FileStream()
    result = fs.get_file_stream("")
  
    assert result == None