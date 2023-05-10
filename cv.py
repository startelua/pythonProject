#VIDEO_URL = WEBURL + "live/amba.m3u8"
VIDEO_URL="http://d.startel.od.ua:3080/b03314015769bb4a1c35bed6ddd4626f/hls/7J7LPmqlBA/djI81biNVY80/s.m3u8"

import cv2
#cv2.namedWindow("GoPro",cv2.CV_WINDOW_AUTOSIZE)

cam = cv2.VideoCapture(VIDEO_URL)

total_frames = cam.get(1)

cam.set(1, 10)
ret, frame = cam.read()
cv2.imwrite('/Users/vlad/PycharmProjects/pythonProject', frame)




pipe = sp.Popen([ FFMPEG_BIN, "-i", VIDEO_URL,
           "-loglevel", "quiet", # no text output
           "-an",   # disable audio
           "-f", "image2pipe",
           "-pix_fmt", "bgr24",
           "-vcodec", "rawvideo", "-"],
           stdin = sp.PIPE, stdout = sp.PIPE)
while True:
    raw_image = pipe.stdout.read(432*240*3) # read 432*240*3 bytes (= 1 frame)
    image =  numpy.fromstring(raw_image, dtype='uint8').reshape((240,432,3))
    cv2.imshow("GoPro",image)
    if cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()

