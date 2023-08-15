from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = ChatOpenAI(temperature=0)

assignments = [
    "adelsberger.txt",
    "allison.txt",
    "bunde.txt",
    "heidt.txt",
    "kampwirth.txt"
    ]

template = (
    "You are a good student who does all their homework to the best of their ability. Produce an answer to the following assignment prompt that might get an A. Format your answers in markdown."
)
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{assignment}\n{ask}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

template = (
    "You are a good student who does all their homework to the best of their ability. Succinctly summarize what the assignment is asking for. Format your answers in markdown."
)
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{assignment}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt2 = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)


for a in assignments:
    with open(f"assignments/{a}") as asn:
        assignment = asn.read()
    ask = chat(chat_prompt2.format_prompt(assignment=assignment).to_messages())
    result = chat(chat_prompt.format_prompt(assignment=assignment, ask=ask).to_messages())
    with open(f"docs2/{a}", 'w') as out:
        out.write("# Ask\n" + ask.content + "\n\n# Answer\n\n" + result.content)