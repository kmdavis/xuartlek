---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Yamaraj"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/huge
statblock: inline
name: "Yamaraj"
level: 20
source: "Monster Core"
aon_id: "creature-3150"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3150"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Yamaraj"
level: "Creature 20"
size: "Huge"
trait_01: "Monitor"
trait_02: "Psychopomp"
trait_03: "Uncommon"
modifier: 37
perception:
  - name: "Perception"
    desc: "Perception +37; darkvision, lifesense 240 feet, _truesight_"
languages: "Chthonian, Diabolic, Empyrean, Requian; telepathy 120 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +33, Athletics +38, Boneyard Lore +40, Deception +34, Diplomacy +34, Intimidation +36, Legal Lore +40, Occultism +38, Religion +38, Society +38"
abilityMods: [10, 7, 7, 10, 7, 6]
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +33; __Ref__: +31; __Will__: +35 +1 status to all saves vs. magic"
hp: 375
health:
  - name: "HP"
    desc: "375 (fast healing 20, lightning drinker); __Immunities__ death effects, disease, electricity (see lightning drinker); __Resistances__ poison 20, void 20"
abilities_mid:
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 60 feet, DC 39"
  - name: "Lightning Drinker"
    desc: "Whenever a yamaraj would take electricity damage if not for its immunity, its fast healing increases to 40 on its next turn. During that turn, if it uses Beetle Breath, the beetles deal 2d12 additional electricity damage."
speed: "35 feet, fly 50 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 (Magical, reach 15 feet) __Damage__ 4d8+18 piercing plus Improved Grab and yamaraj venom and 3d6 shepherd's touch"
  - name: "Melee"
    desc: "⬻ claw +38 (Agile, Magical, reach 15 feet) __Damage__ 4d4+18 slashing plus 3d6 shepherd's touch"
  - name: "Melee"
    desc: "⬻ tail +38 (Magical, reach 20 feet) __Damage__ 4d10+18 bludgeoning plus 3d6 shepherd's touch"
abilities_bot:
  - name: "Beetle Breath"
    desc: "⬺ (Divine) The yamaraj breathes a blast of beetles in a 50-foot cone that deals 14d8 slashing damage and 4d8 persistent slashing damage to creatures in the area with a DC 42 Reflex save. It can't use Beetle Breath again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage and is sickened 1."
  - name: "Failure"
    desc: "The creature takes full damage and is sickened 2."
  - name: "Critical Failure"
    desc: "The creature takes double damage and is sickened 3."
  - name: "Final Judgment"
    desc: "A yamaraj's _manifestation_ spells are used only to pronounce judgment, typically either to restore a dead or destroyed creature to life, bind a creature to the Boneyard, or banish a creature from the Boneyard."
  - name: "Shepherd's Touch"
    desc: "A yamaraj's Strikes have the benefit of a _ghost touch_ property rune and deal an additional 3d6 void damage to living creatures or 3d6 vitality damage to undead."
  - name: "Yamaraj Venom"
    desc: "(Poison) While a creature is clumsy from this poison, it is doomed with the same value"
  - name: "Saving Throw"
    desc: "DC 42 Fortitude"
  - name: "Maximum Duration"
    desc: "10 rounds"
  - name: "Stage 1"
    desc: "3d8 poison damage and clumsy 1 (1 round)"
  - name: "Stage 2"
    desc: "5d8 poison damage and clumsy 2 (1 round)"
  - name: "Stage 3"
    desc: "7d8 poison damage and clumsy 3 (1 round)."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44 - __5th__ Translocate (at will), Mind Probe (at will) - __8th__ Chain Lightning (×3), Dispel Magic (×3), Wall of Force - __9th__ Harm, Heal, Seize Soul, Spirit Blast, Wails of the Damned - __10th__ Manifestation (see final judgment), Revival - __Constant (10th)__ Truesight"
  - name: "Rituals"
    desc: "DC 44 - __5th__ Call Spirit, Resurrect"
sourcebook: "_Monster Core_, page 277."
```

```encounter-table
name: Yamaraj
creatures:
  - 1: Yamaraj
```
