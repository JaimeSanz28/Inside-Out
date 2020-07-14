from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from flask import request
from src.helpers.errorHelpers import APIError, Error404, checkValidParams, errorHelper
from bson.json_util import dumps


client = MongoClient(DBURL)
print("Connected to DBURL")
db = client.get_default_database()


# Welcoming API

@app.route("/")
def Welcome_():
     print("Hello")



# Creating new user

@app.route("/user/create/<username>", methods=["GET"])
@errorHelper()
def creandoUsuarioDiferenteAlDeMiriam(username):
    name_taken = db.user.distinct("name")
    add_user= {"username": username}
    if username in name_taken:
        raise APIError(f"User_name {username} already exists")
    else:
        user_id = db.user.insert_one(add_user)
        return dumps(f"The user was succesfully created!! user_name: {username}, user_id: {user_id.inserted_id}")


# Creating new chat

@app.route("/chat/create")
@errorHandler
def createChat():
    """    
    This function creates a new chat with Participants as a param and assigns a groupname to the chat.
    """
    group = request.args.getlist("Participants")
    group_name= request.args.get("Group_name")
    if db.convo.find_one({"Group_name":group_name}) == None:
        create_chat = db.convo.insert({"Group_name":group_name, "Participants": participants}) 
        return dumps(f"The chat was succesfully created!! convo_id: {create_chat}")
    raise APIError(f"Group_name {group_name} already exists")


# Adding user to chat

@app.route("/chat/<conversation_id>/adduser")
@errorHandler
def add_more_tochat(conversation_id):
    """    
    This function adds an existing user to a certain group chat.
    """
    if db.convo.find_one({"_id":ObjectId(conversation_id)}):
        new_user = request.args.get("user_name")
        add_user = db.convo.update({"_id":ObjectId(conversation_id)},{"$push":{"Participants":{"$each": new_user}}})
        return dumps(f"The user was succesfully added to the chat!!! user_id: {new_user}, conversation_id: {conversation_id} ")
    raise Error404("Sorry, that convo has not been created yet. Please be so kind as to try a different one.") 


# Adding message to chat
# (form instead of args because the method is POST and not GET)

@app.route("/chat/<conversation_id>/addmessage/<user_id>",methods = ['POST'])
@errorHandler
def addmessage(conversation_id:
    """    
    This function adds a message to an existing chat.
    """
     if db.convo.find_one({"_id":ObjectId(conversation_id),"Participants":user_id}) :
        add_message= db.chatItem.insert({"conversation_id":ObjectId(conversation_id), "user_id": user, "message":f'{mensaje}'})
        return dumps(f"The message was succesfully added!! message_id: {add_message}")
    raise Error404("Something went wrong, please try again.") 


# Retrieving all messages from x chat

@app.route("/chat/<conversation_id>/list")
def retrieve_all(conversation_id):
    all_m = db.chatItem.find({"conversation_id": ObjectId(conversation_id)}, {"message":1, "_id":0})
    messages= dumps(db.chatItem.find({"conversation_id": ObjectId(conversation_id)}, {"user_id":1,"message":1, "_id":0}))
    return dumps(messages)
