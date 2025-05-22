import torchaudio
from speechbrain.inference.classifiers import EncoderClassifier

file = input("Enter File Name: ")
# 1. Load pretrained ECAPA‐TDNN AccentID model
classifier = EncoderClassifier.from_hparams(
    source="Jzuluaga/accent-id-commonaccent_ecapa",
    savedir="pretrained_ecapa",
    run_opts={"device":"cuda"}  # or {"device":"cpu"} if no GPU
)

# 2. Inference on one file
signal, fs = torchaudio.load(file)     # [1, time], fs=16000
# classify_file handles loading internally, but you can also supply tensors:
out_prob, score, index, text_lab = classifier.classify_file(file)
# text_lab is a list of predicted labels, score is log-posterior for best class

# 3. Compute confidence (%)
#confidence = float(score.exp().item()) * 100  # convert log-posterior to softmax prob
#conf_score = score
confidence = score.item() * 100
print(f"Confidence: {confidence:.2f}%")
print(f"Accent: {text_lab[0]}, Confidence: {confidence:.1f}%")

#print(f"score: {score}")
