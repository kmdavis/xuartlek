---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Troubadour"
tags:
  - pf2e/creature/level/3
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Troubadour"
level: 3
source: "NPC Core"
aon_id: "creature-3575"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3575"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Troubadour"
level: "Creature 3"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +8, Deception +9, Diplomacy +9, Performance +13, Occultism +7, Society +7, Stealth +8, Storytelling Lore +9"
abilityMods: [0, 3, 0, 2, 1, 4]
abilities_top:
  - name: "Bardic Lore"
    desc: "The troubadour can Recall Knowledge on any subject with a +7 modifier."
  - name: "Items"
    desc: "Leather Armor, lute, poetry book, Rapier"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +6; __Ref__: +11; __Will__: +9"
hp: 40
health:
  - name: "HP"
    desc: "40"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Melee"
    desc: "⬻ rapier +11 (deadly 1d8, Disarm, Finesse) __Damage__ 1d6+4 piercing"
abilities_bot:
  - name: "Bard Composition Spells"
    desc: "DC 20, 2 Focus Points - __Cantrips (2nd)__ Courageous Anthem - __2nd__ Counter Performance, Lingering Composition"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 20, attack +12 - __Cantrips (2nd)__ Daze, Figment, Message, Prestidigitation, Read Aura - __1st__ Charm, Illusory Disguise, Soothe, Ventriloquism (3 slots) - __2nd__ Calm, Charm, Embed Message (2 slots)"
sourcebook: "_NPC Core_, page 127."
```

```encounter-table
name: Troubadour
creatures:
  - 1: Troubadour
```
