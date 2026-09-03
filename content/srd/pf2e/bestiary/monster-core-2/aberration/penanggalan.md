---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Penanggalan"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/tanggal
  - pf2e/creature/trait/medium
statblock: inline
name: "Penanggalan"
level: 5
source: "Monster Core 2"
aon_id: "creature-4506"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4506"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Penanggalan"
level: "Creature 5"
size: "Medium"
trait_01: "Aberration"
trait_02: "Tanggal"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Aklo, Common"
skills:
  - name: "Skills"
    desc: "Athletics +12, Deception +14, Intimidation +12, Midwifery Lore +9, Stealth +14"
abilityMods: [3, 5, 2, 0, 2, 5]
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +9; __Ref__: +16; __Will__: +11"
hp: 85
health:
  - name: "HP"
    desc: "85; __Weaknesses__ slashing 5"
abilities_mid:
  - name: "Spewing Bile"
    desc: "When the penanggalan takes slashing damage, the wound spews bile on adjacent creatures, dealing 2d10 poison damage (DC 19 basic Fortitude save). The penanggalan loses their spewing bile and penanggalan bile abilities until the end of their next turn."
speed: "fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ proboscis tongue +15 (Finesse) __Damage__ 2d6+5 piercing plus penanggalan bile"
  - name: "Melee"
    desc: "⬻ entrails +13 __Damage__ 2d4+5 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 2d4+3 bludgeoning, DC 21"
  - name: "Elongate Tongue"
    desc: "⬻ The penanggalan's tongue extends, the membrane stretching and becoming translucent. Until the end of the turn, the penanggalan's proboscis tongue Strikes have a 10-foot reach, and any target is off-guard against the Strike unless it has a Perception DC of 22 or higher or the ability to precisely sense invisible things."
  - name: "Penanggalan Bile"
    desc: "(Disease) A victim's drained condition decreases by 1 per month"
  - name: "Saving Throw"
    desc: "DC 19 Fortitude"
  - name: "Stage 1"
    desc: "drained 1 (1 week)"
  - name: "Stage 2"
    desc: "drained 2 (1 week)"
  - name: "Stage 3"
    desc: "drained 3 (1 week)"
  - name: "Stage 4"
    desc: "dead"
  - name: "Ride Corpse"
    desc: "⬽ (Concentrate, Polymorph) The penanggalan inserts their entrails into their humanoid body, allowing them to appear as and move about like a normal human. The body has 10 Hit Points and the same defenses as the penanggalan. When the body is destroyed, the penanggalan is ejected unharmed. The body becomes a corpse, and if it's neither controlled by the penanggalan nor stored in an alchemical vat, it decays as normal. Tanggal Segmentations Like penanggalans, other tanggals feed on flesh and separate from their body in some form. Such creatures also have their own weaknesses. The manananggal splits from the waist rather than from the neck, and the smell of vinegar repels them instead of signaling their presence. The balan-balan also splits from the neck like the penanggalan, but they leave illusion-draped banana trunks in coffins to resemble the corpses they stole."
sourcebook: "_Monster Core 2_, page 249."
```

```encounter-table
name: Penanggalan
creatures:
  - 1: Penanggalan
```
