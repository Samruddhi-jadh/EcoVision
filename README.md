# 🌊 EcoVision: ML-Powered Plastic Waste Detection

EcoVision is an intelligent machine learning system that uses YOLOv8 to detect and localize plastic waste in ocean and coastal images. By combining engineering, artificial intelligence, and sustainability, this project aims to support India’s environmental efforts and align with global Sustainable Development Goals.

---

## 🎯 Objective

To develop a scalable and efficient AI solution capable of detecting plastic pollution in aquatic environments using real-time image analysis, thus enabling better environmental monitoring and cleanup strategies.

---

## 💡 Key Features

- 🔍 Real-time plastic detection in images
- 🤖 YOLOv8-powered deep learning model
- 📷 Works on ocean, beach, and underwater images
- 📊 High accuracy with robust metrics
- 🌍 Aligned with UN Sustainable Development Goals

---

## 🧰 Tech Stack

- Python  
- YOLOv8 (Ultralytics)  
- PyTorch  
- OpenCV  
- Google Colab  
- Matplotlib & Seaborn  

---

## 📁 Project Structure

```bash
EcoVision/
│
├── dataset/                 # Kaggle Marine Debris dataset
├── runs/                    # YOLOv8 training and detection outputs
├── yolov8_config.yaml       # Custom training configuration
├── train.py                 # Training script for YOLOv8
├── detect.py                # Inference and detection
├── utils/                   # Helper scripts and data processing
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
````

---

## 📊 Training Details (YOLOv8)

* **Model**: YOLOv8n (Nano variant)
* **Epochs**: 100
* **Batch Size**: 16
* **Image Size**: 640x640
* **Optimizer**: SGD
* **mAP\@50**: 0.7937
* **Precision**: 0.7941
* **Recall**: 0.7458

---

## 🌐 Sustainable Development Goals (SDGs)

1. **SDG 14 – Life Below Water**: Protect marine biodiversity by identifying plastic pollution.
2. **SDG 13 – Climate Action**: Promote climate awareness through AI-powered monitoring.
3. **SDG 9 – Industry, Innovation, and Infrastructure**: Leverage innovation and engineering to solve real-world challenges.

---

## 🔍 Existing Solutions & Drawbacks

| Existing Solution                 | Drawbacks                                          |
| --------------------------------- | -------------------------------------------------- |
| **Ocean Cleanup Interceptor**     | High operational cost, limited to large rivers     |
| **Seabin Project**                | Limited to still water, needs frequent maintenance |
| **Plastic Bank App**              | Manual reporting, not scalable in real-time        |
| **Drone + Camera Detection**      | Costly, requires trained operators                 |
| **Traditional Satellite Imagery** | Low resolution and slow processing                 |

---

## 🏆 Why EcoVision is Better

* Fully automated using YOLOv8 deep learning
* Works on both still images and potential video streams
* Highly cost-efficient using open-source tools
* Portable and scalable for field deployments
* Can assist NGOs, government agencies, and researchers

---

## ⚠️ Limitations

1. Limited performance in low-visibility underwater images
2. May misclassify lookalike objects (e.g., seaweed or plastic)
3. Requires labeled dataset and training time
4. Demands GPU/TPU for real-time video inference

---

## 🤝 Contribution

We welcome contributions, ideas, and improvements!
Feel free to fork the repository, raise issues, or make pull requests.

---

## 🧑‍💻 Author

**Name:** Samruddhi Jadhav

---
## 🤝 Contribution

We welcome contributions, ideas, and improvements!
Feel free to fork the repository, raise issues, or make pull requests.
**🚀 This project is open to contribute and enhance the model further.**

---

> 🇮🇳 Made in India with a mission to protect oceans through engineering excellence and AI innovation.
> 🧠 “Engineering minds can build greener oceans. Let EcoVision lead the way.”
