from speechlib import Transcriptor

file = "obama1.wav"
voices_folder = "voices"
language = "english"
log_folder = "logs"
modelSize = "medium"

transcriptor = Transcriptor(file, log_folder, language, modelSize, voices_folder)

res = transcriptor.transcribe()

print("res", res)