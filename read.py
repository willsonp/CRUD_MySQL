import cv2

def capt_video():
    vid = cv2.videoCapture(0)
    cv2.imshow('Video', vid)
    while True:
        ret, frame = vid.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capt_video()