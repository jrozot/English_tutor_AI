# app/grammar_corrector.py

import language_tool_python

class GrammarCorrector:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')

    def correct_text(self, text: str) -> dict:
        """
        Analyzes and corrects grammar in the input text.

        :param text: Original sentence from the user
        :return: Dict with original, corrected version, and feedback
        """
        matches = self.tool.check(text)
        corrected_text = language_tool_python.utils.correct(text, matches)

        return {
            "original": text,
            "corrected": corrected_text,
            "feedback": self._generate_feedback(text, corrected_text, matches)
        }

    def _generate_feedback(self, original: str, corrected: str, matches) -> str:
        if original.strip() == corrected.strip():
            return "¡Buen trabajo! No se encontraron errores."
        else:
            num = len(matches)
            return f"Se encontraron {num} posibles error(es). El texto ha sido corregido."



gc = GrammarCorrector()
res = gc.correct_text("She go to school every days.")
print(res)

# Output:
# {
#   'original': 'She go to school every days.',
#   'corrected': 'She goes to school every day.',
#   'feedback': 'Se encontraron 2 posibles error(es). El texto ha sido corregido.'
# }
