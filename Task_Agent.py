import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def read_task(filepath):
  with open(filepath, "r") as f:
    return f.read()
  

def category_task(task):
  prompt = """ 
          You are a smart Task planning agent.
          Given a list of task. Your role is to categorize into 3 priorities.
          
          Buckets:
          High Priority
          Medium Priority
          Low Priority

          Tasks:
          {task}

          Return response in this format:
          
          High Priority
          - Task 1
          - Task 2

          Medium Priority:
          - Task 1
          - Task 2

          Low Priority:
          - Task 1
          - Task 2
        """

  response = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages= [
      {"role": "user", "content": prompt}
    ]
  )

  return response.choices[0].message.content



if __name__ == "__main__":
  task_text = read_task("task.txt")
  category = category_task(task_text)
  print("\n Category Task \n")
  print("-" * 20)
  print(category)