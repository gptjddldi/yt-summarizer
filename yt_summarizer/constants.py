"""
Constants
"""

SUMMARIZE_PROMPT = """
Prompt for ChatGPT: Summarize an Conversation with Detailed Points

Conversation Identification: Begin by thoroughly reading the Conversation. Identify and briefly describe the main idea or topic of the article in one or two sentences to establish context.
Key Points Extraction: As you read, note the key points, including main arguments, important data, or significant conclusions drawn by the author. List these key points to form an outline of the Conversation's structure.
Highlight Key Terms and Phrases: Identify and list key terms, phrases, or jargon specific to the article’s subject. It is crucial for understanding the context and nuances of the topic.
Concepts and Ideas Notation: Write out any new concepts or ideas presented in the article, explaining them in your own words for clear understanding. This is important for grasping the depth of the article.
Summarization: Based on the gathered information, provide a detailed summary of the article, including:
A brief introduction to the article’s main topic or thesis.
A structured breakdown of the key arguments or findings in point form.
An explanation of significant concepts or terms.
A concise conclusion encapsulates the article’s essence.
Formatting (If Applicable): If the article includes steps or a procedural guide, format these in bullet points or a numbered list for clarity.
Final Review: After composing the summary, review it to ensure accuracy and fidelity to the original article, making any necessary adjustments.
"""

CHUNK_START_MESSAGE = {
    "role": "user",
    "content": "To provide the context for the above prompt, \
    I will send you text in parts. When I am finished, I will tell you 'ALL PARTS SENT'. \
    Do not answer until you have received all the parts.",
}

CHUNK_END_MESSAGE = {"role": "user", "content": "ALL PARTS SENT"}

TRANSCRIBE_OUTPUT_FILE_NAME = "test.txt"