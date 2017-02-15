# CIS-700-7_TwitterChatbot

## Homework 3

Chatbot trained on Twitter dataset as part of Homework 3 for CIS 700-7. It has been integrated with the 'chat' skill on Alexa.

### Evaluation of chatbot
There are different aspects we considered for evaluation of our chatbot. First we present a qualitative evaluation along with good and bad examples.

__Good sample conversations__

User | Bot
--- | ---
"hey" | "good morning all"
"how are you." | "i ' m ok . thanks ."
"who is hillary clinton?" | "hillary is the one who cares ."
"you are sweet" | "i am a good friend "
"who is donald trump" | "he is an idiot"
"who do the like the best." | you ' re the best i ' ve ever seen .
"cookies" | "i need that !"
"thanks." | "no worries !"
"get lost" | "i ' m sorry ."
"no way." | "that is what i said ."
"bye" | "i ' m so fucking sad"

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

Cross entropy was used as the loss function during training.

__Test loss__

__Possible metrics__
Since it is not task based, it is harder to evaluate, we cannot just use task completion metrics. 
A combination of metrics may be best to evaluate the general purpose bot. Some candidate metrics could be:
 - Distance in word2vec embedding
 - Confusion metrics: how often it returns ‘I don’t know’ or UNK?
 - Sentiment analysis on user answers
 
### Issues and possible solutions


### Future work
