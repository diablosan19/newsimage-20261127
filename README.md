# Friday 27 November 2026: 36 stories, 10 regions

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/diablosan19/newsimage-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/diablosan19/newsimage-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

**The World Front Page** — one 1024×1024 image summing up Friday 27 November
2026: 36 stories across 10 regions and 15 fields, drawn from the overnight
wires (Reuters, AP, BBC, NYT and others).

## The day

Three big leads — the Kuwait drone strike that killed two Italian
technicians, Hamas weighing its reply as Israeli strikes kill 10 in Gaza,
and the Thanksgiving storms that cut power to 800,000 in the US — plus ten
illustrated panels, a 23-story numbered list, a UTC first-wire timeline, a
world pin map (pins 1–13), a region-count bar, a markets ticker, and a DATE
CHECK box that
names the big prior-day stories (COP31, the Macy's parade postponement, the
US tariff package, the Huawei verdict) and keeps them out of the edition.

Every headline traces to a wire or primary source dated 27 November 2026,
with per-story sourcing labels (OFFICIAL / CONFIRMED / REPORTED). All scenes
are drawn with PIL primitives — no photographs, no external assets.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node stdlib only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, verifying the PNG magic bytes and the 1 MiB
cap. Both runs write identical bytes.

## Build

`draw_news27.py` renders `entry.png` from scratch (Python 3 + Pillow,
system fonts only). Re-run it to regenerate the image, then re-run `main.ts`.

## License

MIT — see `LICENSE`.
