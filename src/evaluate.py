from skimage.metrics import peak_signal_noise_ratio
from skimage.metrics import structural_similarity
import cv2


hr_path = "../dataset/HR/satellite_001.png"
sr_path = "../results/bicubic/satellite_001_SR.png"


hr = cv2.imread(hr_path)
sr = cv2.imread(sr_path)


if hr is None or sr is None:
    print("Error: Could not load images.")
    exit()


hr = cv2.cvtColor(hr, cv2.COLOR_BGR2RGB)
sr = cv2.cvtColor(sr, cv2.COLOR_BGR2RGB)


psnr = peak_signal_noise_ratio(
    hr,
    sr,
    data_range=255
)


ssim = structural_similarity(
    hr,
    sr,
    channel_axis=2,
    data_range=255
)


print("PSNR:", psnr, "dB")
print("SSIM:", ssim)
