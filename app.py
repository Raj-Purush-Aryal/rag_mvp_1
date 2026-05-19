from flask import Flask, request, jsonify

from rag import ask_question


app = Flask(__name__)



@app.route("/")
def home():

    return {
        "message": "RAG API is running"
    }



@app.route("/ask", methods=["POST"])
def ask():

    
    data = request.get_json()


    question = data.get("question")

    answer = ask_question(question)

   
    return jsonify({
        "question": question,
        "answer": answer
    })



if __name__ == "__main__":
    app.run(debug=True)