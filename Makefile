.DEFAULT_GOAL := achemso

all: achemso

achemso:
	pdflatex si
	bibtex si
	pdflatex si
	pdflatex si

clean:
	rm si.aux
	rm si.bbl
	rm si.log
	rm si.blg
	rm si.pdf
