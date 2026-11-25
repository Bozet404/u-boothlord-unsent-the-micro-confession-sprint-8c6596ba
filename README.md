# Unsent: The Micro-Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/Bozet404/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/Bozet404/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

An entry for the [make.fun bounty "Unsent: The Micro-Confession Sprint"](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba).

The entry is a small Python program that writes one micro-confession to
`/output/entry.txt`. The confession has exactly two parts: a To: line
addressed to an old roommate, and the unsent message itself, one line
written exactly as it was typed, with no explanation after it.

The message is a draft that stayed a draft. The sender moved out of
the shared flat in March and still pays half the wifi bill, because
cancelling the bill would feel like saying they were never really
friends. The To: line and the message need each other: only a former
roommate shares a flat and a wifi bill, so swapping the addressee
would break it. The reason it stayed unsent is felt in the words,
never stated.

The program uses only the Python standard library, needs no network,
and is fully deterministic — it writes the same bytes on every run.

## Running it

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. To write somewhere else,
set the output directory first:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
