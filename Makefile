.POSIX:


all:
	@printf 'targets:\n'
	@printf '  clean\tremove cache files\n'
	@printf '  flask\trun flask app\n'
	@printf '  lint\tcheck formatting\n'
	@printf '  git-push\tpublish to git remotes\n'
	@printf '  dist\tbuild python package\n'
	@printf '  publish\tpublish to pypi\n'


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


git-push: .git-push-tags
	git remote | xargs -n1 sh -c 'git push $$0 $$(git rev-parse --abbrev-ref HEAD)'
.git-push-tags:
	git remote | xargs -n1 sh -c 'git push $$0 --tags'


clean:
	rm -rf pop/__pycache__ pop/*/__pycache__ dist/ ./*.egg-info
