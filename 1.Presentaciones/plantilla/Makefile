PROJECT=Presentacion
TEX=pdflatex
BIBTEX=bibtex
BUILDTEX=$(TEX) $(PROJECT).tex

all: clean comp open clean

comp:
	$(BUILDTEX)
	#	$(BIBTEX) $(PROJECT)
	$(BUILDTEX)
	$(BUILDTEX)

open: clean
	evince $(PROJECT).pdf &

clean:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.toc *.out *~	
