#!/usr/bin/env python3
"""
WhisperPrice — Audio & Podcast Transcription Arbitrage Calculator — Command-Line Cost Calculator
Live Web Calculator: https://sectoroneventures.github.io/whisper-price/
"""
import argparse

PROVIDERS = [
  {
    "name": "Faster-Whisper Large-v3 on Vast.ai (RTX 3090)",
    "cost_per_unit": 0.0018,
    "min_monthly": 0.19,
    "speed_note": "120x real-time speed on 24GB GPU ($0.19/hr)",
    "cta_label": "Boot 1-Click Whisper Box \u2192",
    "cta_url": "https://cloud.vast.ai/?ref_id=749467&template_id=fe790f7a807c2d4e7b3bb717f7ed4c78",
    "highlight": true
  },
  {
    "name": "Apify Audio & Video Transcript Actors",
    "cost_per_unit": 0.04,
    "min_monthly": 0.0,
    "speed_note": "Pulls transcripts + metadata straight from URLs ($5/mo free credit)",
    "cta_label": "Try Apify Free \u2192",
    "cta_url": "https://apify.com?fpr=infrabench7552",
    "highlight": false
  },
  {
    "name": "Standard Managed Speech-to-Text API ($0.006/min)",
    "cost_per_unit": 0.36,
    "min_monthly": 0.0,
    "speed_note": "Per-minute API billing ($360 per 1,000 hours)",
    "cta_label": "Switch to Rented GPU & Save 99% \u2192",
    "cta_url": "https://cloud.vast.ai/?ref_id=749467&template_id=fe790f7a807c2d4e7b3bb717f7ed4c78",
    "highlight": false
  },
  {
    "name": "Enterprise Transcription SaaS ($0.024/min)",
    "cost_per_unit": 1.44,
    "min_monthly": 0.0,
    "speed_note": "High per-minute markup ($1,440 per 1,000 hours)",
    "cta_label": "Compare Self-Hosted GPU Setup \u2192",
    "cta_url": "https://cloud.vast.ai/?ref_id=749467",
    "highlight": false
  }
]

def main() -> None:
    parser = argparse.ArgumentParser(description="Interactive audio transcription cost calculator comparing managed speech-to-text APIs ($0.36-$1.44/hr) against Faster-Whisper Large-v3 on rented GPUs ($0.0016/hr).")
    parser.add_argument("--volume", type=float, default=500, help="Monthly Audio / Meeting / Podcast Hours to Transcribe")
    args = parser.parse_args()
    print(f"=== {args.volume:g} audio hours/mo Cost Comparison ===")
    for p in PROVIDERS:
        cost = max(float(p["min_monthly"]), args.volume * float(p["cost_per_unit"]))
        print(f"* {p['name']}: ${cost:,.2f}/mo ({p['speed_note']})")
        print(f"  -> {p['cta_url']}")
    print(f"\nInteractive web calculator: https://sectoroneventures.github.io/whisper-price/")

if __name__ == "__main__":
    main()
