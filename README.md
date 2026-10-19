# WhisperPrice — Audio & Podcast Transcription Arbitrage Calculator

👉 **Live Interactive Calculator:** **[https://sectoroneventures.github.io/whisper-price/](https://sectoroneventures.github.io/whisper-price/)**

Managed transcription APIs charge $0.36 to $1.50 per hour of audio ($360-$1,500 for 1,000 hours), while Faster-Whisper Large-v3 on a $0.19/hr Vast.ai RTX 3090 transcribes ~120 hours of audio in 60 minutes (effective cost $0.0016/hr — a 99.5% cost arbitrage).

---

## Quick Comparison Table

| Stack / Provider | Notes | Direct Link |
| :--- | :--- | :--- |
| **Faster-Whisper Large-v3 on Vast.ai (RTX 3090)** | 120x real-time speed on 24GB GPU ($0.19/hr) | **[Launch / Compare →](https://cloud.vast.ai/?ref_id=749467&template_id=fe790f7a807c2d4e7b3bb717f7ed4c78)** |
| **Apify Audio & Video Transcript Actors** | Pulls transcripts + metadata straight from URLs ($5/mo free credit) | **[Launch / Compare →](https://apify.com?fpr=infrabench7552)** |
| **Standard Managed Speech-to-Text API ($0.006/min)** | Per-minute API billing ($360 per 1,000 hours) | **[Launch / Compare →](https://cloud.vast.ai/?ref_id=749467&template_id=fe790f7a807c2d4e7b3bb717f7ed4c78)** |
| **Enterprise Transcription SaaS ($0.024/min)** | High per-minute markup ($1,440 per 1,000 hours) | **[Launch / Compare →](https://cloud.vast.ai/?ref_id=749467)** |

---

## Run From Your Terminal (`cli.py`)

```bash
python3 cli.py --volume 500
```

## Related Developer Cost Calculators
* **[GPU Memory & Hourly Price Calculator](https://sectoroneventures.github.io/infrabench/)**
* **[Headless Browser & Scraping API Benchmark](https://sectoroneventures.github.io/infrabench/headless-scraper-benchmark.html)**
* **[Docker VPS vs. Cloud Scraper TCO Estimator](https://sectoroneventures.github.io/infrabench/docker-vps-tco-estimator.html)**
