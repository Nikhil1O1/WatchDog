import time

import cv2
import numpy as np

from spot_diff import spot_diff


def find_motion():

	motion_detected = False
	is_start_done = False

	cap = cv2.VideoCapture(0)

	check = []
	
	print("Capturing Frame...")
	time.sleep(1)
	frame1 = cap.read()
	print("Frame Captured")
	_, frm1 = cap.read()
	frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

	
	while True:
		_, frm2 = cap.read()
		frm2 = cv2.cvtColor(frm2, cv2.COLOR_BGR2GRAY)

		diff = cv2.absdiff(frm1, frm2)

		_, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

		contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

		#look at it
		contors = [c for c in contors if cv2.contourArea(c) > 25]


		if len(contors) > 5:
			cv2.putText(thresh, "motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			motion_detected = True
			is_start_done = False

		elif motion_detected and len(contors) < 3:
			if (is_start_done) == False:
				start = time.time()
				is_start_done = True
				end = time.time()

			end = time.time()

			print(end-start)
			if (end - start) > 4:
				frame2 = cap.read()
				cap.release()
				cv2.destroyAllWindows()
				x = spot_diff(frame1, frame2)
				if x == 0:
					print("running again")
					return

				else:
					print("found motion")
					return

		else:
			cv2.putText(thresh, "no motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

		cv2.imshow("Analysing...", frm1)

		_, frm1 = cap.read()
		frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

		if cv2.waitKey(1) == 27:
			
			break

	return

def rem_find_motion(stop_event = 1):
	
	motion_detected = False
	is_start_done = False

	cap = cv2.VideoCapture(0)

	check = []
	
	print("Capturing Frame...")
	time.sleep(1)
	frame1 = cap.read()
	print("Frame Captured")
	_, frm1 = cap.read()
	frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

	start = time.time()
	while True:
		_, frm2 = cap.read()
		frm2 = cv2.cvtColor(frm2, cv2.COLOR_BGR2GRAY)

		diff = cv2.absdiff(frm1, frm2)

		_, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

		contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

		#look at it
		contors = [c for c in contors if cv2.contourArea(c) > 25]


		if len(contors) > 5:
			cv2.putText(thresh, "motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
			motion_detected = True
			is_start_done = False

		elif motion_detected and len(contors) < 3:
			if (is_start_done) == False:
				start = time.time()
				is_start_done = True
				end = time.time()

			end = time.time()

			print(end-start)
			if (end - start) > 4:
				frame2 = cap.read()
				cap.release()
				cv2.destroyAllWindows()
				x = spot_diff(frame1, frame2)
				if x == 0:
					print("running again")
					return

				else:
					print("found motion")
					return

		else:
			cv2.putText(thresh, "no motion detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

		cv2.imshow("Analysing...", frm1)

		_, frm1 = cap.read()
		frm1 = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

		if cv2.waitKey(1) == 27 or time.time() - start >= stop_event*10:
			break

	return

