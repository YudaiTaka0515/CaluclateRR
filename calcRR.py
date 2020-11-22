import cv2
import numpy as np
from scipy.fftpack import fft
from scipy import signal
import matplotlib.pyplot as plt


def CalculateRR(time, _signal):
    # print("calculating RR...")
    N = len(time)
    # hamming = np.hamming(N)
    _signal = _signal - np.mean(_signal)
    _signal = signal.detrend(_signal)
    # signal = signal * hamming
    dt = time[-1] - time[-2]
    frequency = np.linspace(0, 1.0 / dt, N)
    # signal_f = fft(signal) / (N / 2)
    signal_f = fft(_signal) / (N / 2)
    signal_f = np.abs(signal_f)
    # rr_candidate = []
    for i in range(5):
        index = np.where(signal_f == np.sort(signal_f)[-i])
        rr_candidates = frequency[index]
        # print(rr_candidates)
        for rr_candidate in rr_candidates:
            if (rr_candidate > 0.1) and (rr_candidate < 2):
                return rr_candidate*60

    print("Error")
    return 0


def CalculateMinTemperature(image, b_box, is_bottom_half=False):
    top, left, bottom, right = b_box
    if is_bottom_half:
        top = top + (bottom - top) // 2
        interest_region = image[top:bottom, left:right, :]
    else:
        interest_region = image[top:bottom, left:right, :]
    min_temperature = np.min(interest_region)
    return min_temperature


def CalculateMeanTemperature(image, b_box, is_bottom_half=False):
    top, left, bottom, right = b_box
    is_nose = is_bottom_half
    # is_bottom_half = False
    if is_bottom_half:
        top = top + (bottom - top) // 2
        interest_region = image[top:bottom, left:right, :]
    else:
        interest_region = image[top:bottom, left:right, :]
    mean_temperature = np.mean(interest_region)
    if is_nose:
        pass
        # CalculateHogeHoge(interest_region)
    return mean_temperature


def CalculateHogeHoge(interest_region):
    hist_image = cv2.equalizeHist(interest_region[:, :, 0])
    hist_image[hist_image > 200] = 255
    hist_image[hist_image < 200] = 0
    cv2.namedWindow("a")
    cv2.imshow("a", hist_image)



def ShowFFT(time, signal):
    N = len(time)
    hamming = np.hamming(N)
    # ham_signal = signal * hamming
    ham_signal = signal
    dt = time[-1] - time[-2]
    frequency = np.linspace(0, 1.0/dt, N)
    signal_f = fft(signal) / (N / 2)
    ham_signal_f = fft(ham_signal) / (N / 2)

    print("raw_signal")
    for i in range(5):
        index = np.where(signal_f == np.sort(signal_f)[-i])
        print(frequency[index])

    print("ham_signal")
    for i in range(5):
        index = np.where(ham_signal_f == np.sort(ham_signal_f)[-i])
        print(frequency[index])

    fig = plt.figure()

    # add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
    ax1 = fig.add_subplot(2, 2, 1, xlabel="time", ylabel="amplitude")
    ax2 = fig.add_subplot(2, 2, 2, xlabel="frequency", ylabel="amplitude")
    ax3 = fig.add_subplot(2, 2, 3, xlabel="time", ylabel="amplitude")
    ax4 = fig.add_subplot(2, 2, 4, xlabel="frequency", ylabel="amplitude")

    # 生信号
    ax1.plot(time, signal)
    ax2.plot(frequency, np.abs(signal_f))

    # 窓処理をかけた信号
    ax3.plot(time, ham_signal)
    ax4.plot(frequency, np.abs(ham_signal_f))

    fig.tight_layout()
    fig.savefig("01")
    fig.show()


