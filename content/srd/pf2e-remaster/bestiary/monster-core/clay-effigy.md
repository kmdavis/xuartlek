---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Clay Effigy"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/mindless
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Clay Effigy"
level: 10
source: "Monster Core"
aon_id: "creature-2881"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2881"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Clay Effigy"
level: "Creature 10"
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
skills:
  - name: "Skills"
    desc: "Athletics +24"
abilityMods: [6, -1, 6, -5, 0, -5]
abilities_top:
  - name: "Sacred Art"
    desc: "The creator of a clay effigy can dedicate the effigy to a deity while constructing it. If the deity allows a divine sanctification, the effigy is sanctified to that deity, gaining the holy or unholy trait as appropriate."
ac: 29
armorclass:
  - name: "AC"
    desc: "29; __Fort__: +23; __Ref__: +16; __Will__: +17"
hp: 175
health:
  - name: "HP"
    desc: "175; __Immunities__ bleed, death effects, disease, doomed, drained, fatigued, healing, mental, nonlethal attacks, paralyzed, poison, sickened, spirit, unconscious, vitality, void; __Resistances__ physical 10 (except adamantine), spells 10 (except cold, earth, or water)"
abilities_mid:
  - name: "Effigy's Curse"
    desc: "(curse, divine) When a creature damages the clay effigy, it must succeed at a DC 27 Will save or be afflicted with the effigy's curse. The accursed becomes fatigued when it carries part of the effigy or any item the effigy was assigned to guard. This fatigue can't be removed until the creature has given up such items for at least 24 hours."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +24 (Magical, reach 10 feet, Sanctified) __Damage__ 2d10+6 bludgeoning plus 2d6 spirit"
abilities_bot:
  - name: "Cast Out"
    desc: "⬺ (Divine, Sanctified, Spirit) A 20-foot emanation of spiritual energy pushes against intruders, as though trying to drive their souls away. Each creature in the area takes 8d6 spirit damage depending on a DC 29 Will save. The clay effigy can't Cast Out again for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and 3d6 persistent spirit damage. The persistent damage ends if the creature moves over 60 feet from the clay effigy or the effigy is destroyed."
  - name: "Critical Failure"
    desc: "As failure, except the persistent damage is increased to 6d6."
  - name: "Heavy Stride"
    desc: "⬺ The clay effigy Strides and can move through the spaces of Medium and smaller creatures. Each creature it moves through must succeed at a DC 29 Reflex save or be knocked prone. Clay Shards The remains of clay effigies are worth more to archaeologists and scholars than to merchants. The magnificent treasures often guarded by these ancient wardens, however, are another matter entirely."
sourcebook: "_Monster Core_, page 64."
```

```encounter-table
name: Clay Effigy
creatures:
  - 1: Clay Effigy
```
