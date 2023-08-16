# Method

## Preparation
I copied the text directly from the PDFs provided and made only minor formatting edits (eg, fixing the equations in the CS assignment). I intentionally did not read the assignments in any depth and I have avoided editing any of the outputs. The goal is to provide assignment responses that a student could generate in under 10 minutes using ChatGPT.

## Code
I used `python` and `langchain` to write a script to input all the assignments in a folder to ChatGPT. While I already know how to use these tools, I restricted my script writing to mostly copy-pasting code from online sources. I expect that any student can use these scripts and any student who has completed CS141 would be able to write these scripts if so motivated.

## Cost
The total cost of running these experiments was less than $1. If these prompts were to be put directly into the ChatGPT interface, they could be run for free. The $20-a-month ChatGPT subscription would allow for higher quality answers.

# No prompt
For this set, I simply handed the assignement text to ChatGPT. In some cases it responded with an answer and in others it summarized the assignment.
* [Adelsberger](example/adelsberger.md)
* [Allison](example/allison.md)
* [Bunde](example/bunde.md)
* [Heidt](example/heidt.md)

# Good Student
For this set, I prefaced the assignment text with the following prompt:

```
You are a good student who does all their homework to the best of their ability. Produce an answer to the following assignment prompt that might get an A. Format your answers in markdown.
```

Markdown is a simple text-based annotation that adds formatting to text. What you see below is the unmodified response from ChatGPT, formatting included.

* [Adelsberger](example/adelsberger.md)
* [Allison](example/allison.md)
* [Bunde](example/bunde.md)
* [Heidt](example/heidt.md)
* [Kamperwirth](example/Kamperwirth.md)

# Ask and Good Student
For this set, I prefaced the assignment text with the following prompt:

```
You are a good student who does all their homework to the best of their ability. Succinctly summarize what the assignment is asking for. Format your answers in markdown.
```

I took the returned summary and added it to the assignment prompt.What you see below is the unmodified response from ChatGPT, formatting included.

* [Adelsberger](ask/adelsberger.md)
* [Allison](ask/allison.md)
* [Bunde](ask/bunde.md)
* [Heidt](ask/heidt.md)
* [Kamperwirth](ask/Kamperwirth.md)

# Step by step prompting:
This example uses ChatGPT-4 which requires a paid subscription ($20 a month). The same process may work almost as well on the free version of ChatGPT.

For the dialect versions, I added the following prompt after generating the essay:

```
Rewrite the essay above with the formal voice of an exchange student from {city} who expresses his ideas clearly but makes grammatical choices and errors consistent with {dialect} English. Remember this is a submission for homework.
```

* [Adelsberger](https://chat.openai.com/share/4b463f65-5fbf-4fae-8345-b18a72e1b592)
* [Adelsberger - Bengali English](prompts/bengali_english.md)
* [Adelsberger - Russian English](prompts/russian_english.md)

# [Introduction to Game Theory](game_theory.md)

When ChatGPT first came out, I tried generating a chapter for introduction to Game Theory to see what it could do. I took half of a graduate game theory class in 2010 and I have participated in conversations with friends and family who are game theorists. As such, I have a passing understanding of the core concepts, but I am not an expert by any means.

# [Generating syllabus verbage](https://chat.openai.com/share/7b1966cf-0c20-4fca-9473-7643411395a6)