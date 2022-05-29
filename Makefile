build:
	conda env create -f environment.yml
	rm -rf ./{bin,conf} && mkdir ./{bin,conf}
	mkdir -p ./bin/lib/{collection, validation, preprocessing, training, deployment}
	touch ./bin/main.py
	touch ./bin/lib/{collection, validation, preprocessing, training, deployment}/__init__.py