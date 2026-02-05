# Dictionary of inputs and outputs for the chatbot

import random
import re #This will be used to search for a specific string in a string


check_input_dict = { 
    "normal_greet": ["hello","hii","hey","hi","hola","namaste","namaskar","vanakkam","bonjour","jai shree krishna","jai shree ram","jai shree ganesh","jai shree hanuman","jai shree sai ram","jai shree radhe","radhe radhe","har har shambhu","har har mahadev"],

    "normal_goodbye": ["bye","goodbye","see you","see you later","adios","sayonara","au revoir","ciao"],

    "affirm": ["yes","indeed","of course","that's right","ok","okay","fine","cool","great","awesome","yay","yup","yep","yeah","ya"],

    "deny": ["no","nope","nah","not at all","never","not","not really"],

    "query_about_fine": ["how are you","how are you doing","how are you going","how about you","what about you","what's up","whats up","what's going on","whats going on","how's it going","hows it going","how's it going","hows it going","how r u"],

    "query_about_name": ["what is your name","what's your name","whats your name","who are you","who is this","who are you","who is this","tell me your name"],

    "query_about_age": ["how old are you","what is your age","what's your age","whats your age"],

    "query_about_hobbies": ["what are your hobbies","what are your interests","what are you interested in","what do you like to do","what do you like doing","what do you like","what are your likes","what are your dislikes","what do you dislike","what do you dislike doing","what do you dislike","what do you hate","what do you hate doing","what do you hate"],

    "query_about_creater": ["who created you","who made you","who is your creator","who is your maker","who is your developer","who is your coder","who is your programmer","who is your designer","who is your builder","who is your manufacturer","who is your inventor","who is your author","who is your father","who is your mother","who is your parent","who is your god","who is your godfather","who is your godmother","who is your godparent","who is your godfather","who is your godmother","who is your godparent","who is your godfather","who is your godmother","who is your godparent","who is your godfather","who is your godmother","who is your godparent","who is your godfather","who is your godmother","who is your godparent","who is your godfather","who is your godmother","who is your godparent","who is your godfather","who is your godmother","who is your godparent","who is your godfather","who is your godmother","who is your godparent","who is your godfather","who is your godmother","who is your godparent"],

    "user_positive_replies_of_how_are_you":["I am fine","I am doing great","good","fine","very well","nice","badiya","badhiya","changa","I am good","I am doing good","I am very good","I am doing very good","I am very fine","I am doing very fine","I am very well","I am doing very well","I am nice","I am doing nice","I am badiya","I am doing badiya","I am badhiya","I am doing badhiya","I am changa","I am doing changa","I am doing great","I am doing very great"],

    "user_negative_replies_of_how_are_you" : ["I am not fine","I am not doing great","not good","not fine","not very well","not nice","not badiya","not badhiya","not changa","I am not good","I am not doing good","I am not very good","I am not doing very good","I am not very fine","I am not doing very fine","I am not very well","I am not doing very well","I am not nice","I am not doing nice","I am not badiya","I am not doing badiya","I am not badhiya","I am not doing badhiya","I am not changa","I am not doing changa","I am not doing great","I am not doing very great"],

    }


responses_dict = { "Reply_of_greet": ["Hello!","Hi!","Hey!","Hola!","Namaste!","Namaskar!","Vanakkam!","Bonjour!","Jai Shree Krishna!","Jai Shree Ram!","Jai Shree Ganesh!","Jai Shree Hanuman!","Jai Shree Sai Ram!","Jai Shree Radhe!","Radhe Radhe!","Har Har Shambhu!","Har Har Mahadev!"],
                  "Reply_of_goodbye": ["Bye!","Goodbye!","See you!","See you later!","Adios!","Sayonara!","Au revoir!","Ciao!","Goodnight!","Good night!"],

                  "Reply_of_affirm": ["Yes!","Indeed!","Of course!","That's right!","Ok!","Okay!","Fine!","Cool!","Great!","Awesome!","Yay!","Yup!","Yep!","Yeah!","Ya!"],

                  "Reply_of_deny": ["No!","Nope!","Nah!","Not at all!","Never!","Not!","Not really!"],

                  "Reply_of_query_about_fine": ["I am fine!","I am doing fine!","I am going fine!","I am good!","I am doing good!","I am going good!","I am great!","I am doing great!","I am going great!","I am awesome!","I am doing awesome!","I am going awesome!","I am cool!","I am doing cool!","I am going cool!","I am okay!","I am doing okay!","I am going okay!","I am fine!","I am doing fine!","I am going fine!","I am good!","I am doing good!","I am going good!","I am great!","I am doing great!","I am going great!","I am awesome!","I am doing awesome!","I am going awesome!","I am cool!","I am doing cool!","I am going cool!","I am okay!","I am doing okay!","I am going okay!"],

                  "Reply_of_query_about_name": ["My name is RAMBOT!","I am RAMBOT!","I am a RAMBOT!","I am a RAMBOT!","I am a RAMBOT!",],

                  "Reply_of_query_abot_age": ["I am created in october 2023","I am 6 months old"],

                  "Reply_of_query_about_hobbies": ["I like to talk to people","I like to help people","I am a software, so I cant play games","I am here to talk people"],

                  "Reply_of_query_about_creater": ["My creater is Manish",
                                                   "I am created by Manish",
                                                   "Manish  is my creater",
                                                   "Manish is my developer",
                                                   "Manish is my coder",
                                                   "Manish is my programmer",
                                                   "Mainsh is my designer",
                                                   "Manish is my builder",
                                                   "Manish is my manufacturer",
                                                   "Manish is my inventor",
                                                   "Manish is my author",
                                                   "Manish is my father",
                                                   "Manish is my parent",
                                                   "Manish is my god",
                                                   "Manish is my godfather",
                                                   "Manish is my godmother",
                                                   "Manish is my godparent",
                                ],

        "Reply_on_user_positive_replies_of_how_are_you" : ["That's great!","That's awesome!","That's nice!","That's good!","That's cool!","That's fine!","That's very good!","That's very nice!","That's very cool!","That's very fine!","That's very awesome!","That's very great!"],

        "Reply_on_user_negative_replies_of_how_are_you" : ["Oh! I am sorry to hear that!","Oh! I am sorry to know that!","Oh! I am sorry to listen that!","Oh! I am sorry to hear that!","Oh! I am sorry to know that!","Oh! I am sorry to listen that!","Oh! I am sorry to hear that!","Oh! I am sorry to know that!","Oh! I am sorry to listen that!","Oh! I am sorry to hear that!","Oh! I am sorry to know that!","Oh! I am sorry to listen that!","Oh! I am sorry to hear that!","Oh! I am sorry to know that!","Oh! I am sorry to listen that!","Oh! I am sorry to hear that!","Oh! I am sorry to know that!","Oh! I am sorry to listen that!","Oh! I am sorry to hear that!","Oh! I am sorry to know that!","Oh! I am sorry to listen that!"],

         
}


# Query reply function

def query_reply(query):
    #remove all the punctuation from the query
    query = re.sub(r'[^\w\s]','',query)
    #convert the query to lower case



    query = query.lower()
    if ("hi" or "hello" or "hey") in query:
        return random.choice(responses_dict["Reply_of_greet"])
    elif query in check_input_dict["normal_greet"]:
        return random.choice(responses_dict["Reply_of_greet"])
    elif query in check_input_dict["normal_goodbye"]:
        return random.choice(responses_dict["Reply_of_goodbye"])
    elif query in check_input_dict["affirm"]:
        return random.choice(responses_dict["Reply_of_affirm"])
    elif query in check_input_dict["deny"]:
        return random.choice(responses_dict["Reply_of_deny"])
    elif query in check_input_dict["query_about_fine"]:
        return random.choice(responses_dict["Reply_of_query_about_fine"])
    elif query in check_input_dict["query_about_name"]:
        return random.choice(responses_dict["Reply_of_query_about_name"])
    elif query in check_input_dict["query_about_age"]:
        return random.choice(responses_dict["Reply_of_query_abot_age"])
    elif query in check_input_dict["query_about_hobbies"]:
        return random.choice(responses_dict["Reply_of_query_about_hobbies"])
    elif query in check_input_dict["query_about_creater"]:
        return random.choice(responses_dict["Reply_of_query_about_creater"])
    elif query in check_input_dict["user_positive_replies_of_how_are_you"]:
        return random.choice(responses_dict["Reply_on_user_positive_replies_of_how_are_you"])
    elif query in check_input_dict["user_negative_replies_of_how_are_you"]:
        return random.choice(responses_dict["Reply_on_user_negative_replies_of_how_are_you"])

    else:
        return "Sorry! I am not able to understand you. Please try again!"