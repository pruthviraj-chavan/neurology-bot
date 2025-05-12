from flask import Flask, render_template, request, jsonify
from neurology_qa import NEUROLOGY_QA
from rapidfuzz import process, fuzz

app = Flask(__name__)

def find_best_answer(user_input):
    questions = [qa["question"] for qa in NEUROLOGY_QA]
    # Use rapidfuzz to find the best match
    best_match = process.extractOne(user_input, questions, scorer=fuzz.token_sort_ratio)
    if best_match and best_match[1] > 70:  # 70 is a reasonable threshold for similarity
        matched_question = best_match[0]
        for qa in NEUROLOGY_QA:
            if qa["question"] == matched_question:
                return qa["answer"]
    return "I'm sorry, I don't have an answer for that specific question. Please consult a certified neurologist for more information."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question', '')
    if not user_input:
        return jsonify({'response': 'Please enter a question.'})
    response = find_best_answer(user_input)
    return jsonify({'response': response})

# For local development
if __name__ == '__main__':
    app.run()

# For Vercel deployment
app = app 