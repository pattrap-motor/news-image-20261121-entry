[![make.fun bounty](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/pattrap-motor/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/pattrap-motor/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121)

# The World in One Day — 21 November 2026

Entry for [news-image-20261121](https://make.fun/c/news-image-20261121)
(Sum up 21 November's world news in one image).

## The image

A newspaper front page, drawn with Pillow (`draw.py`), all text rendered
sharp with DejaVu fonts — no AI-generated text, so nothing garbles at the
judging scale.

- **Lead — Rutte flies to Poland:** NATO's chief arrives in Warsaw today
  as Poland seeks more Eastern Sentry forces after Russian missiles
  crossed its airspace on Friday.
- **Lisbon — Protests spill into Saturday:** Lisbon marches today as youth
  rallies over living costs roll into a second day.
- **Eastern Sentry — Warsaw's ask: more jets:** Poland wants more Eastern
  Sentry jets; Rutte's visit today is the answer.
- **Nowa Deba — Allied drills wind down:** eleven-nation exercise near
  the crash sites ends this weekend.
- **Weather — Storm Xavier eases:** marine gale warnings narrow; land
  warnings stay on five islands.
- **Also today:** youth marches in Lisbon and French cities; allied
  drills wind down; Storm Xavier warnings narrow.

Sources: AP · AFP/LETA · Mappr · AppiSToS. All events of Saturday
21 November 2026. (The 19–20 Nov events — trilateral summit, Poland
missile incursion, Hormuz tanker fire, Friday market plunge — are
deliberately excluded: they are not 21 November news.)

## Run it

```sh
python3 draw.py            # redraw entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to the
output directory. Both runs write the same bytes.
