from flask import Flask, jsonify, request
app = Flask(__name__)

faqs = [
    {'id': 1, 'question': 'What is Fruit.ai?', 'answer': 'Fruit.ai is a health management app.'},
    # Add more FAQs as needed
]

@app.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

@app.route('/faqs/<int:id>', methods=['GET'])
def get_faq(id):
    faq = next((faq for faq in faqs if faq['id'] == id), None)
    return jsonify(faq) if faq else ('', 404)

@app.route('/faqs', methods=['POST'])
def create_faq():
    data = request.get_json()
    new_id = max(faq['id'] for faq in faqs) + 1 if faqs else 1
    new_faq = {'id': new_id, **data}
    faqs.append(new_faq)
    return jsonify(new_faq), 201

@app.route('/faqs/<int:id>', methods=['PUT'])
def update_faq(id):
    data = request.get_json()
    faq = next((faq for faq in faqs if faq['id'] == id), None)
    if faq:
        faq.update(data)
        return jsonify(faq)
    return ('', 404)

@app.route('/faqs/<int:id>', methods=['DELETE'])
def delete_faq(id):
    global faqs
    faqs = [faq for faq in faqs if faq['id'] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
