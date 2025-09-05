1. What is Intrusion Detection?

An IDS monitors network traffic or system activity and classifies it as normal or malicious.

Normal traffic → Legitimate browsing, email, file transfers.

Malicious traffic → Port scanning, DDoS attacks, malware communication.

🔹 2. ML Approach for Intrusion Detection

We treat this as a classification problem:

Input: Features from network traffic (e.g., number of packets, connection duration, protocol, source/destination ports, etc.).

Output: Class label (Normal, DoS Attack, Probe, R2L Attack, etc.).

Epoch 1/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 12s 6ms/step - accuracy: 0.9740 - loss: 0.0799 - val_accuracy: 0.9921 - val_loss: 0.0220
Epoch 2/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 19s 5ms/step - accuracy: 0.9915 - loss: 0.0244 - val_accuracy: 0.9936 - val_loss: 0.0177
Epoch 3/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 11s 5ms/step - accuracy: 0.9927 - loss: 0.0196 - val_accuracy: 0.9947 - val_loss: 0.0170
Epoch 4/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 5ms/step - accuracy: 0.9932 - loss: 0.0192 - val_accuracy: 0.9951 - val_loss: 0.0161
Epoch 5/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 5ms/step - accuracy: 0.9939 - loss: 0.0175 - val_accuracy: 0.9942 - val_loss: 0.0137
Epoch 6/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 20s 5ms/step - accuracy: 0.9943 - loss: 0.0155 - val_accuracy: 0.9961 - val_loss: 0.0154
Epoch 7/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 5ms/step - accuracy: 0.9949 - loss: 0.0150 - val_accuracy: 0.9957 - val_loss: 0.0143
Epoch 8/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 12s 6ms/step - accuracy: 0.9952 - loss: 0.0138 - val_accuracy: 0.9963 - val_loss: 0.0148
Epoch 9/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 5ms/step - accuracy: 0.9950 - loss: 0.0139 - val_accuracy: 0.9962 - val_loss: 0.0150
Epoch 10/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 6ms/step - accuracy: 0.9952 - loss: 0.0134 - val_accuracy: 0.9959 - val_loss: 0.0141
Epoch 11/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 5ms/step - accuracy: 0.9954 - loss: 0.0124 - val_accuracy: 0.9954 - val_loss: 0.0144
Epoch 12/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 5ms/step - accuracy: 0.9955 - loss: 0.0122 - val_accuracy: 0.9964 - val_loss: 0.0129
Epoch 13/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 5ms/step - accuracy: 0.9957 - loss: 0.0118 - val_accuracy: 0.9962 - val_loss: 0.0136
Epoch 14/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 11s 6ms/step - accuracy: 0.9960 - loss: 0.0121 - val_accuracy: 0.9964 - val_loss: 0.0179
Epoch 15/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 5ms/step - accuracy: 0.9960 - loss: 0.0145 - val_accuracy: 0.9965 - val_loss: 0.0144
Epoch 16/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 20s 5ms/step - accuracy: 0.9961 - loss: 0.0116 - val_accuracy: 0.9964 - val_loss: 0.0144
Epoch 17/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 11s 5ms/step - accuracy: 0.9964 - loss: 0.0109 - val_accuracy: 0.9961 - val_loss: 0.0146
Epoch 18/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 11s 6ms/step - accuracy: 0.9960 - loss: 0.0102 - val_accuracy: 0.9967 - val_loss: 0.0166
Epoch 19/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 11s 6ms/step - accuracy: 0.9959 - loss: 0.0113 - val_accuracy: 0.9967 - val_loss: 0.0171
Epoch 20/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 20s 6ms/step - accuracy: 0.9964 - loss: 0.0099 - val_accuracy: 0.9969 - val_loss: 0.0173
Epoch 21/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 20s 5ms/step - accuracy: 0.9963 - loss: 0.0102 - val_accuracy: 0.9970 - val_loss: 0.0151
Epoch 22/100
1890/1890 ━━━━━━━━━━━━━━━━━━━━ 10s 5ms/step - accuracy: 0.9962 - loss: 0.0100 - val_accuracy: 0.9967 - val_loss: 0.0168
Validation Accuracy: 0.9964
['label_encoder.joblib']
example test 
['normal' 'normal' 'anomaly' 'anomaly' 'anomaly' 'anomaly' 'anomaly'
 'normal' 'normal' 'normal' 'anomaly' 'anomaly' 'anomaly' 'normal'
 'normal' 'anomaly' 'anomaly' 'anomaly' 'normal' 'anomaly']
