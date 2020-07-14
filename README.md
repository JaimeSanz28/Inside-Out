# Inside-Out
4th Project for Ironhack Data Analytics Bootcamp

<img src="https://www.revuze.it/wp-content/uploads/2019/07/sentiment-analysis-Featured-1024x576.png"/>

#width="500" height="350" 


## Description

This is a **Flask - Api Creation** project for *Ironhack*. 
The purpose of the project is to extract sentiment metrics from text interactions, through the analysis conversations from a chat messaging app (such as Whatsapp or Slack). I have used MongoDB to analyze the data (using pymongo insert methods), NTLK Sentiment Analysis, Docker, Heroku, Cloud databases and recommender systems.

## Schema

<img src=https://mermaid.ink/img/eyJjb2RlIjoiY2xhc3NEaWFncmFtXG4gICAgICBDaGF0SXRlbSA8fC0tIENvbnZlcnNhdGlvbiA6IFwiY29udGFpbnNcIlxuICAgICAgQ2hhdEl0ZW0gPHwtLSBVc2VyIDogXCJoYXMgc2VudFwiXG4gICAgICBDb252ZXJzYXRpb24gPHwtLSBVc2VyIDogXCJpcyBwYXJ0IG9mXCJcbiAgICAgIGNsYXNzIENoYXRJdGVte1xuICAgICAgICAgICtPYmplY3RJZCBcIl9pZFwiXG4gICAgICAgICAgK1N0cmluZyBtZXNzYWdlX3RleHRcbiAgICAgICAgICArT2JqZWN0SWQgdXNlclxuICAgICAgICAgICtPYmplY3RJZCBjb252ZXJzYXRpb25cbiAgICAgIH1cbiAgICAgIGNsYXNzIENvbnZlcnNhdGlvbntcbiAgICAgICAgICArT2JqZWN0SWQgXCJfaWRcIlxuICAgICAgICAgICtTdHJpbmcgbmFtZVxuICAgICAgICAgICtBcnJheTxPYmplY3RJZD4gdXNlcnNcbiAgICAgIH1cbiAgICAgIGNsYXNzIFVzZXJ7XG4gICAgICAgICAgK09iamVjdElkIFwiX2lkXCJcbiAgICAgICAgICArU3RyaW5nIG5hbWVcbiAgICAgIH1cbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9/>


## User and Chat Endpoints

(GET) `/chat/create`
  - **Purpose:** Create a conversation to load messages on it. You can use a `jupyter notebook` to test it using the requests module.
  - **Params:** An array of users ids `[user_id]`
  - **Returns:** `conversation_id`

- (GET) `/chat/<conversation_id>/adduser`
  - **Purpose:** Add a user to a chat conversation
  - **Params:** `user_id`
  - **Returns:** `conversation_id`

- (POST) `/chat/<conversation_id>/addmessage`
  - **Purpose:** Add a message to a conversation. Important: Before adding the chat message to the database, check that the incoming user is part of this conversation. If not, raise an exception.
  - **Params:**
    - `conversation_id`: Chat to store message
    - `user_id`: the user that writes the message
    - `text`: Message text
  - **Returns:** `message_id`

- (GET) `/chat/<conversation_id>/list`
  - **Purpose:** Get all messages from `conversation_id`
  - **Returns:** json array with all messages from this `conversation_id`
​

## Sentiment analysis and recommender
​
- (GET) `/chat/<conversation_id>/sentiment`
  - **Purpose:** Analyze messages from `chat_id`. Use `NLTK` sentiment analysis package for this task
  - **Returns:** json with all sentiments from messages in the chat
​
- (GET) `/user/<user_id>/recommend`
  - **Purpose:** Recommend friend to this user based on chat contents
  - **Returns:** json array with top 3 similar users