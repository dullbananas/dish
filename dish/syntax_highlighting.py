from prompt_toolkit.lexers import Lexer


class DishHighlight(Lexer):
	def __init__(self, interpreter):
		super().__init__()
		self.interpreter = interpreter


	def lex_document(self, document):
		def f(lineno):
			line = document.lines[lineno]

			#if self.interpreter.in_comment:
			if self.interpreter.in_comment or line.startswith('#=='):
				return [('class:pygments.comment.multiline', line)]
			else:
				return [('class:pygments.text', line)]
		return f
