from dish import Dish
from dish.dish import DEFAULT_CONFIG


def test_config():
	d = Dish()
	assert d.config == DEFAULT_CONFIG
	d.config_from_dict({
		'PS1': 'uwu$ '
	})
	assert d.config == {**DEFAULT_CONFIG, 'PS1': 'uwu$ '}
	d.reset_config()
	assert d.config == DEFAULT_CONFIG


def test_prompt_generation():
	d = Dish()

	def uwu_start_tag(attrs):
		result = ''
		for key, val in attrs.items():
			result += f'{key}:{val};'
		return result
	def uwu_end_tag():
		return '[end]'
	d.start_tag_handlers['uwu'] = uwu_start_tag
	d.end_tag_handlers['uwu'] = uwu_end_tag

	d.config['PS1'] = '<uwu one="two" three="four">owo</uwu>'
	prompt = d.generate_prompt('PS1')
	assert prompt == 'one:two;three:four;owo[end]'
