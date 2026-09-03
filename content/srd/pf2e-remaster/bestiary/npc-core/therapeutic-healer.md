---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Therapeutic Healer"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Therapeutic Healer"
level: 7
source: "NPC Core"
aon_id: "creature-3485"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3485"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Therapeutic Healer"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; (16 to Sense Motive)"
languages: "Common; two additional humanoid languages"
skills:
  - name: "Skills"
    desc: "Diplomacy +17, Medicine +17, Occultism +16, Performance +15, Society +14"
abilityMods: [2, 1, 0, 3, 3, 4]
abilities_top:
  - name: "Doctor's Hand"
    desc: "When the therapeutic healer rolls a critical failure on a check to Treat Disease, Treat Poison, or Treat Wounds, they get a failure instead."
  - name: "Items"
    desc: "Chain Shirt, expanded healer's toolkit, Staff"
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +12; __Will__: +18"
hp: 110
health:
  - name: "HP"
    desc: "110; __Resistances__ mental 5"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ staff +13 (two-handed d8) __Damage__ 1d8+6 bludgeoning"
  - name: "Melee"
    desc: "⬻ fist +13 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 25, 2 Focus Points - __4th__ Hymn of Healing"
  - name: "Emotionally Invested"
    desc: "(Emotion, Healing, Mental) When the therapeutic healer casts a spell with the healing trait on a creature other than themself, the healer regains HP equal to the spell's rank."
  - name: "Therapeutic Care"
    desc: "When Treating Wounds, the therapeutic healer can treat up to four targets. If they succeed at a DC 20 check to Treat Wounds, they can also reduce the value of one clumsy, enfeebled, or stupefied condition affecting a single patient by 1. They can reduce a drained or doomed condition instead if they succeed at a DC 30 check. This can't reduce permanent doomed conditions."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 25, attack +17 - __Cantrips (4th)__ Guidance, Shield, Message, Prestidigitation, Telekinetic Projectile - __1st__ Protection, Sanctuary, Soothe (3 slots) - __2nd__ Soothe, Status, Translate (3 slots) - __3rd__ Clear Mind, Soothe, Veil of Privacy (3 slots) - __4th__ Cleanse Affliction, Clear Mind, Soothe (3 slots)"
sourcebook: "_NPC Core_, page 63."
```

```encounter-table
name: Therapeutic Healer
creatures:
  - 1: Therapeutic Healer
```
