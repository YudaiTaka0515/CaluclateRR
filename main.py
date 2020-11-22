import cv2


def CheckThermalCamera():
    print("cv2 version : ", cv2.__version__)
    device_index = 0
    cap = cv2.VideoCapture(device_index + cv2.CAP_DSHOW)
    cap.get(cv2.CAP_PROP_FOURCC)
    # 保存方法に効いてくる
    # cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y', '1', '6', ' '))
    cap.get(cv2.CAP_PROP_FOURCC)

    print(cap.isOpened())
    # cap.set(cv2.CAP_PROP_CONVERT_RGB, False)
    code, frame = cap.read()
    print(code)
    print(frame.shape)
    cv2.imshow("a", frame)
    cv2.waitKey(1000)
    print(frame.dtype)


CheckThermalCamera()

