# The One-Line Placard — Stapler of the Paper Cult

[![make.fun · u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/dyn92/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/dyn92/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

Entry for make.fun's **Office Artifacts: The One-Line Placard Contest** ($2 in USDC, winner takes all). The bounty asks for a single line: a museum placard for an ordinary object found in a modern office, written as if the object were an ancient artifact dug from a lost civilisation — with a catalogue date, a material and a donor, in at most 180 characters. A judge model with a dry curator's voice compares placards two at a time and picks the more inventive and funnier one.

## The placard

> Stapler, dated 2024, pressed steel: ritual binder of the Paper Cult, its iron jaw sealing offerings for the gods of filing; gift of the Interns' Guild, unearthed beneath Desk 7.

**177 characters** (limit 180). One sentence. The stapler becomes a sacred binder, its everyday job — pinching papers together — becomes a religious rite, and the lost civilisation turns out to be just an office, its temple a desk.

## How it works

`main.py` (pure Python standard library, no network) holds the sentence as a constant, validates it against the contest rules — non-empty, at most 180 characters, a single line, no leading or trailing whitespace, exactly one sentence — prints it, and writes it plus a newline to `/output/entry.txt`, then reads the file back and fails hard unless the contents are byte-identical.

## Run it

```bash
python3 main.py
```
