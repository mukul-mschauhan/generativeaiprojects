
import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI  # Import for Gemini access


# Title and Text Input
st.title("Movie Recommendation System with Gemini Pro")
user_input = st.text_input("Enter a movie title, genre, or keywords (e.g., Sci-Fi comedy):")

# Prompt Template with Placeholders
# Added the 'template' argument with the prompt string
template = PromptTemplate(
    input_variables=['user_input'],
    template="Based on your preferences, here are some movie recommendations for {user_input}:\n") 

# Initialize LLM Chain with Gemini Pro
llm=ChatGoogleGenerativeAI(model="gemini-pro")

# Generate Recommendations if user input provided
if user_input:
  # Replace placeholder with user input
  prompt = template.format(user_input=user_input)
  recommendations = llm.predict(text=prompt)
  st.write(f"Recommendations for you:\n {recommendations}")
else:
  st.write("Please enter your movie preferences to get recommendations.")
