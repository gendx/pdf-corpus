PROGRAM=./build-pdf.py

TXTS=$(shell find corpus/ -name "*.txt")
PDFS=$(TXTS:.txt=.pdf)

all: $(PDFS)

%.pdf: %.txt
	$(PROGRAM) $< $@

clean:
	rm -f $(PDFS)

