from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

NR_OF_LINES = int


prompt = """

USE [Hotel]
GO

/****** Object:  Table [dbo].[contact_info]    Script Date: 12/4/2023 10:20:31 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[contact_info](
	[contact_info_id] [int] IDENTITY(1,1) NOT NULL,
	[phone] [nvarchar](50) NOT NULL,
	[email] [nvarchar](50) NOT NULL,
	[address] [nvarchar](500) NOT NULL,
 CONSTRAINT [PK_contact_info] PRIMARY KEY CLUSTERED 
(
	[contact_info_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

"""

def get_response():
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
           {"role": "system", "content": prompt},
            {"role": "user", "content": f"Generate an SQL Server insert statement with 5 lines of dummy data."},
        ]
    )
    # )
    # start_index = completion.choices[0].message.content.find("INSERT INTO")
    # end_index = completion.choices[0].message.content.find(";") + 1
    return completion.choices[0].message.content


















#     def __init__ (self):
#         self.api_key = os.environ.get("OPENAI_API_KEY")

#     def get_response(
#             self, 
#             prompt, 
#             engine="text-davinci-002", 
#             max_tokens=150, 
#             temperature=0.9, 
#             top_p=1, 
#             frequency_penalty=0, 
#             presence_penalty=0, 
#             stop=["\n"]
#             ):
        
#             response = OpenAI.completions.create(
#                 engine=engine,
#                 prompt=prompt,
#                 max_tokens=max_tokens,
#                 temperature=temperature,
#                 top_p=top_p,
#                 frequency_penalty=frequency_penalty,
#                 presence_penalty=presence_penalty,
#                 stop=stop,
#             )
#             return response

# OpenAIUtils = OpenAIUtils()

# prompt = "Tell me a joke"

# response = OpenAIUtils.get_response(prompt)

# print(response.choices[0].text)

# client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# completion = client.chat.completions.create(
#   model="text-davinci-002",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)