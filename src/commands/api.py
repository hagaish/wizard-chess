from __future__ import division

import re
import sys
import enum

from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1 import enums
from google.cloud.speech_v1p1beta1 import types

from .microphone_stream import MicrophoneStream
from .player_command import PlayerCommand

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

recommeneded_pharses = ["King","Queen","Bishop","Rook","Knight","Pawn","to","a","b","c","d","e","f","g","h","1","2","3","4","5","6","7","8"]
boost = 15
command_regex = r'(Queen|King|Bishop|Rook|Knight|Pawn) (to|2) (\w) (\d)'
    
def request_command():
    language_code = 'en-US'

    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        speech_contexts=[{
            "phrases":recommeneded_pharses,
            "boost":boost,
        }],
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content) for content in audio_generator)
        responses = client.streaming_recognize(streaming_config, requests)
        print("here")
        
        for response in responses:
            if not response.results:
                continue

            result = response.results[0]
            if not result.alternatives:
                continue

            # Display the transcription of the top alternative.
            transcript = result.alternatives[0].transcript

            if result.is_final:
                print(transcript)
                
                match = re.search(command_regex, transcript)
                if match:
                    player_command = PlayerCommand(match.group(1),match.group(3),match.group(4))
                    return player_command
                return None

if __name__ == '__main__':
    
    result = request_command()
    print(result)
