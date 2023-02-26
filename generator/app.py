from flask import Flask, render_template, request

import openai

app = Flask("geniusgen")

# Initialize OpenAI API key
openai.api_key = "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"

# Define GPT-3 parameters
model_engine = "text-davinci-002"
prompt = "The User will send you details about their business. I want you to create a detailed business plan with as little information you"

# Function to generate business plan
def generate_business_plan(prompt, model_engine, user_input):
    prompt += " " + user_input + "\n"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5
    ).choices[0].text
    return response

# Route to generate business plan
@app.route('/', methods=['GET', 'POST'])
def business_plan_generator():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            response = generate_business_plan(prompt, model_engine, user_input)
            return render_template('business_plan.html', response=response)
        else:
            error_message = "Please enter some text to generate a business plan."
            return render_template('index.html', error=error_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)