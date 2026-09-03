---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Nuckelavee"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/large
statblock: inline
name: "Nuckelavee"
level: 9
source: "Monster Core"
aon_id: "creature-3110"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3110"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Nuckelavee"
level: "Creature 9"
size: "Large"
trait_01: "Amphibious"
trait_02: "Fey"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; low-light vision"
languages: "Aklo, Common, Fey"
skills:
  - name: "Skills"
    desc: "Athletics +19, Intimidation +19, Nature +16, Stealth +18, Survival +16"
abilityMods: [6, 3, 4, 1, 3, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 striking bastard sword_"
ac: 28
armorclass:
  - name: "AC"
    desc: "28; __Fort__: +19; __Ref__: +16; __Will__: +20"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ disease, poison; __Weaknesses__ cold iron 10"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 30 feet, DC 25"
  - name: "Purity Vulnerability"
    desc: "Unpolluted fresh water burns a nuckelavee like acid, dealing 1d6 damage to it and causing it to be sickened 2. A nuckelavee can't heal from damage when it's in an area that isn't polluted (subject to GM discretion)."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "40 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _bastard sword_ +21 (Magical, reach 10 feet, two-hand d12) __Damage__ 2d8+12 slashing plus 1d6 poison and mortasheen"
  - name: "Melee"
    desc: "⬻ jaws +20 (Agile) __Damage__ 2d8+12 piercing plus 1d6 poison and mortasheen"
  - name: "Melee"
    desc: "⬻ hoof +20 __Damage__ 2d6+12 bludgeoning plus mortasheen"
abilities_bot:
  - name: "Blight Breath"
    desc: "⬺ (Disease, Poison, Primal) The nuckelavee breathes a 30-foot cone of foulness, dealing 8d6 void damage to living creatures in the area with a DC 28 basic Fortitude save. A creature that fails also takes 2d6 persistent bleed damage. The nuckelavee can't use Blight Breath again for 1d4 rounds."
  - name: "Mortasheen"
    desc: "(Disease) The target can't recover from the fatigued condition caused by mortasheen until the disease is cured. Mortasheen gains the virulent trait against animals and plants"
  - name: "Saving Throw"
    desc: "DC 28 Fortitude"
  - name: "Stage 1"
    desc: "Carrier with no ill effect (1 day)"
  - name: "Stage 2"
    desc: "drained 1 and fatigued (1 day)"
  - name: "Stage 3"
    desc: "drained 2 and fatigued (1 day)"
  - name: "Stage 4"
    desc: "dead"
  - name: "Trample"
    desc: "⬽ Medium or smaller, hoof, DC 28 Unfortunate Victims Nuckelavees are equally delighted to murder and feed upon both hapless peasants and altruistic naturalists engaged in the process of cleaning up pollution. Indeed, those who would seek to purify such sites are often regarded as the greater threat by a nuckelavee, as without a befouled land to dwell in, the foul fey would wither away."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 28 - __3rd__ Aqueous Orb - __5th__ Control Water"
  - name: "Rituals"
    desc: "DC 28 - __4th__ Blight"
sourcebook: "_Monster Core_, page 243."
```

```encounter-table
name: Nuckelavee
creatures:
  - 1: Nuckelavee
```
