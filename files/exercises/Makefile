pre02=02
pre03=03

main: ${pre02} ${pre03}

${pre02}: ${pre02}_master.ipynb
	./sep.py ${pre02}_master.ipynb ${pre02}_exercise.ipynb ${pre02}_solution.ipynb

${pre03}: ${pre03}_master.ipynb
	./sep.py ${pre03}_master.ipynb ${pre03}_exercise.ipynb ${pre03}_solution.ipynb

clean:
	rm ${pre03}_exercise.ipynb ${pre03}_solution.ipynb
