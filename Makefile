.POSIX:


all:
	@printf 'targets:\n'
	@printf '  clean\tremove cache files\n'
	@printf '  flask\trun flask app\n'
	@printf '  lint\tcheck formatting\n'
	@printf '  dist\tbuild python package\n'


flask:
	FLASK_DEBUG=1 FLASK_APP=pop flask run


lint:
	pycodestyle pop


dist: .dist
.dist:
	rm -rf dist/
	python -mbuild


publish:
	twine upload --repository pypi dist/*


clean:
	rm -rf pop/__pycache__ pop/*/__pycache__ dist/ ./*.egg-info
