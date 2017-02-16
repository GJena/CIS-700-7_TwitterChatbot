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

The replies of the bot seem relevant and coherent. Some responses might even convince a witness that a human was talking.

__Bad sample conversations__

User | Bot
--- | ---
"tell me something interesting" | "the original thing that was in the 00s"
"what do you think of global warming" | "something better than me . . ."
"what do you think of alexa." | "wow , i ' m so fucking gross ."
"mac or windows" | "just in the UNK"
"i am really hungry." | "i ' m not gonna try it ."
"let us go out for a movie." | "not the same thing ."

The replies of the bot , while mostly gramatically correct, don't make sense. The bot isn't able to give satisfactory responses to the user. In one case , 'UNK' i.e. the unknown token also comes up.

__Train loss__

Cross entropy was used as the loss function during training. 10% of the data was used for cross validation. 
Training and cross validation loss was observed after every 200 epochs.  A set of 15 dialogs was created to test the model based on the response generated. This was done after every 2 hours.
Interestingly, minimum cross validation perplexity did not give the best model (in terms of the response generated). 

Train perplexity: 14.91

eval: bucket 0 perplexity 62.31

eval: bucket 1 perplexity 68.73

eval: bucket 2 perplexity 70.96

eval: bucket 3 perplexity 66.86

__Possible metrics__
Since the bot is not task based but free-form, it is harder to evaluate as we cannot just use task completion metrics. A combination of metrics may be best to evaluate the general purpose bot. According to Grice's maxims, effective communication in conversation can be achieved by:
- Quality: speaker’s utterance is the truth as provable by adequate contextual evidence or domain facts
- Quantity: speaker utterance provides as much information as appropriate, not more, not less
- Relation: speaker’s utterance is relevant to the context and the topic of the conversation
- Manner: speaker’s utterance is direct and straightforward

In light of these maxims, some candidate metrics could be:
 - Distance in sentence embeddings
 - Confusion metric: how often it returns ‘I don’t know’ or UNK or a similar response
 - Syntax tree of the generated response
 - Length of the response (to avoid very short and very long answers)
 - Syntax tree of the generated response
 - Overlap of topics in the entire user's dialog and the entire bot's response to ensure relevancy
 - Number of unique tokens to measure information gain
 
### Issues and possible solutions

**Issue:** The bot response varies depending on the presence/absence of punctuations. **Possible solution:**** Use TweetTokenizer to remove emoticons and punctuations (apart from '.', since AMAZON.LITERAL does not capture other punctuations).

**Issue:** Lowest perplexity doesn't guarantee the best model. 
**Possible solution:** Use a more appropriate loss function or a better metric to evaluate the model.

**Issue:** The chatbot doesn't remember previous statements and has no understanding of context.
**Possible solution:** Incorporate memory for recollection and context of conversation.
 
### Future work
 
Future work consists of dealing with the above-mentioned issues. Alternative datasets can be considered to cover a wider range of topics for training. A reinforcement architecture can also be added to inculcate feedback from the users into the model, which may include sentiment/tone analysis. User-specific personalities can be created for the bot which come into play for a given person. The twitter chatbot can also be compared with other bots like ALICE, TickTock. 


