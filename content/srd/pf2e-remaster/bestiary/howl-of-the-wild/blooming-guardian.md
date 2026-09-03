---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Blooming Guardian"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/large
statblock: inline
name: "Blooming Guardian"
level: 15
source: "Howl of the Wild"
aon_id: "creature-3256"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3256"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Blooming Guardian"
level: "Creature 15"
size: "Large"
trait_01: "Beast"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; low-light vision, scent (imprecise) 40 feet"
languages: "Fey; _speak with animals_, _speak with plants_"
skills:
  - name: "Skills"
    desc: "Athletics +30, Intimidation +21, Nature +29, Survival +27"
abilityMods: [5, 3, 5, 1, 3, 1]
abilities_top:
  - name: "Petal Form"
    desc: "The blooming guardian can dissipate momentarily into a swirling cloud of petals and pollen to pass over brambles and slip through cracks. When Striding in woodland terrain, the blooming guardian ignores difficult terrain and can pass through obstacles so long as there is a small passageway."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +32; __Ref__: +23; __Will__: +25"
hp: 360
health:
  - name: "HP"
    desc: "360; __Resistances__ void 15; __Weaknesses__ fire 15"
abilities_mid:
  - name: "Buck"
    desc: "⬲ DC 36"
speed: "50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ antlers +28 __Damage__ 4d12+5 piercing"
  - name: "Melee"
    desc: "⬻ hooves +26 __Damage__ 4d10+5 bludgeoning plus Improved Knockdown"
abilities_bot:
  - name: "Budding Siphon"
    desc: "⬻ (Aura, Primal, Stance, Void) 20 feet. A blooming guardian is in a constant state of decomposition; to keep this entropy at bay, the flowers that cover their antlers continually siphon life from the surrounding area. All living creatures that enter or start their turn in the emanation take 6d4 void damage (DC 36 basic Fortitude save). At the start of their turn in any round that the blooming guardian deals damage with siphoning buds, they gain 10 temporary Hit Points, plus 2 temporary Hit Points for each creature damaged beyond the first since the blooming guardian's last turn, to a maximum of 20 temporary Hit Points."
  - name: "Full Bloom"
    desc: "⬻ (Poison, Primal, Stance) The flowers on the blooming guardian's antlers bloom, unveiling their brilliance as they eat away at their host. While in this stance, the blooming guardian's Strikes deal an additional 2d4 poison damage plus 5 persistent poison damage; on a hit, a target must succeed at a DC 36 Fortitude save or become enfeebled 2. The blooming guardian takes 5 persistent poison damage as long as it's in Full Bloom."
  - name: "Goring Charge"
    desc: "⬺ The blooming guardian Strides twice and makes an antlers Strike after either Stride. If the Strike hits, the blooming guardian deals an extra 2d12 bludgeoning damage, and the target takes a –2 circumstance penalty to its next Fortitude save against blossom siphon."
  - name: "Wail of the Forest"
    desc: "⬺ (Primal, Void)"
  - name: "Requirements"
    desc: "The blooming guardian is in Full Bloom"
  - name: "Effect"
    desc: "The blooming guardian confronts their mortality, causing their flowers to burst and spray their pollen. All creatures in a 40-foot cone take 10d10 void damage with a DC 36 Fortitude save. The blooming guardian then exits Full Bloom and can't enter it again for 1d4 rounds."
  - name: "Critical Success"
    desc: "No effect."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and becomes drained 1. Creatures that are enfeebled lose that condition and increase the drained condition by the same value."
  - name: "Critical Failure"
    desc: "As failure, but double damage."
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 33 - __3rd__ Animal Vision - __Constant (4th)__ Speak with Animals, Speak with Plants"
sourcebook: "_Howl of the Wild_, page 128."
```

```encounter-table
name: Blooming Guardian
creatures:
  - 1: Blooming Guardian
```
