import google.generativeai as genai

def get_response(model, prompt):
    response = model.generate_content(prompt)
    return response.text