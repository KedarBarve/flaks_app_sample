import openai
from openai import OpenAI
import sys
import json
import os
import sys
from dotenv import load_dotenv,find_dotenv

load_dotenv()

#print ( (os.environ.get("OPENAI_API_KEY")) )

api_key = os.getenv("OPENAI_API_KEY")
#print ( "here1" )
#sys.exit()
#client = OpenAI(api_key=OPEN_AI_KEY)
client = OpenAI()

def read_file_into_buffer(file_path):

    try :
        with open(file_path, 'r') as file:
            file_contents = file.read()

        return file_contents
    except Exception as e :
        print ( str (e) )
        return None
    

def generate_summary_and_sentiment(data, prompt , topic , max_tokens=256):
    
    # Specify the summarization prompt

    if prompt :
        summarization_prompt = prompt 
        summarization_prompt = summarization_prompt.replace("##DATA_SUPPLIED##" , data )
        summarization_prompt = summarization_prompt.replace("##topic##" , topic )
    else :
        sys.exit()

    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        temperature = 0.4,
        messages = [
            {"role": "user", "content": summarization_prompt}
        ]
    )

    summary =  response.choices[0].message.content.strip()
    #return response.choices[0].message.content.strip()

    #print ( response )

    # Request sentiment analysis using ChatGPT
    #sentiment_response = openai.Completion.create(
    #    engine="text-davinci-002",
    #    prompt=sentiment_prompt,
    #    max_tokens=max_tokens,
    #    api_key=api_key
    #)

    # Extract and return the summary and sentiment analysis
    #summary = summarization_response.choices[0].text
    #sentiment = sentiment_response.choices[0].text
    
    #return {'summary': summary, 'sentiment': sentiment} 
    return {'summary': summary }

def generate_description (prompt , data , topic , max_tokens=256):
    
    # Specify the summarization prompt

    if not prompt :
        sys.exit()

    
#    prompt_enhancer = "50) Do not mention Json Data as source in any answers\n 51) Do not mention any entry detail in question or answers\n\n 52) Do not mention any scores  or other related statistics \n\n 53) Generate individual output as a paragraph and not as json data  for each of the items in the json list data\n\n. Format the output as json list"
    prompt_enhancer = "Do not mention Json Data as source in any answers\n 51) Do not mention any entry detail in question or answers\n\n . Do not mention any scores  or other related statistics \n\n" 

    summarization_prompt = prompt  + "\n\n"  + prompt_enhancer + "\n\n" + "Json Data Section : \n" + data


    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        temperature = 0.4,
        messages = [
            {"role": "user", "content": summarization_prompt}
        ]
    )

    search_result =  response.choices[0].message.content.strip()

    return search_result 

def generate_description_for_list (prompt , company_list , topic )  :

    description_list = []
    for company in company_list :
        print ( "Company ----------------" )
        print ( company )
        print ( "Company ----------------" )
        continue
        llm_company_description = generate_description ( prompt , json.dumps ( company ) , topic )
        description_list.append ( llm_company_description )

    return description_list



def main() :

    input_file_path = sys.argv[1]

    prompt_file_path = str(sys.argv[2])

    topic = str(sys.argv[3])

    print ( f"Topic is {topic}" )

    if prompt_file_path :
        prompt = read_file_into_buffer ( prompt_file_path )
    else:
        print ( "No prompt file" )
        sys.exit()

    if not prompt :
        print ( "No prompt file or prompt " )
        sys.exit()
        

#    print ( f"Prompt is {prompt}" )

    file_content = read_file_into_buffer(input_file_path)

    file_content_dict = json.loads ( file_content )

    #print ( file_content_dict )

    company_list = file_content_dict["data"]["list"]


    for company in company_list :
        del company["search_meta"]
        #print ( company )
        #print ("\n\n" )

#    sys.exit()

    #print ( file_content )

    #sys.exit()

    summary = generate_summary_and_sentiment(file_content,prompt , topic )

    new_prompt = summary["summary"]

    print ( summary )

#    description_list = generate_description_for_list ( new_prompt , company_list , topic  )

    company_list_data = json.dumps ( company_list )
    description = generate_description( new_prompt , company_list_data , topic  )

    print ( description )
    
#    for llm_description in description_list :
#        print ( "------------------------------------" )
#        print ( llm_description )
#        print ( "------------------------------------\n\n" )


main()
