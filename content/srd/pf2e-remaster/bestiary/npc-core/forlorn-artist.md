---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Forlorn Artist"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/elf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Forlorn Artist"
level: 2
source: "NPC Core"
aon_id: "creature-3631"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3631"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Forlorn Artist"
level: "Creature 2"
size: "Medium"
trait_01: "Elf"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; (9 to notice unusual artwork) low-light vision"
languages: "Common, Elven; one regional language"
skills:
  - name: "Skills"
    desc: "Art Lore +11, Crafting +11, Diplomacy +9, Society +8"
abilityMods: [0, 3, -1, 4, 1, 3]
abilities_top:
  - name: "Art Specialist"
    desc: "For encounters involving crafting or evaluating art, the forlorn artist is a 4th-level challenge."
  - name: "Items"
    desc: "art supplies, Leather Armor, Rapier"
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +3; __Ref__: +9; __Will__: +9 +1 circumstance vs. emotion effects"
hp: 26
health:
  - name: "HP"
    desc: "26"
abilities_mid:
  - name: "Flick Ink"
    desc: "⬲"
  - name: "Trigger"
    desc: "The artist is targeted with a melee or ranged Strike by a creature within 15 feet"
  - name: "Effect"
    desc: "The artist flings ink in the attacker's eyes. The attacker must succeed at a DC 18 Reflex save or be blinded. This takes effect before the attacker targets the artist. The blindness lasts until the end of the target's next turn, but the creature can Interact to rub its eyes to attempt a new save to end the condition."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +9 (deadly d8, Disarm, Finesse) __Damage__ 1d6+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +9 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
abilities_bot:
  - name: "Cry of Ages"
    desc: "⬻ The artist channels their loneliness into a wordless wail that forces others to contemplate their mortality. Each enemy in a 30-foot emanation must succeed at a DC 17 Will save or be frightened 1. A creature that critically fails is also stupefied 1 for 1 minute. Each creature is then temporarily immune for 1 minute."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 18 - __Cantrips (1st)__ Figment, Prestidigitation, Sigil"
sourcebook: "_NPC Core_, page 178."
```

```encounter-table
name: Forlorn Artist
creatures:
  - 1: Forlorn Artist
```
