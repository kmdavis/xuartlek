---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Advisor"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Advisor"
level: 5
source: "NPC Core"
aon_id: "creature-3420"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3420"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Advisor"
level: "Creature 5"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Deception +14, Diplomacy +14, Legal Lore +12, Occultism +10, Performance +12, Society +12"
abilityMods: [0, 2, -1, 3, 3, 5]
abilities_top:
  - name: "Placate"
    desc: "An advisor is well versed in soothing agitated nobles. Their calming voice gives them a +2 circumstance bonus to Deception and Diplomacy checks when dealing with members of the nobility."
  - name: "Items"
    desc: "Dagger (2), fine clothes, _minor healing potion_, small harp, Whip"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +8; __Ref__: +11; __Will__: +14"
hp: 60
health:
  - name: "HP"
    desc: "60"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ whip +11 (Disarm, Finesse, Nonlethal, reach 10 feet, Trip) __Damage__ 1d4+4 slashing"
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +11 (Agile, thrown 10 feet, versatile S) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 22, 1 Focus Point - __Cantrips (3rd)__ Rallying Anthem, Courageous Anthem, Uplifting Overture - __3rd__ Counter Performance"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 22, attack +14 - __Cantrips (3rd)__ Daze, Light, Prestidigitation, Shield, Void Warp - __1st__ Command, Force Barrage, Protection, Soothe (3 slots) - __2nd__ Augury, Cleanse Affliction, Soothe, Stupefy (3 slots) - __3rd__ Mind Reading, Soothe, Ring of Truth (2 slots)"
sourcebook: "_NPC Core_, page 14."
```

```encounter-table
name: Advisor
creatures:
  - 1: Advisor
```
