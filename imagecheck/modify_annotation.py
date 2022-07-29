import os


class ModifyAnnotation:
    def __init__(self):
        pass

    @staticmethod
    def modify_annotation(class_name, class_label):
        label_path = f'D:/project/TMC/validation_label/txt/{class_name}/'
        filenames = os.listdir(label_path)
        for filename in filenames:
            print(label_path + filename)
            with open(label_path + filename, 'r+') as f:  # file을 열고 알아서 닫아 줌
                lines = []
                for line in f:
                    if line.startswith('1'):
                        new_line = str(class_label) + line[1:]
                        lines = lines + [new_line]
                    else:
                        lines = lines + [line]
                f.seek(0)  # file pointer 위치를 처음으로 돌림
                f.writelines(lines)  # 수정한 lines를 파일에 다시 씀
                f.truncate()  # 현재 file pointer 위치까지만 남기고 나머지는 정리


if __name__ == '__main__':
    labels = ['plate',
              'BeanRice', 'CabbageKimchi', 'FlatfishSuisi', 'FriedChicken', 'FriedTofuSuisi',
              'HoneyRiceCake', 'Mandu', 'PaKimchi', 'PigHocks', 'PorkCutlet',
              'RoastedFish', 'RolledOmelet', 'SalmonSuisi', 'Sausage', 'SeasonedChicken',
              'ShrimpSuisi', 'SoiedCrab', 'StonePotRice', 'WhiteRice', 'YoungRadishKimchi']
    [ModifyAnnotation.modify_annotation(labels[i], i) for i in range(1, 21)]





