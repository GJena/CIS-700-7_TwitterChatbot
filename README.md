# CIS-700-7_TwitterChatbot

## Homework 3

Chatbot trained on Twitter dataset as part of Homework 3 for CIS 700-7. It has been integrated with the 'chat' skill on Alexa.

### Evaluation of chatbot ### 

There are different aspects we considered for evaluation of our chatbot. First we present a qualitative evaluation along with good and bad examples.

__Good sample conversation__

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

The replies of the bot in the above conversation seem relevant and coherent. Some responses might even convince a witness that a human was talking.

__Bad sample conversation__

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

The replies of the bot in the above conversation, while mostly gramatically correct, don't make sense. The bot isn't able to give satisfactory responses to the user. In one case , 'UNK' i.e. the unknown token also comes up.

__Train loss__

__Test loss__

__Possible metrics__
Since it is not task based, it is harder to evaluate, we cannot just use task completion metrics. 
A combination of metrics may be best to evaluate the general purpose bot. Some candidate metrics could be:
 - Distance in word2vec embedding
 - Confusion metrics: how often it returns ‘I don’t know’ or UNK?
 - Sentiment analysis on user answers
 
### Issues and possible solutions ### 


### Future work ###
