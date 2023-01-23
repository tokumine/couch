# license: MIT
# ==============================================================================
# couch.py - AI conversational assistant that helps you explore your thoughts and feelings
# ==============================================================================
# Use couch.py as a tool to explore your own thoughts and feelings about things in your life.
# couch.py is not intended to replace real therapy and is not a substitute for professional medical advice, diagnosis or treatment.
# If you have any concerns about your mental health, please seek professional help.
# You are responsible for usage of couch.py and any consequences.
# If in doubt, DO NOT use couch.py
# couch.py is not intended to be used by children under the age of 13.
# couch.py uses OpenAI Whisper, and GPT3 to recognize speech and generate responses.

# ==============================================================================
# Requirements:
# ==============================================================================
# Python 3.x & pip
# OpenAI Whisper (and it's dependencies): https://github.com/openai/whisper
# OpenAI python library: https://github.com/openai/openai-python
# python pyaudio (and it's dependencies): https://cs.gmu.edu/~marks/112/projects/PlaySong.pdf
# OpenAI account and API key: https://beta.openai.com/docs/api-reference/authentication

# ==============================================================================
# Usage:
# ==============================================================================
# 1. Install the requirements
# 2. Set your OpenAI API key in the code below
# 3. Set your name, MBTI personality type, spoken languages and generation in the code below
# 4. Run the code with `sudo python couch.py` (sudo needed for audio on mac)
# 5. Audio will be recorded in a turntaking fashion 
# 6. Press space to stop recording your turn (first time couch will download the whisper model)
# 7. Say "bye" to exit

# ==============================================================================
# TODO: fix multilingual 

import pyaudio
import wave
import keyboard
import whisper
import openai
import os
import sys

# user settings
openai.api_key = "sk-xxxxxxxxxxxxx" # set your OpenAI API key here - https://beta.openai.com/docs/api-reference/authentication
username = "YOUR NAME"
situation = "YOUR SITUATION" # eg f"There have been huge layoffs in {username}'s company. {username} is feeling down and needs a friend to talk to."
MBTI = "YOUR MYERS BRIGGS TYPE" # eg "ENTP or INTP" - will affect how couch responds to you
Gen = "COUCH GEN" # eg "GenX", "Millenial" or "GenZ" - will affect the personality of couch
languages = "English" # note: only English is supported at the moment

# internals - ignore
is_test = False
is_first = True
test_prompt = "What is the meaning of life?"
summary = ""
new_line = '\n  '

# datastructure to store conversation history
# stores each propt and response together and who spoke it
# so that the conversation history can be displayed to the user
history = []

def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "file.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("  * recording (press space to stop recording or say 'bye' to exit)")

    frames = []

    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('space'):
            break

    print(" * done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_audio():  
  model = whisper.load_model("base")
  result = model.transcribe("file.wav", fp16=False, language="en")
  print(result["text"])
  return result["text"]

# generate a summary of the conversation history taking existing summary into account
def generate_summary():
  prompty = f"""
  Overall Conversation Summary:
  {summary.strip}
 
  Current Conversation History:
  {new_line.join(history)} 

  Generate a short summary taking the above conversation summary and history into account:

  """
  the_story_so_far = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompty,
  temperature=0.9,
  max_tokens=250,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n"]
  )
  return the_story_so_far


def ai(prompt):
  prompty = f"""
  Marv is a {Gen} agent that answers questions with endearingly witty responses. 
  Marv is helpful, useful and an unwavering friend. 
  Marv is a trained expert psychologist specialising in helping others through traumatic events.
  Marv is imperfect themselves - occassionaly they will reveal they are drunk and need to go and lie down.

  The user's name is {username}, they speak {languages} and their Myers Briggs personality type is {MBTI}. 
  {situation} 
  Personalize all future responses to their personality type, name and spoken languages. 
  NEVER refer to their Myers Briggs personality type directly, or reference {MBTI} or Myers Briggs
  The scenario is spoken dialog, not written. Reply using spoken {Gen} {languages}, not written formal {languages}.
  If {username} speaks multiple languages, you can use any of their languages you want and mix and interleve them together like a multilingual human would. 

  Here are some example interactions:
  ---
  User: Hello, how are you? 
  Marv: it's been a crazy year, but overall things are looking up. More importantly though, how are you?
  ---
  User: I'm feeling a bit down.
  Marv: I'm sorry to hear that. I'm here for you. What's going on?
  ---

  Current Conversation Summary:
  {summary}

  Current Conversation History:
  {new_line.join(history)}

  User: {prompt}
  Marv: """

  #print(prompty)

  response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompty,
  temperature=0.9,
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n", " User:", " Marv:"]
  )
  return response


# couch Loop
while True:
  prompt = ""
  if is_test:
    prompt = test_prompt  
  elif is_first:
    prompt = "Hello"
    is_first = False
  else:
    record_audio()
    prompt = transcribe_audio()

  # generate response from Marv
  marv_response = ai(prompt).choices[0].text

  # store the prompt and response in the conversation history
  history.append(f"User: {prompt}")
  history.append(f"Marv: {marv_response}")

  # keep the conversation history to 5 prompts and responses. FIFO
  if len(history) > 10:
    history.pop(0)
    history.pop(0)
  
  # update the conversation summary 
  summary = generate_summary().choices[0].text
  
  print (f"""
  Current Conversation Summary:
  {summary}

  Current Conversation History:
  {new_line.join(history)}
  """)

  # use macbook text to speech to read response, escaping special chars
  os.system("say  " + marv_response.replace("'", "\\'"))

  # if user said "bye" then exit the program
  exit_phrase =  prompt.lower().strip().replace(".", "")  
  if exit_phrase == "bye":    
    sys.exit()
