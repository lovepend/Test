import cv2
import time
import threading


class Camera:
    def __init__(self, mirror=False):
        self.data = None
        self.cam = cv2.VideoCapture(0)

        self.WIDTH = 640
        self.HEIGHT = 480

        self.center_x = self.WIDTH / 2
        self.center_y = self.HEIGHT / 2
        self.touched_zoom = False

        self.scale = 1
        self.__setup()

        self.recording = False

        self.mirror = mirror

    def __setup(self):
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.WIDTH)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.HEIGHT)
        time.sleep(2)

    def stream(self):
        # streaming thread 함수
        def streaming():
            # 실제 thread 되는 함수
            self.ret = True
            while self.ret:
                self.ret, np_image = self.cam.read()
                if np_image is None:
                    continue
                if self.mirror:
                    # 거울 모드 시 좌우 반전
                    np_image = cv2.flip(np_image, 1)
                self.data = np_image
                k = cv2.waitKey(1)
                if k == ord('q'):
                    self.release()
                    break
        #Thread(target=streaming).start()

    def show(self):
        while True:
            frame = self.data
            if frame is not None:
                cv2.imshow('Davinci AI', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                # q : close
                self.release()
                cv2.destroyAllWindows()
                break

    def release(self):
        self.cam.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    cam = Camera(mirror=True)
    cam.stream()
    cam.show()
