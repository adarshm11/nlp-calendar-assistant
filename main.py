import json
import requests
class main:

    data = {
        "model" : "llama3.2",
        "prompt" : "I have a dinner coming up at 6pm at The Cheesecake Factor. Create an .ics file for this event that also reminds me 10 minute before the event happens. Don't include any other text on the essential text for the .ics file"
    }

    response = requests.post("http://localhost:11434/api/generate", json=data)

    response = response.content.decode("utf-8").strip().split("\n")

    output = ""
    for line in response:
        parsed = json.loads(line)
        output += parsed["response"]
    
    print(output)



