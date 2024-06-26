import os
os.environ['OPENAI_API_KEY'] = 'd5d11772ad6e4d1b9ddd93eba9a58311'
import openai
from dotenv import load_dotenv
openai.api_key = 'd5d11772ad6e4d1b9ddd93eba9a58311'


from sentiment_analysis import *
from transcription import *
from save_as_docx import *

load_dotenv()

openai.api_key = 'd5d11772ad6e4d1b9ddd93eba9a58311'

def meeting_minutes(transcription):
    abstract_summary = abstract_summary_extraction(transcription)
    key_points = key_points_extraction(transcription)
    action_items = action_item_extraction(transcription)
    sentiment = sentiment_analysis(transcription)
    return {
        'abstract_summary': abstract_summary,
        'key_points': key_points,
        'action_items': action_items,
        'sentiment': sentiment
    }

audio_file_path = "./audio/EarningsCall.wav"
transcription = transcribe_audio(audio_file_path, openai)
minutes = meeting_minutes(transcription)
print(minutes)

save_as_docx(minutes, 'meeting_minutes.docx')
