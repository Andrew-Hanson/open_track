import cv2
import math

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
video = 'drop1(30).mp4'


def get_filename(video):
    num = 1
    lead, end = video.split('.')
    while True:
        filename = f'track_{lead}_{num:04}.csv'
        try:
            with open(filename, 'r'):
                pass
        except FileNotFoundError:
            with open(filename, 'w'):
                break
        num += 1
    return filename


def calibrate_data(bench_box, length):
    x, y, w, h = bench_box
    # bench_box_x_len = w
    # bench_box_y_len = h
    print(f'bench_box x:{x}, y:{y}, w:{w}, h:{h}')
    # print(bench_box_x_len)
    # print(bench_box_y_len)
    px_len = max(w, h)
    global scaler
    scaler = length / px_len

    pass


def get_pos(x, y, w, h, height):
    x = (x+x+w)//2
    y = (y+y+h)//2
    if 'drop' in video and '(30)' in video:
        y = 680 - y
    else:
        y = height - y
    return x, y


def get_scale_pos(x, y, w, h, height):
    x = (x+x+w)//2
    x = x*scaler
    y = (y+y+h)//2
    y = y*scaler
    if 'drop' in video and '(30)' in video:
        y = 680*scaler - y
    else:
        y = height * scaler - y
    return x, y


def get_dpos(previous, current):
    if previous is None:
        return 0
    p1 = previous
    p2 = current
    distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return distance


def get_delta_x(previous, current):
    if previous is None:
        return 0
    x1, y1 = previous
    x2, y2 = current
    return x2-x1

def get_delta_y(previous, current):
    if previous is None:
        return 0
    x1, y1 = previous
    x2, y2 = current
    return y2-y1


def track(length):
    def store(x, y, w, h, height, pre, scale_pre, i, fps, filename):
        nonlocal previous
        nonlocal scale_previous
        time = 1 / fps

        with open(filename, 'a') as f:
            pos = get_pos(x, y, w, h, height)
            dpos = get_dpos(pre, pos)
            vx = get_delta_x(pre, pos)
            vy = get_delta_y(pre, pos)
            scale_pos = get_scale_pos(x, y, w, h, height)
            scale_dpos = get_dpos(scale_pre, scale_pos) / time
            scale_vx = (get_delta_x(scale_pre, scale_pos) / time)
            scale_vy = -(get_delta_y(scale_pre, scale_pos) / time)
            previous = pos
            scale_previous = scale_pos
            # scale_pos[1] = height*scaler - scale_pos[1]

            if i == 0:
                f.write(
                    'frame,time,pixel_x,pixel_y,delta_pixel_position,delta_pixel_x,delta_pixel_y,scaled_x,scaled_y,scaled_speed,scaled_x_velocity,scaled_y_velocity')
            f.write(
                '\n' + f'{i + 1},{(i + 1) / fps},{pos[0]},{pos[1]},{dpos},{vx},{vy},{scale_pos[0]},{scale_pos[1]},{scale_dpos},{scale_vx},{scale_vy}')

    previous = None
    scale_previous = None
    cap = cv2.VideoCapture(video)

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f'width:{width}, height:{height}')

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(f'fps:{fps}, frame_count: {frame_count}')

    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
    cv2.imshow('window', frame)
    if __name__ != "__main__":
        benchmark = cv2.selectROI('window', frame)
        print(benchmark)
        # tracker.init(frame, benchmark)
        # success, box = tracker.update(frame)
        x, y, w, h = [int(num) for num in benchmark]
        bench_box = (x, y, w, h)
        calibrate_data(bench_box, length)
    if __name__ == "__main__":
        # benchmark = cv2.selectROI('window', frame)
        benchmark = (675, 120, 25, 425)
        print(benchmark)
        # tracker.init(frame, benchmark)
        # success, box = tracker.update(frame)
        x, y, w, h = [int(num) for num in benchmark]
        bench_box = (x, y, w, h)
        calibrate_data(bench_box, length)
        cv2.rectangle(frame, (bench_box[0], bench_box[1]), (bench_box[0] + bench_box[2], bench_box[1] + bench_box[3]), (0, 255, 0), 2)

    cv2.imshow('window', frame)
    if __name__ == "__main__":
        # bb = cv2.selectROI('window', frame)
        bb = (524, 60, 66, 57)
        tracker.init(frame, bb)
    if __name__ != "__main__":
        bb = cv2.selectROI('window', frame)
        tracker.init(frame, bb)

    filename = get_filename(video)

    i = 0
    while True:
        if i != 0:
            ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        success, box = tracker.update(frame)
        if success:
            x, y, w, h = [int(num) for num in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            center = ((x + x + w) // 2, (y + y + h) // 2)
            radius = 3
            color = (225, 0, 0)
            cv2.circle(frame, center, radius, color, thickness=0, lineType=8, shift=0)
            cv2.rectangle(frame, (bench_box[0], bench_box[1]),
                          (bench_box[0] + bench_box[2], bench_box[1] + bench_box[3]), (0, 255, 0), 2)
            cv2.imshow('window', frame)
            if i == 0:
                print(f'keyframe_box x:{x}, y:{y}, w:{w}, h:{h}')
                cv2.waitKey(0)
            store(x, y, w, h, height, previous, scale_previous, i, fps, filename)
            i += 1

        cv2.imshow('window', frame)
        if cv2.waitKey(1) == ord('q'):
            break
        if cv2.waitKey(1) == ord('p'):
            cv2.waitKey(0)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    track(1)
