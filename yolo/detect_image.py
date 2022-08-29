import torch


class Yolo:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='./weight/best.pt')

    def detect(self, path):
        results = self.model(path)
        df = results.pandas().xyxy[0]
        df = df.loc[df['name'] != 'plate']
        print(df['name'].tolist())
        return df.to_json(orient='records')


if __name__ == '__main__':
    img = './data/test.jpg'
    result_list = Yolo().detect(img)
    print(result_list)
