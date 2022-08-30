import torch
import cv2


class Yolo:
    def __init__(self, path):
        self.results = None
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='./weight/best.pt')
        self.path = path
        self.names = None

    def detect(self):
        results = self.model(self.path)
        df = results.pandas().xyxy[0]
        self.results = df.loc[df['name'] != 'plate']
        print(self.results['name'].tolist())
        print(type(self.results))
        self.draw_rectangle()
        return self.results.to_json(orient='records')

    def get_xy(self):
        return [[round(self.results.iat[x, y]) for y in range(0, 4)] for x in range(len(self.results))]

    def draw_rectangle(self):
        image = cv2.imread(self.path)
        [cv2.rectangle(image, (x, y), (w, h), (0, 0, 255), 2) for (x, y, w, h) in self.get_xy()]
        cv2.imwrite('./save/' + format(self.get_file_name()), image)

    def get_file_name(self):
        return self.path.split('/')[-1]



if __name__ == '__main__':
    img = './data/test.jpg'
    tmc = Yolo(img)
    result_list = tmc.detect()
