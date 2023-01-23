license: MIT  (see licence file for more information)

# shrink.py - AI voice assistant that helps you explore your thoughts and feelings
shrink.py is a little AI tool to conversationally explore your own thoughts and feelings about things in your life

## disclaimer
1. Shrink.py is not intended to replace real therapy and is not a substitute for professional medical advice, diagnosis or treatment.
2. If you have any concerns about your mental health, please seek professional help.
3. You are responsible for usage of shrink.py and any consequences.
4. If in doubt, DO NOT use shrink.py
5. shrink.py is not intended to be used by children under the age of 13.
6. shrink.py uses OpenAI Whisper, and GPT3 to recognize speech and generate responses.

## Requirements:
1. Python 3.x & pip
2. OpenAI Whisper (and it's dependencies): https://github.com/openai/whisper
3. OpenAI python library: https://github.com/openai/openai-python
4. python pyaudio (and it's dependencies): https://cs.gmu.edu/~marks/112/projects/PlaySong.pdf
5. OpenAI account and API key: https://beta.openai.com/docs/api-reference/authentication

## Usage:
1. Install the requirements
2. Set your OpenAI API key in the code below
3. Set your name, MBTI personality type, spoken languages and generation in the code below
4. Run the code with `sudo python shrink.py` (sudo needed for audio on mac)
5. Audio will be recorded in a turntaking fashion 
6. Press space to stop recording your turn (first time shrink will download the whisper model)
7. Say "bye" to exit

## TODO
1. fix multilingual 