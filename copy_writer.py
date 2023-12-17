import openai
from openai import OpenAI

# Function to read the first 10000 characters from a file
def read_file(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read(5000)

# Initialize the OpenAI client
client = OpenAI(
	api_key="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",  # Consider using environment variables for API keys
)

# Start a new chat session
system_prompt = "Je bent een online journalist."
initial_prompt = "Ik stuur je een artikel over film of tv nieuws. Vat het artikel samen in 500 characters MAXIMUM! GEBRUIK GEEN TITELS OF HEADINGS! MAXIMUM 500 CHARACTERS! SCHRIJF HET IN DUTCH! IN HET NEDERLANDS"

# Initialize the messages list
messages = [
	{
		"role": "system",
		"content": system_prompt,
	},
	{
		"role": "user",
		"content": initial_prompt,
	}
]

# File names
file_names = ["written_article.md"]

# Sending content from each article file
for file_name in file_names:
	file_content = read_file(file_name)
	messages.append({"role": "user", "content": file_content})

	# Request a chat completion to process the file content
	chat_completion = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=messages
	)

	if hasattr(chat_completion, 'choices') and len(chat_completion.choices) > 0:
		choice = chat_completion.choices[0]
		if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
			# Append system response to maintain context
			messages.append({"role": "system", "content": choice.message.content})
		else:
			print("No content in the choice message.")
			exit()
	else:
		print("No response or unexpected response structure.")
		exit()

# Request a chat completion to process the final instructions
chat_completion = client.chat.completions.create(
	model="gpt-3.5-turbo",
	messages=messages
)

# Extracting the response
if hasattr(chat_completion, 'choices') and len(chat_completion.choices) > 0:
	choice = chat_completion.choices[0]
	if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
		written_article = choice.message.content.strip()
		# Saving the response to a Markdown file
		with open("post_copy.txt", "w", encoding='utf-8') as txt_file:
			txt_file.write(written_article)
	else:
		print("No content in the choice message.")
		exit()
else:
	print("No response or unexpected response structure.")
	exit()
