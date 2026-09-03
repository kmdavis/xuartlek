---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Jaathoom"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/air
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/genie
  - pf2e/creature/trait/large
statblock: inline
name: "Jaathoom"
level: 5
source: "Monster Core"
aon_id: "creature-3003"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3003"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Jaathoom"
level: "Creature 5"
size: "Large"
trait_01: "Air"
trait_02: "Elemental"
trait_03: "Genie"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "Common, Sussuran; (can't speak any language); cloud of visions"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Arcana +11, Athletics +11, Crafting +9, Deception +11, Diplomacy +13, Society +9, Stealth +12"
abilityMods: [4, 5, 2, 2, 2, 4]
abilities_top:
  - name: "Cloud of Visions"
    desc: "(arcane, aura, mental) 60 feet. A jaathoom has telepathy 60 feet but can only show images, not speak."
  - name: "Items"
    desc: "Scimitar"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +9; __Ref__: +14; __Will__: +11"
hp: 55
health:
  - name: "HP"
    desc: "55"
abilities_mid:
  - name: "Naturally Invisible"
    desc: "The jaathoom is invisible at all times, though when they take a hostile action of any kind, they are hidden instead of undetected until the start of their next turn, as the vague outline of their form is faintly visible for a short period of time."
  - name: "Turbulent Skies"
    desc: "(air, arcane, aura) 20 feet. All squares in the emanation are difficult terrain for Striding and Flying creatures. Creatures with the air trait are immune. The jaathoom can activate or deactivate this aura as a single action with the concentrate trait."
speed: "25 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ scimitar +15 (Forceful, reach 10 feet, Sweep) __Damage__ 1d6+10 slashing"
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Finesse, Magical, Nonlethal, reach 10 feet) __Damage__ 1d4+10 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crashing wind +16 (Air, Arcane, range increment 20 feet) __Damage__ 1d8+8 bludgeoning"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Arcane, Concentrate, Polymorph) The jaathoom transforms into a Small or Medium air elemental or aerial animal, such as an owl. This doesn't affect their statistics, but it could change the damage type of their Strikes."
  - name: "Hurricane Blast"
    desc: "⬻ (Air, Arcane)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The jaathoom moves all creatures without the air trait in their turbulent skies aura 20 feet directly away, clockwise, or counterclockwise. A creature avoids being moved if it succeeds at a DC 21 Fortitude save."
  - name: "Ominous Dreams"
    desc: "⬺ (Mental, Prediction) The jaathoom sends a prophetic dream to a sleeping creature within 10 feet. An unwilling creature avoids the vision if it succeeds at a DC 23 Will save. The jaathoom chooses the dream's subject, but not its exact events. The target sees a brief vision of its future related to that subject, with the effect of _augury_. If the result is bad or mixed, the creature is frightened 2 and can't recover from being frightened until it wakes. Jaathoom Shuyookhs Jaathoom shuyookhs prefer to manifest wishes informed by their visions of the future. They add the following innate spells: __5th__ _illusory creature_, _illusory object_, _nightmare_ (×2), _sleep_ (×2); __4th__ _ill omen_."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 21 - __Cantrips (3rd)__ Detect Magic - __3rd__ Ill Omen, Illusory Creature, Illusory Object, Sleep - __4th__ Nightmare, Vapor Form - __7th__ Interplanar Teleport (to Astral Plane; Elemental Planes; or the Universe only)"
sourcebook: "_Monster Core_, page 157."
```

```encounter-table
name: Jaathoom
creatures:
  - 1: Jaathoom
```
