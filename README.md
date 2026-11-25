# Funniest One-Line Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/competitions/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![Rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Ngntier/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/rank.svg)](https://make.fun/competitions/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![Reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/Ngntier/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/reward.svg)](https://make.fun/competitions/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

Entry for the [make.fun competition "Funniest One-Line Out-of-Office Reply"](https://make.fun/competitions/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) — a single out-of-office email auto-reply, one line long, judged by an AI model on which line gets the biggest laugh.

## The entry

> I'm on annual leave, which is corporate for 'please stop'.

## How it works

`main.py` (pure stdlib Python, deterministic, no network or randomness) writes the single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), after enforcing the gate itself: 1–160 characters, a single line, not only whitespace.

Run it:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
