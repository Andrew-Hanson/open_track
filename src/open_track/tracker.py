import cv2
trackers = {
    'csrt': cv2.TrackerCSRT_create,
    'kcf': cv2.TrackerKCF_create,
    'goturn': cv2.TrackerGOTURN_create,
    'moose': cv2.legacy_TrackerMOSSE.create,
    'old_mil': cv2.legacy_TrackerMIL.create,
    'old_kcf': cv2.legacy_TrackerKCF.create,
    'tld': cv2.legacy_TrackerTLD.create,
    'boosting': cv2.legacy_TrackerBoosting.create,
    'old_csrt': cv2.legacy_TrackerCSRT.create,
    'old_medflow': cv2.legacy_TrackerMedianFlow.create,
    'mil': cv2.TrackerMIL_create}

tracker = trackers['csrt']()

cap = cv2.VideoCapture('20210304_005802000_iOS.MOV')


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
        x, y, w, h = [int(num) for num in box]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('window', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






































