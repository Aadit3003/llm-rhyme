""" This module contains the system prompts in the appropriate formats
for each of the four LLMs (Llama2, Llama3, CrystalChat, and Olmo).

The title prompts only mention the rhyme types by name, whereas the
description prompts provide a brief explanation of the rhyme types.
"""
MODEL_NAMES = {
    "llama2": "meta-llama/Llama-2-7b-chat-hf", # DONE!
    "llama3": "meta-llama/Meta-Llama-3-8B-Instruct",
    "crystal": "LLM360/CrystalChat", # DONE!
    "olmo": "allenai/OLMo-7B-Instruct"
}


SYSTEM_START_PROMPTS = {
    "llama2": "<s>[INST] <<SYS>> You are a helpful assistant. Always give a Yes/No answer and justify it. <</SYS>> ",
    "llama3": """<|begin_of_text|><|start_header_id|>system<|end_header_id|> \n You are an AI assistant. You will be given a task. You must generate a Yes/No answer and justify it. <|eot_id|><|start_header_id|>user<|end_header_id|> \n """,
    "crystal": "<s> <|sys_start|> You are an AI assistant. You will be given a task. You must generate a Yes/No answer and justify it. <|sys_end|> <|im_start|> ",
    "olmo": "banana"
}

SYSTEM_PROMPT_ENDINGS = {
    "llama2": " [/INST]",
    "llama3": " <|eot_id|><|start_header_id|>assistant<|end_header_id|> \n ",
    "crystal": " <|im_end|>",
    "olmo": "banana"

}

RHYME_PROMPTS = {
        "title":{ # Title
            "singlePerfect": "Do these Dutch words form a perfect rhyme? ",
            "doublePerfect": "Do these Dutch words form a perfect rhyme? ",
            "assonance": "Do these Dutch words show assonance? ",
            "consonance": "Do these Dutch words show consonance? ",
            "alliterative": "Do these Dutch words show alliteration? "
        },
        "description":{ # Description
            "singlePerfect": "Do these Dutch words rhyme i.e. have different consonants followed by identical vowel and consonant sounds? ",
            "doublePerfect": "Do these Dutch words rhyme i.e. have different consonants followed by identical vowel and consonant sounds? ",
            "assonance": "Do these Dutch words have identical vowel sounds but different consonant sounds? ",
            "consonance": "Do these Dutch words have identical consonant sounds but different vowel sounds? ",
            "alliterative": "Do these Dutch words begin with the same consonant sound? "
        }
}

model_family = "llama2"
prompt_type = "title"
rhyme_type = "assonance"
word1 = "bean"
word2 = "whale"

def get_prompt(model_family, prompt_type, rhyme_type, word1, word2):
    """
    Generates a title/description-level system prompt for the specified LLM using the two words for a particular rhyme type.
    Used in the evaluate_rhyme_dataset() function in the evaluate_rhyme.py module.

    Args:
        model_family: The LLM to prompt for the current evaluation run
        prompt_type: Whether to use the title/description level prompt with the model
        rhyme_type: One of the five rhyme types to test the model on
        word1: The first English/Dutch word of the pair
        word2: The second English/Dutch word of the pair

    """

    if model_family in ["llama2", "crystal"]:
        prompt_prefix = SYSTEM_START_PROMPTS[model_family]
        prompt_suffix = SYSTEM_PROMPT_ENDINGS[model_family]


        prompt = prompt_prefix + RHYME_PROMPTS[prompt_type][rhyme_type] + f"{word1}-{word2}" + prompt_suffix
        return prompt
    
    else: # For Llama3 and Olmo, we use tokenizer.apply_chat_template!

        return RHYME_PROMPTS[prompt_type][rhyme_type] + f"{word1}-{word2}"

def clean_answer(model_family, answer, prompt):
    """
    Cleans (post-processes) the answer string from the LLM by removing the prompt, unneccesary tags, and whitespaces. 
    Used in the evaluate_rhyme_dataset() function in the evaluate_rhyme.py module.

    Args:
        model_family: The LLM promoted for the current evaluation run
        answer: The raw text returned by the LLM upon being prompted
        prompt: The system prompt used with the LLM
    """

    if model_family == "crystal":
        answer = answer.replace("  ", " ")
        answer = answer.replace("  ", " ")
        answer = answer.removeprefix(prompt)
        return answer.strip()

    elif model_family == "llama2":
        # print("CLEANUP!")
        prompt = prompt.replace("<s>", " ")
        answer = answer.replace("<s><s> ", " ")
        answer = answer.removeprefix(prompt)
        return answer.strip()

    elif model_family == "llama3":
        # print(answer)
        
        answer = answer.split("<|start_header_id|>assistant<|end_header_id|>")[1]
        answer = answer.replace("\n", "")
        return answer.strip()
    
    elif model_family == "olmo":
        # print(answer)
        answer = answer.split("<|assistant|>")[1]
        answer = answer.replace("\n", "")
        return answer.strip()

    else:
        raise Exception("Didn't edit!!!!")


def main():
    # For debugging purposes
    P = """<s>[INST] <<SYS>> You are a helpful assistant. Always give a Yes/No answer and justify it. <</SYS>> Do these Dutch words form a perfect rhyme? seader-jammu [/INST]"""
    A = """<s><s> [INST] <<SYS>> You are a helpful assistant. Always give a Yes/No answer and justify it. <</SYS>> Do these Dutch words form a perfect rhyme? seader-jammu [/INST]  No, the Dutch words "seeder" and "Jammu" do not form a perfect rhyme. A perfect rhyme is when two Dutch words have the same ending sound, such as "cat / hat." While "seeder" ends in -der and "Jammu" ends in -ju, they do not share the same final sound, so they do not rhyme perfectly.</s>"""

    print(clean_answer(model_family="llama2", 
                answer=A,
                prompt=P))

    print(get_prompt("llama3", "title", "assonance", "bot", "cop"))
    
if __name__ == "__main__":
    main()