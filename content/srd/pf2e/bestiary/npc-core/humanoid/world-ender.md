---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "World Ender"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "World Ender"
level: 16
source: "NPC Core"
aon_id: "creature-3622"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3622"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "World Ender"
level: "Creature 16"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Intimidation +28, Nature +27, Religion +25, Society +27"
abilityMods: [4, 3, 7, 7, 3, 2]
abilities_top:
  - name: "Items"
    desc: "_+1 striking major staff of fire_"
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +30; __Ref__: +26; __Will__: +28"
hp: 275
health:
  - name: "HP"
    desc: "275; __Resistances__ fire 15"
abilities_mid:
  - name: "Unyielding Purpose"
    desc: "⬲"
  - name: "Trigger"
    desc: "The world ender would be reduced to 0 HP"
  - name: "Requirements"
    desc: "The world ender has a _volcanic eruption_ spell remaining"
  - name: "Effect"
    desc: "The world ender refuses to let their destructive dream go unrealized, stabilizing at 1 HP just long enough to cast _volcanic eruption_, centered on themself. They die, immolated in the eruption."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _staff of fire_ +28 (Magical, two-hand d8) __Damage__ 2d4+10 bludgeoning plus 3d6 fire"
  - name: "Melee"
    desc: "⬻ fist +27 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+10 bludgeoning plus 3d6 fire"
abilities_bot:
  - name: "Monologue"
    desc: "⭓ (Concentrate)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "Throughout combat, the world ender ceaselessly expounds upon the righteous reasons for their destructive aims and the futility of their enemies' efforts to stop them. They gain a +1 status bonus to Will saves and a +2 status bonus to damage rolls with their spells. Each time they take this action again, the bonuses increase by 1 and 2, respectively. The monologue ends (and the bonuses are lost) if the world ender becomes unable to act or speak, or if they end their turn without having taken this action."
  - name: "Overwhelming Energy"
    desc: "⬻ (Spellshape) If the next action the world ender uses is to Cast a Spell, the spell ignores 20 resistance to energy damage. This applies to all damage the spell deals, including persistent damage and damage caused by an ongoing effect of the spell. A creature's immunities are unaffected."
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 41, attack +33 - __Cantrips (8th)__ Caustic Blast, Electric Arc, Gouging Claw, Ignition, Light - __1st__ Air Bubble, Fleet Step, Gentle Landing, Gust of Wind - __2nd__ Darkvision, Enlarge, Revealing Light, Water Walk - __3rd__ Earthbind (×2), Haste, Slow - __4th__ Fly (×2), Unfettered Movement (×2) - __5th__ Fireball (×2), Magic Passage, Wall of Stone - __6th__ Chain Lightning (×2), Floating Flame, Wall of Fire - __7th__ Blazing Bolt, Fiery Body, Volcanic Eruption (×2) - __8th__ Desiccate, Punishing Winds, Sunburst (×2)"
sourcebook: "_NPC Core_, page 163."
```

```encounter-table
name: World Ender
creatures:
  - 1: World Ender
```
