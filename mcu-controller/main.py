# Yea, there is probably some good framework waiting for me,
# but I just want to have fun. Sometimes reinventing the wheel will serve you.
# But...don't do that in professional work :)

import time
from Controller import Controller

root = Controller()

try:
	lastLoopExecution = time.time()

	while True:
		loopStartExecution = time.time()
		deltaTime = loopStartExecution - lastLoopExecution

		if deltaTime < 0.001:
			continue

		for object in root.createdObjects:
			object.update(deltaTime)

		lastLoopExecution = loopStartExecution
except:
	print("An error occured")
