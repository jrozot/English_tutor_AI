# app/grammar_corrector.py

import language_tool_python
from deep_translator import GoogleTranslator


class GrammarCorrector:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')
        self.translator = GoogleTranslator(source='en', target='es')

    def correct_text(self, text: str) -> dict:
        matches = self.tool.check(text)
        corrected_text = language_tool_python.utils.correct(text, matches)
        translated_text = self._translate(corrected_text)

        feedback = self._generate_feedback(matches)

        return {
            "original": text,
            "corrected": corrected_text,
            "translated": translated_text,
            "feedback": feedback,
            "matches": [self._format_match(match) for match in matches]
        }

    def _translate(self, text: str) -> str:
        try:
            return self.translator.translate(text)
        except Exception:
            return "(traducción fallida)"

    def _generate_feedback(self, matches) -> str:
        if not matches:
            return "¡Buen trabajo! No se encontraron errores."

        feedback_lines = []
        for i, match in enumerate(matches, 1):
            rule_name = match.ruleIssueType or "desconocido"
            message = match.message
            replacements = ", ".join(match.replacements[:3]) if match.replacements else "sin sugerencias"
            example = match.context.strip()

            feedback_lines.append(
                f"{i}. {message} (Ej: “{example}”, Sugerencias: {replacements})"
            )

        return f"Se encontraron {len(matches)} error(es):\n" + "\n".join(feedback_lines)

    def _format_match(self, match) -> dict:
        return {
            "message": match.message,
            "context": match.context,
            "replacements": match.replacements,
            "rule": match.ruleId,
            "offset": match.offset,
            "length": match.errorLength
        }


# Testing (safe to remove in production)
if __name__ == "__main__":
    gc = GrammarCorrector()
    res = gc.correct_text("henlo me are the good person to learn english")
    print("Original:", res["original"])
    print("Corrected:", res["corrected"])
    print("Translated:", res["translated"])
    print("Feedback:\n", res["feedback"])
