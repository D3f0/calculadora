# Compilar las interfases en modulos python

UI_FILES = interfase.ui
PY_FILES = $(UI_FILES:.ui=.py)
UIC = pyuic4

all: ${PY_FILES}

%.py: %.ui
	${UIC} $< > $@