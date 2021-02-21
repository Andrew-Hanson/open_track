import cv2
trackers = {
    'csrt': cv2.TrackerCSRT_create,
    'kcf': cv2.TrackerKCF_create,
    'goturn': cv2.TrackerGOTURN_create,
    'mil': cv2.TrackerMIL_create}
tracker = trackers['csrt']()

cap = cv2.VideoCapture('20210119 185624000 Ios-1.m4v')

ret, frame = cap.read()
frame = cv2.resize(frame, (800, 800))
cv2.imshow('window', frame)
bb = cv2.selectROI('window', frame)
tracker.init(frame, bb)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (800, 800))
    success, box = tracker.update(frame)
    if success:
        x, y, w, h =[int(num) for num in box]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('window', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""105 minutes"""




































