ACTIVATE?=. .venv/bin/activate;

virtualenv:
	@echo "-> Creating virtual environment";
	@python3 -m venv .venv;

install: virtualenv
	@echo "-> Installing dependencies";
	@${ACTIVATE} pip3 install -r etc/requirements.txt;