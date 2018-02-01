import cv2
from additional import *
import random


class Cam(object):

    def __init__(self, cam_id = 0, vi_file_name="videos/rec_", sc_file_name='screens/scr_', dely_time=100, frames= 10.0):
        self.ID = cam_id
        self.vi_file_name = vi_file_name
        self.sc_file_name = sc_file_name
        self.rec = ''
        self.delay = dely_time
        self.fps = frames

        #inits
        self.fourcc = cv2.VideoWriter_fourcc(*'MJPG')

    def create_folder(self):
        chose_path(self.rec)

    def update_vid_filename(self):
        folder_name, file_name = split_path(self.vi_file_name)
        folder = folder_name + " " + date_time_file()
        self.rec = folder + "/" + file_name + date_time() + ".avi"
        self.create_folder()
        time.sleep(.2)
        print (self.rec)

    def update_scr_filename(self):
        folder_name, file_name = split_path(self.sc_file_name)
        folder = folder_name + " " + date_time_file()
        self.rec = folder + "/" +file_name + date_time() + ".jpg"
        self.create_folder()
        print (self.rec)

    def record_video(self):
        self.capture = cv2.VideoCapture(self.ID)
        self.update_vid_filename()
        self.out = cv2.VideoWriter(self.rec, self.fourcc, self.fps, (640, 480))
        i = 0
        while i < self.delay:
            ret, self.frame = self.capture.read()
            self.out.write(self.frame)
            cv2.imshow('frame', self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            i+=1
            print i
        self.capture.release()
        self.out.release()

    def capture_series_of_spanshots(self,count):
        self.capture = cv2.VideoCapture(self.ID)
        i = 0
        while i < count:
            time.sleep(1)
            self.update_scr_filename()
            ret, self.frame = self.capture.read()

            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(self.rec, self.frame)
            i += 1
            print i
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.capture.release()

    def capture_single_snapshot(self):
        self.capture_series_of_spanshots(1)


if __name__ == "__main__":


    # #region EFFICENT
    cap = Cam(0,'videos/Rec_','screens/Scr_',20,10.0)
    # for _ in range(6):
    #     time.sleep(10)
    #     cap.record_video()
    #
    # for _ in range(3):
    #     cap.capture_series_of_spanshots(5)
    #     time.sleep(3)
    #
    # for _ in range(random.randint(10,20)):
    #     time.sleep(random.randint(3,10))
    #     cap.capture_single_snapshot()
    # #endregion
    #
    #
    # cam_2=Cam(vi_file_name="vids/videos",sc_file_name="screeeny/screenY")
    #
    # cam_2.capture_single_snapshot()


    while True:
        cap.capture_single_snapshot()
        time.sleep(10)

