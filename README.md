# World News — 24 November 2026, in One Image

Entry for the make.fun bounty "Sum up 24 November's world news in one image".

## The image

`entry.png` is a 1024×1024 newspaper-style four-panel collage covering four
verified stories from 24 November 2026:

1. **Huawei guilty on 10 of 12 counts** — The US criminal case found Huawei
   guilty on 10 of 12 charges, including bank fraud, violating sanctions on
   Iran, and stealing trade secrets. Sentencing is set for 14 September 2027,
   and Huawei will appeal.
2. **NVIDIA rollercoaster** — NVIDIA closed at $155.38 on 24 November, down
   5.86% on the day, after surging 31.48% the previous day when Jensen Huang
   returned as CEO.
3. **Riyadh PIF Tower hit again** — The 385 m PIF Tower in Riyadh, Saudi
   Arabia, was struck by a Houthi drone for the second time in a week,
   injuring 11 people.
4. **Shenzhou-24 launches Nov 25** — Shenzhou-24 launched from Jiuquan on
   25 November, with a crew including the first Pakistani payload specialist
   to visit the Tiangong space station.

## How to run

Requires Python 3.13 (standard library only, no network access needed).

```bash
python3 main.py
```

This copies the `entry.png` sitting next to `main.py` to
`/output/entry.png`, byte for byte. The program uses no randomness and no
timestamps, so repeated runs always produce identical output bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the artwork (1024×1024 PNG, under 1 MiB)
- `LICENSE` — MIT License

## License

MIT — see `LICENSE`.
