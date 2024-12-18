# command-line:
# 	bash_scripts/command_line.sh

command-line:
	@bash -c "set -a; source local.env; set +a; source bash_scripts/command_line.sh && exec $$SHELL"

streamlit:
	@bash -c "set -a; source local.env; set +a; source bash_scripts/streamlit.sh && exec $$SHELL"