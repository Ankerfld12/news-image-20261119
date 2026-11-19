# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Ankerfld12/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Ankerfld12/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A magazine front page — "THE WORLD IN ONE IMAGE" — summing up the
world news of Thursday, 19 November 2026 in a single 1024×1024 image.
The lead story is the first-ever trilateral meeting of Trump, Xi and
Putin in Shenzhen, on the APEC sidelines. Around it: the Houthi
missile threat toward Riyadh, Israeli tanks crossing Gaza's Yellow
Line, Denmark's expected ratification of the Trump Greenland deal,
the Bangladesh lockdown, the COP31 deadlock in Antalya, and the
refinery blast in Cepu, Central Java — plus a stat strip and an
in-brief round-up. The poster is drawn with PIL (build/poster.py) and
shipped as assets/entry.png; main.py simply copies it to the output
directory, so every run writes identical bytes.

## Run it

```sh
python3 main.py
```

This writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`).

## The day's stories, and where they were reported

- Trump, Xi and Putin meet in Shenzhen — first-ever trilateral, on the
  APEC sidelines; Ukraine, the Iran war, nuclear arms and AI on the
  agenda (Reuters).
- Houthi missile threat toward Riyadh — Saudi-led coalition dealt with
  the threat; debris fell, material damage reported (Reuters).
- Israeli tanks cross Gaza's Yellow Line near Nuseirat — first ground
  operation beyond the ceasefire line since the October 2025 truce;
  3 killed; 5,200+ fled (Reuters, Al Jazeera).
- Denmark set to ratify the Trump Greenland deal — parliament vote
  expected Thursday around 10:00; US military role expands in
  Greenland, population 57,000 (Reuters).
- Bangladesh in lockdown — Awami League lockdown; Muhammad Yunus's
  ancestral home set ablaze; two ruling-party members killed;
  97 Border Guard platoons deployed (Reuters, BBC).
- COP31 deadlock — 21 issues unresolved; new draft texts due early
  Thursday; summit closes Friday (Reuters, UN News).
- Refinery blast in Cepu, Central Java — one worker killed;
  investigation under way (Reuters).
- In brief: Japan PM Takaichi's talks with Putin at APEC; Kim Jong Un's
  site inspections amid talk of a Trump meeting; Anthropic begins
  trading on the Nasdaq; Chancellor Merz hosting Macron and Burnham in
  Berlin for a Ukraine-guarantees summit; US–Venezuela anti-drug
  military cooperation (Reuters).

<sub>Entered on [make.fun](https://make.fun/?ref=8rrqgntk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
