---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Loan Shark"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Loan Shark"
level: 2
source: "NPC Core"
aon_id: "creature-3426"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3426"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Loan Shark"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Accounting Lore +17, Athletics +9, Deception +8, Diplomacy +8, Intimidation +8, Society +15"
abilityMods: [3, 0, 1, 2, 2, 4]
abilities_top:
  - name: "Business Savvy"
    desc: "When making monetary deals, the loan shark gets a +8 circumstance bonus to Deception checks, Diplomacy checks, and their Perception DC."
  - name: "Loan Specialist"
    desc: "For encounters involving monetary deals, the loan shark is a 7th-level challenge."
  - name: "Items"
    desc: "Breastplate, dragon-headed cane (functions as a staff)"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +6; __Will__: +10"
hp: 25
health:
  - name: "HP"
    desc: "25"
abilities_mid:
  - name: "Never off the Hook"
    desc: "(aura, emotion, mental) 60 feet. Creatures in the aura who owe the loan shark money take a –3 circumstance penalty to their Will DC against the loan shark's attempts to Demoralize or Coerce them and can't reduce their frightened value below 1 while in the aura."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dragon-headed cane +9 (two-hand d8) __Damage__ 1d4+5 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+5 bludgeoning __Interest is Due!__ ⬻ (Auditory, Concentrate, Linguistic, Mental)"
abilities_bot:
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The loan shark commands an ally within 30 feet to attack a creature who owes the loan shark money. The ally can use a reaction to Strike the debtor, dealing an additional 1d6 mental damage."
sourcebook: "_NPC Core_, page 19."
```

```encounter-table
name: Loan Shark
creatures:
  - 1: Loan Shark
```
