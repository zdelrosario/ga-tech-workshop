pre01=01_python
pre02=02_pycc
pre03=03_cleaning
pre04=04_data
pre05=05_vis
pre06=06_ml
pre07=07_sl

main:
	make ex
	make strip
	make pack

ex: ${pre01} ${pre02} ${pre03} ${pre04} ${pre05} ${pre06} ${pre07}

${pre01}: ${pre01}_master.ipynb
	./sep.py ${pre01}_master.ipynb ${pre01}_exercise.ipynb ${pre01}_solution.ipynb

${pre02}: ${pre02}_master.ipynb
	./sep.py ${pre02}_master.ipynb ${pre02}_exercise.ipynb ${pre02}_solution.ipynb

${pre03}: ${pre03}_master.ipynb
	./sep.py ${pre03}_master.ipynb ${pre03}_exercise.ipynb ${pre03}_solution.ipynb

${pre04}: ${pre04}_master.ipynb
	./sep.py ${pre04}_master.ipynb ${pre04}_exercise.ipynb ${pre04}_solution.ipynb

${pre05}: ${pre05}_master.ipynb
	./sep.py ${pre05}_master.ipynb ${pre05}_exercise.ipynb ${pre05}_solution.ipynb

${pre06}: ${pre06}_master.ipynb
	./sep.py ${pre06}_master.ipynb ${pre06}_exercise.ipynb ${pre06}_solution.ipynb

${pre07}: ${pre07}_master.ipynb
	./sep.py ${pre07}_master.ipynb ${pre07}_exercise.ipynb ${pre07}_solution.ipynb

strip:
	nbstripout *.ipynb

pack:
	zip exercises.zip \
	${pre01}_exercise.ipynb \
	${pre02}_exercise.ipynb \
	${pre03}_exercise.ipynb \
	${pre04}_exercise.ipynb \
	${pre05}_exercise.ipynb \
	${pre06}_exercise.ipynb \
	${pre07}_exercise.ipynb \
	check_install.ipynb \
	workshop_utils.py \
	data/* \
	incl/* 

