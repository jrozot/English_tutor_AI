# app/routes.py

from flask import Blueprint, request, jsonify, render_template
from app.grammar_corrector import GrammarCorrector

routes = Blueprint('routes', __name__)
gc = GrammarCorrector()

@routes.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@routes.route('/correct', methods=['POST'])
def correct():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({
            "error": "No se recibió texto para corregir."
        }), 400

    text = data['text']
    result = gc.correct_text(text)

    # If you want to add Spanish translation (mock example, replace with actual if needed)
    result['translated'] = translate_to_spanish(result["corrected"])

    return jsonify(result)


# Dummy translation function (replace with real translation service if needed)
def translate_to_spanish(text):
    return f"(traducción simulada) {text}"
