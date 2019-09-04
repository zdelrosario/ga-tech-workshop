pre01=01
pre02=02
pre03=03
pre04=04
pre05=05

main: ${pre01} ${pre02} ${pre03} ${pre04} ${pre05}

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

clean:
	rm ${pre01}_exercise.ipynb ${pre01}_solution.ipynb
	rm ${pre02}_exercise.ipynb ${pre02}_solution.ipynb
	rm ${pre03}_exercise.ipynb ${pre03}_solution.ipynb
	rm ${pre04}_exercise.ipynb ${pre04}_solution.ipynb
	rm ${pre05}_exercise.ipynb ${pre05}_solution.ipynb
