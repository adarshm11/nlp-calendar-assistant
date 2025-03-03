# QuickCal

Calendars are an essential tool for productivity and time management. However, the management of calendars can become a tedious task, with the creation of calendar events to plan everyday tasks like meals, meetings, and leisure activities taking valuable time away from the user. The QuickCal Calendar Assistant aims to streamline this process via the use of a large language model (LLM) to convert plain text into calendar events in the form of `.ics` files.

### LLM Implementation
Due to the time and budget constraints associated with this project, Google's Gemini LLM will be implemented to handle user requests, as opposed to the development of an original LLM. Gemini offers customizable tiers, both free and paid, that can benefit this project.   

When a user inputs a request, the Gemini API will be called with this request passed in, and Gemini will create a `.ics` file that can be easily input into a calendar app. 

### RAG Implementation
In order to optimize the LLM utilization, retrieval-augmented generation (RAG) will be implemented. RAG allows the LLM to adapt to the specific user based on previous requests, allowing for the request to necessitate fewer specific details. A practical example of this is if the user decides to omit the AM or PM keywords in their request. By using the context provided in their current request and the user’s previous events, the LLM can determine the appropriate time to place the event (in the AM or PM) based on relevancy. 

### Technology Stack
To seamlessly integrate the application with iOS and MacOS devices, it is necessary to develop the application using Apple's Swift programming langauge to create a tool that exists in the desktop’s toolbar. Any sensitive data for the RAG database will be end-to-end encrypted using AES-256 and can only be decrypted by the user when retrieving the data. The Firebase DB and LLM will be hosted on a Mint Linux server. The client will communicate to the server using HTTP requests which will be handled on the server side using the Flask framework.  

The Swift app will allow the user to make a request, which will then be routed to the server. The server will utilize the LLM to identify key topics, and if any ambiguity exists the Flask application will query the encrypted Firebase database to fill in the ambiguous fields based on previous similar events. The LLM will then order this data into the Internet Calendaring and Scheduling format, and return it back to the Swift application which will compile it with the `.ics` suffix to append to iCalendar.
