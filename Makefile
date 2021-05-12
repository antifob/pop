.POSIX:


all:
	@printf 'targets:\n'
	@printf '  clean\tremove cache files\n'
	@printf '  flask\trun flask app\n
	@printf '  lint\tcheck formatting\n'


flask:
	FLASK_DEBUG=1 FLASK_APP=pop flask run


lint:
	pycodestyle pop


clean:
	rm -rf pop/__pycache__ pop/*/__pycache__
