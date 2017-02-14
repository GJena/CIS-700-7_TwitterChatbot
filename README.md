# CIS-700-7_TwitterChatbot

## Homework 3

__Evaluate your chatbot.__ Here, you should show some qualitative examples as well as train and test loss. Furthermore, try to be creative and see if you can make a metric for how well your chatbot is doing.

- good qualitative examples

User: "hey"

Bot: "good morning all"

User:  "how are you."

Bot: "i ' m ok . thanks ."

User: "who is hillary clinton?"

Bot: "hillary is the one who cares ."

User: "you are sweet"

Bot:  "i am a good friend ."

User: "who is donald trump"

Bot: "he is an idiot"

User: "who do the like the best."

Bot:  "you ' re the best i ' ve ever seen ."

User: "cookies"

Bot: "i need that !"

User: "thanks."

Bot:  "no worries !"

User: "get lost"

Bot: "i ' m sorry ."

User: "no way."

Bot: "that is what i said ."

User: "bye"

Bot: "i ' m so fucking sad"



- bad qualitative examples

User: "tell me something interesting."

Bot: "the original thing that was in the 00s"

User: "what do you think of global warming"

Bot: "something better than me . . ."

User: "what do you think of alexa."

Bot: "wow , i ' m so fucking gross ."

User: "mac or windows"

Bot: "just in the _UNK"

User: "i am really hungry."

Bot: "i ' m not gonna try it ."

User: "let us go out for a movie."

Bot: "not the same thing ."


- train loss
- test loss
- Our own metric
Since it is not task based, it is harder to evaluate, we cannot just use task completion metrics. 
A combination of metrics may be best to evaluate the general purpose bot. Some candidate metrics could be:
 - Distance in word2vec embedding
 - Confusion metrics: how often it returns ‘I don’t know’ or UNK?
 - Sentiment analysis on user answers
 
__Identify issues__ with your chatbot and suggest possible solutions and future work.
