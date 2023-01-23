license: MIT  (see licence file for more information)

# couch.py - AI conversational voice assistant that helps you explore your thoughts and feelings
couch.py is a little AI tool to conversationally explore your own thoughts and feelings about things in your life. because it uses voice for input and output, you can lie back on the couch with headphones on and talk things out. it's a little like talking to a therapist, but it's not a therapist it's just a little AI tool. Also, unlike a therapist, you can see how it's put together and can talk to it anytime. note the LLM call is NOT private so this should not be used to discuss confidential information or information you don't want others to know)

## disclaimer
1. this is not a confidential service. openai will receive all conversation so do not use it to discuss things you would not want others to know or discuss confidential information
2. couch.py is not intended to replace real therapy and is not a substitute for professional medical advice, diagnosis or treatment.
3. If you have any concerns about your mental health, please seek professional help.
4. You are responsible for usage of couch.py and any consequences.
5. If in doubt, DO NOT use couch.py
6. couch.py is not intended to be used by children under the age of 13.
7. couch.py uses OpenAI Whisper for ASR to recognize speech, and GPT3 to generate responses.

## Requirements:
1. Python 3.x & pip
2. OpenAI Whisper (and it's dependencies): https://github.com/openai/whisper
3. OpenAI python library: https://github.com/openai/openai-python
4. python pyaudio (and it's dependencies): https://cs.gmu.edu/~marks/112/projects/PlaySong.pdf
5. OpenAI account and API key: https://beta.openai.com/docs/api-reference/authentication
6. currently uses inbuilt MacOS "sayTTS" for TTS. So needs OSX. Will change this.

## Usage:
1. Install the requirements
2. Set your OpenAI API key in couch.py
3. Set your name, MBTI personality type, spoken languages and generation in couch.py
4. Run: `sudo python couch.py` (sudo needed for audio on mac)
5. Audio will be recorded in a turntaking fashion 
6. Press space to stop recording your turn (first time couch will download the whisper model)
7. Say "bye" to exit

## TODO
1. fix multilingual 
2. make TTS less dependent on OSX
